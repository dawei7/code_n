# Lucky Four

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUCKFOUR |
| Difficulty Rating | 775 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [LUCKFOUR](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/LUCKFOUR) |

---

## Problem Statement

You are given a list of **T** integers, for each of them you have to calculate the number of occurrences of the digit **4** in the decimal representation.

### Input

The first line of input consists of a single integer **T**, denoting the number of integers in the list.

Then, there are **T** lines, each of them contain a single integer from the list.

### Output

Output **T** lines. Each of these lines should contain the number of occurrences of the digit **4** in the respective integer from the list.

### Constraints

- **1** ≤ **T** ≤ **105**

- (Subtask 1): **0** ≤ Numbers from the list  ≤ **9** - 33 points.

- (Subtask 2): **0** ≤ Numbers from the list  ≤ **109** - 67 points.

---

## Examples

**Example 1**

**Input**

```text
5
447474
228
6664
40
81
```

**Output**

```text
4
0
1
1
0
```

**Explanation**

There are four 4s in the **447474**, no 4s in **228**, one 4s in **6664**

**Separated test cases**

#### Test case 1

**Input for this case**

```text
447474
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
228
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
6664
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
40
```

**Output for this case**

```text
1
```



#### Test case 5

**Input for this case**

```text
81
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/LUCKFOUR)

[Contest](http://www.codechef.com/LTIME21/problems/LUCKFOUR)

**Author:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Tester:** [Roman Furko](http://www.codechef.com/users/furko)

**Editorialist:** [Balajiganapathi Senthilnathan](http://www.codechef.com/users/balajiganapath)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Basic string

### PROBLEM

For each number, you have to count the number of times the digit 4 occurs in it.

### QUICK EXPLANATION

Input the number as a string and count the number of times the character ‘4’ occurs in it.

### EXPLANATION

We may be tempted to input the number as an int, but this is really a string related task. We have to count the number of times a particular character appears in the string. So, taking the input as a string helps us avoid all the complicated stuff we will have to do if we input as a number.

We just have to loop through all characters of the string and if it is ‘4’, increment the answer.

It is also instructive to see how we can solve this if we treat the input as a number.

Say we have a number x = 12345. How can we extract its digits? Observe that we can easily get the rightmost digit(unit’s place) - if we divide x by 10 and take the reminder, it will be the rightmost digit. Further, the quotient we get is the rest of the number. For example, 12345 = 1234 * 10 + 5. So we get both the unit’s place digit and the rest of the number. Now to get the next digit, we continue in the same fashion. When should we stop? Suppose x is a single digit, say x = 1. Now the quotient after dividing by 10 is 0, and we can stop since there are no more digits to process.

Pseudocode:

`
ans = 0
while x > 0:
    remainder = x % 10
    quotient = x / 10
    if remainder == 4 ans++
    x = quotient
`

### Complexity

The number of times the while loop will run is equal to the number of digits. Say d is the number of digits, the complexity will therefore be O(d). Also, if we treat the input as integer, we can see that d = \lceil log_{10} n \rceil. So, the complexity will be \mathcal{O}(log n).

### AUTHOR’S, TESTER’S and Editorialist’s SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/LTIME21/Setter/LUCKFOUR.cpp)

[tester](http://www.codechef.com/download/Solutions/LTIME21/Tester/LUCKFOUR.cpp)

[editorialist](http://www.codechef.com/download/Solutions/LTIME21/Editorialist/LUCKFOUR.cpp)

</details>
