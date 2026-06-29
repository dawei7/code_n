# Lucky lucky number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFLUCK |
| Difficulty Rating | 1302 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHEFLUCK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHEFLUCK) |

---

## Problem Statement

*Every great chef knows that lucky numbers are positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not. *

Our chef has recently returned from the Lucky country. He observed that every restaurant in the Lucky country had a lucky number as its name.
He believes that having a lucky number as a restaurant name can indeed turn out to be very lucky.

Our chef believes that it is possible to make a lucky number having N digits even luckier. Any number following the rules below is called Lucky lucky number -

 1. The number contains only digits 4 and 7.
 2. Count of digit 4 in the number should be divisible by 7.
 3. Count of digit 7 in the number should be divisible by 4.

Help our chef to compute the count of digit 4 in the **smallest** Lucky lucky number having N digits.

### Input

First line contains T, number of test cases. Each of the next T lines contains a number N, the number of digits in the Lucky lucky number to be formed.

1<=T<=1000
1<=N<=1000000000 (10^9)

### Output

If it is not possible to form a Lucky lucky number having N digits, output -1.
Otherwise, output the count of digit 4 in the smallest Lucky lucky number having N digits.

---

## Examples

**Example 1**

**Input**

```text
5
7
4
11
1
15
```

**Output**

```text
7
0
7
-1
7
```

**Explanation**

For the last test case, N = 15, the smallest lucky lucky number is
444444477777777. The count of digit 4 is 7.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
11
```

**Output for this case**

```text
7
```



#### Test case 4

**Input for this case**

```text
1
```

**Output for this case**

```text
-1
```



#### Test case 5

**Input for this case**

```text
15
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CHEFLUCK/)

[Contest](http://www.codechef.com/MAY12/problems/CHEFLUCK/)

### DIFFICULTY

EASY

### EXPLANATION

We want the lucky lucky number to be as small as possible. Thus, we want the number to have maximum number of 4’s placed in the beginning of the number. We can write N = 7Q + R, i.e, R = N mod 7.

If R = 0, count of 4 = 7Q and count of 7 = 0

If R = 1, count of 4 = 7*(Q-1) and count of 7 = 8 ( Thus we are removing some 4’s and placing some 7’s instead. We are trying to remove only the minumum required number of 4’s )

If R = 2, count of 4 = 7*(Q-2) and count of 7 = 16

If R = 3, count of 4 = 7*(Q-3) and count of 7 = 24

If R = 4, count of 4 = 7Q and count of 7 = 4

If R = 5, count of 4 = 7*(Q-1) and count of 7 = 12

If R = 6, count of 4 = 7*(Q-2) and count of 7 = 20

Whenever, count of 4 becomes negative, in any of the above cases, it is impossible to form a lucky lucky number.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/May/Setter/CHEFLUCK.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/May/Tester/CHEFLUCK.cpp).

</details>
