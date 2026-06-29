# Even Pair Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EVENPSUM |
| Difficulty Rating | 1200 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [EVENPSUM](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/EVENPSUM) |

---

## Problem Statement

You are given two positive integers $A$ and $B$. Find the number of pairs of positive integers $(X, Y)$ such that $1 \le X \le A$, $1 \le Y \le B$ and $X + Y$ is even.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$.

### Output
For each test case, print a single line containing one integer ― the number of valid pairs.

### Constraints
- $1 \le T \le 1,000$
- $1 \le A, B \le 10^9$

### Subtasks
**Subtask #1 (10 points):** $A, B \le 10$

**Subtask #2 (10 points):** $A, B \le 1,000$

**Subtask #3 (80 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
4
1 1
2 3
4 6
8 9
```

**Output**

```text
1
3
12
36
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 3
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 6
```

**Output for this case**

```text
12
```



#### Test case 4

**Input for this case**

```text
8 9
```

**Output for this case**

```text
36
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EVENPSUM)

[Div1](https://www.codechef.com/DEC20A/problems/EVENPSUM)

[Div2](https://www.codechef.com/DEC20B/problems/EVENPSUM)

**Setter:**  [Ildar Gainullin](https://www.codechef.com/users/gainullinildar)

**Tester:**  [Alexander Morozov](https://www.codechef.com/users/scanhex)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

None

### PROBLEM:

We are given two positive integers A and B . We need to find the number of pairs of positive integers (X,Y) that can be formed such that 1 \le X \le A  and 1 \le Y \le B and the sum X+Y is even.

### QUICK EXPLANATION:

-

When is the sum of two numbers even? The answer is when either both of the numbers are even or both of them are odd.

-

Thus, count the number of even-even pairs and odd-odd pairs and add them to get the answer.

-

**Be careful of integer overflow!!!** This can happen in some languages such as C++. In that case make sure you use the right datatype to store the variables while finding the answer.

### EXPLANATION:

Let’s recall the definitions of even and odd numbers. A number n is even if n=2 \cdot k for some positive integer k . A number n is odd if n=2 \cdot k+1 for some positive integer k .  We have 4  cases for X and Y:

**Case 1: X is even and Y is odd**

-

Let X=2 \cdot k1 and Y=2 \cdot k2+1 .

-

Then X+Y=2 \cdot k1+2 \cdot k2+1= 2 \cdot k+1 where k=k1+k2 .

-

Therefore, X+ Y is an odd number.

**Case 2: X is odd and Y is even**

-

Let X=2 \cdot k1+1 and Y=2 \cdot k2 .

-

Then X+Y=2 \cdot k1+1+2 \cdot k2=2 \cdot k+1 where k=k1+k2 .

-

Therefore, X+ Y is an odd number.

**Case 3: X is even and Y is even**

-

Let X=2 \cdot k1 and Y=2 \cdot k2 .

-

Then X+Y=2 \cdot k1+2 \cdot k2=2 \cdot k where k=k1+k2 .

-

Therefore, X+ Y is an even number.

**Case 4: X is odd and Y is odd**

-

Let X=2 \cdot k1+1 and Y=2 \cdot k2+1 .

-

Then X+Y=2 \cdot k1+1+2 \cdot k2+1=2 \cdot k where k=k1+k2+1 .

-

Therefore, X+ Y is an even number.

Thus, we have X+Y even in **case 3** and **case 4** . (here all the divisions are integer  divisions) .

-

Total even numbers in [1,A] are A/2 .

-

Total odd numbers in [1,A] are (A+1)/2 .

-

Total even numbers in [1,B] are B/2 .

-

Total odd numbers in [1,B] are (B+1)/2 .

Therefore, the number of pairs (X,Y) where X+Y is odd are

(A/2) \cdot (B/2) + ((A+1)/2) \cdot ((B+1)/2) .

### TIME COMPLEXITY:

O(1) for each testcase.

### SOLUTION:

Editorialist's solution
``    #include <bits/stdc++.h>
    using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int a, b;
		cin >> a >> b;
		long even_a = a / 2;
		long even_b = b / 2;
		long odd_a = (a + 1) / 2;
		long odd_b = (b + 1) / 2;
		long ans = even_a * even_b + odd_a * odd_b;
		cout << ans << endl;
	}
	return 0;
}
``

Setter's solution
``#include <cmath>

#include <functional>

#include <fstream>

#include <iostream>

#include <vector>

#include <algorithm>

#include <string>

#include <set>

#include <map>

#include <list>

#include <time.h>

#include <math.h>

#include <random>

#include <deque>

#include <queue>

#include <cassert>

#include <unordered_map>

#include <unordered_set>

#include <iomanip>

#include <bitset>

#include <sstream>

#include <chrono>

#include <cstring>

using namespace std;

typedef long long ll;

#ifdef iq

mt19937 rnd(228);

#else

mt19937 rnd(chrono::high_resolution_clock::now().time_since_epoch().count());

#endif

int main()

{

#ifdef iq

freopen("a.in", "r", stdin);

#endif

ios::sync_with_stdio(0);

cin.tie(0);

int t;

cin >> t;

while (t--)

{

int a, b;

cin >> a >> b;

int even_a = a / 2, even_b = b / 2;

int odd_a = (a + 1) / 2, odd_b = (b + 1) / 2;

ll ans = even_a * (ll)even_b + odd_a * (ll)odd_b;

cout << ans << " \n";

}

}
``

# VIDEO EDITORIAL (English):

# VIDEO EDITORIAL (Hindi):

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
