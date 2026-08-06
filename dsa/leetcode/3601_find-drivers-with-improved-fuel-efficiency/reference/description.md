## Description

Table: `drivers`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| driver_id   | int     |
| driver_name | varchar |
+-------------+---------+
driver_id is the unique identifier for this table.
Each row contains information about a driver.

```

Table: `trips`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trip_id       | int     |
| driver_id     | int     |
| trip_date     | date    |
| distance_km   | decimal |
| fuel_consumed | decimal |
+---------------+---------+
trip_id is the unique identifier for this table.
Each row represents a trip made by a driver, including the distance traveled and fuel consumed for that trip.

```

Write a solution to find drivers whose **fuel efficiency has improved** by **comparing** their average fuel efficiency in the** first half** of the year with the **second half** of the year.

<ul>
	<li>Calculate **fuel efficiency** as `distance_km / fuel_consumed` for **each** trip</li>
	<li>**First half**: January to June, **Second half**: July to December</li>
	<li>Only include drivers who have trips in **both halves** of the year</li>
	<li>Calculate the **efficiency improvement** as (`second_half_avg - first_half_avg`)</li>
	<li>**Round **all** **results** **to** `2` **decimal** **places</li>
</ul>

Return *the result table ordered by efficiency improvement in **descending** order, then by driver name in **ascending** order*.

The result format is in the following example.
