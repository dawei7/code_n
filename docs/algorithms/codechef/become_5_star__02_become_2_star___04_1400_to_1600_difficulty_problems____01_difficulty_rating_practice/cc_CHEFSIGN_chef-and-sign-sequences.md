# Chef and Sign Sequences

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSIGN |
| Difficulty Rating | 1563 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [CHEFSIGN](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/CHEFSIGN) |

---

## Problem Statement

Chef found a strange string yesterday - a string of signs **s**, where each sign is either a **'<'**, **'='** or a **'>'**. Let N be the length of this string. Chef wants to insert N + 1 positive integers into this sequence and make it valid. A valid sequence is a sequence where every sign is preceded and followed by an integer, and the signs are correct. That is, if a sign '<' is preceded by the integer *a* and followed by an integer *b*, then *a* should be less than *b*. Likewise for the other two signs as well.

Chef can take some positive integers in the range **[1, P]** and use a number in the range as many times as he wants.

Help Chef find the minimum possible **P** with which he can create a valid sequence.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains the string of signs **s**, where each sign is either **'<'**, **'='** or a **'>'**.

### Output

For each test case, output a single line containing an integer corresponding to the minimum possible **P**.

### Constraints

- 1 ≤ **T, |s|** ≤ 105

- 1 ≤ Sum of **|s|** over all test cases in a single test file ≤ 106

### Subtasks

**Subtask #1 (30 points)**

- 1 ≤ **T, |s|** ≤ 103

- 1 ≤ Sum of **|s|** over all test cases in a single test file ≤ 104

**Subtask #2 (70 points)**

- Original constraints

---

## Examples

**Example 1**

**Input**

```text
4
<<<
<><
<=>
<=<
```

**Output**

```text
4
2
2
3
```

**Explanation**

Here are some possible valid sequences which can be formed with the minimum **P** for each of the test cases:

`
1 < 2 < 3 < 4
1 < 2 > 1 < 2
1 < 2 = 2 > 1
1 < 2 = 2 < 3
`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
<<<
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
<><
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
<=>
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
<=<
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/JULY17/problems/CHEFSIGN)

[Contest](https://www.codechef.com/problems/CHEFSIGN)

**Author:** [Dmytro Berezin](https://www.codechef.com/users/berezin)

**Primary Tester:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

Given a sequence of **N** arithmetic signs **( = , + , - )** between **N+1** unknown integers. You are allowed to fix these integers using numbers in the range [1,P] such that the expression is true when you read it from left to right. (Numbers don’t violate the signs). You are asked to calculate **minimum** possible **P** such you can construct a valid expression.

### EXPLANATION:

First of all, it’s clear that we can drop all **‘=’** signs and pretend that they never existed, because each number which follows an ‘=’ sign would be identical to the number preceding this sign. So these signs aren’t affecting our answer at all.

After discarding all ‘=’ signs our answer would be :

**P = max(maximum number of consecutive ‘<’ signs, maximum number of consecutive ‘>’ signs) + 1**

Let’s process our expression from left to right, If we are facing **X (X ? P-1)** consecutive ‘<’ signs, our starting number would be **P-X**, and we increment our last number by 1 after each sign,so the number after the last sign would be exactly **P** (which will be followed by ‘>’ sign). Our last number will be followed by **Y** consecutive ‘>’ signs, so we assign the next number to **Y (Y < P)** and we decrement the last number by 1 by each ‘>’ sign we process. The number after the last sign would be **1**.  (In case our expression starts with ‘>’ the situation would just be reversed).

After that we would have another block of **Z** consecutive ‘<’ signs, so we assign the next number to **P-Z (P-Z ? 1)** so the number after the last sign would be **P** and we continue…

Following this approach, the last number after a block of consecutive ‘<’ signs would be **P** (the maximal value), and the last number after a block of consecutive ‘>’ signs would be **1** (the minimal value). So according to our bold assumption below we can assign values using numbers in the range **[1,P]** without violating the signs.

Let’s take an example:

<<<=>=>=>>><<>>>><<<<<>><<>>

After removing = signs our sequence would be

<<< >>>>> << >>>> << >>>>>

(Blocks are separated by spaces for clarity)

here P = max(3 , 5 , 2 , 4 , 5 , 2 , 2 , 2) + 1 = 6

Our sequence would be

**3** < 4 < 5 < **6** > 5 > 4 > 3 > 2 > **1** < **5** < **6** > **4** > 3 > 2 > **1** < **5** < 6 > 5 > 4 > 3 > 2 > 1

### AUTHOR’S AND TESTER’S SOLUTIONS:

**TESTER’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Tester/CHEFSIGN.cpp)

**EDITORIALIST’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Editorialist/CHEFSIGN.cpp)

</details>
