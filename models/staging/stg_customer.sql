{{ config(
    materialized='table',
    catalog='hive_catalog',
    schema='gold',
    properties={
      'file_format': 'parquet',
      'compression': 'snappy'
    }
) }}

SELECT
    pk_branch_bank,
    fk_bank_code,
    NOW() as processed_at
FROM
    {{ source('list_silver_tables', 'dim_t_list_branch_bank_adv_wdr') }}
