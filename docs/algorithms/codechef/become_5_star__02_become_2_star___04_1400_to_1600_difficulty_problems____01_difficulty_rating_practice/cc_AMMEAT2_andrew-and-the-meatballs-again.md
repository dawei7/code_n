# Andrew and the Meatballs again

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AMMEAT2 |
| Difficulty Rating | 1597 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [AMMEAT2](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/AMMEAT2) |

---

## Problem Statement

Andrew likes meatballs very much as you know.

He has **N** plates of meatballs, here the **i**th plate contains exactly **i** meatballs. Andrew wants to take exactly **K** plates to his trip to Las Vegas.

On this occasion, he wants to choose the **K** plates by a strange way: if both **i**th and **j**th plates are chosen, then **i** and **j** must not be [relative prime](http://en.wikipedia.org/wiki/Coprime_integers), for all **1 ≤ i < j ≤ N**.

Please help him to choose **K** plates. Output one of the possible choices.

### Input

The first line of the input contains an integer **T**, denoting the number of test cases. The description of **T** test cases follows. The first line and only line of each test case contains two space-separated integers **N** and **K**.

### Output

For each test case, output **K** distinct integers, denoting the number of selected plates, where the plates are numbered from **1** to **N**. If there are multiple solutions, any one will do. If it is impossible to choose **K** plates, print only one integer **-1**.

### Constraints

- **1** ≤ **T** ≤ **7**

- **1** ≤ **K** ≤ **N** ≤ **777**

---

## Examples

**Example 1**

**Input**

```text
2
100 3
100 100
```

**Output**

```text
45 63 35
-1
```

**Explanation**

**Example case 1**: One of the possible choices is that he takes **45**th plate, **63**rd plate, and **35**th plate. Because
**GCD(45, 63) = 9**,
**GCD(45, 35) = 5**,
**GCD(63, 35) = 7**.

**Example case 2**: He must choose all **N = K** plates in this case. But, for example, the pair of **3**rd plate and **5**th plate does not satisfy his desire. So it is impossible to choose **K** plates.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 3
```

**Output for this case**

```text
45 63 35
```



#### Test case 2

**Input for this case**

```text
100 100
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/AMMEAT2)

[Contest](http://www.codechef.com/COOK33/problems/AMMEAT2)

# Difficulty:

SIMPLE

# Pre-requisites:

Ad-hoc

# Problem:

Given integers **N** and **K**, pick **K** integers in 1…**N**, such that no two chosen integers are relatively prime.

# Explanation:

Let us try to construct a set of **K** integers such that no two are coprime. If we choose a number x (>1), and pick all multiples of x, then clearly no two of them will be coprime (all the numbers are divisible by x)! Thus, we can pick a set of size floor(**N**/x) having such a property. Thus, it is in our interest to have x small.

Indeed, if we pick x = 2, then for any **K** <= floor(**N**/2), we can just output the set 2, 4, 6, …, 2**K**. Hence, we have the sufficient condition when **K** <= floor(**N**/2).

It turns out that this sufficient condition is also necessary (almost). The fact is, when **K** > **N**/2, any set of size **K** will have some 2 consecutive elements. These consecutive elements will then be coprime.

The only special case is where (**N**, **K**) = (1, 1). In this case, since **K** = 1, we can output plate 1 and we’re done.

Formally, we can prove the necessity as follows:

If **K** = 1, we output 1 and we are done.

If **K** > 1, then we can can never have 1 in our set.

Then, from (2i, 2i+1), we can pick only one of the two. That is, we can pick only one from (2, 3), (4, 5), …, which gives us the bound of floor(**N**/2).

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/COOK33/Setter/AMMEAT2.cpp)

# Tester’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/COOK33/Tester/AMMEAT2.cpp)

</details>
