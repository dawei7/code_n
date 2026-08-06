## Description

The `cities` table contains one row for every unique `(state, city)` pair. Summarize the cities belonging to each state, but retain only states that contain at least three cities and have at least one city whose first letter matches the first letter of the state name.

For every retained state, combine all of its city names into one comma-and-space-separated string ordered alphabetically. Also report how many of those cities begin with the state's initial letter. Sort the final rows by that matching-city count from largest to smallest; when counts tie, sort state names in ascending alphabetical order.
