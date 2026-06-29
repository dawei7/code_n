# Possible Victory

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | T20MCH |
| Difficulty Rating | 769 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [T20MCH](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/T20MCH) |

---

## Problem Statement

Chef is playing in a T20 cricket match. In a match, Team A plays for 20 overs. In a single over, the team gets to play 6 times, and in each of these 6 tries, they can score a maximum of 6 runs. After Team A's 20 overs are finished, Team B similarly plays for 20 overs and tries to get a higher total score than the first team. The team with the higher total score at the end wins the match.

Chef is in Team B. Team A has already played their 20 overs, and have gotten a score of $R$. Chef's Team B has started playing, and have already scored $C$ runs in the first $O$ overs. In the remaining $20 - O$ overs, find whether it is possible for Chef's Team B to get a score high enough to win the game. That is, can their final score be strictly larger than $R$?

---

## Input Format

- There is a single line of input, with three integers, $R, O, C$.

---

## Output Format

Output in a single line, the answer, which should be "YES" if it's possible for Chef's Team B  to win the match and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $0 \leq C \leq R \leq 720$
- $1 \leq O \leq 19$
- $0 \leq C \leq 36 * O$

---

## Examples

**Example 1**

**Input**

```text
719 18 648
```

**Output**

```text
YES
```

**Explanation**

In the remaining $20-O = 2$ overs, Team B gets to play $2*6 = 12$ times, and in each try, they can get a maximum of 6 score. Which means that the maximum score that they can acheieve in these 2 overs is $12*6 = 72$. Thus, the maximum total score that Team B can achieve is $C+72 = 720$. $720$ is strictly more than Team A's score of $719$, and hence Chef's Team B can win this match.

**Example 2**

**Input**

```text
720 18 648
```

**Output**

```text
NO
```

**Explanation**

Similar to the previous explanation, the maximum total score that Team B can achieve is $720$, which isn't strictly greater than Team A's $720$.Hence Chef's Team B can't win this match.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/T20MCH)

[Contest: Division 1](https://www.codechef.com/START2A/problems/T20MCH)

[Contest: Division 2](https://www.codechef.com/START2B/problems/T20MCH)

[Contest: Division 3](https://www.codechef.com/START2C/problems/T20MCH)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# PROBLEM:

Chef is playing a T20 cricket match, and the opposite team has scored R runs in total. Chef has already scored C runs in O overs. There are a total of 20 overs that Chef can play, and in each over, there are 6 balls. The maximum runs that Chef can score in a single ball is 6 and assume that extras are not awarded in this match. Find if it is possible for the Chef to win the game if the winner has to score strictly higher runs than the opponent.

# EXPLANATION:

In order to win the match, Chef should have a score strictly greater than the opponent’s score. The score of the opponent is already given to us as R. We are also given a score of C which Chef has scored in O overs.

Number of overs that are left in the game:

20-O

Chef can score 6 runs in each ball and hence 36 runs in an over. Hence the maximum runs that Chef can score in the remaining overs are:

(20-O)*36

Hence, the maximum score of Chef will be:

S=C+(20-O)*36

Now if the Chef score S is strictly greater than the opponent’s score R i.e (S>R), then Chef wins the game otherwise he loses.

# TIME COMPLEXITY:

O(1)

# SOLUTIONS:

Setter
``#include<bits/stdc++.h>

using namespace std;

const int maxs = 720, maxo = 19;

int main()
{
    int r, o, c; cin >> r >> o >> c;
    assert(c <= 36 * o);
    string ans = (r - c < 36 * (20 - o) ? "yEs" : "nO");
    cout << ans << endl;
}
``

Tester
``#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>
using namespace __gnu_pbds;
using namespace __gnu_cxx;
#ifndef rd
#define trace(...)
#define endl '\n'
#endif
#define pb push_back
#define fi first
#define se second
#define int long long
typedef long long ll;
typedef double f80;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<ll,ll> pll;
#define double long double
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const int infi=0x3f3f3f3f;
const ll infl=0x3f3f3f3f3f3f3f3fLL;
const int mod=998244353;
//const int mod=1000000007;
typedef vector<int> vi;
typedef vector<ll> vl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> oset;
auto clk=clock();
mt19937_64 rang(chrono::high_resolution_clock::now().time_since_epoch().count());
int rng(int lim) {
	uniform_int_distribution<int> uid(0,lim-1);
	return uid(rang);
}
int powm(int a, int b) {
	int res=1;
	while(b>0) {
		if(b&1)
			res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
}

long long readInt(long long l,long long r,char endd){
	long long x=0;
	int cnt=0;
	int fi=-1;
	bool is_neg=false;
	while(true){
		char g=getchar();
		if(g=='-'){
			assert(fi==-1);
			is_neg=true;
			continue;
		}
		if('0'<=g && g<='9'){
			x*=10;
			x+=g-'0';
			if(cnt==0){
				fi=g-'0';
			}
			cnt++;
			assert(fi!=0 || cnt==1);
			assert(fi!=0 || is_neg==false);

			assert(!(cnt>19 || ( cnt==19 && fi>1) ));
		} else if(g==endd){
			if(is_neg){
				x= -x;
			}
			assert(l<=x && x<=r);
			return x;
		} else {
			assert(false);
		}
	}
}
string readString(int l,int r,char endd){
	string ret="";
	int cnt=0;
	while(true){
		char g=getchar();
		assert(g!=-1);
		if(g==endd){
			break;
		}
		cnt++;
		ret+=g;
	}
	assert(l<=cnt && cnt<=r);
	return ret;
}
long long readIntSp(long long l,long long r){
	return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
	return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
	return readString(l,r,'\n');
}
string readStringSp(int l,int r){
	return readString(l,r,' ');
}

void solve() {
	int r=readIntSp(0,720),o=readIntSp(1,19),c=readIntLn(0,min(r,36*o));
	string ans;
	if(c+(20-o)*36>r) {
		ans="yes";
	} else {
		ans="no";
	}
	for(char &i:ans) {
		if(rng(2))
			i=i-'a'+'A';
	}
	cout<<ans<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(1);
//	int t=readIntLn(1,100000);
	int t=1;
//	cin>>t;
	fr(i,1,t)
		solve();
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int r,o,c;
  cin>>r>>o>>c;

  int rem=20-o;

  if(c+rem*36>r)
    cout<<"YES"<<"\n";
  else
    cout<<"NO"<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  t=1;

  while(t--)
    solve();

return 0;
}

``

</details>
