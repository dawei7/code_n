# The Block Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PALL01 |
| Difficulty Rating | 830 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [PALL01](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/PALL01) |

---

## Problem Statement

The citizens of Byteland regularly play a game. They have blocks each denoting some integer from 0 to 9. These are arranged together in a random manner without seeing to form different numbers keeping in mind that the first block is never a 0. Once they form a number they read in the reverse order to check if the number and its reverse is the same. If both are same then the player wins. We call such numbers *palindrome*.

Ash happens to see this game and wants to simulate the same in the computer. As the first step he wants to take an input from the user and check if the number is a palindrome and declare if the user wins or not.

### Input

The first line of the input contains T, the number of test cases. This is followed by T lines containing an integer N.

### Output

For each input output "wins" if the number is a palindrome and "loses" if not, in a new line.

### Constraints

1<=T<=20

1<=N<=20000

---

## Examples

**Example 1**

**Input**

```text
3
331
666
343
```

**Output**

```text
loses
wins
wins
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
331
```

**Output for this case**

```text
loses
```



#### Test case 2

**Input for this case**

```text
666
```

**Output for this case**

```text
wins
```



#### Test case 3

**Input for this case**

```text
343
```

**Output for this case**

```text
wins
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [The Block Game Practice Problem in 500 to 1000 difficulty problems](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/PALL01)

### [](#problem-statement-1)Problem Statement:

The problem asks to determine whether a given number is a **palindrome**. A number is considered a **palindrome** if it reads the same from both ends. In other words, if the number is reversed, it should remain identical to the original number.

The task is to take multiple test cases, check each number, and determine if it is a palindrome or not, outputting “wins” if it’s a palindrome and “loses” if it is not.

### [](#approach-2)Approach:

To solve this problem, we can use the reverse of a number and compare it to the original number.

**Reverse the Number Using Modulo and Division**:

- For a given number `N`, we can reverse the number using the following steps:

- Take the last digit of `N` using `N % 10`.

- Append this digit to a new number, which is initially set to 0, by multiplying the new number by 10.

- Divide `N` by 10 to remove the last digit.

- Continue this process until `N` becomes 0.

- The new number generated will be the reverse of the original number.

**Check for Palindrome**:

- After reversing the number, compare the reversed number with the original number.

- If they are equal, then the number is a palindrome and the output is “wins”.

- If they are not equal, the output is “loses”.

### [](#complexity-3)Complexity;

- **Time Complexity:** The time complexity for each test case is `O(d)` where `d` is the number of digits in the number `N`.

- **Space Complexity:** `O(1)` since we are only using a constant amount of extra space.

</details>
