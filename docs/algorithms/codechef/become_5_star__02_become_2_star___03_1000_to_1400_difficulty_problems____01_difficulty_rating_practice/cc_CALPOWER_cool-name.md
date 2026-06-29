# Cool Name

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CALPOWER |
| Difficulty Rating | 1223 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CALPOWER](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CALPOWER) |

---

## Problem Statement

Sardar Singh has many men fighting for him, and he would like to calculate the power of each of them to better plan for his fight against Ramadhir.

The power of a string $S$ of lowercase English alphabets is defined to be
$$
\sum_{i = 1}^{|S|} i\cdot ord(S_i)
$$
where $ord(S_i)$ is the position of $S_i$ in the alphabet, i.e, $ord('a') = 1, ord('b') = 2, \dots, ord('z') = 26$.

Each of Sardar Singh's men has a name consisting of lowercase English alphabets. The power of a man is defined to be the maximum power over all possible rearrangements of this string.

Find the power of each of Sardar Singh's men.

---

## Input Format

- The first line of input contains an integer $T$, denoting the total number of Sardar Singh's men.
- Each of the next $T$ lines contains a single string $S_{i}$, the name of Sardar Singh's $i$-th man.

---

## Output Format

- Output $T$ lines, each containing a single integer. The $i$-th of these lines should have the power of the $i$-th of Sardar Singh's men.

---

## Constraints

- $1 \leq T \leq 60$
- $1 \leq |S_{i}| \leq 100$
- $S_i$ consists of lowercase english alphabets only.

---

## Examples

**Example 1**

**Input**

```text
1
faizal
```

**Output**

```text
273
```

**Explanation**

The rearrangement with maximum power is $aafilz$. Its power can be calculated as
$$
1\cdot ord('a') + 2\cdot ord('a') + 3\cdot ord('f') + 4\cdot ord('i') + 5\cdot ord('l') + 6\cdot ord('z')
$$
which equals $273$.
It can be verified that no rearrangement gives a larger power.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem statement](https://www.codechef.com/CSNS21C/problems/CALPOWER)

[Contest source](https://www.codechef.com/CSNS21C)

***Author, Editorialist :*** [Dhananjay Raghuwanshi](https://www.codechef.com/users/dhananjay_777)

***Tester :*** [Miten Shah](https://www.codechef.com/users/mtnshh)

#
[](#difficulty-1)DIFFICULTY:

Simple

#
[](#prerequisites-2)PREREQUISITES:

Sorting

#
[](#problem-3)PROBLEM:

Given a string S of lowercase english alphabets, we need to find maximum value of the string.

The value of a string S, is defined as ? i * (position of i_{th} letter of S in alphabets), for i = 1,2 … length of S. We can transform S in any of the possible rearrangements of this string S.

#
[](#explanation-4)EXPLANATION:

- For some index i of the string S it’s contribution in the value of the array is proportional to   i * (position of i_{th} letter of S in alphabets) . So to maximise the value of the array we need to maximise the above multiplication. The above product will be maximum if for a lager i, the character at i_{th} position in S comes later in alphabets. So from the above explanation, the rearrangement of  string S that will have maximum is the one sorted in non decreasing order.

#
[](#solution-5)SOLUTION :

c++ Solution
``#include <bits/stdc++.h>
using namespace std;

signed main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int ans = 0, n;
        string s;
        cin >> s;
        n = s.size();
        sort(s.begin(), s.end());
        for (int i = 0; i < n; i++)
            ans += (i + 1) * (s[i] - 'a' + 1);
        cout << ans << endl;
    }
}
``

C++ Tester's Solution
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

const int max_q = 1e2;

const ll N = 100005;
const ll INF = 1e12;

void solve(){
    string s = readStringLn(1, max_q);
    sort(all(s));
    ll ans = 0, n = s.length();
    rep(i,0,n){
        ans += (s[i] - 'a' + 1) * (i + 1);
    }
    cout << ans << endl;
}

int main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    ll q = readIntLn(1, max_q);
    while(q--){
        solve();
    }
    assert(getchar()==-1);
}
``

</details>
