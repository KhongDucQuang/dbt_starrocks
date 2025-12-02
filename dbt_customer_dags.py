
from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig

# Config
PROJECT_DIR = "/opt/airflow/dags/dbt_starrocks"
PROFILES_YML = "/opt/airflow/dags/dbt_starrocks/profiles/profiles.yml"

project_cfg = ProjectConfig(dbt_project_path=PROJECT_DIR)
profile_cfg = ProfileConfig(
    profile_name="dbt_starrocks",
    target_name="dev",
    profiles_yml_filepath=PROFILES_YML,
)
exec_cfg = ExecutionConfig(dbt_executable_path="dbt")

check_dbt_starrocks = DbtDag(

    project_config=project_cfg,
    profile_config=profile_cfg,
    execution_config=exec_cfg,

    dag_id="check_dbt_starrocks",
    description="Run dbt (spark, method=session) on K8s using Hive catalog + MinIO",
    start_date=datetime(2025, 10, 26),
    catchup=False,
    tags=["dbt", "spark", "cosmos", "delta", "hive"],
)


