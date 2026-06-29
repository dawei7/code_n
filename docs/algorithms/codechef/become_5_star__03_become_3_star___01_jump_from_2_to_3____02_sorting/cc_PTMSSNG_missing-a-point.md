# Missing a Point

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PTMSSNG |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [PTMSSNG](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/PTMSSNG) |

---

## Problem Statement

Chef has $N$ axis-parallel rectangles in a 2D Cartesian coordinate system. These rectangles may intersect, but it is guaranteed that all their $4N$ vertices are pairwise distinct.

Unfortunately, Chef lost one vertex, and up until now, none of his fixes have worked (although putting an image of a point on a milk carton might not have been the greatest idea after all...). Therefore, he gave you the task of finding it! You are given the remaining $4N-1$ points and you should find the missing one.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- Then, $4N-1$ lines follow. Each of these lines contains two space-separated integers $x$ and $y$ denoting a vertex $(x, y)$ of some rectangle.

### Output
For each test case, print a single line containing two space-separated integers $X$ and $Y$ ― the coordinates of the missing point. It can be proved that the missing point can be determined uniquely.

### Constraints
- $T \le 100$
- $1 \le N \le 2 \cdot 10^5$
- $|x|, |y| \le 10^9$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

### Subtasks
**Subtask #1 (20 points):**
- $T = 5$
- $N \le 20$

**Subtask #2 (30 points):** $|x|, |y| \le 10^5$

**Subtask #3 (50 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
2
1 1
1 2
4 6
2 1
9 6
9 3
4 3
```

**Output**

```text
2 2
```

**Explanation**

The original set of points are:
![fig1](https://i.imgur.com/7oHoe86.png =333x211)

Upon adding the missing point $(2, 2)$, $N = 2$ rectangles can be formed:
![fig1](https://i.imgur.com/N8ceCw0.png =333x211)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PTMSSNG)

[Div-2 Contest](https://www.codechef.com/JULY20B/problems/PTMSSNG)

[Div-1 Contest](https://www.codechef.com/JULY20A/problems/PTMSSNG)

***Author:*** [Áron Noszály](https://www.codechef.com/users/sanroylozan)

***Tester:*** [Encho Misev](https://www.codechef.com/users/enchom)

***Editorialist:*** [Áron Noszály](https://www.codechef.com/users/sanroylozan)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

Observations, Data structures, Sorting, Bitwise operations

# PROBLEM:

There are 4N-1 different points in the plane. You should find a point P such that together they form N axis-aligned non-degenerate rectangles. It is guaranteed that the answer exists and is unique.

# QUICK EXPLANATION:

Let’s consider all 4N points, the number of points with a given x or y coordinate is always even. By taking away exactly one point, one vertical count and one horizontal count will be odd, those will be the coordinates of the point that we are searching

# EXPLANATION:

One possible approach is to start with small cases, let N=1 draw a rectangle and take one of its vertices away, we can instantly recover the missing point P (even if we have a really short memory :D), because no matter what, there’s only one point on both the vertical line and horizontal line through P, and in the other vertical/horizontal lines there are 0 or 2 points.

It might immediately be clear that parity is the key, by extending the idea and adding a few more rectangles we can see that each extra rectangle contributes either 2 or 0 points to each vertical/horizontal line. Therefore the lines containing the missing point will surely have an odd amount of points and the rest of lines will have an even amount of points, so it’s enough to find these two lines and at their intersection will be P. Mathematicians call this an [invariant](https://en.wikipedia.org/wiki/Invariant_(mathematics)), we can simply say that the parity of the number of points in some vertical/horizontal is invariant to adding more rectangles.

There are multiple ways to implement the above idea:

- A simple bruteforce algorithm for checking every possible horizontal and vertical line, the complexity is O(N^2) which is enough for the first subtask.

- We can use a data structure like `std::map` in C++, `TreeMap` in Java or a `dictionary` in Python  to maintain the number of points in each horizontal and vertical line.

- Sort all the x and y coordinates and loop through them to find the one with odd frequency.

We could think that simply changing the data structure to a hash-based one with O(1) queries/updates (like `unordered_map` in C++ or `HashMap` in Java) should work, yes it may do trick and our complexity would be O(N), however I was evil and included some antihash tests.

There is a much better way! Note that taking the bitwise xor of the x coordinates of all 4N-1 points will actually just give us P's x coordinate, since each of the other x coordinates is present an even number of times they cancel out, while P's x coordinate is in the input an odd number of times. Similarly for the y coordinate. So now we have an algorithm with O(N) time complexity.

# SOLUTIONS:

Setter's Solution

Sorting method
``#include<bits/stdc++.h>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int T;
	cin>>T;
	while(T--) {
		int n;
		cin>>n;
		vector<int> x, y;
		for(int i=0;i<4*n-1;++i) {
			int X,Y;
			cin>>X>>Y;
			x.push_back(X);
			y.push_back(Y);
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		int ans_x=-1,ans_y=-1;
		auto find_odd=[&](vector<int>& x) -> int {
			int i,j;
			for(i=0;i<(int)x.size();i=j) {
				j=i;
				while(j<(int)x.size() && x[i]==x[j]) {
					j++;
				}

				if((j-i)&1) return x[i];
			}
			return -1;
		};

		ans_x=find_odd(x);
		ans_y=find_odd(y);
		cout<<ans_x<<" "<<ans_y<<"\n";
	}
	return 0;
}
``

Using map
``#include<bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	int T;
	cin>>T;
	while(T--) {
		int n;
		cin>>n;
		map<int,int> X,Y;
		for(int i=0;i<4*n-1;++i) {
			int x,y;
			cin>>x>>y;
			X[x]++;
			Y[y]++;
		}

		int ans_x=-1, ans_y=-1;
		for(auto i:X) {
			if(i.second&1) ans_x=i.first;
		}

		for(auto i:Y) {
			if(i.second&1) ans_y=i.first;
		}

		assert(ans_x!=-1 && ans_y!=-1);
		cout<<ans_x<<" "<<ans_y<<"\n";
	}
}
``

XOR solution
``#include<bits/stdc++.h>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int T;
	cin>>T;
	while(T--) {
		int n;
		cin>>n;
		int ans_x=0, ans_y=0;
		for(int i=0;i<4*n-1;++i) {
		    int x,y;
		    cin>>x>>y;
		    ans_x^=x;
		    ans_y^=y;
		}
		cout<<ans_x<<" "<<ans_y<<"\n";
	}
	return 0;
}
``

Tester's Solution
``#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;

int t;
int n;
map<int, int> rows, cols;

int main()
{
    int i,j;
    int test;

    scanf("%d", &t);

    for (test=1;test<=t;test++)
    {
        rows.clear();
        cols.clear();

        scanf("%d", &n);

        for (i=1;i<=4*n-1;i++)
        {
            int x, y;

            scanf("%d %d", &x, &y);

            auto it = rows.find(x);

            if (it != rows.end())
            {
                (*it).second++;
            }
            else
            {
                rows.insert(make_pair(x, 1));
            }

            it = cols.find(y);

            if (it != cols.end())
            {
                (*it).second++;
            }
            else
            {
                cols.insert(make_pair(y, 1));
            }
        }

        int r, c;
        for (auto it = rows.begin(); it != rows.end(); it++)
        {
            if ( (*it).second % 2 == 1 )
                r = (*it).first;
        }

        for (auto it = cols.begin(); it != cols.end(); it++)
        {
            if ( (*it).second % 2 == 1 )
                c = (*it).first;
        }

        printf("%d %d\n", r, c);
    }

    return 0;
}
``

</details>
