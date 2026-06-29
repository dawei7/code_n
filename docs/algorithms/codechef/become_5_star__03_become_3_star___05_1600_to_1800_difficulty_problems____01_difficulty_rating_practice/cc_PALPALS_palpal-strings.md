# Palpal Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PALPALS |
| Difficulty Rating | 1776 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [PALPALS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/PALPALS) |

---

## Problem Statement

A string is called a *Palpal string* if it can be divided into contiguous substrings such that:
- Each character of the whole string belongs to exactly one substring.
- Each of these substrings is a palindrome with length greater than $1$.

For example, "abbbaddzcz" is a Palpal string, since it can be divided into "abbba", "dd" and "zcz".

You are given a string $s$. You may rearrange the characters of this string in any way you choose. Find out if it is possible to rearrange them in such a way that you obtain a Palpal string.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $s$.

### Output
For each test case, print a single line containing the string `"YES"` if the characters of $s$ can be rearranged to form a Palpal string or `"NO"` if it is impossible (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \le T \le 10^5$
- $1 \le |s| \le 100$
- $s$ contains only lowercase English letters
- the sum of $|s|$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
acbbbadzdz
abcd
xyxyxy
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Example case 1:** The string "acbbbadzdz" can be rearranged to "abbbaddzcz", which is the Palpal string mentioned above.

**Example case 2:** It can be shown that "abcd" cannot be rearranged to form a Palpal string.

**Example case 3:** The string "xyxyxy" is already a Palpal string, since it can divided into "xyx" and "yxy".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
acbbbadzdz
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
abcd
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
xyxyxy
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PALPALS)

[Contest: Division 2](https://www.codechef.com/LTIME93B/problems/PALPALS)

[Contest: Division 3](https://www.codechef.com/LTIME93C/problems/PALPALS)

**Author:**  [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:**  [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:**  [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Simple

# PREREQUISITES:

None

# PROBLEM:

You are given a string S (consisting of lowercase Latin letters only) and you can rearrange the letters of this string in any way. You have to find out if it is possible to rearrange the letters of string S to obtain a Palpal string.

A string S (consisting of lowercase Latin letters only) is called a Palpal string if it can be divided into contiguous substrings such that:

- Every Character of the string is present in one and only one substring.

- Every Substring is a palindrome of length \ge 2

# EXPLANATION:

Our task is to divide the string into contiguous substring of length greater than or equal to two, such that every substring is a palindrome.

If there is a palindromic substring and we delete the leftmost and the rightmost character from this substring, the resulting substring will remain palindromic. It means to create a palindromic substring of length x, we need to create a palindromic substring of a smaller length too. Hence the most optimal way to divide the string is in the smallest length possible which is 2.

Dividing the string S into substrings of length 2 will also increase palindromic substrings which will be useful when we need to insert the odd character in these substrings as explained later.

Now we will try to form palindromic substrings of length 2. We can see that, if any letter is present an odd number of times in this string then a single character of this letter won’t be able to form a palindromic substring of length 2. But all such characters can be inserted in between substring of length 2 since the addition of this character won’t make the substring non-palindromic. It means that there should be enough substrings such that all such characters could be inserted.

Let us suppose the count of such characters is y. Now if the number of substrings of length 2 is more than or equal to y, then it is always possible to insert such characters in between the substrings making the substring still palindromic. If such conditions satisfy then it is possible to rearrange the letters of string S to obtain a Palpal string.

# TIME COMPLEXITY:

O(|S|) per test case.

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;
#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int32_t main()
{
    IOS;
    int T; cin >> T;
    while(T--)
    {
        string s; cin >> s;
        int single = 0, pair = 0;
        vector<int> freq(26);
        for(int i = 0; i < (int)s.size(); i++)
            freq[s[i] - 'a']++;
        for(int i = 0; i < 26; i++)
        {
            pair += freq[i] / 2;
            single += freq[i] % 2;
        }
        if(single <= pair)
            cout << "yeS";
        else
            cout << "No";
        cout << "\n";
    }
    return 0;
}
``

Tester
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
#define int long long
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
int powm(int a, int b) {
	int res=1;
	while(b) {
		if(b&1)
			res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
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

int sum_s=0;
void solve() {
	string s=readStringLn(1,100);
	sum_s+=sz(s);
	assert(sum_s<=1000'000);
	for(char i:s)
		assert('a'<=i&&i<='z');
	vi cnt(26,0);
	for(char i:s)
		cnt[i-'a']++;
	int ones=0,eves=0;
	for(int i:cnt)
		if(i) {
			ones+=i%2;
			eves+=i/2;
		}
	if(ones>eves) {
		cout<<"NO"<<endl;
	} else
		cout<<"YES"<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(10);
	int t=readIntLn(1,100000);
//	int t;
//	cin>>t;
	fr(i,1,t)
		solve();
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
  {
    string s;
    cin>>s;

    int n=(int)(s.size());

    int count[26]={};

    for(int i=0;i<(int)s.size();i++)
    {
      count[s[i]-'a']++;
    }

    int odd=0;

    for(int i=0;i<26;i++)
    {
      if(count[i]%2!=0)
      {
        odd++;
      }
    }

    int total=n-odd;
    total/=2;

    if(total<odd)
    {
      cout<<"NO"<<"\n";
    }
    else
    {
      cout<<"YES"<<"\n";
    }
  }

return 0;
}

``

# VIDEO EDITORIAL:

</details>
