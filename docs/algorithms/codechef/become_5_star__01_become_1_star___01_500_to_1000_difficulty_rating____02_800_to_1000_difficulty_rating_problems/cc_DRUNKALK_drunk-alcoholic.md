# Drunk Alcoholic

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DRUNKALK |
| Difficulty Rating | 874 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [DRUNKALK](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/DRUNKALK) |

---

## Problem Statement

Faizal is very sad after finding out that he is responsible for Sardar's death. He tries to drown his sorrows in alcohol and gets very drunk. Now he wants to return home but is unable to walk straight. For every $3$ steps forward, he ends up walking one step backward.

Formally, in the $1^{st}$ second he moves $3$ steps forward, in the $2^{nd}$ second he moves $1$ step backwards, in the $3^{rd}$ second he moves $3$ steps forward, in $4^{th}$ second $1$ step backwards, and so on.

How far from his initial position will Faizal be after $k$ seconds have passed?
Assume that Faizal's initial position is $0$.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $k$, the number of seconds after which Faizal's position is to be calculated.

---

## Output Format

- For each test case, output a single line containing one integer - Faizal's position after $k$ seconds.

---

## Constraints

- $1 \leq T \leq 100000$
- $0 \leq k \leq 100000$
- The sum of $k$ over all test cases does not exceed $1000000$

---

## Examples

**Example 1**

**Input**

```text
3
5
11
23
```

**Output**

```text
7
13
25
```

**Explanation**

**1st Test Case**
- Faizal walks $3$ steps forward in the $1^{st}$ second, ending up at $3$
- Faizal walks $1$ step backward in the $2^{nd}$ second, ending up at $2$
- Faizal walks $3$ steps forward in the $3^{rd}$ second, ending up at $5$
- Faizal walks $1$ step backward in the $4^{th}$ second, ending up at $4$
- Faizal walks $3$ steps forward in the $5^{th}$ second, ending up at $7$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
11
```

**Output for this case**

```text
13
```



#### Test case 3

**Input for this case**

```text
23
```

**Output for this case**

```text
25
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem statement](https://www.codechef.com/CSNS21C/problems/DRUNKALK)

[Contest source](https://www.codechef.com/CSNS21C)

***Author, Editorialist :*** [Raghav Agarwal](https://www.codechef.com/users/rag_hav13)

***Tester :*** [Miten Shah](https://www.codechef.com/users/mtnshh)

#
[](#difficulty-1)DIFFICULTY:

Cakewalk

#
[](#prerequisites-2)PREREQUISITES:

None

#
[](#problem-3)PROBLEM:

A person moves 3 steps forward in odd second and 1 step backward in even seconds. Calculate the distance traveled by the person after n seconds.

#
[](#explanation-4)EXPLANATION:

###
[](#linear-time-5)Linear time

Since the constraints are small we could also simulate the whole walk. By incrementing distance by 3 for odd seconds and decreasing it by 1 in even seconds.

###
[](#constant-time-6)Constant time

In 2 seconds the person moves 3 forward and 1 backward, that is he moves a net of 2 steps forward every two seconds. Thus if n is even the total distance travelled will be just n. While if n is odd, then n - 1 is even, and the distance travelled in n - 1 seconds is n - 1, then in the last second 3 more forward steps are taken. So total distance will be n - 1 + 3 = n + 2 for odd n.

#
[](#solution-7)SOLUTION :

c++ Solution (Linear)
``#include <bits/stdc++.h>
#define fast_io std::ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL)

using namespace std;

int main() {
        fast_io;
        long long t;
        cin >> t;

        int sum = 0;
        while (t--) {
                bool f = 1;
                int k;
                cin >> k;
                sum += k;

                long long ans = 0;

                while (k--) {
                        ans += f ? 3 : -1;
                        f = !f;
                }
                cout << ans << '\n';
        }
}
``

C++ Tester's solution
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

const int max_q = 1e5;
const int max_k = 1e5;
const int max_sum_k = 1e6;

const ll N = 100005;
const ll INF = 1e12;

void solve(ll k){
    if(k % 2 == 0){
        cout << k << endl;
    }
    else{
        cout << k + 2 << endl;
    }
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ll q = readIntLn(1, max_q);
    ll sum_k = 0;
    while(q--){
        ll k = readIntLn(0, max_k);
        solve(k);
        sum_k += k;
    }
    assert(sum_k <= max_sum_k);
    assert(getchar()==-1);
}
``

</details>
