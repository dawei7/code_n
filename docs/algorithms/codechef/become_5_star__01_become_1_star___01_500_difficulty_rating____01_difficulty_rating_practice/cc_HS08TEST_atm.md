# ATM

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HS08TEST |
| Difficulty Rating | 410 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [HS08TEST](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HS08TEST) |

---

## Problem Statement

Pooja would like to withdraw X US Dollar from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges).  For each successful withdrawal the bank charges 0.50 US Dollar.

Calculate Pooja's account balance after an attempted transaction.

---

## Input Format

Each input contains 2 numbers $X$ and $Y$. \
$X$ is the amount of cash which Pooja wishes to withdraw. \
$Y$ is Pooja's initial account balance.

---

## Output Format

Output the account balance after the attempted transaction, given as a number with two digits of precision.  If there is not enough money in the account to complete the transaction, output the current bank balance.

---

## Constraints

- $0 \lt X \leq 2000$ - the amount of cash which Pooja wishes to withdraw.
- $0 \leq Y \leq 2000$ with two digits of precision - Pooja's initial account balance.

---

## Examples

**Example 1**

**Input**

```text
30 120.00
```

**Output**

```text
89.50
```

**Explanation**

Example - Successful Transaction

**Example 2**

**Input**

```text
42 120.00
```

**Output**

```text
120.00
```

**Explanation**

Example - Incorrect Withdrawal Amount (not multiple of 5)

**Example 3**

**Input**

```text
300 120.00
```

**Output**

```text
120.00
```

**Explanation**

Example - Insufficient Funds

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/HS08TEST)

**Author:** [ADMIN](http://www.codechef.com/users/admin)

**Editorialist:** [SUSHANT AGARWAL](http://www.codechef.com/users/sushant96)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

Basic looping,Basic Input/Output,Data Types

### EXPLANATION:

Please refer to the sample solution given by editorialist.

### EDITORIALIST’S SOLUTION:

Editorialist’s solution can be found [here](http://www.codechef.com/viewsolution/5608929).

</details>
