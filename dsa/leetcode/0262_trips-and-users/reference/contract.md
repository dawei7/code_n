## Function Contract

**Inputs**

- `Trips(id, client_id, driver_id, city_id, status, request_at)`: Trip requests and their outcomes.
- `Users(users_id, banned, role)`: User roles and ban status.

**Return value**

Return columns `Day` and `Cancellation Rate` for every qualifying date, with the rate rounded to two decimal places. Row order does not matter.
