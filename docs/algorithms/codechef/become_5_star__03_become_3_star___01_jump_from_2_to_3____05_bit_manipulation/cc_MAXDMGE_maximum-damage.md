# Maximum Damage

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXDMGE |
| Difficulty Rating | 1636 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [MAXDMGE](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/MAXDMGE) |

---

## Problem Statement

Nasir and two of his henchmen are planning to attack $N$ shops of the Qureshi clan. The shops are conveniently lined up, and numbered from $1$ to $N$. The $i$-th shop contains $A_i$ kg of coal.

For a given subarray of shops $[A_L, A_{L+1}, \dots, A_R]$, the *bitwise and* of this subarray is defined to be the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) of the coal contained in each of the shops, i.e, $A_L \& A_{L+1} \& \dots \& A_R$.

The damage caused when bombing the $i$-th shop is computed to be the maximum *bitwise and* over all subarrays containing shop $i$, and whose size is **strictly larger than 1**.

For each shop ($1\leq i\leq N$), find the damage caused when Nasir bombs it.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, denoting the number of shops.
- The second line of each test case contains $N$ space-separated integers, the $i$-th of which is $A_i$, representing the amount of coal in the $i$-th shop.

---

## Output Format

For each test case, print a single line containing $N$ integers $d_1,d_2,\ldots,d_n$ where $d_i$ represents the maximum damage that can be caused if the $i$-th shop is to be bombed.

---

## Constraints

- $1 \leq T \leq 10000$
- $2 \leq N \leq 2 \cdot 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5
29 412 671 255 912
6
166 94 184 114 1124 298
```

**Output**

```text
28 156 159 159 144 
6 24 48 96 96 32
```

**Explanation**

**Test case 1:** There are several choices of subarray which give the maximum for each index. One such choice is given below:

For shop $1$, choose subarray $[29, 412, 671, 255]$

For shop $2$, choose subarray $[412, 671, 255]$

For shop $3$, choose subarray $[671, 255]$

For shop $4$. choose subarray $[671, 255]$

For shop $5$, choose subarray $[412, 671, 255, 912]$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
29 412 671 255 912
```

**Output for this case**

```text
28 156 159 159 144
```



#### Test case 2

**Input for this case**

```text
6
166 94 184 114 1124 298
```

**Output for this case**

```text
6 24 48 96 96 32
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXDMGE)

[Div-1 Contest](https://www.codechef.com/CSNS21A/problems/MAXDMGE)

[Div-2 Contest](https://www.codechef.com/CSNS21B/problems/MAXDMGE)

[Div-3 Contest](https://www.codechef.com/CSNS21C/problems/MAXDMGE)

***Author:*** [Ansh Gupta](https://www.codechef.com/users/anshg0711)

***Tester:*** [Miten Shah](https://www.codechef.com/users/mtnshh)

***Editorialist:*** [Ansh Gupta](https://www.codechef.com/users/anshg0711)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#prerequisites-3)PREREQUISITES:

Bit Manipulation

#
[](#problem-4)PROBLEM:

Nasir and two of his henchmen are planning to attack N shops of the Qureshi clan. The shops are conveniently lined up, and numbered from 1 to N. The i-th shop contains A_i kg of coal. For each shop (1\leq i\leq N), find the damage caused when Nasir bombs it.

#
[](#quick-explanation-5)QUICK EXPLANATION:

Given an array of n numbers, for each index we have to select a subarray of size greater than 1 including that index such that we can get the maximum *Bitwise &*  possible.

#
[](#explanation-6)EXPLANATION:

Let suppose a number x, if we take *Bitwise &* of  x with another number y, the resultant will be less than or equal to x i.e ( x&y ) \leq x.

So increasing the size of subarray will not increase the resultant. So we will select Subarray of minimum size i.e 2 including the index itself, which means we have to select one more index either from left or to the right of that index.

Pseudo code

``for(ll i=1;i<=n;i++){
    if(i==1)cout<<(shop[i]&shop[i+1])<<" ";
    else if(i==n)cout<<(shop[i-1]&shop[i])<<" ";
    else cout<<max((shop[i]&shop[i+1]),(shop[i-1]&shop[i]))<<" ";
}
``

#
[](#time-complexity-7)TIME COMPLEXITY:

Overall time complexity would be be: O(n) per test case, where n is the number of shops

#
[](#solutions-8)SOLUTIONS:

Setter's Solution
``
#include "bits/stdc++.h"
using namespace std;
#define ll long long
int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    assert(1 <= t && t <= 10000);
    ll sum = 0;
    while (t--) {
        ll n;
        cin >> n;
        sum += n;
        assert(n > 1 && n <= 200000);
        assert(n < 1000000000);
        assert(sum <= 200000);
        ll arr[n + 2];
        for (ll i = 0; i < n; i++)cin >> arr[i + 1];
        arr[0] = 0;
        arr[n + 1] = 0;
        for (ll i = 1; i <= n; i++)cout << max(arr[i]&arr[i + 1], arr[i - 1]&arr[i]) << " ";
        cout << endl;

    }

}

``

Tester's Solution
``// created by mtnshh

#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define rb pop_back
#define ti tuple<int, int, int>
#define pii pair<int, int>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define mp make_pair
#define mt make_tuple

#define rep(i,a,b) for(ll i=a;i<b;i++)
#define repb(i,a,b) for(ll i=a;i>=b;i--)

#define err() cout<<"--------------------------"<<endl;
#define errA(A) for(auto i:A)   cout<<i<<" ";cout<<endl;
#define err1(a) cout<<#a<<" "<<a<<endl
#define err2(a,b) cout<<#a<<" "<<a<<" "<<#b<<" "<<b<<endl
#define err3(a,b,c) cout<<#a<<" "<<a<<" "<<#b<<" "<<b<<" "<<#c<<" "<<c<<endl
#define err4(a,b,c,d) cout<<#a<<" "<<a<<" "<<#b<<" "<<b<<" "<<#c<<" "<<c<<" "<<#d<<" "<<d<<endl

#define all(A)  A.begin(),A.end()
#define allr(A)    A.rbegin(),A.rend()
#define ft first
#define sd second

#define V vector<ll>
#define S set<ll>
#define VV vector<V>
#define Vpll vector<pll>

#define endl "\n"

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        // char g = getc(fp);
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
            // cerr << x << " " << l << " " << r << endl;
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
        // char g=getc(fp);
        assert(g != -1);
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

const int max_q = 1e4;
const int max_n = 2e5;
const int max_ai = 1e9;

const ll N = 200005;
const ll INF = 1e12;

void solve(ll n){
    ll A[n];
    rep(i,0,n){
        if(i!=(n-1))
            A[i] = readIntSp(0, max_ai);
        else
            A[i] = readIntLn(0, max_ai);
    }
    rep(i,0,n){
        ll ans = 0;
        if(i!=0)
            ans = max(ans, A[i]&A[i-1]);
        if(i!=(n-1))
            ans = max(ans, A[i]&A[i+1]);
        cout << ans << " ";
    }
    cout << endl;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ll q = readIntLn(1, max_q);
    ll sum_n = 0;
    while(q--){
        ll n = readIntLn(1, max_n);
        solve(n);
        sum_n += n;
    }
    assert(sum_n <= max_n);
    assert(getchar()==-1);
}
``

Editorialist's Solution
``
#include "bits/stdc++.h"
using namespace std;
#define ll long long
int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    assert(1 <= t && t <= 10000);
    ll sum = 0;
    while (t--) {
        ll n;
        cin >> n;
        sum += n;
        assert(n > 1 && n <= 200000);
        assert(n < 1000000000);
        assert(sum <= 200000);
        ll arr[n + 2];
        for (ll i = 0; i < n; i++)cin >> arr[i + 1];
        arr[0] = 0;
        arr[n + 1] = 0;
        for (ll i = 1; i <= n; i++)cout << max(arr[i]&arr[i + 1], arr[i - 1]&arr[i]) << " ";
        cout << endl;

    }

}

``

</details>
