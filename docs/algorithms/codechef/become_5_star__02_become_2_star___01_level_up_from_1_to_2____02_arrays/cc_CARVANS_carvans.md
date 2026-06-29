# Carvans

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CARVANS |
| Difficulty Rating | 1264 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [CARVANS](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/CARVANS) |

---

## Problem Statement

Most problems on CodeChef highlight chef's love for food and cooking but little is known about his love for racing sports. He is an avid Formula 1 fan. He went to watch this year's Indian Grand Prix at New Delhi. He noticed that one segment of the circuit was a long straight road. It was impossible for a car to overtake other cars on this segment. Therefore, a car had to lower down its speed if there was a slower car in front of it. While watching the race, Chef started to wonder how many cars were moving at their maximum speed.

Formally, you're given the maximum speed of N cars in the order they entered the long straight segment of the circuit. Each car prefers to move at its maximum speed. If that's not possible because of the front car being slow, it might have to lower its speed. It still moves at the fastest possible speed while avoiding any collisions. For the purpose of this problem, you can assume that the straight segment is infinitely long.

Count the number of cars which were moving at their maximum speed on the straight segment.

### Input

The first line of the input contains a single integer T denoting the number of test cases to follow. Description of each test case contains 2 lines. The first of these lines contain a single integer N, the number of cars. The second line contains N space separated integers, denoting the maximum speed of the cars in the order they entered the long straight segment.

### Output

For each test case, output a single line containing the number of cars which were moving at their maximum speed on the segment.

### Constraints

1 ≤ T ≤ 100

1 ≤ N ≤ 10,000

All speeds are distinct positive integers that fit in a 32 bit signed integer.

Each input file will not be larger than 4 MB (4,000,000,000 bytes) in size.

**WARNING!** The input files are very large. Use faster I/O.

---

## Examples

**Example 1**

**Input**

```text
3
1
10
3
8 3 6
5
4 5 1 2 3
```

**Output**

```text
1
2
2
```

**Explanation**

**Test case $1$:** There is only $1$ car. Thus, it can move at its maximum speed.

**Test case $2$:** The first car moves at speed $8$. The second car can move at speed $3$ without colliding with the first car. For the third car, if it moves at speed $6$, it would collide with the second car after some finite amount of time. The maximum speed at which the third car can move avoiding any collision is $3$. Thus, $2$ cars can move at their maximum speed.

**Test case $3$:** Following are the maximum speeds of all the cars.
- The first car moves at a maximum speed of $4$.
- The maximum speed at which the second car can move without colliding is $4$.
- The third car can move at its maximum speed which is $1$.
- The maximum speed at which the fourth car can move without colliding is $1$.
- The maximum speed at which the fifth car can move without colliding is $1$.

Thus, two cars can move at their maximum speed. These cars are car $1$ and $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
10
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
8 3 6
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
4 5 1 2 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CARVANS)

[Contest](http://www.codechef.com/COOK26/problems/CARVANS)

## DIFFICULTY

CAKEWALK

## PREREQUISITES

Simple Math

## PROBLEM

There are N cars on a narrow road that are moving in the same direction. Each car has maximum speed. No car can overtake other cars on this road. Each car will move at the maximum possible speed while avoiding any collisions. Count the number of cars which are moving at their maximum speeds.

## QUICK EXPLANATION

Intuitively, a car is moving at its maximum speed if and only if all cars in front of it are moving at greater speeds (otherwise it will overtake the slower car). Therefore, the answer is the number of such cars.

## EXPLANATION

Suppose that the cars are numbered 1 through N from front to back, and the maximum speed of the i-th car is maxSpeed[i]. From the intuitive observation above, we can directly come up with this naive solution:

`
answer = 0
for i = 1; i <= N; i++:
    allGreater = true
    for j = 1; j <= i-1; j++:
        if maxSpeed[j] < maxSpeed[i]:
            allGreater = false
    if allGreater:
        answer = answer + 1
`

Unfortunately, this solution runs in O(N^2) time, which will surely time out. We will need other observations.

Consider each car. From the problem statement, each car will:

- Avoid any collisions. Since the road is narrow, therefore, it will not move at greater speed than the car directly in front of it (if any).

- Move at the maximum possible speed. Therefore, it will move at speed of exactly min(the maximum speed of the car, the speed of the car directly in front of it).

From those observations, we can calculate the speed of each car in O(1) time. When calculating the speed of the i-th car, we have to know the speed of the (i-1)st car. Therefore, we must calculate the speeds in the right order (i.e., from the first car to the last car on the road). After that, we compare the speed of each car with its maximum speed.

A direct implementation of the above solution is as follows. This solution runs in O(N) time, which will pass the time limit.

`
answer = 0

speed[1] = maxSpeed[1]
for i = 2; i <= N; i++:
    speed[i] = min(maxSpeed[i], speed[i-1])

for i = 1; i <= N; i++:
    if speed[i] == maxSpeed[i]:
        answer = answer + 1
`

Exercise

Try to solve this problem without creating the additional speed[]/maxSpeed[] array. Hint: we can always store only the speed of the last car we consider instead of storing all speeds in speed[] array.

## SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK26/Setter/CARVANS.py)

## TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK26/Tester/CARVANS.cpp).

</details>
