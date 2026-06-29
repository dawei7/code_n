# Workers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFWORK |
| Difficulty Rating | 1146 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [CHEFWORK](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/CHEFWORK) |

---

## Problem Statement

There are $N$ workers; each worker is of one of the following three types:
- A *translator* translates some text from Chef's language to another language.
- An *author* writes some text in Chef's language.
- An *author-translator* can both write a text in Chef's language and translate it to another language.

Chef wants to have some text written and translated into some language (different from Chef's language). Chef can't do either of those tasks, but he can hire workers. For each $i$ ($1 \le i \le N$), if he hires the $i$-th worker, he must pay that worker $c_i$ coins.

Help Chef find the minimum total number of coins he needs to pay to have a text written and translated. It is guaranteed that it is possible to write and translate a text.

---

## Input Format

- The first line of the input contains a single integer $N$ denoting the number of workers.
- The second line contains $N$ space-separated integers $c_1, c_2, ..., c_N$ denoting the numbers of coins Chef has to pay each hired worker.
- The third line contains $N$ space-separated integers $t_1, t_2, ..., t_N$ denoting the types of workers. For each valid $i$, the $i$-th worker is a translator if $t_i = 1$, an author if $t_i = 2$ or an author-translator if $t_i = 3$.

---

## Output Format

- Print a single line containing one integer — the minimum number of coins Chef has to pay.

---

## Constraints

- $1 \le N \le 1,000$
- $1 \le c_i \le 100,000$ for each valid $i$
- $1 \le t_i \le 3$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
5
1 3 4 6 8
1 2 1 2 3
```

**Output**

```text
4
```

**Explanation**

Chef can hire 2 workers: worker 1, who is a translator, and worker 2, who is an author. In total, he pays them $1 + 3 = 4$ coins.

**Example 2**

**Input**

```text
4
10 8 2 5
1 2 3 3
```

**Output**

```text
2
```

**Explanation**

Chef can hire 1 worker: worker 3, who is an author-translator. In total, he pays them $2$ coins.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS:

[Div2](https://www.codechef.com/APRIL18B/problems/CHEFWORK)

[Practice](https://www.codechef.com/problems/CHEFWORK)

**Setter-** [Adlet Zeineken](https://www.codechef.com/users/adlet_zeineken)

**Tester-** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist-** [???](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

CAKEWALK

### PRE-REQUISITES:

Array, Looping, Sorting (optional).

### PROBLEM:

There are 3 type of workers, where the first type only translates, second type only writes and third type does both, we are to find minimum cost to write and translate a piece of text. We are given the information of type of worker, and how many coins he will charge for his service.

### QUICK EXPLANATION:

We clearly see that the answer will be {min} (C_3,C_1+C_2) where {C}_{i} denotes the cost of cheapest worker of type i. With that, we just have to take care of cases where -

- There are no workers of type C_1 or C_2 .

- No worker of type {C}_{3}.

### EXPLANATION :

This editorial will describe two approaches, one which is easy and intended one, and another which is followed by me (a bit complex- but its intended to expose you guys to data structures).

**Easy Approach [#1](https://discuss.codechef.com/tags/1)**

This is a fairly simple problem. What we must focus on, is finding the minimum cost of workers of all three types.

There can be multiple ways to do so. One way is to iterate over the array thrice, each time finding minimum cost of worker of the required type. If no worker of that type exists, we simply put {C}_{i}=INF where INF can be some large number, more than 2*{10}^{5} (preferably **INTMAX**).

With this data, we can simply find answer as min(C_3,C_1+C_2), which was stated above.

**My Approach (Medium)-**

My approach intends to introduce you people to data types, and this time it is [vectors](http://www.cplusplus.com/reference/vector/vector/) (in C++) and any equivalent data structure in other languages. In context to editorial, you can think like, vector is an array where you can insert and delete elements from end in O(1) time. (although its much more than that!)

What I did was, I created an array of vectors, of size 4 (just to follow 1-based indexing). In my solution, worker[i][j] represents a worker of type i take j coins to do his work. I sorted the vectors of all 3 types, took care of conditions when worker of a specific type are absent, and simply printed the answer (because after sorting, the first element is the minimum).

Dont worry if this seems complex to you now, but do make sure to understand this at some point of time :).

### SOLUTION:

Setter

[Tester](http://campus.codechef.com/APR18TST/viewsolution/18025007/) - He essentially did the same as in approach 1 we discussed. His array F[i] is equivalent to our C_i.

[Editorialist](http://campus.codechef.com/APR18TST/viewsolution/18063261/)

### CHEF VIJJU’S CORNER

1.Make it a point to learn vectors. A proper command over data structures are needed to master algorithms. Vectors are very commonly used in Graph Algorithms. You can refer to [here](https://www.geeksforgeeks.org/vector-in-cpp-stl/) for more on vectors

2.Any other approaches are welcomed

</details>
