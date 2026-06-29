# Magical Planks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MKGPLNKS |
| Difficulty Rating | 1467 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [MKGPLNKS](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/MKGPLNKS) |

---

## Problem Statement

Ryan is a boy from a small town,  who has been given a task by his father. He has $N$ wooden planks, numbered from $1$ to $N$, which are colored either black or white.

His task is to color all planks the same color! But there is some magic in the winds of his small town. Whenever he colors the $i^{th}$ ( plank which has the color $S_i$ ) to a color $P$ then following events happen:
 - if $2 \leq i \leq N$ and $S_i = S_{i - 1}$, then color of $(i - 1)^{th}$ plank changes to $P$.
 - if $1 \leq i \leq N - 1$ and $S_i = S_{i + 1}$, then color of $(i + 1)^{th}$ plank changes to $P$.

Now this process continues for the newly colored planks also. If none of the neighbors have same color, then nothing happens to the neighbors.

Suppose Ryan has planks which have their coloring : $B B W W W B$
If Ryan colors the fourth plank( whose color is $W$ ) to color $B$, then the finally the planks would be colored as following:

 $B B B B B B$

Ryan can choose any **one** of the $N$ planks and change its color as many times as he wants. Determine the minimum number of times Ryan has to paint a plank such that all planks get the same color at the end.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case consists of an integer $N$ the number of planks
- Second line of each test case consists of a string $S$ of size $N$,where the $i$ th character denotes the color of plank $i$

---

## Output Format

For each testcase, output a single integer denoting the minimum number of times Ryan has to paint a **single** plank such that all planks get the same color at the end.

---

## Constraints

- $1 \leq T \leq 10^{5}$
- $1 \leq N \leq 10^5$
-  $S$ consists only of characters $B$ and $W$
- The sum of $N$ over all cases doesn't exceed $10^{5}$.

---

## Examples

**Example 1**

**Input**

```text
4
6
BBWWWB
5
WWBWB
2
BB
9
WWBBBBBWW
```

**Output**

```text
1
2
0
1
```

**Explanation**

**Test case 1:**
The first test case is already described in the question.

**Test case 2:**
Ryan can paint the third plank to $W$. After doing so the color string of planks become $W W W W B$. Then he can again paint the third plank to the color $B$.
After doing so the string goes through following transitions:
 - The color of **third** plank changes to $B$. ( The string becomes $W W B W B$ )
 - The color of **second** and **fourth** plank changes to $B$. ( The string becomes $W B B B B$ )
 - The color of **first** plank changes to $B$. ( The string becomes $B B B B B$ )

Finally, all planks have same color.

**Test case 3:**
All planks have the same color.

**Test case 4:**
Ryan can paint any of the planks numbered from $3$ to $7$ to $W$, and all these planks will be colored to $W$!

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
BBWWWB
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5
WWBWB
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2
BB
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
9
WWBBBBBWW
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Contest Div1 : [Here](https://www.codechef.com/FZBZ21A/problems/MKGPLNKS)

Contest Div2 : [Here](https://www.codechef.com/FZBZ21B/problems/MKGPLNKS)

Contest Div3 : [Here](https://www.codechef.com/FZBZ21C/problems/MKGPLNKS)

Setter : [Ronels Macwan](https://www.codechef.com/users/need_for_code)

Tester : [Manan Grover](https://www.codechef.com/users/mexomerf) , [Samarth Gupta](https://www.codechef.com/users/samarth2017), [Harsh Rajani](https://www.codechef.com/users/harshrajani460)

**DIFFICULTY**

Cake Walk

**Pre Requisites**

None

**Quick Explanation :**

If all planks are of the same color, then just output 0.

Otherwise, count the number of continuous groups of color B and W.

Paint the plank whose color has the minimum groups.

**Explanation** :

Let’s make continuous groups of same color, because when we paint a plank, all

neighboring planks of same color are also colored. Let’s call them grps_b , and

grps_w, denoting the number of groups of color black and white respectively.Then

the answer is min(grps_b,grps_w).

The proof is as follows:

A group can have at most 2 neighbouring groups (they will be of same color). When

we color a plank of a group to the color of it’s neighbor, then it will merge with them

and they will form a single group after that. If we repeat this process , we will

eventually end up with all planks colored the same. If we start with a Black plank , it

will take grps_b moves, and grps_w moves if we start with a white plank.Hence the

ans is min(grps_b,grps_w) moves.

**Time Complexity**

O(N)

**Solutions**

Setter’s Code:

``#include <bits/stdc++.h>
using namespace std;

void solve(){
  int grps_w=0,grps_b=0;

  int n,i;
  string s;
  cin >> n >> s;

  for(i=0;i<n;i++){

      assert(s[i]=='B' || s[i]=='W');

    int j=i+1;

    if(s[i]=='W'){
      grps_w++;

      while(j<n && s[j]==s[i]){
        j++;
      }
    } else {
      grps_b++;
      while(j<n && s[j]==s[i]){
        j++;
      }
    }

    i=j-1;
  }

  cout << min(grps_b,grps_w) << "\n";

}

signed main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  //A soln

   #ifndef ONLINE_JUDGE
     freopen("input.txt","r",stdin);
      freopen("output.txt","w",stdout);
      freopen("error.txt","w",stderr);
    #endif

  int tests;
  cin >> tests;

  while(tests--){
    solve();
  }

}

``

Tester’s Code:

``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
#define asc(i,a,n) for(I i=a;i<n;i++)
#define dsc(i,a,n) for(I i=n-1;i>=a;i--)
#define forw(it,x) for(A it=(x).begin();it!=(x).end();it++)
#define bacw(it,x) for(A it=(x).rbegin();it!=(x).rend();it++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lb(x) lower_bound(x)
#define ub(x) upper_bound(x)
#define fbo(x) find_by_order(x)
#define ook(x) order_of_key(x)
#define all(x) (x).begin(),(x).end()
#define sz(x) (I)((x).size())
#define clr(x) (x).clear()
#define U unsigned
#define I long long int
#define S string
#define C char
#define D long double
#define A auto
#define B bool
#define CM(x) complex<x>
#define V(x) vector<x>
#define P(x,y) pair<x,y>
#define OS(x) set<x>
#define US(x) unordered_set<x>
#define OMS(x) multiset<x>
#define UMS(x) unordered_multiset<x>
#define OM(x,y) map<x,y>
#define UM(x,y) unordered_map<x,y>
#define OMM(x,y) multimap<x,y>
#define UMM(x,y) unordered_multimap<x,y>
#define BS(x) bitset<x>
#define L(x) list<x>
#define Q(x) queue<x>
#define PBS(x) tree<x,null_type,less<I>,rb_tree_tag,tree_order_statistics_node_update>
#define PBM(x,y) tree<x,y,less<I>,rb_tree_tag,tree_order_statistics_node_update>
#define pi (D)acos(-1)
#define md 1000000007
#define rnd randGen(rng)
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
int main(){
  mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
  uniform_int_distribution<I> randGen;
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  I t;
  t=readInt(1,100000,'\n');
  I nn=0;
  while(t--){
    I n;
    n=readInt(1,100000,'\n');
    nn+=n;
    S s;
    s=readString(n,n,'\n');
    asc(i,0,n){
      assert(s[i]=='W' || s[i]=='B');
    }
    I x=0,y=0;
    asc(i,0,n-1){
      if(s[i]=='W' && s[i+1]=='B'){
        x++;
      }
      if(s[i]=='B' && s[i+1]=='W'){
        y++;
      }
    }
    cout<<max(x,y)<<"\n";
  }
  assert(nn<=100000);
  return 0;
}
``

</details>
