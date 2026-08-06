## Description

Table: `Countries`

```text
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| country_id    | int     |
| country_name  | varchar |
+---------------+---------+
country_id is the primary key (column with unique values) for this table.
Each row of this table contains the ID and the name of one country.
```

Table: `Weather`

```text
+---------------+------+
| Column Name   | Type |
+---------------+------+
| country_id    | int  |
| weather_state | int  |
| day           | date |
+---------------+------+
(country_id, day) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the weather state in a country for one day.
```

Write a solution to find the type of weather in each country for **November 2019**.

The type of weather is:
* **Cold** if the average `weather_state` is less than or equal `15`,
* **Hot** if the average `weather_state` is greater than or equal to `25`, and
* **Warm** otherwise.

Return the result table in **any order**.
