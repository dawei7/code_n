# Vaccine Distribution

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VACCINE2 |
| Difficulty Rating | 1219 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [VACCINE2](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/VACCINE2) |

---

## Problem Statement

Finally, a COVID vaccine is out on the market and the Chefland government has asked you to form a plan to distribute it to the public as soon as possible. There are a total of $N$ people with ages $a_1, a_2, \ldots, a_N$.

There is only one hospital where vaccination is done and it is only possible to vaccinate up to $D$ people per day. Anyone whose age is $\ge 80$ or $\le 9$ is considered to be *at risk*. On each day, you may not vaccinate both a person who is at risk and a person who is not at risk. Find the smallest number of days needed to vaccinate everyone.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $D$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

### Output
For each test case, print a single line containing one integer ― the smallest required number of days.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^4$
- $1 \le D \le 10^5$
- $1 \le a_i \le 100$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
10 1
10 20 30 40 50 60 90 80 100 1
5 2
9 80 27 72 79
```

**Output**

```text
10
3
```

**Explanation**

**Example case 1:** We do not need to worry about how the people are grouped, since only one person can be vaccinated in a single day. We require as many days as there are people.

**Example case 2:** There are two people at risk and three people who are not at risk. One optimal strategy is to vaccinate the two people at risk on day $1$ and the remaining three on the next $2$ days.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 1
10 20 30 40 50 60 90 80 100 1
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
5 2
9 80 27 72 79
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/VACCINE2)

[Div2](https://www.codechef.com/DEC20B/problems/VACCINE2)

**Setter:**  [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:**  [Alexander Morozov](https://www.codechef.com/users/scanhex)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

[Ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)

### PROBLEM:

We have an array of ages for N people. Anyone whose age is  \ge 80 or  \le 9 is considered to be at risk. Per day, you can only vaccinate up to D people and on each day you cannot vaccinate both categories of people (those who are at risk and those who are not at risk). The task is to find the minimum number of days to vaccinate all N people.

### QUICK EXPLANATION:

First find the minimum numbers of days to vaccinate all the people who are at risk, then find the same for all the people who are not at risk and add the results to get the required answer.

### EXPLANATION:

Since on a particular day we can’t vaccinate both risky people and non-risky people, let us treat both the cases separately and finally add both the results to get the final answer.

-

First count the number of people who are at risk. Let the count be R . Since on each day we can give vaccine to atmost D people, the minimum number of days required to vaccinate all the risky people wll be \Bigl\lceil \dfrac{R}{D} \Bigr\rceil .

-

The number of people who are not at risk will be N-R . Similar to the above case, the minimum number of days required to vaccinate all the non-risky people will be \Bigl\lceil \dfrac{N-R}{D} \Bigr\rceil .

-

Therefore, the minimum number of days required to vaccinate all N people will be

\Bigl\lceil \dfrac{R}{D} \Bigr\rceil + \Bigl\lceil \dfrac{N-R}{D} \Bigr\rceil .

### TIME COMPLEXITY:

O(n) for each testcase.

### SOLUTION:

Editorialist's solution (C++)
``#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, d;
		cin >> n >> d;
		vector<int> a(n);
		for (int i = 0; i < n; i++)
			cin >> a[i];

		int risk = 0, not_risk = 0;

		for (int i = 0; i < n; i++)
		{
			if (a[i] >= 80 || a[i] <= 9)
				risk++;
			else
				not_risk++;
		}

		int ans = (risk / d) + (risk % d > 0) + (not_risk / d) + (not_risk % d > 0);
		cout << ans << endl;
	}
	return 0;
}
``

Setter's solution (Java)
``import java.util.*;
import java.io.*;
public
class Main
{
	static PrintWriter out;
	static InputReader in;
public
	static void main(String args[]) throws IOException
	{
		out = new PrintWriter(System.out);
		// out = new PrintWriter(new FileWriter("/home/daanish/CP/codechef/LearningTeam/Testing/2020/Long/Dec/2/out.txt"));
		in = new InputReader();
		new Main();
		out.flush();
		out.close();
	}
	Main()
	{
		solve();
	}
	final int maxd = (int)1e5;
	final int maxn = (int)1e4;
	void solve()
	{
		int t = in.nextInt();
		while (t-- > 0)
		{
			int n = in.nextInt(), d = in.nextInt();
			int c1 = 0, c2 = 0;
			for (int i = 0; i < n; i++)
			{
				int x = in.nextInt();
				if ((x >= 0 && x <= 9) || (x >= 80 && x <= 100))
					c2++;
				else if (x > 9 && x < 80)
					c1++;
			}
			if (c1 + c2 != n || n > maxn || n < 0 || d > maxd || d < 0 || t > 9 || t < 0)
				System.out.println("wrong test no: " + t);

			out.println(((c2 + d - 1) / d + (c1 + d - 1) / d));
		}
	}
public
	static class InputReader
	{
		BufferedReader br;
		StringTokenizer st;
		InputReader() throws IOException
		{
			br = new BufferedReader(new InputStreamReader(System.in));
			// br = new BufferedReader(new FileReader("/home/daanish/CP/codechef/LearningTeam/Testing/2020/Long/Dec/2/in.txt"));
		}
	public
		int nextInt()
		{
			return Integer.parseInt(next());
		}
	public
		long nextLong()
		{
			return Long.parseLong(next());
		}
	public
		double nextDouble()
		{
			return Double.parseDouble(next());
		}
	public
		String next()
		{
			while (st == null || !st.hasMoreTokens())
			{
				try
				{
					st = new StringTokenizer(br.readLine());
				}
				catch (IOException e)
				{
				}
			}
			return st.nextToken();
		}
	}
}
``

# VIDEO EDITORIAL:

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
