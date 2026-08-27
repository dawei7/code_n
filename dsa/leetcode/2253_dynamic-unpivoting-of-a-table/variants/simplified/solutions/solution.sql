CREATE PROCEDURE UnpivotProducts()
BEGIN
    -- Write your PostgreSQL query statement below.
    SET group_concat_max_len = 5000;
    WITH
        t AS (
            SELECT column_name
            FROM information_schema.columns
            WHERE
                table_schema = DATABASE()
                AND table_name = 'Products'
                AND column_name != 'product_id'
        )
    SELECT
        STRING_AGG('SELECT product_id, \'',
            column_name,
            '\' store, ',
            column_name,
            ' price FROM Products WHERE ',
            column_name,
            ' IS NOT NULL', ' UNION ') INTO @sql from t;
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END;
