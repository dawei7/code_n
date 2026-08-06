## Description

Table: `Flights`

```text
+---------------+------+
| Column Name   | Type |
+---------------+------+
| flight_id     | int  |
| capacity      | int  |
+---------------+------+
flight_id is the column with unique values for this table.
Each row of this table contains flight id and its capacity.
```

Table: `Passengers`

```text
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| passenger_id  | int      |
| flight_id     | int      |
| booking_time  | datetime |
+---------------+----------+
passenger_id is the column with unique values for this table.
Each row of this table contains passenger id, flight id, and their booking time.
```

Passengers book tickets for flights in advance. If the number of passengers booking a flight exceeds the flight's capacity, the remaining passengers are placed on a waiting list.

Write a solution to report the booking status of each passenger.

- If the passenger gets a seat, their status should be **Confirmed**.
- If the passenger is placed on the waiting list, their status should be **Waitlist**.

Return the result table ordered by `passenger_id` in **ascending** order.
