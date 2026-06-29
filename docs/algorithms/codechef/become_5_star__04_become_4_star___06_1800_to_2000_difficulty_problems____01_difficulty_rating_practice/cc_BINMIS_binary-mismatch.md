# Binary Mismatch

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BINMIS |
| Difficulty Rating | 1836 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [BINMIS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/BINMIS) |

---

## Problem Statement

You have a binary string $S$ of length $N$.

You must perform the following operation on the binary string $S$ **exactly once**:
- Choose two integers $L$ and $R$ $(1 \le L \le R \le N)$ and invert the [substring](https://en.wikipedia.org/wiki/Substring) $S_{L \dots R}$ (i.e change $1$ to $0$ and change $0$ to $1$).

Determine whether you can make the number of zeroes in $S$ equal to number of ones in $S$ by performing the above operation exactly once. If there exists a way, also output the bounds of the chosen substring.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases.
- The first line of each test case contains a single integer $N$ — the length of string $S$.
- The second line of each test case contains a binary string $S$ of length $N$.

---

## Output Format

For each test case, output `NO` if there is no way to make the number of zeroes equal to number of ones.

Otherwise, output `YES`. In the next line, output two integers $L$ and $R$ $(1 \le L \le R \le N)$ — bounds of the chosen substring. If there are multiple answers, print any.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 ≤ T ≤ 10000$
- $1 ≤ N ≤ 10^5$
- $S$ is a binary string, i.e, contains only characters $0$ and $1$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
01
3
010
4
1000
```

**Output**

```text
YES
1 2
NO
YES
4 4
```

**Explanation**

**Test case 1**: We can pick $L = 1$ and $R = 2$ to obtain: $\underline{01} \rightarrow 10$, which contains equal number of zeroes and ones.

**Test case 2**: It can be proven that there is no way to make the number of zeroes equal to number of ones.

**Test case 3**: We can pick $L = 4$ and $R = 4$ to obtain: $100\underline{0} \rightarrow 1001$, which contains equal number of zeroes and ones.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START34A/problems/BINMIS)

[Contest Division 2](https://www.codechef.com/START34B/problems/BINMIS)

[Contest Division 3](https://www.codechef.com/START34C/problems/BINMIS)

[Contest Division 4](https://www.codechef.com/START34D/problems/BINMIS)

Setter: [Divyansh Gupta](https://www.codechef.com/users/dash2199)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

Count of a unique element in any range of an array using concept similar to prefix sum .

#
[](#problem-4)PROBLEM:

You have a binary string S of length N.

You must perform the following operation on the binary string S **exactly once**:

- Choose two integers L and R (1 \le L \le R \le N) and invert the [substring](https://en.wikipedia.org/wiki/Substring) S_{L \dots R} (i.e change 1 to 0 and change 0 to 1).

Determine whether you can make the number of zeroes in S equal to number of ones in S by performing the above operation exactly once. If there exists a way, also output the bounds of the chosen substring.

#
[](#quick-explanation-5)QUICK EXPLANATION:

Whenever the length of the string is even it is possible to make the count of zeroes and count of ones  equal by inverting some prefix of the string.

#
[](#explanation-6)EXPLANATION:

If N is odd the count of zeroes and ones in the string can never be made equal as addition of two same numbers is even. Therefore when N is odd the answer is always `NO`. Now, we will prove that when N is even it is always possible to invert some prefix of the string to make the count of ones and the count of zeroes in the string equal.

Let P_i represent the prefix of the string S ending at index i \:i.e.  substring formed by the first i characters of the string S ? S[1..........i]. Let the difference between the count of ones and the count of zeroes in string S be a.

Suppose we invert the complete string S the difference now becomes -a. Also, Inverting P_1 changes a by 2 and Inverting P_2 changes the difference obtained by inverting P_1 again by 2. Overall, Inverting P_{i+1} changes the difference obtained on inverting P_i by 2. This means by inverting prefixes of different length we can make difference equal to all values from -a to a where adjacent values differ by 2. Let a>0 then some possible differences are -a, -a+2..........a-2, a.

Also as the length of the string S is even therefore either both the count of zeroes and count of ones in string S are even or they both are odd. This means that initial difference a is an even number. This means that the possible difference take the value of all even numbers between -a to a which includes 0.

Lets Ones_i represent the  numbers of 1 in the prefix of length i. We just need to find an index i such that inverting P_i makes the count of zeroes and the count of ones equal to N/2. This boils down to finding an index i such that Ones_n-N/2=2\cdot Ones_i - i.

#
[](#time-complexity-7)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-8)SOLUTION:

Setter's solution
``#include<bits/stdc++.h>
#include<string>

using namespace std;

#define ll long long int
#define ld long double
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz(x) ((int)(x).size())
#define deb(x) cout<< #x << '=' << x <<endl
#define MOD 1000000007

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin>>t;

    for(int tc = 1; tc <= t; tc++){
        ll n;
        cin>>n;

        string s;
        cin>>s;

        if(n % 2 == 1){
            cout<<"nO\n";
        }else{
            ll ones = 0 , zeroes = 0;
            for(int i = 0; i < n; i++){
                ones += (s[i] == '1');
                zeroes += (s[i] == '0');
            }

            ll req = (ones - zeroes)/2 , cur = 0 , l = 1 , r = 1;
            for(int i = 0; i < n; i++){
                cur += (s[i] == '1');
                cur -= (s[i] == '0');

                if(cur == req){
                    r = i + 1;
                    break;
                }
            }
            cout<<"YeS\n";
            cout<<l<<" "<<r<<"\n";
        }
    }
    return 0;
}
``

Tester-1's Solution (Python)
``for _ in range(int(input())):
	n = int(input())
	s = input()
	if n%2 == 1:
		print('NO')
	else:
		print('YES')
		dif = s.count('1') - s.count('0')
		curdif = 0
		for i in range(n):
			if s[i] == '0':
				curdif -= 1
			else:
				curdif += 1
			if 2*curdif == dif:
				print(1, i+1)
				break

``

Tester-2's Solution
``#include <bits/stdc++.h>
using namespace std;
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif

/*
------------------------Input Checker----------------------------------
*/

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

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

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

/*
------------------------Main code starts here----------------------------------
*/
int MAX=100000;
int check_bin(string s){
    for(auto it:s){
        if((it!='0')&&(it!='1')){
            return 0;
        }
    }
    return 1;
}
int sum_cases=0;
void solve(){
    int n=readIntLn(1,MAX);
    sum_cases+=n;
    string s=readStringLn(n,n);
    assert(check_bin(s));
    vector<int> freq(5,0);
    for(auto it:s){
        freq[it-'0']++;
    }
    int req=freq[1]-freq[0];
    int now=0;
    map<int,int> prvs; prvs[0]=1;
    s=" "+s;
    if(abs(req)&1){
        cout<<"NO\n";
        return;
    }
    req/=2;
    for(int i=1;i<=n;i++){
        if(s[i]=='1'){
            now--;
        }
        else{
            now++;
        }
        if(prvs[now+req]!=0){
            cout<<"YES\n";
            cout<<prvs[now+req]<<" "<<i<<"\n";
            return;
        }
        prvs[now]=i+1;
    }
    cout<<"NO\n";
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    int test_cases=readIntLn(1,10000);
    while(test_cases--){
        solve();
    }
    assert(getchar()==-1);
    assert(sum_cases<=(2*MAX));
    return 0;
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(),_obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
const int N=1e5+11,mod=1e9+7;
ll max(ll a,ll b) {return ((a>b)?a:b);}
ll min(ll a,ll b) {return ((a>b)?b:a);}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
int n;
cin>>n;
string s;
cin>>s;
if(n&1)
{
    cout<<"NO"<<'\n';
    return ;
}
int p[n+1]={0};
for(int i=1;i<=n;i++)
p[i]=p[i-1]+(s[i-1]=='1');
for(int i=1;i<=n;i++)
{
    if(p[n]-(n/2)==2*p[i]-i)
    {
        cout<<"YES"<<'\n'<<1<<' '<<i<<'\n';
        break;
    }
}
return ;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int test=1;
    cin>>test;
    while(test--) sol();
}

``

</details>
