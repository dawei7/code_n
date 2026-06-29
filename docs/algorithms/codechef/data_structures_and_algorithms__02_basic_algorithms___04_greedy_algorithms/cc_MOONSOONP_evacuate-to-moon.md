# EVacuate to Moon

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MOONSOONP |
| Difficulty Rating | 1479 |
| Difficulty Band | Greedy Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Greedy Algorithms |
| Official Link | [MOONSOONP](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA03/problems/MOONSOONP) |

---

## Problem Statement

Pesla needs to charge $N$ cars before sending them to space. The $i^{th}$ car has an energy capacity $A_i$ Watt-hours.

There are $M$ power outlets. The $j^{th}$ outlet provides a power of $B_j$ Watt.
If an outlet can charge **at most** one car and a car can be charged by **at most** one outlet, find the **maximum** total energy (in Watt-hours) stored in all cars after $H$ hours.

Note:
- A power outlet **cannot** charge a different car even after completely charging a car.
- Energy is the product of power and time. For instance, a car can store $1$ Watt-hour of energy if it is charged at a power station with $1$ Watt power for $1$ hour.

---

## Input Format

- The first line of input will contain a single integer $T$, the number of test cases.
- The first line of each test case contains $3$ space-separated integers $N$, $M$, and $H$, the number of cars, the number of power outlets, and the number of hours respectively.
- The second line of each test case contains $N$ space-separated integers, the energy capacities (in Watt-hour) of the $N$ cars.
- The third line of each test case contains $M$ space-separated integers, the power (in Watt) of the $M$ power outlets.

---

## Output Format

For each test case, print the maximum total energy (in Watt-hours) stored in all cars after $H$ hours.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, M, H, A_i, B_i\leq 10^5$
- The sum of $N$ over all test cases won't exceed $10^5$.
- The sum of $M$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1 2 2
100
20 40
2 1 2
10 20
11
3 2 1
30 30 30
40 20
```

**Output**

```text
80
20
50
```

**Explanation**

**Test case $1$:** We use the second power outlet to charge the car. After $2$ hours, $40\cdot2 = 80$ watt-hours of energy is stored in the car.

**Test case $2$:** We use the power outlet to charge the second car. After $2$ hours, $11\cdot2 = 22$ watt-hours of energy is generated but since the car has the capacity of $20$, it will store only $20$ watt-hours of energy.

**Test case $3$:** We use the first power outlet to charge the first car and second outlet to charge the second car. After $1$ hour, the first car will store $30$ watt-hours of energy (due to its maximum capacity) and second car will store $20$ watt-hours of energy.

Thus, the cars will store a total of $50$ watt-hours of energy.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 2
100
20 40
```

**Output for this case**

```text
80
```



#### Test case 2

**Input for this case**

```text
2 1 2
10 20
11
```

**Output for this case**

```text
20
```



#### Test case 3

**Input for this case**

```text
3 2 1
30 30 30
40 20
```

**Output for this case**

```text
50
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [EVacuate to Moon in Greedy Algorithms](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA03/problems/MOONSOONP)

### [](#problem-statement-1)Problem Statement:

Pesla needs to charge N cars before sending them to space. The ith car has an energy capacity of A_i Watt-hours.

There are M power outlets. The jth outlet provides a power of B_j Watt.

If an outlet can charge at most one car and a car can be charged by at most one outlet, find the maximum total energy (in Watt-hours) stored in all cars after H hours.

### [](#approach-2)Approach:

**1. Understanding the Problem**:

- Each car has a maximum energy capacity.

- Each power outlet provides a certain power and can charge one car for a given duration.

- The total energy stored in each car after charging is the minimum of the energy supplied by the outlet (based on its power and time) and the car’s capacity.

**2. Calculating Energy**:

- For each outlet, calculate the total energy it can provide over the given time, which is `B[j] * H`.

- Sort both the car capacities and the calculated energies from the outlets in descending order.

- Use a greedy strategy to assign the highest available energy to the highest capacity car, ensuring that no outlet is reused and no car is charged more than once.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(NlogN + MlogM)` for sorting the car capacities and outlet energies. The rest of the operations are linear, i.e.,  `O(min(N, M))` for each test case. Total time complexity: `O(NlogN + MlogM)`.

- **Space Complexity:** `O(1)` For auxiliary space , `O(N + M)` for input space.

</details>
