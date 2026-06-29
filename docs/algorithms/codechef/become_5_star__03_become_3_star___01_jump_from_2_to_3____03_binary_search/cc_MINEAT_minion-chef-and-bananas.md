# Minion Chef and Bananas

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINEAT |
| Difficulty Rating | 1781 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [MINEAT](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/MINEAT) |

---

## Problem Statement

Minion Chef likes to eat bananas a lot. There are **N** piles of bananas in front of Chef; for each **i** (1 ≤ **i** ≤ **N**), the **i**-th pile contains **Ai** bananas.

Chef's mother wants her to eat the bananas and be healthy. She has gone to the office right now and will come back in **H** hours. Chef would like to make sure that she can finish eating all bananas by that time.

Suppose Chef has an *eating speed* of **K** bananas per hour. Each hour, she will choose some pile of bananas. If this pile contains at least **K** bananas, then she will eat **K** bananas from it. Otherwise, she will simply eat the whole pile (and won't eat any more bananas during this hour).

Chef likes to eat slowly, but still wants to finish eating all the bananas on time. Therefore, she would like to choose the minimum **K** such that she is able to eat all the bananas in **H** hours. Help Chef find that value of **K**.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains two space-separated integers **N** and **H** denoting the number of piles and the number of hours after which Chef's mom will come home.

- The second line contains **N** space-separated integers **A1, A2, ..., AN**.

### Output

For each test case, print a single line containing one integer — the minimum possible value of **K**.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- **N** ≤ **H** ≤ 109

- 1 ≤ **Ai** ≤ 109 for each valid **i**

### Subtasks

**Subtask #1 (30 points):**

- 1 ≤ **N** ≤ 100

- **Ai** ≤ 103 for each valid **i**

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
3 3
1 2 3
3 4
1 2 3
4 5
4 3 2 7
```

**Output**

```text
3
2
4
```

**Explanation**

**Test case $1$:** Chef can choose $K = 3$ bananas per hour. This way,
- In the first hour, Chef eats the pile $1$ as the number of bananas in the pile is less than equal to $3$.
- In the second hour, Chef eats the pile $2$ as the number of bananas in the pile is less than equal to $3$.
- In the third hour, Chef eats the pile $3$ as the number of bananas in the pile is less than equal to $3$.

 Chef can finish eating all the bananas in $3$ hours. It can be shown that $3$ bananas per hour is the minimum possible speed with which Chef can finish all bananas in $3$ hours.

**Test case $2$:** Chef can choose $K = 2$ bananas per hour. This way,
- In the first hour, Chef eats the pile $1$ as the number of bananas in the pile is less than equal to $2$.
- In the second hour, Chef eats the pile $2$ as the number of bananas in the pile is less than equal to $2$.
- In the third hour, Chef eats the $2$ bananas from pile $3$. $1$ banana is left in pile $3$.
- In the fourth hour, Chef eats the remaining banana from pile $3$ as the number of bananas in the pile is less than equal to $2$.

 Chef can finish eating all the bananas in $4$ hours. It can be shown that $2$ bananas per hour is the minimum possible speed with which Chef can finish all bananas in $4$ hours.

**Test case $3$:** Chef can choose $K = 4$ bananas per hour. This way,
- In the first hour, Chef eats the pile $1$ as the number of bananas in the pile is less than equal to $4$.
- In the second hour, Chef eats the pile $2$ as the number of bananas in the pile is less than equal to $4$.
- In the third hour, Chef eats the pile $3$ as the number of bananas in the pile is less than equal to $4$.
- In the fourth hour, Chef eats the $4$ bananas from pile $4$. $3$ bananas are left in pile $4$.
- In the fifth hour, Chef eats the remaining bananas from pile $4$ as the number of bananas in the pile is less than equal to $4$.

 Chef can finish eating all the bananas in $5$ hours. It can be shown that $4$ bananas per hour is the minimum possible speed with which Chef can finish all bananas in $5$ hours.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
1 2 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 4
1 2 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 5
4 3 2 7
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINK:

[Div1](http://www.codechef.com/MARCH18A/problems/MINEAT), [Div2](http://www.codechef.com/MARCH18B/problems/MINEAT)

[Practice](http://www.codechef.com/problems/MINEAT)

**Author:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Tester:** [Triveni Mahatha](http://www.codechef.com/users/triveni)

**Editorialist:** [Adarsh Kumar](http://www.codechef.com/users/adkroxx)

## DIFFICULTY:

Easy-Medium

## PREREQUISITES:

Binary search

## PROBLEM:

You are given an array A of N integers. You need to find the smallest K that satisfies this inequality; \sum \limits_{i=1}^N \left \lceil \frac{A[i]}{K} \right \rceil \le H, where \left \lceil \right \rceil indicates the [ceil function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions).

## EXPLANATION:

According to the problem statement, Chef will need \left \lceil \frac{A[i]}{K} \right \rceil hours to finish the i^{th} pile. Hence, we need to find the smallest K that satisfies this inequality; \sum \limits_{i=1}^N \left \lceil \frac{A[i]}{K} \right \rceil \le H.

### subtask #1
Iterate over values of $K$ from $1$ to $MAX$ and break whenever you find the solution. Time complexity for the same will be $O(N.MAX)$, where $MAX$ is maximum element that can be present in the array.

### subtask #2
For this subtask we need something better than brute-force. Hence, we will try to make some-observations first. Lets name the left side of our function as cost function. Observe that, our cost function is inversely proportional to $K$. Our cost function will decrease while $K$ increases. At some point it will become smaller than $H$. We need to find this point. Observe that, this problem has reduced to standard formulation of binary search problem. We just need to binary search on values of $K$ now and change the limits of $K$ according to the difference between our cost function and $H$. For more implementation details, you can have a look at attached solutions.

## Time Complexity:

O(N.log(MAX))

## AUTHOR’S AND TESTER’S SOLUTIONS

[Setter’s solution](http://www.codechef.com/download/Solutions/MARCH18/Setter/MINEAT.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/MARCH18/Tester/MINEAT.cpp)

</details>
