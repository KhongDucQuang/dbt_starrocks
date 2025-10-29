SELECT
    id, 
    name,
    email,
    created_at,
    partition_date,
    -- Giả sử bạn muốn thêm cột thời gian xử lý
    NOW() as processed_at
FROM
    {{ source('mbs_bronze', 'customer_raw') }}
