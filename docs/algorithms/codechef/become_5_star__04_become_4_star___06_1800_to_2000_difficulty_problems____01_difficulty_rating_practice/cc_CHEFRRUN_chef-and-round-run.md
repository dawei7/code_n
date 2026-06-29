# Chef and Round Run

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFRRUN |
| Difficulty Rating | 1847 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [CHEFRRUN](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/CHEFRRUN) |

---

## Problem Statement

Chef cooks nice receipes in the cafeteria of his company. The cafe contains **N** boxes with food enumerated from **1** to **N** and are placed in a circle in clocwise order (boxes **1** and **N** are adjacent). Each box has unlimited amount of food with a tastyness level of **Ai**. Chef invented a definition of a magic box!

- Chef picks a box **i** and stays in front of it.

- Now Chef eats food from box **i** and **skips** next **Ai** boxes.

- Now Chef is staying at some other (probably even the same!) box and repeats.

- Box **i** is a magic box if at some point of such game started from box **i**, Chef will find himself staying in front of it again.

When Chef came home, Chef's dog Tommy asked him about how many magic boxes were in the cafe? Help Chef to in finding that!

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains a single integer **N** denoting the number of boxes.

The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the tastyness levels of each box.

### Output

For each test case, output a single line containing number of magical boxes.

### Constraints

- **1** ≤ sum of all **N** over all the test cases in a single test file ≤ **106**

- **0** ≤ **Ai** ≤ **109**

### Subtasks

- **Subtask #1 (30 points):** **1** ≤ sum of all **N** over all the test cases ≤ **104**; **1** ≤ **N** ≤ **1000**

- **Subtask #2 (70 points):** **1** ≤ sum of all **N** over all the test cases ≤ **106**; **1** ≤ **N** ≤ **105**

---

## Examples

**Example 1**

**Input**

```text
3
4
1 1 1 1
4
3 0 0 0
4
0 0 0 2
```

**Output**

```text
4
1
2
```

**Explanation**

**Example case 1.**

Here are Chef's paths if he starting from each the box:
`
**1**->**3**->**1**
**2**->**4**->**2**
**3**->**1**->**3**
**4**->**2**->**4**
`
As you see, all **4** boxes are magical.

**Example case 2.**

Here are Chef's paths if he starts from each box appropriately:
`
**1**->**1**
**2**->**3**->**4**->**1**->**1**
**3**->**4**->**1**->**1**
**4**->**1**->**1**
`
AS you see, only box **1** is magical.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 1 1 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4
3 0 0 0
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
0 0 0 2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

(Note: the editorials are written in a hurry and without having solved the problems, so there may be mistakes. Feel free to correct them / inform me.)

###
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFRRUN)

[Contest](https://www.codechef.com/AUG16/problems/CHEFRRUN)

**Author:** [Dmytro Berezin](https://www.codechef.com/users/berezin)

**Tester:** [Sergey Kulik](https://www.codechef.com/users/xcwgf666)

**Editorialist:** [Xellos](https://www.codechef.com/users/xellos0)

###
[](#difficulty-2)DIFFICULTY:

SIMPLE

###
[](#prerequisites-3)PREREQUISITES:

graphs

###
[](#problem-4)PROBLEM:

There are N boxes in a circle. From box i, you can only move A_i+1 times clockwise. Count the starting boxes which you’ll reach again during such a walk.

###
[](#quick-explanation-5)QUICK EXPLANATION:

You’re given a so-called functional graph; count the vertices which lie on cycles. Find all cycles by moving from each vertex over unvisited vertices, then move along each cycle to count them in linear time.

###
[](#explanation-6)EXPLANATION:

Let’s number the boxes 0 through N-1. Now, we can say that the boxes are vertices of a directed graph with exactly one outgoing edge from i to (i+A_i+1)\%N. This graph has a well-known property: if we move from any vertex along those edges, we’ll eventually encounter exactly one cycle and stay on it.

So let’s start in some vertex v_s and move along edges. If we encounter a vertex that was visited before (for some earlier starting vertex), we already visited the cycle that follows, so there’s nothing to do for that v_s. Otherwise, we’ll have to encounter a cycle that wasn’t visited before - as soon as we visit a vertex that was visited before, but for the current v_s, we can conclude that this vertex v_c lies on that new cycle. Then, it’s sufficient to move along this cycle until we get back to v_c and count the vertices visited on it.

After doing that for all v_s, all cycles had to be visited, so we’ve counted the number of vertices on cycles - th answer to our problem. Time and memory complexity: O(N), since we can’t visit any vertex more than twice this way.

###
[](#authors-and-testers-solutions-7)AUTHOR’S AND TESTER’S SOLUTIONS:

The author’s solution can be found [here](https://www.codechef.com/download/Solutions/AUG16/Setter/CHEFRRUN.cpp).

Tester's solution
``#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

const int MAXN = 100000 + 10;

int a[MAXN], tag[MAXN], w[MAXN];

int main () {
    int sumN = 0;
	int testCases;
	cin >> testCases;
	while (testCases--) {
		int n;
		cin >> n;
        sumN += n;
        assert(1 <= n && n <= 100000);
		for(int i = 1; i <= n; i++) {
			cin >> a[i];
            assert(0 <= a[i] && a[i] <= 1000000000);
			a[i] = (i + a[i] + 1) % n;
			if (a[i] == 0)
				a[i] = n;
			tag[i] = 0;
		}
		for(int i = 1; i <= n; i++)
			if (tag[i] == 0) {
				int pos = i;
				int wn = 0;
				while (!tag[pos]) {
					w[++wn] = pos;
					tag[pos] = 3;
					pos = a[pos];
				}
				if (tag[pos] <= 2) {
					for(int i = 1; i <= wn; i++)
						tag[w[i]] = 1;
				} else {
					int currentTag = 1;
					for(int i = 1; i <= wn; i++) {
						if (w[i] == pos)
							currentTag = 2;
						tag[w[i]] = currentTag;
					}
				}
			}
		int ret = 0;
		for(int i = 1; i <= n; i++)
			ret += (tag[i] == 2);
		cout << ret << endl;
	}
    assert(1 <= sumN && sumN <= 1000000);
	return 0;
}

``

###
[](#related-problems-8)RELATED PROBLEMS:

</details>
