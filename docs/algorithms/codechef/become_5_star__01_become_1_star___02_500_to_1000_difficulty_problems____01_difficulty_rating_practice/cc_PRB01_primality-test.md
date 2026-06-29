# Primality Test

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRB01 |
| Difficulty Rating | 794 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [PRB01](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PRB01) |

---

## Problem Statement

Alice and Bob are meeting after a long time. As usual they love to play some math games. This times Alice takes the call and decides the game. The game is very simple, Alice says out an integer and Bob has to say whether the number is prime or not. Bob as usual knows the logic but since Alice doesn't give Bob much time to think, so Bob decides to write a computer program.

Help Bob accomplish this task by writing a computer program which will calculate whether the number is prime or not.

Note that 1 is not a prime number.

### Input

The first line of the input contains an integer T, the number of testcases. T lines follow.

 Each of the next T lines contains an integer N which has to be tested for primality.

### Output

For each test case output in a separate line, "yes" if the number is prime else "no."

### Constraints

- 1 **≤** **T** **≤** 20

- 1 **≤** **N** **≤** 100000

---

## Examples

**Example 1**

**Input**

```text
5
23
13
20
1000
99991
```

**Output**

```text
yes
yes
no
no
yes
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
23
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
13
```

**Output for this case**

```text
yes
```



#### Test case 3

**Input for this case**

```text
20
```

**Output for this case**

```text
no
```



#### Test case 4

**Input for this case**

```text
1000
```

**Output for this case**

```text
no
```



#### Test case 5

**Input for this case**

```text
99991
```

**Output for this case**

```text
yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Primality Test Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PRB01)

### [](#problem-statement-1)Problem Statement:

Given an integer N, the task is to determine whether it is a prime number or not. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

### [](#approach-2)Approach:

- If `N≤1`, return “no” because 1 is not a prime number.

- Use a boolean variable `isPrime` initialized to `true` .

- Iterate from `2` to less than `N` using a loop.

- If is divisible by any number within this range, set `isPrime` to `false` and break the loop.

- If `isPrime` remains `true` , print “yes”.

- Otherwise, print “no”.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` for each number `N`. This approach is simple but not efficient for large values of `N`.

- **Space Complexity:** `O(1)`, as no additional space is used apart from basic variables.

</details>
