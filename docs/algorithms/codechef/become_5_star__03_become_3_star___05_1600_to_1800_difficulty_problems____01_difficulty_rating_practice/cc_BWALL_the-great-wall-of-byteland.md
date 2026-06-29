# The Great Wall of Byteland

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BWALL |
| Difficulty Rating | 1796 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [BWALL](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/BWALL) |

---

## Problem Statement

In order to protect the southern border of Bytelandian Empire against intrusions by various nomadic groups, the Emperor of Byteland has decided to build a wall along the southern border. The best architect Johny is recruited for the task.

In order to minimise the cost of raw material, Johny is restricted to use only following two kinds of building blocks:
X      #

XX

The height of the wall is fixed and is 2 units, but the length of the wall varies. As a part of his job Johny needs to find out the number of ways he can construct the wall using above two types of building blocks where the length of the wall is specified. Write a program to help Johny.

### Input Format:

The first line contains the number of test cases T followed by T lines. Each of the next lines contains an integer N representing the length of the wall.

### Output Format:

Print T lines one for each test case, containing an integer that represents the number of ways of constructing the wall, modulo 1000000007.

**Constraints:**
1<=T<=1000
1<=N<=10^9

---

## Examples

**Example 1**

**Input**

```text
3
7
2
13
```

**Output**

```text
655
5
272767
```

**Explanation**

### Explanation of 2nd Test Case

**Given:**
`N = 2`

We want to count all possible ways to build the wall using the allowed tiles. Each configuration below represents one valid way.

---

### All 5 Possible Ways

```
1) ####
```

```
2) X#XX
```

```
3) #XXX
```

```
4) XXX#
```

```
5) XX#X
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
```

**Output for this case**

```text
655
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
13
```

**Output for this case**

```text
272767
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/BWALL/)

[Contest](http://www.codechef.com/MAY11/problems/BWALL/)

### DIFFICULTY

EXPLANATION

[

1024×768
](https://s3.amazonaws.com/codechef_shared/download/Solutions/2011/May/ed1.jpg)

[

1024×768
](https://s3.amazonaws.com/codechef_shared/download/Solutions/2011/May/ed2.jpg)

[

1024×768
](https://s3.amazonaws.com/codechef_shared/download/Solutions/2011/May/ed3.jpg)

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/May/Setter/BWALL.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/May/Tester/BWALL.cpp).

</details>
