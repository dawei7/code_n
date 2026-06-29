# Pawri Meme

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PAWRI |
| Difficulty Rating | 1182 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [PAWRI](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/PAWRI) |

---

## Problem Statement

Lately, Chef has been inspired by the "pawri" meme. Therefore, he decided to take a string $S$ and change each of its substrings that spells "party" to "pawri". Find the resulting string.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

### Output
For each test case, print a single line containing the string after it is modified by Chef.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq |S| \leq 10^5$
- $S$ contains only lowercase English letters

---

## Examples

**Example 1**

**Input**

```text
3
part
partypartiparty
yemaihuyemericarhaiauryahapartyhorahihai
```

**Output**

```text
part
pawripartipawri
yemaihuyemericarhaiauryahapawrihorahihai
```

**Explanation**

**Example case 1:** There is no substring "party" in the original string.

**Example case 2:** The original string has $2$ substrings "party".

**Example case 3:** There is only a single substring "party" in the original string.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
part
```

**Output for this case**

```text
part
```



#### Test case 2

**Input for this case**

```text
partypartiparty
```

**Output for this case**

```text
pawripartipawri
```



#### Test case 3

**Input for this case**

```text
yemaihuyemericarhaiauryahapartyhorahihai
```

**Output for this case**

```text
yemaihuyemericarhaiauryahapawrihorahihai
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PAWRI)

[Contest: Division 1](https://www.codechef.com/COOK127A/problems/PAWRI)

[Contest: Division 2](https://www.codechef.com/COOK127B/problems/PAWRI)

[Contest: Division 3](https://www.codechef.com/COOK127C/problems/PAWRI)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Nandini Kapoor](https://www.codechef.com/users/costheta_z)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Brute force, Strings

# PROBLEM:

Lately, Chef has been inspired by the **pawri** meme. Therefore, he decided to take a string S and change each of its substrings that spell **party** to **pawri**. Find the resulting string.

# QUICK EXPLANATION:

We will traverse the given string and at any instant we find the word **party**  we shall replace it with **pawri**.

# EXPLANATION:

We need to replace all the occurrences spelling **party** with **pawri**.  To achieve this we will run a loop from the beginning of the string to 4 less than its end and at every index check for the presence of the substring **party** starting from that index. In other words, for every i such that 0\leq i\lt S.size()-4,  we check whether S[i:i+4] spells **party** and if it does, we change S[i:i+4] to **pawri** instead. We needn’t go beyond 4 less than the length of the string because any substring starting at indices beyond that would have length less than 5 (which is the desired length to match with **party**). Also note that once we have found a substring matching **party** say from index i to i+4, we can skip checking substrings starting from i+1 to i+4 because no suffix of **party** is also its prefix, and thus none of the substrings starting from any of those characters would turn out to be **party**.

The substring S[i:i+4], on arriving at subsequent indices can be obtained (for matching) as well as replaced using functions defined by respective languages that serve the purpose (for example `S.substr(i, length)` in C++ for returning substring starting at index i of specified length and `S.replace(i, length, Sr)` for replacing it with the string S{r}). In this particular case, as the substring is small in length, individual characters can be matched and replaced easily from i to i+4 without the aid of such functions as well.

Another way to approach the problem could utilize [KMP algorithm for pattern searching](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/). But it would not significantly affect the time complexity, as no two consecutive windows will both be prefixes to the pattern. This happens because our pattern “party” consists of all different characters.

# TIME COMPLEXITY:

O(N) per test case.

N being the length of the string given, T(N)=(N-4)\times 5.

Note that `std::string::substr` as [documented](http://www.cplusplus.com/reference/string/string/substr/) has its complexity unspecified, but generally linear in the length of the returned object, which in this case is 5.

# SOLUTIONS:

Setter

Tester
``    #pragma GCC optimize("Ofast")
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
    typedef long double f80;
    typedef pair<int,int> pii;
    typedef pair<double,double> pdd;
    //#define double long double
    #define pll pair<ll,ll>
    #define sz(x) ((long long)x.size())
    #define fr(a,b,c) for(int a=b; a<=c; a++)
    #define rep(a,b,c) for(int a=b; a<c; a++)
    #define trav(a,x) for(auto &a:x)
    #define all(con) con.begin(),con.end()
    const int infi=0x3f3f3f3f;
    const ll infl=0x3f3f3f3f3f3f3f3fLL;
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

    void solve() {
        string s=readStringLn(1,100000);
        for(char i:s)
            assert(('a'<=i&&i<='z')||('A'<=i&&i<='Z'));
        for(int i=0; i+4<sz(s); i++) {
            if(s.substr(i, 5)=="party") {
                s[i+2]='w';
                s[i+3]='r';
                s[i+4]='i';
            }
        }
        cout<<s<<endl;
    }
    signed main() {
        ios_base::sync_with_stdio(0),cin.tie(0);
        srand(chrono::high_resolution_clock::now().time_since_epoch().count());
        cout<<fixed<<setprecision(10);
        int t=readIntLn(1,10);
    //  int t;
    //  cin>>t;
        fr(i,1,t)
            solve();
    #ifdef rd
        cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
    #endif
    }

``

Editorialist
``    #include<bits/stdc++.h>
    using namespace std;

    #define _z ios_base::sync_with_stdio(false); cin.tie(NULL);
    #define int long long int
    #define endl "\n"
    #define mod 1000000007
    #define pb_ push_back
    #define mp_ make_pair
    //______________________________z_____________________________

    void solve()
    {
        string s;
        cin>>s;
        for(int i=0; i<s.size(); i++) {
            if(i+4<s.size() && s.substr(i, 5)=="party") {
                s[i+2]='w';
                s[i+3]='r';
                s[i+4]='i';
                i+=4;
            }
        }
        cout<<s<<endl;
    }

    int32_t main()
    {
        _z;
        int t=1;
        cin>>t;
        while(t--)
        {
            solve();
        }
    }

``

</details>
