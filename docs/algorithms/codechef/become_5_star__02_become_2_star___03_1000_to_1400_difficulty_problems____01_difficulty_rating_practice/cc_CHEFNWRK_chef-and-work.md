# Chef and Work

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFNWRK |
| Difficulty Rating | 1185 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [CHEFNWRK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CHEFNWRK) |

---

## Problem Statement

Chef has $N$ small boxes arranged on a line from $1$ to $N$. For each valid $i$, the weight of the $i$-th box is $W_i$. Chef wants to bring them to his home, which is at the position $0$. He can hold any number of boxes at the same time; however, the total weight of the boxes he's holding must not exceed K at any time, and he can only pick the ith box if all the boxes between Chef's home and the ith box have been either moved or picked up in this trip.

Therefore, Chef will pick up boxes and carry them home in one or more round trips. Find the smallest number of round trips he needs or determine that he cannot bring all boxes home.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $W_1, W_2, \ldots, W_N$.

### Output
For each test case, print a single line containing one integer ― the smallest number of round trips or $-1$ if it is impossible for Chef to bring all boxes home.

### Constraints
- $1 \le T \le 100$
- $1 \le N, K \le 10^3$
- $1 \le W_i \le 10^3$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
4
1 1 
2
2 4
1 1
3 6
3 4 2
3 6
3 4 3
```

**Output**

```text
-1
1
2
3
```

**Explanation**

**Example case 1:** Since the weight of the box higher than $K$, Chef can not carry that box home in any number of the round trip.

**Example case 2:** Since the sum of weights of both boxes is less than $K$, Chef can carry them home in one round trip.

**Example case 3:** In the first round trip, Chef can only pick up the box at position $1$. In the second round trip, he can pick up both remaining boxes at positions $2$ and $3$.

**Example case 4:** Chef can only carry one box at a time, so three round trips are required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
2
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
2 4
1 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3 6
3 4 2
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
3 6
3 4 3
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFNWRK)

[Contest](https://www.codechef.com/COOK121B/problems/CHEFNWRK)

[Video Editorial](https://youtu.be/tg0cDl__2-8)

**Setter:** [Ritesh Gupta](https://www.codechef.com/users/rishup_nitdgp)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Ishmeet Singh Saggu](https://www.codechef.com/users/psychik)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Ad-hoc and Greedy

# PROBLEM:

You have given N boxes, where the weight of i-th box is W_i. Chef has to take all the boxes by making one or more round trips. In each trip, he can pick any number of boxes as long as the total weight doesn’t exceed K. Also, you can pick up the i-th box only if all the boxes between Chef’s home and the i-th box have been either moved or picked up in current trip.

# EXPLANATION:

First, let us check that is it possible to pick every box, i.e. W_i \leq K, if for any box W_i > K then it is not possible to pick this box and answer will be -1.

In the first trip, start at box 1  and keep on going to the right until the total sum of boxes \leq K. (greedily picking up as many boxes as possible).

``int pickedUp = 0;
while((i < N) && (weight[i]+pickedUp <= K)) { // try to go as right as you can.
	pickedUp += weight[i];
	i ++;
}
``

If all the boxes are picked up then stop and the answer is 1 else suppose you can pick up till box i, so now start the second trip from box i+1. Continue the process until you have picked up all the boxes.

# TIME COMPLEXITY:

- In each test case we are doing a single linear iteration over the weight of boxes and, as the number of trips can’t be more than the number of boxes(when the answer is possible). So total time complexity per test case is O(N).

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin >> t;

    while(t--)
    {
        int n,k;
        cin >> n >> k;

        int ans = 0;
        int sum = 0;

        vector <int> v(n);

        for(int i=0;i<n;i++)
            cin >> v[i];

        bool flag = false;

        for(int i=0;i<n;i++)
        {
            if(v[i] > k)
                flag = true;
        }

        if(flag)
        {
            cout << -1 << endl;
            continue;
        }

        for(int i=0;i<n;i++)
        {
            sum += v[i];

            if(sum > k)
            {
                ans++;
                sum = v[i];
            }
        }

        if(sum > 0)
            ans++;

        cout << ans << endl;
    }
}
``

Tester's Solution
``#include <bits/stdc++.h>
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
//#define int long long
typedef long long ll;
typedef long double f80;
#define double long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const ll infl=0x3f3f3f3f3f3f3f3fLL;
const int infi=0x3f3f3f3f;
//const int mod=998244353;
const int mod=1000000007;
typedef vector<int> vi;
typedef vector<ll> vl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> oset;
auto clk=clock();
mt19937_64 rang(chrono::high_resolution_clock::now().time_since_epoch().count());
int rng(int lim) {
    uniform_int_distribution<int> uid(0,lim-1);
    return uid(rang);
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

int w[1005];
void solve() {
    int n,k;
    n=readIntSp(1,1000);
    k=readIntLn(1,1000);
    fr(i,1,n) {
        if(i!=n)
            w[i]=readIntSp(1,1000);
        else
            w[i]=readIntLn(1,1000);
    }
    int ans=1,we=0;
    fr(i,1,n) {
        if(w[i]>k) {
            cout<<-1<<endl;
            return;
        }
        we+=w[i];
        if(we>k) {
            ans++;
            we=w[i];
        }
    }
    cout<<ans<<endl;
}

signed main() {
    ios_base::sync_with_stdio(0),cin.tie(0);
    srand(chrono::high_resolution_clock::now().time_since_epoch().count());
    cout<<fixed<<setprecision(8);
    int t=readIntLn(1,100);
//  cin>>t;
    while(t--)
        solve();
    assert(getchar()==EOF);
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

void solveTestCase() {
	int N, K;
	cin >> N >> K;
	vector<int> weight(N);
	for(int i = 0; i < N; i ++) {
		cin >> weight[i];
	}
	for(int i = 0; i < N; i ++) {
		if(weight[i] > K) { // If there is a box with weight higher than K, then chef can't lift it so answer is impossible or -1.
			cout << -1 << '\n';
			return;
		}
	}
	int trips = 0, id = 0;
	while(id < N) {
		trips ++;
		int pickedUp = 0;
		while((id < N) && (weight[id]+pickedUp <= K)) { // try to go as right as you can.
			pickedUp += weight[id];
			id ++;
		}
	}
	cout << trips << '\n';
}

int main() {
	ios_base::sync_with_stdio(0); // fast IO
	cin.tie(0);
	cout.tie(0);

	int testCase;
	cin >> testCase;
	for(int i = 1; i <= testCase; i ++) {
		solveTestCase();
	}

	return 0;
}
``

### Video Editorial

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
