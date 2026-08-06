## Description

`Drivers` records when each driver joined Hopper. `Rides` records ride requests and their request dates, including requests that were never accepted. `AcceptedRides` identifies accepted requests and the driver who completed each one.

For every month of 2020, calculate the percentage of active drivers who worked during that month. A driver is active in a month if the driver joined by that month's final day. A driver is working in a month if that driver completed at least one accepted ride whose request date falls in the month; multiple accepted rides by the same driver still count that driver once.

If a month has no active drivers, report 0. Round percentages to two decimal places and return all twelve months in ascending numeric order.
