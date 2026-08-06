## Description

An analysis uses three tables: `Drivers` records each driver's identity, experience, and accident count; `Vehicles` associates drivers with their vehicles and fuel types; and `Trips` records the distance, duration, and passenger rating for each vehicle's completed trips. Evaluate driver performance separately within every fuel type represented by completed trips.

For each driver and fuel type, compute the average rating across all matching trips and the total distance of those trips. Select the driver with the greatest average; break an average tie by greater total distance, and then by fewer accidents. Report one winner per fuel type with the average rounded to two decimal places, and order the result by `fuel_type` in ascending order.
