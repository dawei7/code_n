## Description

The `cities` table records a city together with the state that contains it. Combine all cities belonging to the same state into one comma-and-space-separated string.

Within each combined string, list city names in ascending order. Return one row per represented state, and order those rows by state name in ascending order.

Each `(state, city)` pair is unique, so every stored city contributes once to its state's list. Preserve each name exactly as stored while applying the two required ascending orders.
