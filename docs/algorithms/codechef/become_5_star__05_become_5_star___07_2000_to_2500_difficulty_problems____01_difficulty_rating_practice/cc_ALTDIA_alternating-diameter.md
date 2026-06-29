# Alternating Diameter

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALTDIA |
| Difficulty Rating | 2300 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ALTDIA](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ALTDIA) |

---

## Problem Statement

Chef stumbled upon $B$ black nodes and $W$ white nodes and now wants to construct a tree using them.

Chef is bamboozled by the total number of trees that can be constructed using these nodes. To reduce this count, Chef considered only those trees which have **at least** one diameter that has alternating colors i.e. a black node is followed by a white node and a white node is followed by a black node.

Help Chef in finding out the tree with the **minimum** possible diameter among all the trees that satisfies the above condition. If no tree satisfies the above conditions, print $-1$. If multiple trees satisfies the above condition, print any.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers $B, W$ representing the number of black and white nodes respectively.

---

## Output Format

- If a tree can be constructed that fulfils all the requirements then
    - In the first line, output a string of length $B + W$ in which the $i^{th}$ character (1-based indexing) is either `W` or `B` denoting the colour of the $i^{th}$ node as black or white respectively.
    - In the following $B + W - 1$ lines, output two integers $U$ and $V$ denoting an edge between $U^{th}$ and $V^{th}$ node.
- If no tree fulfils the requirements print `-1` in a single line.

---

## Constraints

- $1 \leq T \leq 100$
- $0 \leq B, W \leq 1000$
- $1 \leq B + W \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
1 1
0 2
1 2
```

**Output**

```text
WB
2 1
-1
WBW
1 2
2 3
```

**Explanation**

**Test case $1$:** The tree has only one path between the nodes $1$ and $2$ which is the diameter and also alternating in color. The checker will handle multiple possible answers so you can also swap the colors of the node to achieve the same result.

**Test case $2$:** There is only one tree possible and its diameter would consist of all white nodes only. Therefore there is no tree which satisfies the given conditions.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ALTDIA)

[Contest: Division 1](https://www.codechef.com/MAY221A/problems/ALTDIA)

[Contest: Division 2](https://www.codechef.com/MAY221B/problems/ALTDIA)

[Contest: Division 3](https://www.codechef.com/MAY221C/problems/ALTDIA)

[Contest: Division 4](https://www.codechef.com/MAY221D/problems/ALTDIA)

***Author:*** [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

Trees, greedy algorithms

#
[](#problem-4)PROBLEM:

Chef has B black nodes and W white nodes. Help him construct a tree using these nodes such that it has at least one diameter that alternates between colors, and the diameter is minimized.

#
[](#explanation-5)EXPLANATION:

Hint

Excluding a few corner cases, it’s always possible to achieve diameter 3.

Full solution

This is a problem which one can gain insight into by working a few small cases out on paper. You will quickly notice that, except a handful of cases where the answer is -1, it’s always possible to create a tree of diameter 3 that has an alternating diameter.

It turns out that this is indeed the full solution. The cases can be split as follows:

- If B + W = 1, the tree consists of only one node. There’s only one such tree, and it has an alternating diameter so in this case, simply print this tree

- If B + W > 1 but either B = 0 or W = 0, the answer is -1. This is because any tree with at least 2 nodes has a diameter of at least 2, and since every node will have the same color, it’s impossible to find a tree with alternating colors on its diameter.

- If B = W = 1, there’s again only one type of tree possible, and it’s easy to see that it indeed works.

- Finally, we have the case when B + W \gt 1, both B \gt 0 and W \gt 0, and either B \gt 1 or W \gt 1. Many constructions work in this case, here’s an example:

- Without loss of generality, let W > 1 (if not, swap what we do with B and W). Assign the color B to nodes 1, 2, \ldots, B and the color W to nodes B+1, B+2, \ldots, B+W. Now, for each 2 \leq i \leq B+W, join node i to node 1, forming a ‘star’ tree. This tree has diameter 3, and since there are at least 2 white nodes, an alternating diameter as well, going `white - black - white` via the central node.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(B + W) per test.

#
[](#code-7)CODE:

Setter (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    assert(t <= 100);
    while(t--) {
        int a, b;
        cin >> a >> b;
        assert(a > -1 && a <= 1000);
        assert(b > -1 && b <= 1000);
        assert(a + b > 0 && a + b <= 1000);
        if((!a || !b) && (a + b) > 1) {
            cout << "-1\n";
            continue;
        }
        for(int i = 1; i <= a; i++) cout << "B";
        for(int i = 1; i <= b; i++) cout << "W";
        cout << "\n";
        int n = a + b;
        if(b == 1)
            for(int i = 1; i < n; i++) cout << i << " " << n << "\n";
        else
            for(int i = 2; i <= n; i++) cout << i << " 1\n";
    }
}

``

Editorialist (Python)
``for _ in range(int(input())):
	b, w = map(int, input().split())
	if b+w == 1:
		if b == 1:
			print('B')
		else:
			print('W')
	elif b == 0 or w == 0:
		print(-1)
	else:
		print('B'*b + 'W'*w)
		for i in range(1, b+w):
			if b == 1:
				print(1, i+1)
			else:
				print(i, b+w)
``

</details>
