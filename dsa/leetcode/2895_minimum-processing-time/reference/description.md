### 1. Description

You have a certain number of processors, each having 4 cores. The number of tasks to be executed is four times the number of processors. Each task must be assigned to a unique core, and each core can only be used once.

You are given an array `processorTime` representing the time each processor becomes available and an array `tasks` representing how long each task takes to complete. Return the *minimum* time needed to complete all tasks.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]

**Output:** 16

**Explanation:**

Assign the tasks at indices 4, 5, 6, 7 to the first processor which becomes available at $time = 8$, and the tasks at indices 0, 1, 2, 3 to the second processor which becomes available at $time = 10$.

The time taken by the first processor to finish the execution of all tasks is $max(8 + 8, 8 + 7, 8 + 4, 8 + 5) = 16$.

The time taken by the second processor to finish the execution of all tasks is $max(10 + 2, 10 + 2, 10 + 3, 10 + 1) = 13$.

</div>
#### Example 2

<div class="example-block">
**Input:** processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]

**Output:** 23

**Explanation:**

Assign the tasks at indices 1, 4, 5, 6 to the first processor and the others to the second processor.

The time taken by the first processor to finish the execution of all tasks is $max(10 + 3, 10 + 5, 10 + 8, 10 + 4) = 18$.

The time taken by the second processor to finish the execution of all tasks is $max(20 + 2, 20 + 1, 20 + 2, 20 + 3) = 23$.

</div>

### 4. Constraints

- $1 \le n = \text{processorTime.length} \le 25000$

- $1 \le \text{tasks.length} \le 10^{5}$

- $0 \le \text{processorTime}[i] \le 10^{9}$

- $1 \le \text{tasks}[i] \le 10^{9}$

- $\text{tasks.length} = 4 * n$