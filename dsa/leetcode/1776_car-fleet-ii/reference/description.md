## Description

There are `n` cars traveling at different speeds in the same direction along a one-lane road. You are given an array `cars` of length `n`, where `cars[i] = [position_i, speed_i]` represents:

<ul>
	<li>`position_i` is the distance between the `i^th` car and the beginning of the road in meters. It is guaranteed that `position_i < position_i+1`.</li>
	<li>`speed_i` is the initial speed of the `i^th` car in meters per second.</li>
</ul>

For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the **slowest** car in the fleet.

Return an array `answer`, where `answer[i]` is the time, in seconds, at which the `i^th` car collides with the next car, or `-1` if the car does not collide with the next car. Answers within `10^-5` of the actual answers are accepted.
