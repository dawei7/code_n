# Jumping in the hills

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HILLS |
| Difficulty Rating | 1216 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [HILLS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/HILLS) |

---

## Problem Statement

There are **N** hills in a row numbered 1 through **N** from left to right. Each hill has a height; for each valid **i**, the height of the **i**-th hill is **Hi**. Chef is initially on the leftmost hill (hill number 1). He can make an arbitrary number of jumps (including zero) as long as the following conditions are satisfied:

- Chef can only jump from each hill to the next hill, i.e. from the **i**-th hill, he can jump to the **i+1**-th hill (if it exists).

- It's always possible to jump to a hill with the same height as the current hill.

- It's possible to jump to a taller hill if it's higher than the current hill by no more than **U**.

- It's possible to jump to a lower hill if it's lower than the current hill by no more than **D**.

- Chef can use a parachute and jump to a **lower** hill regardless of its height (as long as it's lower than the current hill). This jump can only be performed at most once.

Chef would like to move as far right as possible. Determine the index of the rightmost hill Chef can reach.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains three space-separated integers **N**, **U** and **D**.

- The second line contains **N** space-separated integers **H1, H2, ..., HN**.

### Output

For each test case, print a single line containing one integer — the index of the rightmost reachable hill.

### Constraints

- 1 ≤ **T** ≤ 100

- 1 ≤ **N** ≤ 100

- 1 ≤ **U**, **D** ≤ 1,000,000

- 1 ≤ **Hi** ≤ 1,000,000 for each valid **i**

### Subtasks

**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 3 2
2 5 2 6 3
5 2 3
4 4 4 4 4
5 2 7
1 4 3 2 1
```

**Output**

```text
3
5
1
```

**Explanation**

**Example case 1:** Chef can jump to second hill because it's higher by no more than **U**=3 than first hill, to jump to third hill Chef has to use parachute
 because it's lower than second hill by 3 which is more than **D**=2, Chef can't jump to fourth hill because it's higher than third hill by 4 which is more than **U**=3

**Example case 2:** All hills are of the same height, so chef can reach the last hill with no problems.

**Example case 3:** Chef can't jump to second hill because it's too high for him

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3 2
2 5 2 6 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5 2 3
4 4 4 4 4
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
5 2 7
1 4 3 2 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/HILLS)

[Contest](http://www.codechef.com/LTIME57/problems/HILLS)

**Author:** [Hasan Jaddouh](http://www.codechef.com/users/kingofnumbers)

**Tester:** [Misha Chorniy](http://www.codechef.com/users/mgch)

**Editorialist:** [Suchan Park](http://www.codechef.com/users/tncks0121)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

There are N hills in a row. The height of the i-th hill is H[i]. Chef is initially on the 1st hill.

When Chef is at hill i, Chef can jump to the adjacent hill j if and only if H[i] - D \le H[j] \le H[j] + U without a parachute, and H[j] < H[i] with a parachute. Chef is allowed to use the parachute *at most once*.

Find the rightmost hill that the Chef can reach.

### QUICK EXPLANATION:

Simulate the whole process. Use the parachute as late as possible.

### EXPLANATION:

Since the Chef can only jump to the adjacent hill, we can make a `for`-loop that iterates the current position of Chef.

Using the parachute when the Chef can jump without the parachute is obviously a waste. Therefore the Chef should continuously jump without a parachute as long as he can.

So, we can simulate the whole process using a `for` loop, like this:

``for i = 1 to N: // i denotes the position of the Chef
  if (i == N) {
    // If the Chef is on the rightmost hill,
    // there is nothing to do.
  }
  else if (H[i] - D <= H[i+1] <= H[i] + U) {
    // if the Chef is able to jump on his own,
    // just jump without a parachute
  }
  else if (H[i+1] < H[i]) {
    // Chef can jump if the parachute is left

    if(parachute isn't used) {
      Use the parachute.
    }else {
      Break the loop. (since the Chef cannot jump)
    }
  }
  else {
    // Chef cannot jump when the next hill is too high

    Break the loop. (since the Chef cannot jump)
  }
``

One can check whether the parachute is used or not by setting a boolean-type variable. (true if used, false otherwise)

The answer will be the maximum i visited during the loop.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME57/Setter/HILLS.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME57/Tester/HILLS.cpp).

</details>
