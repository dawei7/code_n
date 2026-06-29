# TCS Examination

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXAMTIME |
| Difficulty Rating | 1006 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [EXAMTIME](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/EXAMTIME) |

---

## Problem Statement

Two friends, Dragon and Sloth, are writing a computer science examination series.
There are three subjects in this series: $\text{DSA}$, $\text{TOC}$, and $\text{DM}$. Each subject carries $100$ marks.

You know the individual scores of both Dragon and Sloth in all $3$ subjects. You have to determine who got a better rank.

The rank is decided as follows:
- The person with a bigger total score gets a better rank
- If the total scores are tied, the person who scored higher in $\text{DSA}$ gets a better rank
- If the total score and the $\text{DSA}$ score are tied, the person who scored higher in $\text{TOC}$ gets a better rank
- If everything is tied, they get the same rank.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers denoting the scores of Dragon in $\text{DSA}$, $\text{TOC}$ and $\text{DM}$ respectively.
- The second line of each test case contains three space-separated integers denoting the scores of Sloth in $\text{DSA}$, $\text{TOC}$ and $\text{DM}$ respectively.

---

## Output Format

- For each test case, if Dragon got a better rank then output `"Dragon"`, else if Sloth got a better rank then output `"Sloth"`. If there was a tie then output `"Tie"`. Note that the string you output should not contain quotes.
- The output is **case insensitive**. For example, If the output is "Tie" then "TiE", "tiE", "tie", etc are also considered correct.

---

## Constraints

- $1 \leq T \leq 1000$
- Each score of both Dragon and Sloth lies between $0$ and $100$.

---

## Examples

**Example 1**

**Input**

```text
4
10 20 30
30 20 10
5 23 87
5 23 87
0 15 100
100 5 5
50 50 50
50 49 51
```

**Output**

```text
SLOTH
TIE
DRAGON
DRAGON
```

**Explanation**

- For the first test case, Sloth and Dragon have the same total score but Sloth gets a better rank because he has a higher score in $\text{DSA}$.
- For the second test case, Sloth and Dragon have the same rank because they have the same score among all subjects.
- For the third test case, Dragon gets a better rank because he has a greater total score.
- For the fourth test case, Sloth and Dragon have the same total score and same $\text{DSA}$ score. Dragon gets a better rank because he has a greater $\text{TOC}$ score.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 20 30
30 20 10
```

**Output for this case**

```text
SLOTH
```



#### Test case 2

**Input for this case**

```text
5 23 87
5 23 87
```

**Output for this case**

```text
TIE
```



#### Test case 3

**Input for this case**

```text
0 15 100
100 5 5
```

**Output for this case**

```text
DRAGON
```



#### Test case 4

**Input for this case**

```text
50 50 50
50 49 51
```

**Output for this case**

```text
DRAGON
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JAN222A/problems/EXAMTIME)

[Contest Division 2](https://www.codechef.com/JAN222B/problems/EXAMTIME)

[Contest Division 3](https://www.codechef.com/JAN222C/problems/EXAMTIME)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Two friends, Dragon and Sloth, are writing a computer science examination series. There are three subjects in this series : \text{DSA, TOC} and \text{DM}. Each subject carries 100 marks.

You know the individual scores of both Dragon and Sloth in all 3 subjects. You have to determine who got a better rank.

The rank is decided as follows:

- The person with a bigger total score gets a better rank.

- If the total scores are tied, the person who scored higher in \text{DSA} gets a better rank.

- If the total score and the \text{DSA} score are tied, the person who scored higher in \text{TOC} gets a better rank.

- If everything is tied, they get the same rank.

#
[](#explanation-5)EXPLANATION:

In this problem, we just need to implement the problem statement. The focus is on our ability to translate the problem statement into functioning error-free code.

We can simply check all the conditions required for determining the rank using if-else statements.

The point to note is that the priority of subjects matter. The priority order is:

\text{Total score > DSA score > TOC score > DM score}

Based on the order, we check if the scores are equal at the current priority level. If they are, we have an answer, else, we move to the lower priority level.

See solutions for implementation.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp> //required
//#include <ext/pb_ds/tree_policy.hpp> //required

//using namespace __gnu_pbds; //required
using namespace std;
//template <typename T> using ordered_set =  tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

// ordered_set <int> s;
// s.find_by_order(k); returns the (k+1)th smallest element
// s.order_of_key(k); returns the number of elements in s strictly less than k

#define pb               push_back
#define mp(x,y)          make_pair(x,y)
#define all(x)           x.begin(), x.end()
#define allr(x)          x.rbegin(), x.rend()
#define leftmost_bit(x)  (63-__builtin_clzll(x))
#define rightmost_bit(x) __builtin_ctzll(x) // count trailing zeros
#define set_bits(x)      __builtin_popcountll(x)
#define pow2(i)          (1LL << (i))
#define is_on(x, i)      ((x) & pow2(i)) // state of the ith bit in x
#define set_on(x, i)     ((x) | pow2(i)) // returns integer x with ith bit on
#define set_off(x, i)    ((x) & ~pow2(i)) // returns integer x with ith bit off
#define fi               first
#define se               second

typedef long long int ll;
typedef long double ld;

const int MOD = 1e9+7; // 998244353;
const int MX = 2e5+5;
const ll INF = 1e18; // not too close to LLONG_MAX
const ld PI = acos((ld)-1);
const ld EPS = 1e-8;
const int dx[4] = {1,0,-1,0}, dy[4] = {0,1,0,-1}; // for every grid problem!!

// hash map and operator overload from https://www.youtube.com/watch?v=jkfA0Ts6YBA
// Custom hash map
struct custom_hash
{
    static uint64_t splitmix64(uint64_t x)
    {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const
    {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};
template <typename T1, typename T2> // Key should be integer type
using safe_map = unordered_map<T1, T2, custom_hash>;

// Operator overloads
template<typename T1, typename T2> // cin >> pair<T1, T2>
istream& operator>>(istream &istream, pair<T1, T2> &p) { return (istream >> p.first >> p.second); }
template<typename T1, typename T2> // cout << pair<T1, T2>
ostream& operator<<(ostream &ostream, const pair<T1, T2> &p) { return (ostream << p.first << " " << p.second); }

template<typename T> // cin >> array<T, 2>
istream& operator>>(istream &istream, array<T, 2> &p) { return (istream >> p[0] >> p[1]); }
template<typename T> // cout << array<T, 2>
ostream& operator<<(ostream &ostream, const array<T, 2> &p) { return (ostream << p[0] << " " << p[1]); }

template<typename T> // cin >> vector<T>
istream& operator>>(istream &istream, vector<T> &v){for (auto &it : v) cin >> it; return istream;}
template<typename T> // cout << vector<T>
ostream& operator<<(ostream &ostream, const vector<T> &c) { for (auto &it : c) cout << it << " "; return ostream; }

ll power(ll x, ll n, ll m = MOD){
    if (x == 0 && n == 0) return 0; // undefined case
    ll res = 1;
    while (n > 0){
        if (n % 2)
            res = (res * x) % m;
        x = (x * x) % m;
        n /= 2;
    }
    return res;
}

clock_t startTime;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
double getCurrentTime()           {return (double)(clock() - startTime) / CLOCKS_PER_SEC;}
string to_string(string s)        {return '"' + s + '"';}
string to_string(const char* s)   {return to_string((string) s);}
string to_string(bool b)          {return (b ? "true" : "false");}
int inv(int x, int m = MOD)       {return power(x, m - 2, m);}
int getRandomNumber(int l, int r) { uniform_int_distribution<int> dist(l, r); return dist(rng);}

// https://github.com/the-tourist/algo/blob/master/misc/debug.cpp
template <typename A, typename B>
string to_string(pair<A, B> p) {return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";}
template <typename A>
string to_string(A v) {
  bool first = true;
  string res = "{";
  for (const auto &x : v) {
    if (!first) {
      res += ", ";
    }
    first = false;
    res += to_string(x);
  }
  res += "}";
  return res;
}
void debug_out() { cerr << endl; }
template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
  cerr << " " << to_string(H);
  debug_out(T...);
}

#ifdef LOCAL_DEBUG
	#define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
	#define debug(...) ;
#endif

// highly risky #defines
#define int ll // disable when you want to make code a bit faster
#define endl '\n' // disable when dealing with interactive problems

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef array<int,2> edge; // for graphs, make it array<int,3> for weighted edges

string p1 = "DRAGON";
string p2 = "SLOTH";

void solve(){
	// code starts from here
	vi a(3), b(3);
    cin >> a >> b;

    if(a == b){
        cout << "TIE" << endl;
        return;
    }

    int s1 = accumulate(all(a), 0);
    int s2 = accumulate(all(b), 0);

    if(s1 > s2){
        cout << p1 << endl;
        return;
    }
    if(s2 > s1){
        cout << p2 << endl;
        return;
    }

    if(a[0] > b[0] || (a[0] == b[0] && a[1] > b[1])) cout << p1 << endl;
    else cout << p2 << endl;
}

signed main(){
 	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	//startTime = clock();

	int T = 1;
	cin >> T;

	for(int _t = 1; _t <= T; _t++){
		solve();
	}

	//cerr << getCurrentTime() << endl;
	return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

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

int main()
{
	int T=readIntLn(1,1000);
	while(T--){
        int DSA1 = readIntSp(0, 100), TOC1 = readIntSp(0, 100), DM1 = readIntLn(0, 100);
        int DSA2 = readIntSp(0, 100), TOC2 = readIntSp(0, 100), DM2 = readIntLn(0, 100);

        pair<int, pair<int, pair<int, int>>> p1 = {DSA1+TOC1+DM1, {DSA1, {TOC1, DM1}}};
        pair<int, pair<int, pair<int, int>>> p2 = {DSA2+TOC2+DM2, {DSA2, {TOC2, DM2}}};
        if(p1 > p2)cout<<"Dragon\n";
        else if(p1 < p2)cout<<"SloTh\n";
        else cout<<"TiE\n";
	}
	assert(getchar()==-1); // Ensures that there are no extra characters at the end.
	cerr<<"SUCCESS\n"; // You should see this on the http://campus.codechef.com/files/stderr/SUBMISSION_ID page, at the bottom.
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

#define sync {ios_base ::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);}
#define rep(n) for(int i = 0;i<n;i++)
#define rep1(a,b) for(int i = a;i<b;i++)
#define int long long int
#define mod 1000000007

int n;

void solve()
{
    int a[2][3];
    cin>>a[0][0]>>a[0][1]>>a[0][2];
    cin>>a[1][0]>>a[1][1]>>a[1][2];

    int dscore = a[0][0] + a[0][1] + a[0][2];
    int sscore = a[1][0] + a[1][1] + a[1][2];

    string d = "Dragon";
    string s = "Sloth";
    string t = "Tie";

    if(dscore != sscore){ //Total Score
        if(dscore > sscore)
            cout<<d;
        else
            cout<<s;
    }
    else if(a[0][0] != a[1][0]){  //DSA Score
            if(a[0][0] > a[1][0])
                cout<<d;
            else
                cout<<s;
    }
    else if(a[0][1] != a[1][1]){  //TOC Score
        if(a[0][1] > a[1][1])
            cout<<d;
        else
            cout<<s;
    }
    else{  //Tie
        cout<<t;
    }
}

int32_t main()
{

    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif

    sync;
    int t = 1;
    cin>>t;
    while(t--){
        solve();
        cout<<"\n";
    }
    return 0;
}
``

</details>
