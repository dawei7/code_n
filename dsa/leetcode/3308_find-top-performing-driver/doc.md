# Find Top Performing Driver

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3308 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-top-performing-driver/) |

## Problem Description

### Goal

An analysis uses three tables: `Drivers` records each driver's identity, experience, and accident count; `Vehicles` associates drivers with their vehicles and fuel types; and `Trips` records the distance, duration, and passenger rating for each vehicle's completed trips. Evaluate driver performance separately within every fuel type represented by completed trips.

For each driver and fuel type, compute the average rating across all matching trips and the total distance of those trips. Select the driver with the greatest average; break an average tie by greater total distance, and then by fewer accidents. Report one winner per fuel type with the average rounded to two decimal places, and order the result by `fuel_type` in ascending order.

### Function Contract

**Inputs**

- `Drivers(driver_id, name, age, experience, accidents)`: One row per driver; `driver_id` is unique.
- `Vehicles(vehicle_id, driver_id, model, fuel_type, mileage)`: Vehicle assignments and their fuel types.
- `Trips(trip_id, vehicle_id, distance, duration, rating)`: Completed trips, including integer passenger ratings from 1 through 5.

`Vehicles.driver_id` refers to `Drivers.driver_id`, and `Trips.vehicle_id` identifies the vehicle used for each trip.

**Return value**

Return columns `fuel_type`, `driver_id`, `rating`, and `distance`. `rating` is the winning driver's average trip rating rounded to two decimals, and `distance` is that driver's total trip distance for the fuel type. Sort rows by `fuel_type` ascending.

### Examples

#### Example 1

- **Input:** Alice and Charlie drive gasoline vehicles with average ratings 4.5 and 5.0; Bob drives an electric vehicle with average rating 4.5. Their total distances are 80, 100, and 180 respectively.
- **Output:** `[("Electric", 2, 4.50, 180), ("Gasoline", 3, 5.00, 100)]`

Charlie wins the gasoline partition by rating, while Bob is the only electric driver with completed trips.
