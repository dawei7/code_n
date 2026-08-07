SELECT
    ROUND(
        100.0 * AVG(
            CASE
                WHEN order_date = customer_pref_delivery_date THEN 1.0
                ELSE 0.0
            END
        ),
        2
    ) AS immediate_percentage
FROM Delivery;
