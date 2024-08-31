"""
first_dag
DAG auto-generated by Astro Cloud IDE.
"""

from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
import pendulum

from airflow.operators.empty import EmptyOperator

default_args={
    "owner": "aptitudet19@gmail.com,Open in Cloud IDE",
}

@dag(
    default_args=default_args,
    schedule="0 0 * * *",
    start_date=pendulum.from_format("2024-08-31", "YYYY-MM-DD").in_tz("UTC"),
    catchup=False,
    owner_links={
        "aptitudet19@gmail.com": "mailto:aptitudet19@gmail.com",
        "Open in Cloud IDE": "https://cloud.astronomer.io/cm09ouj4o0m0o01n52eom3fx3/cloud-ide/cm09pdvzc0m2y01n5kiyvbdyu/cm0idbkwk06n801n937kif6tt",
    },
)
def first_dag():
    empty_operator_1 = EmptyOperator(
        task_id="empty_operator_1",
    )

dag_obj = first_dag()
