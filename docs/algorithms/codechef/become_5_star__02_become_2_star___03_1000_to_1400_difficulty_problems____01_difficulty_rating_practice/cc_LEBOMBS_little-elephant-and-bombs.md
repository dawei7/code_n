# Little Elephant and Bombs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LEBOMBS |
| Difficulty Rating | 1284 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LEBOMBS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LEBOMBS) |

---

## Problem Statement

The Little Elephant from the Zoo of Lviv currently is on the military mission. There are **N** enemy buildings placed in a row and numbered from left to right strating from **0**. Each building **i** (except the first and the last) has exactly two adjacent buildings with indices **i-1** and **i+1**. The first and the last buildings have just a single adjacent building.

Some of the buildings contain bombs. When bomb explodes in some building it destroys it and all adjacent to it buildings.

You are given the string **S** of length **N**, where **Si** is **1** if the **i**-th building contains bomb, **0** otherwise. Find for the Little Elephant the number of buildings that will not be destroyed after all bombs explode. Please note that all bombs explode simultaneously.

### Input

The first line contains single integer **T** - the number of test cases. **T** test cases follow. The first line of each test case contains the single integer **N** - the number of buildings. The next line contains the string **S** of length **N** consisted only of digits **0** and **1**.

### Output

In **T** lines print **T** inetgers - the answers for the corresponding test cases.

### Constraints

1 <= **T** <= 100

1 <= **N** <= 1000

---

## Examples

**Example 1**

**Input**

```text
3
3
010
5
10001
7
0000000
```

**Output**

```text
0
1
7
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
010
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
5
10001
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
7
0000000
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/LEBOMBS)

[Contest](http://www.codechef.com/AUG12/problems/LEBOMBS)

### DIFFICULTY:

Cake walk

### PREREQUISITES:

None

### PROBLEM:

You’re given an array of houses some of which have a bomb and others don’t. These bombs will explode simultaneously and when bomb in **ith** house explodes, it destroys adjacent houses. Your task is to find out the number of houses which aren’t destroyed.

### QUICK EXPLANATION:

For every house check if it is destroyed or not.

### DETAILED EXPLANATION:

There are two almost similar ways of solving this problem. Key idea is to find out for each house if it is destroyed or not. How do we check if **ith** house will be destroyed or not? It will be destroyed iff at least one of **i-1**, **i** and **i+1**th houses have a bomb. Just beware of the boundaries as first and last houses have only one adjacent house. So final solution is :

``saved_count = 0
for i from 1 to N
    destroyed = false
    if( S[i] == '1') destroyed = true
    if( i > 1 and S[i-1] == '1') destroyed = true
    if( i < N and S[i+1] == '1') destroyed = true
    if( not destroyed)
        saved_count += 1
print saved_count
``

An alternative solution would be to move over houses with bombs and mark those houses that will explode.

``bool will_be_destroyed [N]
fill( will_be_destroyed, false)

for i from 1 to N
    if S[i] == '1'
        will_be_destroyed[i] = true
        if(i > 1) will_be_destroyed[i-1] = true
        if(i < N) will_be_destroyed[i+1] = true

saved_count = 0
for i from 1 to N
    if(not will_be_destroyed[i])
        saved_count += 1

print saved_count
``

Both of these are **O(N)** solutions and very comfortably fit in time limit.

### SETTER’S SOLUTION:

Will be uploaded soon.

### TESTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/August/Tester/LEBOMBS.c).

</details>
