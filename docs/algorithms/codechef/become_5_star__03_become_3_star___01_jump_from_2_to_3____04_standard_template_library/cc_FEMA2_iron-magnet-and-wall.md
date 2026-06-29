# Iron, Magnet and Wall

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FEMA2 |
| Difficulty Rating | 1725 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [FEMA2](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/FEMA2) |

---

## Problem Statement

Chef loves to play with iron (Fe) and magnets (Ma). He took a row of $N$ cells (numbered $1$ through $N$) and placed some objects in some of these cells. You are given a string $S$ with length $N$ describing them; for each valid $i$, the $i$-th character of $S$ is one of the following:
- 'I' if the $i$-th cell contains a piece of iron
- 'M' if the $i$-th cell contains a magnet
- '_' if the $i$-th cell is empty
- ':' if the $i$-th cell contains a conducting sheet
- 'X' if the $i$-th cell is blocked

If there is a magnet in a cell $i$ and iron in a cell $j$, the *attraction power* between these cells is $P_{i,j} = K+1 - |j-i| - S_{i,j}$, where $S_{i,j}$ is the number of cells containing sheets between cells $i$ and $j$. This magnet can only *attract* this iron if $P_{i, j} \gt 0$ and there are no blocked cells between the cells $i$ and $j$.

Chef wants to choose some magnets (possibly none) and to each of these magnets, assign a piece of iron which this magnet should attract. Each piece of iron may only be attracted by at most one magnet and only if the attraction power between them is positive and there are no blocked cells between them. Find the maximum number of magnets Chef can choose.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains a single string $S$ with length $N$.

### Output
For each test case, print a single line containing one integer ― the maximum number of magnets that can attract iron.

### Constraints
- $1 \le T \le 2,000$
- $1 \le N \le 10^5$
- $0 \le K \le 10^5$
- $S$ contains only characters 'I', 'M', '_', ':' and 'X'
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^6$

### Subtasks
**Subtask #1 (30 points):** there are no sheets, i.e. $S$ does not contain the character ':'

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4 5
I::M
9 10
MIM_XII:M
```

**Output**

```text
1
2
```

**Explanation**

**Example case 1**: The attraction power between the only magnet and the only piece of iron is $5+1-3-2 = 1$. Note that it decreases with distance and the number of sheets.

**Example case 2:**
The magnets in cells $1$ and $3$ can attract the piece of iron in cell $2$, since the attraction power is $10$ in both cases. They cannot attract iron in cells $6$ or $7$ because there is a wall between them.

The magnet in cell $9$ can attract the pieces of iron in cells $7$ and $6$; the attraction power is $8$ and $7$ respectively.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 5
I::M
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
9 10
MIM_XII:M
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FEMA2)

[Div-2 Contest](https://www.codechef.com/NOV20B/problems/FEMA2)

[Div-1 Contest](https://www.codechef.com/NOV20A/problems/FEMA2)

***Author:***  [Avinish Kumar](https://www.codechef.com/users/a_coder_hack)

**Tester:**  [Istvan Nagy](https://www.codechef.com/users/https://www.codechef.com/users/istva_adm)

# DIFFICULTY:

Easy

# PREREQUISITES:

Queue

# PROBLEM:

Chef loves to play with iron (Fe) and magnets (Ma). He took a row of N cells (numbered 1 through N) and placed some objects in some of these cells. You are given a string S with length N describing them; for each valid i, the i-th character of S is one of the following:

- ‘I’ if the i-th cell contains a piece of iron

- ‘M’ if the i-th cell contains a magnet

- ‘_’ if the i-th cell is empty

- ‘:’ if the i-th cell contains a conducting sheet

- ‘X’ if the i-th cell is blocked

If there is a magnet in a cell i and iron in a cell j, the *attraction power* between these cells is P_{i,j} = K+1 - |j-i| - S_{i,j}, where S_{i,j} is the number of cells containing sheets between cells i and j. This magnet can only *attract* this iron if P_{i, j} \gt 0 and there are no blocked cells between the cells i and j.

Chef wants to choose some magnets (possibly none) and to each of these magnets, assign a piece of iron which this magnet should attract. Each piece of iron may only be attracted by at most one magnet and only if the attraction power between them is positive and there are no blocked cells between them. Find the maximum number of magnets Chef can choose.

# QUICK EXPLANATION:

We will try to collect an iron at an index with the least possible magnet’s index which has yet not been used to collect any other Iron.

# EXPLANATION:

First thing is whenever we encounter a Wall it divides the string into two parts. And those parts can not have any relation or attraction between themselves.

Sheet reduces the magnetic strength by an additional one so simply add an extra position near the sheet. This will automatically reduce the strength by one. So create a new string adding an additional sheet whenever it is encountered. We will now work on the new string.

We will try to collect an iron at an index with the least possible magnet’s index which has yet not been used to collect any other Iron. As higher we will go in the index, the chance of using the magnet with less index will get less as its range is limited. So try to find the minimum index of magnet that can collect the iron and increment the ans if such magnet is found.

Create two empty queues (one for the magnets (qm) and other for the iron (qi)). qi will contain the iron indexes and qm contains magnet indexes found till current index and yet not used by any Magnet and Iron respectively. Start reading the characters from the 0th index.

If a magnet is found try reading qi for an index that is in the range of magnet until qi gets empty. If such iron is found increase the ans counter else insert this index to qm. And vice versa if iron is found.

# SOLUTIONS:

Setter's Solution
``/*
    * @authr AVINISH KUMAR
    * @college BIT MESRA
*/

#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll t;
    cin >> t;
    while (t--)
    {

        ll n, k;
        cin >> n >> k;
        string s;
        cin >> s;

        string new_s = "";

        //sheet reduces the magnetic strength by an additional one so simple
        //add an extra position with sheet. This will automatically reduce the
        //strength by one.
        for (auto i : s)
        {
            if (i == ':')
            {
                new_s += i;
            }
            new_s += i;
        }

        //Queues to store index of Magnet and Iron found till the index
        //and yet not used
        queue<ll> qi; //iron indexes
        queue<ll> qm; //magnets indexes

        //the current index of string
        int j = 0;

        //it stores the number of iron collectible by magnet
        int ans = 0;

        for (auto i : new_s)
        {
            //If current character is Iron, we will check the queue for the Magnet whose
            //index is in range of K. If no such Magnet is found we push the Iron's index
            //to qi queue. If there is such Magnet, we will pop the Magnet out of queue qm and
            //increment the ans as the Iron can be collected by that Magnet.
            if (i == 'I')
            {
                while (!qm.empty() && qm.front() + k < j)
                {
                    qm.pop();
                }

                if (!qm.empty())
                {
                    ans++;
                    qm.pop();
                }

                else
                {
                    qi.push(j);
                }
            }

            //vice versa if magnet is found.
            else if (i == 'M')
            {

                while (!qi.empty() && qi.front() + k < j)
                {
                    qi.pop();
                }

                if (!qi.empty())
                {
                    ans++;
                    qi.pop();
                }

                else
                {
                    qm.push(j);
                }
            }

            //if there is a wall then simply remove all the previous magnets and irons
            else if (i == 'X')
            {
                while (!qm.empty())
                {
                    qm.pop();
                }
                while (!qi.empty())
                {
                    qi.pop();
                }
            }

            //increment the index of string
            j++;
        }

        //output the final answer
        cout << ans << endl;
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>

using namespace std;

//FEMA2
uint32_t calc(const string& s, int K)
{
	int N = s.length();
	int i = 0, m = 0, res = 0;
	while (i < N && m < N)
	{
		while (i < N && (i < m - K || s[i] != 'I'))
			++i;
		while (m < N && (m < i - K || s[m] != 'M'))
			++m;
		if (i < N && m < N && abs(i - m) <= K)
		{
			++res;
			++i;
			++m;
		}
	}
	return res;
}

int main(int argc, char** argv)
{
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int tc = 0; tc < T; ++tc)
	{
		int N, K;
		string s;
		cin >> N >> K;
		cin >> s;
		string z;
		uint32_t res = 0;
		for(auto c: s)
		{
			if (c == '_')
				z += ' ';
			else if (c == ':')
				z += "  ";
			else if (c == 'X')
			{
				if (z.length())
					res+=calc(z, K);
				z.clear();
			}
			else
				z += c;
		}
		if (z.length())
			res += calc(z, K);
		cout << res << endl;
	}
	return 0;
}
``

# VIDEO EDITORIAL (Hindi):

# VIDEO EDITORIAL (English):

</details>
