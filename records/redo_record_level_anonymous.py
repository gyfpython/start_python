import json
import time
import requests

airflow_host = 'http://10.68.193.109:8080'
airflow_env = 'gf_prod'
airflow_re_calc_anonymous_dag = "{airflow_env}_record_anonymous_dag".format(airflow_env=airflow_env)


def trigger_re_calc_anonymous_dag(record_code):
    dag_url = "{airflow_host}/api/experimental/dags/{airflow_re_calc_anonymous_dag}/dag_runs".format(
        airflow_host=airflow_host,
        airflow_re_calc_anonymous_dag=airflow_re_calc_anonymous_dag
    )
    airflow_headers = {
        "content-type": "application/json"
    }
    dag_run_data = {
        "run_id": "{record_code}_reclac_anonymous".format(record_code=record_code),
        "conf": {
            "recordCode": record_code
        }
    }

    requests.post(
        url=dag_url, headers=airflow_headers, data=json.dumps(dag_run_data)
    )
    time.sleep(1.5)


def get_record_codes(files: str):
    records_list = open(files)
    records_json = json.loads(records_list.readlines()[0])
    # print(records_json)
    try:
        if records_json["recordIds"]:
            return records_json["recordIds"]
        else:
            return []
    except Exception as error:
        print(error)


for record in get_record_codes('2020_04_02_11_48_55_RecordIds.txt'):
    if record:
        print(record)
        trigger_re_calc_anonymous_dag(record)

