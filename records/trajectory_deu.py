import json
import time
import requests


env = 'deu-prod'
es_host = 'http://10.76.1.238:9200'
es_records_per_scroll=1000

airflow_host = 'http://10.68.193.109:8080'
airflow_env = 'deu_prod'
airflow_re_calc_trajectory_dag = "{airflow_env}_record_oea_dag".format(airflow_env=airflow_env)


def get_scroll_response(response):
    scroll_id = response['_scroll_id']
    record_codes = []
    for obj in response['hits']['hits']:
        record_codes.append(obj['_source']['record_code'])
    return scroll_id, record_codes


def get_first_scroll():
    url = "{es_host}/{env}:record/record_info/_search?scroll=1h".format(es_host=es_host, env=env)
    headers = {
        "content-type": "application/json"
    }
    data = {
        "size": es_records_per_scroll,
        "_source": ["record_code"],
        "query": {
            "bool": {
                "should": [
                    {
                        "bool": {
                            "must_not": [
                                {
                                    "exists": {
                                        "field": "speed_osm_max"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "bool": {
                            "must": [
                                {
                                    "exists": {
                                        "field": "speed_osm_max"
                                    }
                                },
                                {
                                    "term": {
                                        "speed_osm_max": {
                                            "value": "0"
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
    return get_scroll_response(response)


def get_next_scroll(scroll_id):
    url = "{es_host}/_search/scroll".format(es_host=es_host)
    headers = {
        "content-type": "application/json"
    }
    data = {
        "scroll": "1h",
        "scroll_id": "{scroll_id}".format(scroll_id=scroll_id)
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
    return get_scroll_response(response)


def del_scroll(scroll_id):
    url = "{es_host}/_search/scroll".format(es_host=es_host)
    headers = {
        "content-type": "application/json"
    }
    data = {
        "scroll_id": "{scroll_id}".format(scroll_id=scroll_id)
    }
    requests.delete(url=url, headers=headers, data=json.dumps(data))


def trigger_re_calc_trajectory_dag(record_code):
    dag_url = "{airflow_host}/api/experimental/dags/{airflow_re_calc_trajectory_dag}/dag_runs".format(
        airflow_host=airflow_host,
        airflow_re_calc_trajectory_dag=airflow_re_calc_trajectory_dag
    )
    airflow_headers = {
        "content-type": "application/json"
    }
    dag_run_data = {
        "run_id": "{record_code}_reclac_trajectory_new1".format(record_code=record_code),
        "conf": {
            "recordCode": record_code
        }
    }

    requests.post(
        url=dag_url, headers=airflow_headers, data=json.dumps(dag_run_data)
    )
    time.sleep(1.5)


if __name__ == "__main__":
    scroll_id, record_codes = get_first_scroll()
    total_amount = 0
    while record_codes:
        total_amount += len(record_codes)
        for record_code in record_codes:
            print("trigger {dag}_record_oea_dag of {record_code}".format(
                dag=airflow_env,
                record_code=record_code
            ))
            trigger_re_calc_trajectory_dag(record_code)
        scroll_id, record_codes = get_next_scroll(scroll_id)
    del_scroll(scroll_id)
    print("trigger recalc trajectory for records[{amount}]".format(amount=total_amount))
