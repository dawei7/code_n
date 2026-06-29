# When to take medicine

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEDIC |
| Difficulty Rating | 1522 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [MEDIC](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/MEDIC) |

---

## Problem Statement

You visit a doctor on a date given in the format $yyyy:mm:dd$. Your doctor suggests you to take pills every alternate day starting from that day. You being a forgetful person are pretty sure won’t be able to remember the last day you took the medicine and would end up in taking  the medicines on wrong days.

So you come up with the idea of taking medicine on the dates whose day is odd or even depending on whether $dd$ is odd or even. Calculate the number of pills you took on right time before messing up for the first time.

###Note:
Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100; the centurial years that are exactly divisible by 400 are still leap years. For example, the year 1900 is not a leap year; the year 2000 is a leap year.

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, in the format $yyyy:mm:dd$

###Output:
For each testcase, output in a single line the required answer.

###Constraints
- $ 1 \leq T \leq 1000 $
- $ 1900 \leq yyyy \leq 2038 $
- $yyyy:mm:dd$ is a valid date

---

## Examples

**Example 1**

**Input**

```text
1
2019:03:31
```

**Output**

```text
1
```

**Explanation**

You can take pill on the right day only on 31st March. Next you will take it on 1st April which is not on the alternate day.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [When to take medicine Practice Problem in 1400 to 1600 difficulty problems](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/MEDIC)

### [](#problem-statement-1)Problem Statement:

In this problem, you are given a starting date, and you’re supposed to take medicine every alternate day. The challenge is to count how many days you take the medicine on the “right” day, which is defined as:

- You take the medicine on a day if the day of the month is either odd or even, depending on whether the starting day (given in the input) is odd or even.

You need to calculate how many times you take the medicine correctly before you mess up (i.e., when the day of the month is wrong, based on the alternating pattern).

### [](#approach-2)Approach:

- **Leap Year Function**: A helper function to check if a given year is a leap year.

- **Day Calculation**: A function to check how many days are in a given month, considering whether the year is a leap year or not. A year is a leap year if it is divisible by `4`, but not divisible by `100`, unless also divisible by `400`.

- **Main Logic**:

- Start with the given date.

- Alternate the day by adding `2` days.

- If the current day matches the alternating pattern (odd or even), we increment the count. Check if the day of the month is valid (either odd or even).

- Stop when the alternation pattern is violated.

### [](#complexity-3)Complexity:

- **Time Complexity:** The complexity per test case is proportional to the number of days in a year (since we are iterating day by day). For a year, this would be at most `365` days (or `366` in a leap year).

- **Space Complexity:** The space complexity is `O(1)` as we are only storing a few variables and not using any large data structures.

</details>
