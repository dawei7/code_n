# PerMEXuation 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMEX |
| Difficulty Rating | 1874 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [PERMEX](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/PERMEX) |

---

## Problem Statement

You are given an integer $N$ and a ($0$-indexed) binary string $A$ having length $N+1$.

Find any permutation $P$ of ${0,1,2,...,N-1}$ (or determine that it does not exist) that satisfies the following conditions for all $i$ ($0 \le i \le N$):
- if $A_i = 0$: No contiguous segment of $P$ has $\texttt{mex}$ equal to $i$
- if $A_i = 1$: There exists at least one contiguous segment of $P$ that has $\texttt{mex}$ equal to $i$

If multiple permutations exist that satisfy the given conditions, print any.

Note: $\texttt{mex}$ of a segment is the smallest non-negative number that does not occur in that segment.

---

## Input Format

- The first line contains the number of test cases $T$. Description of the test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line of each test case contains the binary string $A$ of length $N + 1$.

---

## Output Format

For each test case print :
   - $\texttt{Yes}$ if there exists a permutation $P$ that satisfies the conditions described in the statement, followed by the permutation $P$ in the next line (If multiple permutations exist that satisfy the given conditions, print any).
   - $\texttt{No}$ otherwise.

You may print each character of $\texttt{Yes}$ and $\texttt{No}$ in uppercase or lowercase (for example, $\texttt{yes}$, $\texttt{yEs}$, $\texttt{YES}$ will be considered identical).

---

## Constraints

- $1 \leq T \leq  10^4$
- $2 \leq N \leq 3 \cdot 10^5$
- $|A| = N + 1$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2
111
5
110100
5
110101
7
11100111
```

**Output**

```text
Yes
0 1
No
Yes
0 2 1 4 3
Yes
0 1 3 4 2 5 6
```

**Explanation**

**Test case-1:** One of the possible permutations satisfying the given conditions is [$0, 1$] because:
- $\texttt{mex}([1]) = 0$. Therefore the condition is satisfied for $i = 0$.
- $\texttt{mex}([0]) = 1$. Therefore the condition is satisfied for $i = 1$.
- $\texttt{mex}([0, 1]) = 2$. Therefore the condition is satisfied for $i = 2$.

**Test case-2:** It can be proven that no permutation exists that satisfies the given conditions.

**Test case-3:** One of the possible permutations satisfying the given conditions is [$0, 2, 1, 4, 3$] because:
- $\texttt{mex}([2]) = 0$. Therefore the condition is satisfied for $i = 0$.
- $\texttt{mex}([0, 2]) = 1$. Therefore the condition is satisfied for $i = 1$.
- There does not exist any segment with $\texttt{mex} = 2$. Therefore the condition is satisfied for $i = 2$.
- $\texttt{mex}([0, 2, 1]) = 3$. Therefore the condition is satisfied for $i = 3$.
- There does not exist any segment with $\texttt{mex} = 4$. Therefore the condition is satisfied for $i = 4$.
- $\texttt{mex}([0, 2, 1, 4, 3]) = 5$. Therefore the condition is satisfied for $i = 5$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK138A/problems/PERMEX)

[Contest Division 2](https://www.codechef.com/COOK138B/problems/PERMEX)

[Contest Division 3](https://www.codechef.com/COOK138C/problems/PERMEX)

[Contest Division 4](https://www.codechef.com/COOK138D/problems/PERMEX)

**Setter:** [Nabil Boudra](https://www.codechef.com/users/boredm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

[MEX](https://en.wikipedia.org/wiki/Mex_(mathematics))

#
[](#problem-4)PROBLEM:

You are given an integer N and a (0-indexed) binary string A having length N+1.

Find any permutation P of {0,1,2,...,N-1} (or determine that it does not exist) that satisfies the following conditions for all i (0 \le i \le N):

- if A_i = 0: No contiguous segment of P has \texttt{mex} equal to i

- if A_i = 1: There exists at least one contiguous segment of P that has \texttt{mex} equal to i

If multiple permutations exist that satisfy the given conditions, print any.

Note: \texttt{mex} of a segment is the smallest non-negative number that does not occur in that segment.

#
[](#explanation-5)EXPLANATION:

When is the answer -1?

We have to find a permutation P of \{0,1,2,...,N-1\}.

-

Consider a subarray of length 1, containing only the i^{th} element. If P_i \neq 0, for this subarray of length 1 , the `MEX` is 0.

Since N \geq 2, there is always a subarray of length 1 such that it does not contain any 0 and thus, its `MEX` would be 0. This implies that the value of A_0 must be 1.

-

Similarly, consider a subarray of length 1 which contains only the i^{th} element such that P_i = 0. For this subarray, the `MEX` is 1.

Since P always contains a 0, there is always a subarray of length 1 such that its `MEX` is 1. In other words, the value of A_1 must be 1.

-

Consider the subarray of length N. This includes the whole permutation P. Thus, all the elements in the range [0, N-1] are included in this subarray and its `MEX` is N.

This implies that the value of A_N must be equal to 1.

To conclude, if any value out of A_0, A_1 or A_N is 0, no possible permutation exists which satisfies the given conditions and thus, the answer is -1.

If the values of A_0, A_1 and A_N are 1, we can always construct a solution.

We can construct a permutation P such that, for all the indices i (i>0) and A_i = 1, the `MEX` of the prefix of length i is equal to i. To construct this:

-

Start with the identity permutation. This means we set P_i = i for all (0 \leq i \leq N-1). Currently, for all prefixes of this permutation, the `MEX` of the prefix is equal to the length of the prefix.

-

Consider j as the first index where A_i = 0. Since for all indices <j, A_i = 1, we keep the prefix of length (j-1) as the identity permutation. Thus, P_k = k for all (0 \leq k <j-1).

If we keep the value of the (j-1)^{th} element (0-based indexing) as (j-1), we would have a subarray (prefix of length j) for which the `MEX` is equal to j.

Since A_j = 0, we have to avoid this. For that, we can swap the values P_{j-1} and P_{j}. Now, the resultant permutation looks like [0, 1, 2, …, j-2, j, j-1, j+1,..., N-1].

Note that in this permutation, there exists no subarray, where `MEX` of the subarray is j.

-

Based on the same observation, for all indices i where A_i = 0, we swap the (i-1)^{th} and i^{th} elements of P (0-based indexing).

-

If A_i = 1, the (i-1)^{th} element of P remains unchanged. Thus, the `MEX` of the prefix of length i is equal to i **only** when A_i = 1.

**P.S.**  This construction guarantees the lexicographically minimum permutation P which satisfies all the conditions.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(N) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
void solve(){
    int n;
    string a;
    cin>>n>>a;
    if(a[0]==a[1]&&a[1]==a.back()&&a[0]=='1'){
        cout<<"Yes\n";
        vector<int> res(n);
        for(int i=0;i<n;i++) res[i]=i;
        for(int i=0;i<n;i++) if(a[i]=='0') swap(res[i],res[i-1]);
        for(int&x:res)
            cout<<x<<" ";
        cout<<'\n';
    }
    else
        cout<<"No\n";
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t = 1;
    cin >> t;
    while(t--) solve();
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
int n;
int a[300001];
int main(){
    ios::sync_with_stdio(false);cin.tie(0);
    int t;cin >> t;
    while(t--){
    	cin >> n;
    	for(int i=0; i<=n ;i++){
    		char c;cin >> c;
    		a[i]=c-48;
		}
		if(a[0]==0 || a[1]==0 || a[n]==0){
			cout << "No\n";continue;
		}
		cout << "Yes\n";
		int ptr=1;
		cout << "0 ";
		while(ptr!=n){
			int nx=ptr+1;
			while(!a[nx]) nx++;
			for(int i=nx-1; i>=ptr ;i--) cout << i << ' ';
			ptr=nx;
		}
		cout << '\n';
	}
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    string s;
	    cin>>s;
	    if(s[0]=='0' || s[1]=='0' || s[n]=='0'){
	        cout<<"No";
	    }
	    else{
	        cout<<"Yes\n";
	        int p[n];
	        for(int i = 0; i<n; i++){
	            p[i] = i;
	        }
	        for(int i=1; i<=n; i++){
	            if(s[i]=='0'){
	                swap(p[i-1], p[i]);
	            }
	        }
	        for(int i = 0; i<n; i++) cout<<p[i]<<' ';
	    }
	    cout<<endl;
	}
	return 0;
}
``

</details>
