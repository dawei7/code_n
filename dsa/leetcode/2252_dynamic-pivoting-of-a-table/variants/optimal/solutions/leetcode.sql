CREATE PROCEDURE PivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 1000000;

    SELECT GROUP_CONCAT(
        DISTINCT CONCAT(
            'MAX(CASE WHEN store = ',
            QUOTE(store),
            ' THEN price END) AS `',
            REPLACE(store, '`', '``'),
            '`'
        )
        ORDER BY store
        SEPARATOR ', '
    )
    INTO @store_columns
    FROM Products;

    SET @pivot_query = CONCAT(
        'SELECT product_id, ',
        @store_columns,
        ' FROM Products GROUP BY product_id'
    );

    PREPARE pivot_statement FROM @pivot_query;
    EXECUTE pivot_statement;
    DEALLOCATE PREPARE pivot_statement;
END
