## Description

There are `n` cars traveling at different speeds in the same direction along a one-lane road. You are given an array `cars` of length `n`, where $\text{cars}[i] = [\text{position}_{i}, \text{speed}_{i}]$ represents:

- $\text{position}_{i}$ is the distance between the $$i^{\text{th}}$$ car and the beginning of the road in meters. It is guaranteed that $\text{position}_{i} < \text{position}_{i}+1$.

- $\text{speed}_{i}$ is the initial speed of the $$i^{\text{th}}$$ car in meters per second.

For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the **slowest** car in the fleet.

Return an array `answer`, where $\text{answer}[i]$ is the time, in seconds, at which the $$i^{\text{th}}$$ car collides with the next car, or `-1` if the car does not collide with the next car. Answers within $10^{-5}$ of the actual answers are accepted.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $cars = [[1,2],[2,1],[4,3],[7,2]]$
- **Output:** `[1.00000,-1.00000,3.00000,-1.00000]`
- **Explanation:** After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
#### Example 2

- **Input:** $cars = [[3,4],[5,4],[6,3],[9,1]]$
- **Output:** `[2.00000,1.00000,1.50000,-1.00000]`
### Constraints

- $1 \le \text{cars.length} \le 10^{5}$

- $1 \le \text{position}_{i}, \text{speed}_{i} \le 10^{6}$

- $\text{position}_{i} < \text{position}_{i}+1$