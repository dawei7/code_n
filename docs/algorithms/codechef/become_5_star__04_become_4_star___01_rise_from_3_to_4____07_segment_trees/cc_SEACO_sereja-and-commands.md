# Sereja and Commands

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEACO |
| Difficulty Rating | 1990 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Segment Trees |
| Official Link | [SEACO](https://www.codechef.com/practice/course/3to4stars/LP3TO407/problems/SEACO) |

---

## Problem Statement

Sereja has an array **A** consisting of **n** integers. Initially, all the elements of array are zero.

Sereja writes down **m** commands on a piece of a paper. The commands are enumerated from **1** to **m**. These commands can be of the following two types of commands:

-  **l r (1 ≤ l ≤ r ≤ n)** — Increase all elements of the array by one, whose indices belongs to the range **[l, r]**

-  **l r (1 ≤ l ≤ r ≤ m)** — Execute all the commands whose indices are in the range **[l, r]**. It's guaranteed that **r** is strictly less than the enumeration/number of the current command.

Can you please help Sereja in executing all the commands written on this piece of paper.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line contains integers **n** and **m**. Next **m** lines contain Sereja's commands in the format, described in statement: **t**, **l**, **r**, where **t** - number of type (1 or 2).

### Output

For each test case on different lines print an array **a**, after executing all the commands. The numbers have to be separated by spaces. As the numbers can be quite large, print them modulo **109 + 7**.

### Constraints

- **1** ≤ **T** ≤ **3**

- **1** ≤ **n, m** ≤ **105**

### Subtasks

- Subtask #**1** (20 points): 1 ≤ **n, m** ≤ 10

- Subtask #**2** (30 points): 1 ≤ **n, m** ≤ 1000

- Subtask #**3** (50 points): original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 5
1 1 2
1 4 5
2 1 2
2 1 3
2 3 4
1 2
1 1 1
1 1 1
10 10
1 1 10
2 1 1
2 1 2
2 1 3
2 1 4
2 1 5
2 1 6
2 1 7
2 1 8
2 1 9
```

**Output**

```text
7 7 0 7 7
2
512 512 512 512 512 512 512 512 512 512
```

**Explanation**

**Example case 1.**.

After the first command, the resulting array is [1 1 0 0 0], after second [1 1 0 1 1].

On third command, we repeat the 1'st and the 2'nd command, so that resulting array is [2 2 0 2 2].

After fourth command, the array will looks like [4 4 0 4 4].

Last command will apply 3'rd and 4'th commands,
which by themselves will apply 1'st, 2'nd, 1'st, 2'nd, 3'rd(1'st, 2'nd), so resulting arrays is [7 7 0 7 7].

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/SEACO)

[Contest](http://www.codechef.com/SEPT17/problems/SEACO)

**Author:** [Sergey Nagin](http://www.codechef.com/users/sereja)

**Tester:** [Jingbo Shang](http://www.codechef.com/users/jingbo_adm)

**Editorialist:** [Hanlin Ren](http://www.codechef.com/users/r_64)

### DIFFICULTY:

Easy-Medium

### PREREQUISITES:

[Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree), difference array

### PROBLEM:

You’re given an array a consisting of n zeros initially. You need to perform two kinds of commands:

- Add 1 to a[l\sim r];

- Perform all commands whose indices are in [l,r], where r<(the index of current command)

After performing these commands, output the final array.

### QUICK EXPLANATION:

For each command, we need to count how many times it’s executed during the whole process, denoted by cnt[i]. We can iterate the commands backwards, and every time we meet a command 2\ l\ r which is executed k times, we add k to cnt[l\sim r]. When we know cnt[i] for every command i of type 1, we can easily figure out the answer by maintaining the difference array of a.

### EXPLANATION:

#### subtask 1

### brute force

We have n,m\le 10 and we can use brute force. We just write a procedure `op(i)` that performs the i-th operation, and do what the problem asks us to do:

``op(i) :
	if type[i] == 1 then
		for j = l[i] to r[i] do
			a[j] += 1
	else //type[i] == 2
		for j = l[i] to r[i] do
			op(j)
``

### a faster algorithm

Let f_{i,j} be the number of time that a[j] was increased when performing operation i.

For the first type, f_{i,j} is very easy to compute: if l_i\le j\le r_i, then f_{i,j}=1, otherwise f_{i,j}=0.

For the second type, a single operation i should be equivalent to the sum of all operations indexed in [l_i,r_i]. So for any j, f_{i,j} is the sum of f_{k,j}'s where l_i\le k\le r_i.

Once we know for every command, how many contribution it does to every element in array, we can compute the answer. Pseudocode:

``f = [empty array of m*n]
for i = 1 to m do
	if type[i] == 1 then
		for j = l[i] to r[i] do
			f[i][j] = 1
	else
		for k = l[i] to r[i] do
			for j = 1 to n do
				f[i][j] = f[i][j] + f[k][j]
	//perform this operation
	for j = 1 to n do
		a[j] = a[j] + f[i][j]
``

The total time complexity is O(nm^2).

#### subtask 2

Let cnt[i] be the number of times that command i is executed. If we know cnt[1\sim m], this problem will become much easier.

How to compute cnt[]? We don’t know cnt[1] but we know cnt[m] must be 1. If the command m is of the form 2\ l_m\ r_m, then cnt[l_m\sim r_m] will increase by 1. Then we look at command m-1: originally its cnt is 1, however if it’s executed by command m then its cnt should be 2. Also this command might influence other cnt[]'s as well: if it’s of the form 2\ l_{m-1}\ r_{m-1}, then cnt[l_{m-1}\sim r_{m-1}] will increase by cnt[m-1]. Next we can consider cnt[m-2] and the same things happen again and again…

This gives us an algorithm to compute cnt[]. Initially all cnt[i]'s should be 1. Let’s then iterate the commands backwards. When we process a command i, if it’s of the form 2\ l\ r, we add cnt[i] to cnt[l\sim r]. Pseudocode:

``cnt = [array of 1's]
for i = m downto 1 do
  if type[i] == 2 then
    for j = l[i] to r[i] do
      cnt[j] += cnt[i]
``

Once we know all cnt[]'s, for any command i of the form 1\ l\ r, we simply add cnt[i] to a[l\sim r].

The overall time complexity is O(nm).

#### subtask 3

We need to optimize the code above. When we need to add the same value on a segment, we may consider maintaining its **difference sequence**. Formally, let dcnt[i]=cnt[i]-cnt[i+1], then adding c to cnt[l\sim r] is equivalent to:

-
dcnt[r] \gets dcnt[r]+c;

-
dcnt[l-1]\gets dcnt[l-1]-c.

When we’re dealing with command i, cnt[i\sim M] is fixed(there won’t be modifications on them anymore). Thus we can calculate cnt[i] immediately, using the formula cnt[i]=dcnt[i]+cnt[i+1]. As we obtained cnt[i], we can update the array dcnt[] when i-th operation is type 2. Pseudocode:

``dcnt = [array of 0's]
cnt[m + 1] = 1
for i = m downto 1 do
  cnt[i] = dcnt[i] + cnt[i + 1]
  if type[i] == 2 then
    dcnt[r[i]] += cnt[i]
    dcnt[l[i] - 1] -= cnt[i]
``

This gives an O(m) algorithm for computing cnt[].

We can use the same trick to obtain the final array: let da[i]=a[i]-a[i+1], then adding c to a[l\sim r] is equivalent to:

-
da[r]\gets da[r]+c;

-
da[l-1]\gets da[l-1]-c.

After all modifications are done, we calculate the suffix sum of da, and that’s the array a we want. Pseudocode:

``da, a = [array of 0's]
for i = 1 to m do
  if type[i] == 1 then
    da[r[i]] += cnt[i]
    da[l[i] - 1] -= cnt[i]
for i = n downto 1 do
  a[i] = a[i + 1] + da[i]
``

The overall complexity is O(n+m).

### ALTERNATIVE SOLUTION:

To maintain cnt[], you need to support two operations: adding on a segment and querying on one position. Since this problem has some special structure, it can be done in linear time. Generally such kind of problems can be solved in time O(m(\log m+\log n)), if you use data structures such as [segment trees](https://en.wikipedia.org/wiki/Segment_tree) or [Fenwick trees](https://en.wikipedia.org/wiki/Fenwick_tree).

If your solution is different with ours, feel free to leave a comment.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/SEPT17/Tester/SEACO.cpp).

Editorialist’s solution can be found [here](http://www.codechef.com/download/Solutions/SEPT17/Editorialist/SEACO.cpp).

</details>
