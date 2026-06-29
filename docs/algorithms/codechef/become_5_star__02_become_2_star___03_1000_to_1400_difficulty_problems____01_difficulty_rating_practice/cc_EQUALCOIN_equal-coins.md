# Equal Coins

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQUALCOIN |
| Difficulty Rating | 1233 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [EQUALCOIN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/EQUALCOIN) |

---

## Problem Statement

Chef has $X$ coins worth $1$ rupee each and $Y$ coins worth $2$ rupees each. He wants to distribute all of these $X+Y$ coins to his two sons so that the total value of coins received by each of them is the same. Find out whether Chef will be able to do so.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of $T$ test cases follows.
- Each test case consists of a single line of input containing two space-separated integers $X$ and $Y$.

---

## Output Format

For each test case, print "YES" (without quotes) if Chef can distribute all the coins equally and "NO" otherwise. You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^3$
- $0 \leq X, Y \leq 10^8$
- $ X + Y \gt 0$

---

## Examples

**Example 1**

**Input**

```text
4
2 2
1 3
4 0
1 10
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** Chef gives each of his sons $1$ coin worth one rupee and $1$ coin worth two rupees.

**Test case $3$:** Chef gives each of his sons $2$ coins worth one rupee.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 3
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 0
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
1 10
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/NOV21A/problems/EQUALCOIN)

[Contest Division 2](https://www.codechef.com/NOV21B/problems/EQUALCOIN)

[Contest Division 3](https://www.codechef.com/NOV21C/problems/EQUALCOIN)

[Practice](https://www.codechef.com/problems/EQUALCOIN)

**Setter:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# [](#difficulty-2)DIFFICULTY

Cakewalk

# [](#prerequisites-3)PREREQUISITES

None

# [](#problem-4)PROBLEM

Chef has X coins worth 1 rupee each and Y coins worth 2 rupees each. He wants to distribute all of these X+Y coins to his two sons so that the total value of coins received by each of them is the same. Find out whether Chef will be able to do so.

# [](#quick-explanation-5)QUICK EXPLANATION

Chef can only divide the coins equally only when the total worth of coins is even and either there’s at least one coin worth 1 or the number of coins worth 2 is even.

# [](#explanation-6)EXPLANATION

First of all, since the chef aims to divide the total value of coins into two equal parts, the total worth of all coins should be even. The total worth is X*1 + Y*2 = X+2*Y.

Hence, if X+2*Y is odd (which happens when X is odd), then it is not possible to divide coins.

Let’s assume that X is even. So X+2*Y is even as well. Let’s assume X+2*Y = 2*P for some P.

Two cases may arise

- P is odd: We need at least two coins worth 1 since each son must receive at least one coin worth 1 to obtain an odd value sum. Example: for X = 0 and Y = 3,  P = 3, but there’s no way to obtain odd sum with only coins worth 2.

- P is even: It is possible to divide always.

Hence, we can generalize. We need

- Total value (X+2*Y) to be even. AND

- Either X \gt 0 or Y must be even.

Tip: For problems like this, it is worth trying all tests with say 0 \leq X, Y \lt 5 if facing any issues

### [](#exercize-7)Exercize

Prove that the following conditions are also a valid solution for this problem.

The answer is YES if either of the following is satisfied.

- (X+2*Y) is multiple of 4

- (X+2*Y) is multiple of 2 and X \gt 0

### [](#exercize-2-8)Exercize 2

Prove the correctness of my solution. Tip: I wrote conditions for NO case.

# [](#time-complexity-9)TIME COMPLEXITY

The time complexity is O(1) per test case.

# [](#solutions-10)SOLUTIONS

Setter's Solution
``    #include<bits/stdc++.h>
    using namespace std;

    int main() {
      int t; cin >> t;
      while (t--) {
        int a, b;
        cin >> a >> b;
        int sum = a + 2 * b;
        if (sum % 4 == 0) {
          cout << "YES\n";
        } else if (sum % 2 == 0 && a > 0) {
          cout << "YES\n";
        } else {
          cout << "NO\n";
        }
      }
    }
``

Tester's Solution
``    #include <bits/stdc++.h>
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
    int main(){
      mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
      uniform_int_distribution<I> randGen;
      ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
      #ifndef ONLINE_JUDGE
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
      #endif
      I t;
      cin>>t;
      while(t--){
        I x,y;
        cin>>x>>y;
        if(x%2==0 && (y%2==0 || x>0)){
          cout<<"YES\n";
        }else{
          cout<<"NO\n";
        }
      }
      return 0;
    }
``

Editorialist's Solution
``    import java.util.*;
    import java.io.*;
    class EQUALCOIN{
        //SOLUTION BEGIN
        void pre() throws Exception{}
        void solve(int TC) throws Exception{
            int X = ni(), Y = ni();
            if(X%2 != 0 || (X == 0  && Y%2 == 1))pn("NO");
            else pn("YES");
        }
        //SOLUTION END
        void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
        static boolean multipleTC = true;
        FastReader in;PrintWriter out;
        void run() throws Exception{
            in = new FastReader();
            out = new PrintWriter(System.out);
            //Solution Credits: Taranpreet Singh
            int T = (multipleTC)?ni():1;
            pre();for(int t = 1; t<= T; t++)solve(t);
            out.flush();
            out.close();
        }
        public static void main(String[] args) throws Exception{
            new EQUALCOIN().run();
        }
        int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
        void p(Object o){out.print(o);}
        void pn(Object o){out.println(o);}
        void pni(Object o){out.println(o);out.flush();}
        String n()throws Exception{return in.next();}
        String nln()throws Exception{return in.nextLine();}
        int ni()throws Exception{return Integer.parseInt(in.next());}
        long nl()throws Exception{return Long.parseLong(in.next());}
        double nd()throws Exception{return Double.parseDouble(in.next());}

        class FastReader{
            BufferedReader br;
            StringTokenizer st;
            public FastReader(){
                br = new BufferedReader(new InputStreamReader(System.in));
            }

            public FastReader(String s) throws Exception{
                br = new BufferedReader(new FileReader(s));
            }

            String next() throws Exception{
                while (st == null || !st.hasMoreElements()){
                    try{
                        st = new StringTokenizer(br.readLine());
                    }catch (IOException  e){
                        throw new Exception(e.toString());
                    }
                }
                return st.nextToken();
            }

            String nextLine() throws Exception{
                String str = "";
                try{
                    str = br.readLine();
                }catch (IOException e){
                    throw new Exception(e.toString());
                }
                return str;
            }
        }
    }
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
