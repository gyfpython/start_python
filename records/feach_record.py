import json
import time
import requests


def re_clac_rainy_snow_records(ip: str, port: str, env: str, airflow_ip: str, airflow_port: str, airflow_env: str):
    # get record list
    url = 'http://' + ip + ':' + port + '/' + env + ':record/record_info/_search'
    headers = {
        "content-type": "application/json"
    }
    data = {
        "query" : {
            "nested" : {
                "path" : "file_attr",
                "query" : {
                    "bool" : {
                        "should" :[
                            {"term" : {"file_attr.weather.name" : "Rainy"}},
                            {"term" : {"file_attr.weather.name" : "Snow"}}
                        ]
                    }
                }
            }
        },
        "_source" :["record_code"],
        "size":10000
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(data)).json()
    record_list = []
    for obj in response['hits']['hits']:
        # trigger dag
        airflow_url = "http://" + airflow_ip + ":" + airflow_port + \
                      '/api/experimental/dags/' + airflow_env + '_record_oea_dag/dag_runs'
        dag_run_data = {
            "run_id": obj['_id'] + "_reclac_weather",
            "conf": {
                "recordCode": obj['_id']
            }
        }
        airflow_headers = {
            "content-type": "application/json"
        }
        response = requests.post(url=airflow_url, headers=airflow_headers, data=json.dumps(dag_run_data))
        time.sleep(1.5)
        print(response)
        record_list.append(obj['_id'])
    return record_list

