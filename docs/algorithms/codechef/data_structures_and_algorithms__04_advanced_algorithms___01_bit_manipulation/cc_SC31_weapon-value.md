# Weapon Value

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SC31 |
| Difficulty Rating | 1204 |
| Difficulty Band | Bit Manipulation |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Bitwise Operators |
| Official Link | [SC31](https://www.codechef.com/learn/course/bit-manipulation/BITM04/problems/SC31) |

---

## Problem Statement

A competition with $N$ participants (numbered $1$ through $N$) is taking place in Chefland. There are $N-1$ rounds in the competition; in each round, two arbitrarily chosen contestants battle, one of them loses and drops out of the competition.

There are $10$ types of weapons (numbered $1$ through $10$). You are given $N$ strings $S_1, S_2, \ldots, S_N$; for each valid $i$ and $j$, the $j$-th character of $S_i$ is '1' if the $i$-th contestant initially has a weapon of type $j$ or '0' otherwise. During each battle, for each type $j$ such that both contestants in this battle currently have weapons of type $j$, these weapons of both contestants are destroyed; after the battle, the winner collects all remaining (not destroyed) weapons of the loser. Note that each contestant may win or lose regardless of the weapons he/she has.

Chef is feeling bored watching the contest, so he wants to find the maximum possible number of weapons the winner of the tournament could have after the last battle, regardless of which contestants fight in which battles or the results of the battles. Can you help him?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains a single string $S_i$.

### Output
For each test case, print a single line containing one integer ― the maximum number of weapons the winner could have.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $|S_i| = 10$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):** $1 \le N \le 10$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
3
1110001101
1010101011
0000000011
```

**Output**

```text
4
```

**Explanation**

**Example case 1:** If the first person defeats the second person, weapons $1$, $3$, $7$ and $10$ are destroyed. Then, if the third person defeats the first person (who now has weapons $2$, $5$, $8$ and $9$), weapons $9$ are destroyed and the winner has weapons $2$, $5$, $8$ and $10$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SC31)

[Div-2 Contest](https://www.codechef.com/NOV19B/problems/SC31)

***Author:***  [Hritik Aggarwal](https://www.codechef.com/users/invincibel)

***Tester:***  [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

***Editorialist:***  [Michael Nematollahi](https://www.codechef.com/users/watcher)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

XOR

# PROBLEM:

You are given a N non-negative integers in their binary representations. As long as there are at least two numbers in this set, you take two of them and replace them with their xor.

If you choose the order of the operations optimally, what is the maximum number of bits in the final number that you can achieve?

# QUICK EXPLANATION:

The order of operations does not matter. Hence, you can do the operations in an arbitrary order and find out what the final result is.

# EXPLANATION:

The first thing to notice is that when two contestants A and B fight, it doesn’t matter who wins. The winner ends up with the same set of weapons regardless of whether it’s A or B.

The next thing to note is that if we think of the input strings as binary representations of integers,

when two contestants with sets of weapons S and T fight, the winner’s set of weapons will be S \oplus T.

The above-mentioned two observations convert the original problem statement to the shorter version described above in the PROBLEM section.

Finally, because the XOR operations is both commutative and associative, it doesn’t matter in which order we arrange the fights; the final resulting number will always be the same.

Another way to think about this is that the final contestant will have the i^{th} weapon iff there are an odd number of contestants who have the i^{th} weapon at the beginning. The reason is that the outcome of a battle does not change the parity of the number of contestants who have the i^{th} weapon (you can confirm this by drawing all possible scenarios).

What this means is that we can arrange the fights in any arbitrary order and check what the final number is and output the number of bits in it set to 1.

The overall time complexity of this solution is O(N).

To view an implementation of the described solution, refer to the editorialist’s solution.

# SOLUTIONS:

Setter's Solution
``/******************************************
* AUTHOR : HRITIK AGGARWAL *
******************************************/
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define N 100005
#define MOD 1000000007
#define dd double
#define vi vector<int>
#define vll vector<ll>
#define forr(i, n) for(int i = 0; i < n; i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep1(i,b) for(int i=1;i<=b;i++)
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define ms(s, n) memset(s, n, sizeof(s))
#define F first
#define S second
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define int ll
ll po(ll a, ll x,ll m){ if(x==0){return 1;}ll ans=1;ll k=1;  while(k<=x) {if(x&k){ans=((ans*a)%m);} k<<=1; a*=a; a%=m; }return ans; }
int32_t main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    #ifndef ONLINE_JUDGE
     freopen("input.txt", "r", stdin);
     freopen("b.txt", "w", stdout);
    #endif
    int t;
    cin>>t;
    while(t--){
    	int n;
    	cin>>n;
    	string s[n];
    	forr(i,n){
    		//cout<<"a";
    		cin>>s[i];
    	}
    	//cout<<s[0]<<"\n";
    	if(s[0].length()==1){
    		int ans=0;

    	for(int i=0;i<1;i++){
    		int sum=0;
    		forr(j,n){
    			int nu = s[j][i]-'0';

    			sum^=nu;
    		}
    		ans+=sum;
    	}

    	cout<<ans<<"\n";
    }
    else{
    	int ans=0;

    	for(int i=0;i<10;i++){
    		int sum=0;
    		forr(j,n){
    			int nu = s[j][i]-'0';

    			sum^=nu;
    		}
    		ans+=sum;
    	}

    	cout<<ans<<"\n";
    }
	}
return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
int rint(char nxt){
  char ch=getchar();
  int v=0;
  int sgn=1;
  if(ch=='-')sgn=-1;
  else{
    assert('0'<=ch&&ch<='9');
    v=ch-'0';
  }
  while(true){
    ch=getchar();
    if('0'<=ch && ch<='9')v=v*10+ch-'0';
    else{
      assert(ch==nxt);
      break;
    }
  }
  return v*sgn;
}
string rword(char nxt){
  string ans="";
  while(true){
    char ch=getchar();
    if(ch==nxt)break;
    ans.push_back(ch);
  }
  return ans;
}
int main(){
  int t=rint('\n');
  while(t--){
    int n=rint('\n');
    assert(1<=n&&n<=1e5);

    vector<int>ans(123,0);
    vector<string>all;
    for(int i=0;i<n;i++){
      string b=rword('\n');
      for(char ch:b)assert(ch=='0' || ch=='1');
      all.push_back(b);
      for(int j=0;j<int(b.size());j++){
        ans[j]^=(b[j]-'0');
      }
    }
    for(int i=1;i<n;i++)assert(all[i].size()==all[i-1].size());
    int o=0;
    for(int x:ans)o+=x;
    printf("%d\n",o);
  }
  assert(getchar()==EOF);
  return 0;
}
``

Editorialist's Solution
``#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define F first
#define S second

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	while (te--){
		int n; cin >> n;
		int x = 0;
		while (n--){
			string s; cin >> s;
			reverse(s.begin(), s.end());
			int y = 0;
			for (int j = 0; j < 10; j++)
				if (s[j] == '1')
					y ^= 1<<j;
			x ^= y;
		}
		cout << __builtin_popcount(x) << "\n";
	}
	return 0;
}
``

</details>
