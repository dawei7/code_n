CREATE PROCEDURE UnpivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 1000000;

    SELECT GROUP_CONCAT(
        CONCAT(
            'SELECT product_id, ',
            QUOTE(column_name),
            ' AS store, `',
            REPLACE(column_name, '`', '``'),
            '` AS price FROM Products WHERE `',
            REPLACE(column_name, '`', '``'),
            '` IS NOT NULL'
        )
        ORDER BY ordinal_position
        SEPARATOR ' UNION ALL '
    )
    INTO @unpivot_query
    FROM information_schema.columns
    WHERE table_schema = DATABASE()
      AND table_name = 'Products'
      AND column_name <> 'product_id';

    PREPARE unpivot_statement FROM @unpivot_query;
    EXECUTE unpivot_statement;
    DEALLOCATE PREPARE unpivot_statement;
END
