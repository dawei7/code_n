### 1. Description

You are given an integer `mountainHeight` denoting the height of a mountain.

You are also given an integer array `workerTimes` representing the work time of workers in **seconds**.

Each worker may reduce the mountain's height by any **non-negative integer** amount. If worker `i` reduces the height by `x`, then:

- reducing the first unit of height takes $\text{workerTimes}[i]$ seconds,

- reducing the second unit takes $\text{workerTimes}[i] * 2$ seconds,

- ...

- reducing the `x`-th unit takes $\text{workerTimes}[i] * x$ seconds.

The total time spent by worker `i` is the sum of the times required for all `x` units they reduce. As all workers operate simultaneously, the total time required is the **maximum** time spent by any worker.

Return an integer representing the **minimum** number of seconds required for the workers to make the height of the mountain 0.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** mountainHeight = 4, workerTimes = [2,1,1]

**Output:** 3

**Explanation:**

One way the height of the mountain can be reduced to 0 is:

- Worker 0 reduces the height by 1, taking $\text{workerTimes}[0] = 2$ seconds.

- Worker 1 reduces the height by 2, taking $\text{workerTimes}[1] + \text{workerTimes}[1] * 2 = 3$ seconds.

- Worker 2 reduces the height by 1, taking $\text{workerTimes}[2] = 1$ second.

Since they work simultaneously, the minimum time needed is $max(2, 3, 1) = 3$ seconds.

</div>
#### Example 2

<div class="example-block">
**Input:** mountainHeight = 10, workerTimes = [3,2,2,4]

**Output:** 12

**Explanation:**

- Worker 0 reduces the height by 2, taking $\text{workerTimes}[0] + \text{workerTimes}[0] * 2 = 9$ seconds.

- Worker 1 reduces the height by 3, taking $\text{workerTimes}[1] + \text{workerTimes}[1] * 2 + \text{workerTimes}[1] * 3 = 12$ seconds.

- Worker 2 reduces the height by 3, taking $\text{workerTimes}[2] + \text{workerTimes}[2] * 2 + \text{workerTimes}[2] * 3 = 12$ seconds.

- Worker 3 reduces the height by 2, taking $\text{workerTimes}[3] + \text{workerTimes}[3] * 2 = 12$ seconds.

The number of seconds needed is $max(9, 12, 12, 12) = 12$ seconds.

</div>
#### Example 3

<div class="example-block">
**Input:** mountainHeight = 5, workerTimes = [1]

**Output:** 15

**Explanation:**

There is only one worker in this example, so the answer is $\text{workerTimes}[0] + \text{workerTimes}[0] * 2 + \text{workerTimes}[0] * 3 + \text{workerTimes}[0] * 4 + \text{workerTimes}[0] * 5 = 15$.

</div>

### 4. Constraints

- $1 \le mountainHeight \le 10^{5}$

- $1 \le \text{workerTimes.length} \le 10^{4}$

- $1 \le \text{workerTimes}[i] \le 10^{6}$