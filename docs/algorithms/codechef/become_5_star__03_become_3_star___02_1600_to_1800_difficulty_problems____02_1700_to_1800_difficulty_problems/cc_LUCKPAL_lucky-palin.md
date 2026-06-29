# Lucky Palin

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUCKPAL |
| Difficulty Rating | 1744 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [LUCKPAL](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/LUCKPAL) |

---

## Problem Statement

Chef Palin, as his name suggests, is always very interested in palindromic strings. Recently, he made a pretty interesting discovery on palindromes and that made him feel really Lucky. He came across something known as Lucky Palindromes. He defines a string as being a lucky palindrome if it is a palindrome containing the string "lucky" as a substring. As always, now he wants to turn every string he comes across into a lucky palindrome. Being a chef, he is a man of patience and creativity, so he knows the operation of replacing any character of the string with any other character very well and he can perform this action infinitely many times. He wants you to write a program that can help him convert a given string to a lucky palindrome using the minimum number of operations and if several such lucky palindromes are possible, then output the lexicographically smallest one.

**Input**

The first line contains a single integer T <= 100 the number of testcases. The following T lines each contain a string of length <= 1000 and only containing characters 'a'-'z'.

**Output**

For each line of testcase, your program should output on a single line, the required lucky palindrome along with the minimum number of operations, both separated by a single space. If there is no lucky palindrome possible, then just output "unlucky" in a single line.

---

## Examples

**Example 1**

**Input**

```text
3
laubcdkey
luckycodechef
aaaaaaaa
```

**Output**

```text
luckykcul 8
luckycocykcul 6
unlucky
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
laubcdkey
```

**Output for this case**

```text
luckykcul 8
```



#### Test case 2

**Input for this case**

```text
luckycodechef
```

**Output for this case**

```text
luckycocykcul 6
```



#### Test case 3

**Input for this case**

```text
aaaaaaaa
```

**Output for this case**

```text
unlucky
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/LUCKPAL)

[Contest](http://www.codechef.com/OCT11/problems/LUCKPAL)

### DIFFICULTY

EASY

### EXPLANATION

The problem is solvable by Greedy Algorithm. For each i >= 0 and j >=0, i < j such that string[i….j] = “lucky”, find the lexicographically smallest palindrome that can be constructed in a greedy manner using minimum number of replacement operations. So the problem can be divided into two tasks:

- Place the substring “lucky” at all possible locations in the string.

- For each such location of substring “lucky”, find the lexicographically smallest palindrome using minimum number of replacement operations while maintaining the substring “lucky”.

Let’s define each string obtained in task 1 as: “xxxxxluckyxxxxx” with str[a…b] = “lucky”. Now, second task can be achieved by iterating over the string starting with i = 0 and j = n-1 (n = string length), until i <= j. At each iteration, we have the following possibilities:

- str[i] = str[j] , requires no replacement operation

- str[i] != str[j] , either requires 1 replacement or no solution is possible

a. i < a and j > b, requires 1 replacement

i. if str[i] < str[j], str[j] = str[i]

ii. str[i] > str[j], str[i] = str[j]

b. a >= i and i <= b and j > b, requires 1 replacement

i. str[j] = str[i], cannot change str[i] as it is part of “lucky”

c. i < a and a >= j and j <= b, requires 1 replacement

i. str[i] = str[j], cannot change str[j] as it is part of “lucky”

d. a >= i,j <= b, cannot be converted to palindrome containing “lucky”

Final answer is the string obtained after task 2 with minimum number of replacement operations and lexicographically smallest one. If no such string exists, then “unlucky”.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/October/Setter/LuckPal.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/October/Tester/LuckPal.java).

</details>
