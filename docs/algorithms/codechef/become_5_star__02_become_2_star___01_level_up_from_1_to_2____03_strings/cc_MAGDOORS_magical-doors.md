# Magical Doors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAGDOORS |
| Difficulty Rating | 1355 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [MAGDOORS](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/MAGDOORS) |

---

## Problem Statement

Chef wants to cross a hallway of $N$ doors. These $N$ doors are represented as a string. Each door is initially either open or close, represented by $1$ or $0$ respectively. Chef is required to go through all the doors one by one in the order that they appear, starting from the leftmost door and moving only rightwards at each step.

To make the journey easier, Chef has a magic wand, using which Chef can flip the status of all the doors at once.
Determine the minimum number of times Chef has to use this wand to cross the hallway of doors.

For example, the doors are $10011$. Chef will start from the left and enter the first door. After passing through that door, the magic wand is waved. This flips the string to $01100$. Now Chef passes through the next two doors in one go. Again, just before reaching the 4th door, the magic wand is waved. Now that the string is in its original state, Chef passes through the last two doors as well.
The minimum number of times the magic wand needed to be used here was $2$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single string $S$, representing the doors as given in the problem.

---

## Output Format

For each test case, print a single line containing one integer denoting the minimum number of times the magic wand needs to be used.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq |S| \leq 10^5$
- Sum of $|S|$ over all test cases $ \leq 2 \cdot 10^6 $

---

## Examples

**Example 1**

**Input**

```text
3
111
010
10011
```

**Output**

```text
0
3
2
```

**Explanation**

- **Test Case $1$**: Since all the doors are already open, Chef doesn't need to use the magic wand at all.
- **Test Case $2$**: Chef will use the wand the first time to open door $1$. This operation makes the string "101". Chef again needs to use the wand to open door $2$, and then one last time to open door $3$. In total, Chef used the wand $3$ times.
- **Testcase $3$**: As explained in the problem statement above.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
111
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
010
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
10011
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START13C/problems/MAGDOORS)

[Contest - Division 2](https://www.codechef.com/START13B/problems/MAGDOORS)

[Contest - Division 1](https://www.codechef.com/START13A/problems/MAGDOORS)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#problem-3)PROBLEM:

You are standing in front of a hallway with N consecutive doors. You want to cross through the N doors.

You may only walk through open doors. You also have a magic wand, that can flip the state of all doors. Determine the minimum number of times you need to use the wand.

#
[](#explanation-4)EXPLANATION:

The solution is rather straightforward.

If the door we have to cross is open, simply walk through it (it makes no sense to use the wand and close the door) and if the door is closed, use the wand, flipping the status of all doors, and then walk through the door.

All that remains is to implement the above idea efficiently. Everytime we use the wand, it is inefficient to manually flip the status of all doors.

Rather, if we have used the wand k times thus far, the status of any door is equal to its initial state if k is even, and is flipped otherwise (the proof of which is trivial and left to the reader as an exercise).

Therefore, we iterate through the doors from left to right, and in each step, check if the door is open or closed (with the above trick) and use the wand appropriately.

#
[](#time-complexity-5)TIME COMPLEXITY:

Since we iterate through the N doors once, the total time complexity is

O(N)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51712438).

Author’s solution can be found [here](https://www.codechef.com/viewsolution/51709994).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
