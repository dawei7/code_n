# Array Rotation Returns

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRT |
| Difficulty Rating | 1818 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [ARRT](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/ARRT) |

---

## Problem Statement

You are given a sequence $A_1, A_2, \ldots, A_N$ which contains pairwise distinct elements and a sequence $B_1, B_2, \ldots, B_N$, which also contains pairwise distinct elements (but not necessarily distinct from elements of $A$). For each valid $i$, $1 \leq A_i, B_i \leq 2 \cdot N$.

You may rotate $B$ as many times as you want. A rotation consists of moving the first element of the sequence to the end. Afterwards, let's define a sequence $C_1, C_2, \ldots, C_N$ as $C_i = (A_i + B_i) \% N$ for each valid $i$.

There are $N$ possible sequences $C$. Find the lexicographically smallest of these sequences.

**Note:** A sequence $x$ is lexicographically smaller than a different sequence $y$ if $x_i < y_i$, where $i$ is the smallest valid index where the sequences $x$ and $y$ differ.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

---

## Output Format

For each test case, print a single line containing $N$ space-separated integers $C_1, C_2, \ldots, C_N$ denoting the lexicographically smallest sequence.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 2 \cdot N$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
1
3
1 4 5
1 3 4
```

**Output**

```text
1 2 0
```

**Explanation**

**Example case 1:** After rotating $B$ once, it becomes $(3,4,1)$. Now $C = (1,2,0)$. This is the lexicographically smallest of all possible sequences $C$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ARRT)

[Contest: Division 3](https://www.codechef.com/LTIME98C/problems/ARRT)

[Contest: Division 2](https://www.codechef.com/LTIME98B/problems/ARRT)

[Contest: Division 1](https://www.codechef.com/LTIME98A/problems/ARRT)

**Author:** [Prasant Kumar](https://www.codechef.com/users/prasant21)

**Tester :** [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Easy

# PREREQUISITES:

Observation

# PROBLEM:

Given a sequence A which contains distinct elements and array B which also contains distinct elements of size N, and 1 \leq A_i, B_i \leq 2 \cdot N.

You can rotate B as many times as you want. Print lexicographically smallest array C, C is defined as C_i = (A_i + B_i) \% N, here i is i-th element from left.

If we have two arrays x and y, then x is lexicographically smaller if x_i < y_i, where i is the first index in which the arrays x and y differ.

# EXPLANATION:

To find the lexicographically smallest array, one needs to find those arrays which have their starting number smallest among all possible arrays that can be formed.

Hence we need to find the such starting points of an array B which gives us C_0 = (A_0 + B_i) \% N, to be the smallest number among all possible starting points.

**Claim:** There can exist at most 2 starting points.

Proof

Given that all the elements of the array B lie in the range of [1,2*N] and are distinct. Let’s say some value X that lies in the array B gives us the minimum value. Then C_0 will be:

C_0 = (A_i + X)\% N

C_0 = A_i\%N + X\%N

Now let’s see what are the other possible values by which we can replace X and still get the same C_0. As

X\%N = (X+k*N)\%N

Hence we can replace X with (X+k*N). Now, what is the range of k such that (X+k*N) lies in the range of [1,2*N] such that X lies in the range of [1, N].

(X+k*N) \le 2*N

We can see that k cannot be greater than 2, hence there exists at most 2  values for which C_0 will be smallest among all possible choices and those are X and X+N.

Finally, we can find at most two arrays, and print the lexicographically smallest array out of them.

# TIME COMPLEXITY:

O(N) per test case

# SOLUTIONS:

Author
``#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define endl "\n"

bool cmp(vector<int> &a,vector<int> &b){

	int n=a.size();
	for(int i=0;i<n;i++){
		if(a[i]==b[i])continue;

		return (a[i]<b[i]);
	}
	return 1;
}

signed main(){

	ios_base::sync_with_stdio(0) , cin.tie(0);
//	freopen("nt.txt","r",stdin);
//	freopen("new_out.txt","w",stdout);
	int t;cin>>t;
	while(t--){
		int n;cin>>n;
		int arr[n],brr[n];
		for(int i=0;i<n;i++){
			cin>>arr[i];
		}
		for(int i=0;i<n;i++){
			cin>>brr[i];
		}
		int mini=1e9;
		for(int i=0;i<n;i++){
			int temp=(arr[0]+brr[i])%n;
			mini=min(temp,mini);
		}

		vector<int> st;
		for(int i=0;i<n;i++){
			int temp=(arr[0]+brr[i])%n;
			if(temp==mini){
				st.push_back(i);
			}
		}
		vector<vector<int>> permutations;

		for(int j : st){
			vector<int> temp;
			for(int i=0;i<n;i++){
				temp.push_back((arr[i]+brr[j])%n);
				j++;
				j%=n;
			}
			permutations.push_back(temp);
		}

		sort(permutations.begin(),permutations.end(),cmp);

		for(int x : permutations[0]){
			cout<<x<<" ";
		}cout<<endl;

	}

	return 0;
}

``

Tester
``
#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

void solve() {
    int n;
    cin >> n;
    vi a(n), b(n);
    rep(i, 0, n) cin >> a[i];
    rep(i, 0, n) cin >> b[i];
    int bmod = n;
    vi best;
    rep(i, 0, n) {
        int val = (a[0] + b[i]) % n;
        if(val < bmod) {
            bmod = val;
            best.clear();
        }
        if(val == bmod) best.push_back(i);
    }
    vector<vi> vc;
    for(int i : best) {
        vi v;
        rep(j, 0, n) v.push_back((a[j] + b[(i + j) % n]) % n);
        vc.push_back(v);
    }
    vi c = *min_element(all(vc));
    rep(i, 0, n) cout << c[i] << ' ';
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) solve();
}
``

Editorialist
``// Subtask 2

#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
	int n;
	cin>>n;

	int a[n],b[n];

	for(int i=0;i<n;i++)
	{
		cin>>a[i];
		a[i] = a[i] % n;
	}

	int mi = n-1;

	for(int i=0;i<n;i++)
	{
		cin>>b[i];
		b[i] = b[i] % n;

		mi = min(mi,(a[0]+b[i])%n);
	}

	set<vector<int>> s1;

	int co = 0;

	for(int i=0;i<n;i++)
	{
		if((a[0]+b[i])%n==mi)
		{
			co++;
			vector <int> v1;

			for(int j=0;j<n;j++)
				v1.push_back((a[j]+b[(i+j)%n])%n);

			s1.insert(v1);
		}
	}

	assert(co<=2);

	vector <int> ans = *s1.begin();

	for(auto itr: ans)
		cout<<itr<<" ";

	cout<<"\n";
}

int32_t main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

  // freopen("input.txt","r",stdin);
  // freopen("output.txt","w",stdout);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
