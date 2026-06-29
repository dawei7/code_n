# XOR-ORED

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XORORED |
| Difficulty Rating | 1621 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [XORORED](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/XORORED) |

---

## Problem Statement

Given an array $A$ of $N$ non-negative integers, you can choose any non-negative integer $X$ and replace every element $A_i$ with $(A_i\oplus X)$ Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Using the above operation exactly once, your goal is to **minimize** the bitwise OR of the new array. In other words, find $X$ such that $(A_1\oplus X)\lor \cdots \lor (A_N \oplus X)$ is minimized, where $\lor$ denotes the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

Find the value of $X$ and the minimum possible bitwise OR of the new array.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then $T$ test cases follow.
- The first line of each test case contains a single integer $N$ - the length of the array.
- The next line contains $N$ integers $A_1,\ldots, A_N$.

---

## Output Format

For each test case, print two integers: $X$ and the minimum possible bitwise OR of the new array.

If there are multiple values of $X$ that achieve the minimum bitwise OR, print any of them.

---

## Constraints

- $1 \leq T \leq 5000$
- $ 1 \leq N \leq 100 $
- $ 0 \leq  A_i \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
1
2
4 6
```

**Output**

```text
6 2
```

**Explanation**

Here, if we take $X=6$, then our expression would become $(4\oplus 6) \lor (6\oplus 6) = 2\lor 0 = 2$, which is the minimum possible.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/XORORED)

[Contest: Division 3](https://www.codechef.com/COOK131C/problems/XORORED)

[Contest: Division 2](https://www.codechef.com/COOK131B/problems/XORORED)

[Contest: Division 1](https://www.codechef.com/COOK131A/problems/XORORED)

**Author:** [ Prasant Kumar](https://www.codechef.com/users/prasant21)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

Bitwise Operations, Bit Manipulation

# PROBLEM:

Given an array A of N non-negative integers, you can choose any non-negative integer X and replace every element A_i with (A_i?X) Here, ? denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Using the above operation exactly once, your goal is to **minimize** the bitwise OR of the new array. In other words, find X such that (A_1?X) ? \ldots ?(A_N?X) is minimized, where ? denotes the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

# EXPLANATION

### Observations

- While taking OR, if any of the number has i^{th} bit ON then result will also have i^{th} bit ON.

- If a number has i^{th} bit set, then doing XOR with 2^i resets the i^{th} bit.

-
0? 0 = 0, 0?1 = 1, 1?0 = 1, 1?1=0

-
0? 0 = 0, 0?1 = 1, 1?0 = 1, 1?1 =1

### Finding X

Now let’s come back to the problem. We want to do choose an X and do XOR with all array elements. And after this, we calculate OR of all the elements. The task is to minimise the final OR.

We want to find X such that it minimises the final OR. Now let’s look at the problem bitwise. Let’s say we want to find if i^{th} bit in X should be 0 or 1?

There are 3 possible cases:

Case 1: If all the elements of A has i^{th} bit 0.

In this case, X should have i^{th} bit 0.

Why?

If X has i^{th} bit 1 then doing XOR of X with any A_j will turn the i^{th} bit 1. In other words, doing A_j ? X will set the i^{th} bit of A_j as 1. This will further lead to being the i^{th} bit 1 in final OR value which we want to minimise. Hence it should be 0 in X.

Case 2: If all the elements of A has i^{th} bit 1.

In this case, X should have i^{th} bit 1.

Why?

If X has i^{th} bit 1 then doing XOR of X with any A_j will turn the i^{th} bit 0. In other words, doing A_j ? X will reset the i^{th} bit of A_j as 0. And as we are doing XOR of X with every element of A hence it would make it 0 in all the elements. Hence the final OR will have i^{th} bit 0 as all elements have it 0.

Case 3: If some of the elements of A has i^{th} bit 0 and some of them has 1.

In this case, X can have i^{th} bit either 0 or 1. It doesn’t change the final OR value.

Why?

As some of the elements has i^{th} bit 0 and others have 1. If we do not have i^{th} bit 1 in X then the elements which already had it 1 will still have it 1 even after XOR hence final OR value will also have i^{th} bit 1.

Similarly, if we make i^{th} bit 1 in X then after XOR, the elements which earlier had it 1 will have it 0 but the ones which had it 0 will have 1 now. Hence final OR value will also have i^{th} bit 1.

So in both cases, final OR value has i^{th} bit 1 hence it does not matter if i^{th} bit of X is 0 or 1 in this case.

As explained above, just check for every bit of X and find the value of X.

### Alternate Approach to Find X

As we saw in previous approach, i^{th} bit of X remains 0 if its 0 in all the elements. It becomes 1 if its 1 in all the elements. For other cases, we can either have it 0 or 1.

So if we take OR of all the elements then the OR will also have i^{th} bit 0 if it was 0 in all the elements. And 1 otherwise.

Hence that is also a valid X which will give us minimum OR after XOR.

So X = A_1 ? A_2 ? \ldots ? A_N.

Once we have X, do A_i := A_i ? X for all i and finally find OR of all the elements.

# TIME COMPLEXITY:

O(N \cdot \log max(A) ) or O(N) per test case

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
#define int long long
#define endl "\n"
int inf=1e9;
signed main(){

	ios_base::sync_with_stdio(0) , cin.tie(0);
	int t;cin>>t;
	assert(t<=5000 and t>=1);
	while(t--){
		int n;cin>>n;
		assert(n<=100 and n>=1);
		int arr[n];
		int OR=0,AND=-1;
		for(int i=0;i<n;i++){
			cin>>arr[i];
			OR|=arr[i];
			AND&=arr[i];
			assert(arr[i]<=inf and arr[i]>=0);
		}
		cout<<AND<<" "<<(OR-AND)<<endl;
	}
	return 0;
}
``

Tester's Solution
``/* in the name of Anton */

/*
  Compete against Yourself.
  Author - Aryan (@aryanc403)
  Atcoder library - https://atcoder.github.io/ac-library/production/document_en/
*/

#ifdef ARYANC403
    #include <header.h>
#else
    #pragma GCC optimize ("Ofast")
    #pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx")
    //#pragma GCC optimize ("-ffloat-store")
    #include<bits/stdc++.h>
    #define dbg(args...) 42;
#endif

using namespace std;
#define fo(i,n)   for(i=0;i<(n);++i)
#define repA(i,j,n)   for(i=(j);i<=(n);++i)
#define repD(i,j,n)   for(i=(j);i>=(n);--i)
#define all(x) begin(x), end(x)
#define sz(x) ((lli)(x).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define endl "\n"

typedef long long int lli;
typedef long double mytype;
typedef pair<lli,lli> ii;
typedef vector<ii> vii;
typedef vector<lli> vi;

const auto start_time = std::chrono::high_resolution_clock::now();
void aryanc403()
{
#ifdef ARYANC403
auto end_time = std::chrono::high_resolution_clock::now();
std::chrono::duration<double> diff = end_time-start_time;
    cerr<<"Time Taken : "<<diff.count()<<"\n";
#endif
}

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

vi readVectorInt(int n,lli l,lli r){
    vi a(n);
    for(int i=0;i<n-1;++i)
        a[i]=readIntSp(l,r);
    a[n-1]=readIntLn(l,r);
    return a;
}

const lli INF = 0xFFFFFFFFFFFFFFFL;

lli seed;
mt19937 rng(seed=chrono::steady_clock::now().time_since_epoch().count());
inline lli rnd(lli l=0,lli r=INF)
{return uniform_int_distribution<lli>(l,r)(rng);}

class CMP
{public:
bool operator()(ii a , ii b) //For min priority_queue .
{    return ! ( a.X < b.X || ( a.X==b.X && a.Y <= b.Y ));   }};

void add( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt==m.end())         m.insert({x,cnt});
    else                    jt->Y+=cnt;
}

void del( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt->Y<=cnt)            m.erase(jt);
    else                      jt->Y-=cnt;
}

bool cmp(const ii &a,const ii &b)
{
    return a.X<b.X||(a.X==b.X&&a.Y<b.Y);
}

const lli mod = 1000000007L;
// const lli maxN = 1000000007L;

    lli T,n,i,j,k,in,cnt,l,r,u,v,x,y;
    lli m;
    string s;
    vi a;
    //priority_queue < ii , vector < ii > , CMP > pq;// min priority_queue .

int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    // freopen("txt.in", "r", stdin);
    // freopen("txt.out", "w", stdout);
// cout<<std::fixed<<std::setprecision(35);
T=readIntLn(1,5e3);
while(T--)
{

    n=readIntLn(1,1e2);
    a=readVectorInt(n,0,1e9);
    lli c=0,d=0;
    for(auto x:a){
        c|=x;
        d|=~x;
    }
    cout<<c<<" "<<(c&d)<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``/*
 * @author: vichitr
 * @date: 25th July 2021
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fast ios::sync_with_stdio(0); cin.tie(0);

void solve() {
	int N; cin >> N;
	int A[N];
	for (int i = 0; i < N; i++)
		cin >> A[i];
	int X = 0;
	// find X by taking OR of all the elements.
	for (int i = 0; i < N; i++) {
		X |= A[i];
	}
	// do XOR and find OR
	int ans = 0;
	for (int i = 0; i < N; i++) {
		ans |= (A[i] ^ X);
	}
	cout << X << ' ' << ans << '\n';
}

signed main() {
	fast;

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int t = 1;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		// cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
``

If you have other approaches or solutions, let’s discuss in comments.If you have other approaches or solutions, let’s discuss in comments.

</details>
