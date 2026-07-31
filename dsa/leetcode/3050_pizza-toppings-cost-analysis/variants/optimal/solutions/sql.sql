SELECT
    first_topping.topping_name
        || ',' || second_topping.topping_name
        || ',' || third_topping.topping_name AS pizza,
    ROUND(
        first_topping.cost + second_topping.cost + third_topping.cost,
        2
    ) AS total_cost
FROM Toppings AS first_topping
INNER JOIN Toppings AS second_topping
    ON first_topping.topping_name < second_topping.topping_name
INNER JOIN Toppings AS third_topping
    ON second_topping.topping_name < third_topping.topping_name
ORDER BY total_cost DESC, pizza ASC;
