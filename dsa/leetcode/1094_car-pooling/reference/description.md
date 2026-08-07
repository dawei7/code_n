## Description

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where $\text{trips}[i] = [\text{numPassengers}_{i}, \text{from}_{i}, \text{to}_{i}]$ indicates that the $$i^{\text{th}}$$ trip has $\text{numPassengers}_{i}$ passengers and the locations to pick them up and drop them off are $\text{from}_{i}$ and $\text{to}_{i}$ respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `true`* if it is possible to pick up and drop off all passengers for all the given trips, or *`false`* otherwise*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $trips = [[2,1,5],[3,3,7]], capacity = 4$
- **Output:** `false`
#### Example 2

- **Input:** $trips = [[2,1,5],[3,3,7]], capacity = 5$
- **Output:** `true`
### Constraints

- $1 \le \text{trips.length} \le 1000$

- $\text{trips}[i].length = 3$

- $1 \le \text{numPassengers}_{i} \le 100$

- $0 \le \text{from}_{i} < \text{to}_{i} \le 1000$

- $1 \le capacity \le 10^{5}$