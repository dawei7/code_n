## Description

`Drivers` records when drivers joined Hopper. `Rides` records ride requests and their request dates, including requests that were never accepted. `AcceptedRides` identifies the accepted requests and stores each accepted ride's distance and duration.

For every consecutive three-month window wholly contained in 2020, compute the average monthly accepted-ride distance and duration. The first window is January through March and the last is October through December. For each metric, sum all accepted-ride values across the window and divide by 3, including zero for a month with no accepted rides. Round both results to two decimal places.
