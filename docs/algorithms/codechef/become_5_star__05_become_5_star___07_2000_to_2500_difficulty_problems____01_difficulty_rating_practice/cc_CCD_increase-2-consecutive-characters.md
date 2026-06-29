# Increase 2 consecutive characters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CCD |
| Difficulty Rating | 2171 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CCD](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CCD) |

---

## Problem Statement

Chef has $2$ strings $A$ and $B$ of equal length $N$. Both strings contain lowercase english alphabets only.

Chef can perform several moves on string $A$. In one move, Chef has to:
- Select an index $i \space (1 \leq i \leq N-1)$.
- Replace $A[i]$ with $(A[i]+1)$.
- Replace $A[i+1]$ with $(A[i+1]+1)$.

For example, if $A = \texttt{abcze}$, a valid move would be to select index $3$. This way the string becomes $\texttt{abdae}$ after performing the move. Note that the value at an index is cyclically incremented. This means that, $\texttt{a} \rightarrow \texttt{b}$, $\texttt{b} \rightarrow \texttt{c}$, $\ldots$, $\texttt{z} \rightarrow \texttt{a}$.

Chef has been asked to answer $Q$ queries. Each query is of the form:
- $L$ $R$: Given $1 \leq L \leq R \leq N$, Chef wants to know if it is possible to convert the substring $A[L, R]$ to $B[L, R]$ by performing the above mentioned move **any** number of times.

For each query, output in a single line $\texttt{Yes}$, if the conversion is possible using any number of moves. Otherwise, print $\texttt{No}$.

**NOTE:** Queries are **independent**. Thus, the original strings $A$ and $B$ would be retained to process next query. For each query solve for substrings $A[L,R]$ and $B[L,R]$ only. So valid values for $i$ will be among $L$ to $R - 1$ only.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- First line of each test case contains two integers $N, Q$.
- Second line of each test case contains string $A$.
- Third line of each test case contains string $B$.
- $Q$ lines follow, where the $i^{th}$ line contains two integers $L_i R_i$ - the $i^{th}$ query.

---

## Output Format

Output $Q$ lines, where the $i^{th}$ line contains the answer to the $i^{th}$ query. The answer is $\texttt{Yes}$, if the conversion is possible using any number of moves. Otherwise, the answer is $\texttt{No}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{yEs}$, $\texttt{yes}$, $\texttt{Yes}$ and $\texttt{YES}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq Q \leq 2\cdot 10^5$
- $1 \leq L \le R \le N$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
- Sum of $Q$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
1
5 3
abcdz
nbhea
2 2
1 3
4 5
```

**Output**

```text
Yes
No
Yes
```

**Explanation**

**Test Case $1$:**
- For the first query, the substring $A[2,2] = \texttt{b}$ is already same as $B[2,2] = \texttt{b}$. Thus, the answer is $\texttt{Yes}$.
- For the second query, it can be proven that the substring $A[1,3]$ can never be made equal to $B[1,3]$ using any number of moves.
- For the third query, the substring $A[4,5] = \texttt{dz}$ and $B[4,5] = \texttt{ea}$. Applying the move on index $4$, we get $A[4] = \texttt{e}$ and $A[5] = \texttt{a}$. Hence, after one move, $A[4,5] = B[4,5]$. Thus, the answer is $\texttt{Yes}$ in this case.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CCD)

[Div-2 Contest](https://www.codechef.com/START29B/problems/CCD)

[Div-3 Contest](https://www.codechef.com/START29C/problems/CCD)

[Div-4 Contest](https://www.codechef.com/START29D/problems/CCD)

***Author:*** [Arpit Kesharwani](https://www.codechef.com/users/anript)

***Tester:*** [Anshu Garg](https://www.codechef.com/users/anshugarg12)

***Editorialist:*** [Arpit Kesharwani](https://www.codechef.com/users/anript)

#
[](#difficulty-2)DIFFICULTY:

EASY

#
[](#problem-3)PROBLEM:

Given two strings A, B and Q queries, for each query we have to choose substring A[L...R] and see if it is possible it to convert to B[L..R] by cyclically incrementing two consecutive characters of A[L…R].

#
[](#explanation-4)EXPLANATION:

Each query can be solved in O(R-L) as:

For query: L, R.

We will iterate over the substring from lowest to highest index and use the operation on [i,i+1] to change A[i] = B[i] for i \lt R.

If the last character A[R] becomes equal to B[R] after doing above operations the answer is YES else it is NO.

The above process of updating at each index and be mathematically expressed as:

Let C_i = B_i - A_i, be the number of operations to convert A_i to B_i if increasing single character were allowed.

Also for each query let’s define D_i as the number of operation we apply at index i.

Then, mathematically D_i = C_i - D_{i-1} as after applying D_{i-1} operation on index i-1, A_i changes to A_i + D_{i-1}, so to make it equal to B_i we do B_i - (A_i + D_{i-1}) operations on i^{th} index.

So, we get the value of D_R as:

D_R = C_R - C_{R-1} + C_{R-2} + .... (-1)^{R-L} C_L

As we cannot apply any operation at R^{th} position so if we want substrings to be equal D_R must be 0. Therefore the alternating sum of C_i in range L to R must be zero modulo 26 for answer to be YES .

Modulo 26 is required because operations are cyclic with length 26, as applying the same operation to an index 26 times, results in the same result. So, if D_R = 26\cdot p + t  (where t is the remainder of D_R modulo 26), then applying operation at R, D_R times is same as applying operation at R, t times.

#
[](#solutions-5)SOLUTIONS:

Setter's Solution
``#include<iostream>

using namespace std ;

int main() {
	int test_cases ;
	cin >> test_cases ;
	long long sum_n = 0, sum_q = 0;
	for(int test_case = 1; test_case <= test_cases; ++ test_case) {
		int n, q; cin >> n >> q;
		string a, b; cin >> a >> b;
		int E[n+1]; E[0] = 0;
		for(int i=1;i<=n;++i) {
			int c = (b[i-1]-a[i-1]+26)%26;
			E[i] = E[i-1];
			if(i%2 == 0) E[i] += c;
			else E[i] -= c;
		}

		while(q--) {
			int l,r; cin >> l >> r;
			if((E[r]-E[l-1])%26) cout << "NO\n";
			else cout << "YES\n";
		}
	}
}
``

</details>
