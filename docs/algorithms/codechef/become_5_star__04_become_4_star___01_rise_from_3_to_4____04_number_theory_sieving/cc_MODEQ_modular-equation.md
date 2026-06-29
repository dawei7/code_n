# Modular Equation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MODEQ |
| Difficulty Rating | 1761 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [MODEQ](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/MODEQ) |

---

## Problem Statement

Given integers $N$ and $M$, find the number of ordered pairs $(a, b)$ such that $1 \le a < b \le N$ and $((M\ \mathrm{mod}\ a)\ \mathrm{mod}\ b) = ((M\ \mathrm{mod}\ b)\ \mathrm{mod}\ a)$.

###Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The only line of each test case contains two integers $N$, $M$.

###Output
For each testcase, output in a single line the answer to the problem.

###Constraints
- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^6$
- $1 \leq M \leq 5\cdot 10^5$
- The sum of $N$ over all test cases does not exceed $10^6$.

**Note:** Multiplier for JAVA for this problem is reduced to $1.25$ instead of usual $2$.

###Subtasks
**Subtask #1 (10 points):**
- $1 \leq T \leq 10$
- $2 \leq N \leq 10^3$
- $1 \leq M \leq 10^5$

**Subtask #2 (40 points):**
- $1 \leq T \leq 100$
- $2 \leq N \leq 10^5$
- $1 \leq M \leq 10^5$
- The sum of $N$ over all test cases does not exceed $10^6$.

**Subtask #3 (50 points):** Original Constraints

---

## Examples

**Example 1**

**Input**

```text
3
3 5
3 6
3 10
```

**Output**

```text
2
3
2
```

**Explanation**

**Test Case $1$:** There are $2$ valid pairs satisfying the conditions. These are:
- $(1, 2)$: $(1 \le 1 \lt 2 \le N)$. Given $M = 5$, $((5 \%1) \%2) = (0\%2) = 0$. Also, $((5 \%2) \%1) = (1\%1) = 0$.
- $(1, 3)$: $(1 \le 1 \lt 3 \le N)$. Given $M = 5$, $((5 \%1) \%3) = (0\%3) = 0$. Also, $((5 \%3) \%1) = (2\%1) = 0$.

**Test Case $2$:** There are $3$ valid pairs satisfying the conditions. These are:
- $(1, 2)$: $(1 \le 1 \lt 2 \le N)$. Given $M = 6$, $((6 \%1) \%2) = (0\%2) = 0$. Also, $((6 \%2) \%1) = (0\%1) = 0$.
- $(1, 3)$: $(1 \le 1 \lt 3 \le N)$. Given $M = 6$, $((6 \%1) \%3) = (0\%3) = 0$. Also, $((6 \%3) \%1) = (0\%1) = 0$.
- $(2, 3)$: $(1 \le 2 \lt 3 \le N)$. Given $M = 6$, $((6 \%2) \%3) = (0\%3) = 0$. Also, $((6 \%3) \%2) = (0\%2) = 0$.

**Test Case $3$:** There are $2$ valid pairs satisfying the conditions. These are:
- $(1, 2)$: $(1 \le 1 \lt 2 \le N)$. Given $M = 10$, $((10 \%1) \%2) = (0\%2) = 0$. Also, $((10 \%2) \%1) = (0\%1) = 0$.
- $(1, 3)$: $(1 \le 1 \lt 3 \le N)$. Given $M = 10$, $((10 \%1) \%3) = (0\%3) = 0$. Also, $((10 \%3) \%1) = (1\%1) = 0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3 6
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
3 10
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MAY21A/problems/MODEQ)

[Contest Division 2](https://www.codechef.com/MAY21B/problems/MODEQ)

[Contest Division 3](https://www.codechef.com/MAY21C/problems/MODEQ)

[Practice](https://www.codechef.com/problems/MODEQ)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester & Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

Binary Search, Basic maths would do.

# PROBLEM

Given N and M, find the number of ordered pairs (a, b) such that 1  \leq a < b \leq N and ((M \bmod a) \bmod b) = ((M \bmod b) \bmod a)

# QUICK EXPLANATION

- For a given a, only b for which above equation holds is when M - M \bmod a is divisible by b and b < a

- We can precompute factors of all possible M in sorted order, in order to count such b by binary searching for each a.

# EXPLANATION

### Subtask 1

Since N is small, we can try all pairs (a, b) and check the condition, counting the pairs for which the condition is satisfied. This solution works in O(N^2) time, which is sufficient for subtask 1.

### Some Math

We can no longer try all pairs. Let’s focus on the condition.

((M \bmod a) \bmod b) = ((M \bmod b) \bmod a)

Since a < b, ((M \bmod a) \bmod b) = M \bmod a

Hence, (M \bmod a) = ((M \bmod b) \bmod a) is what we need.

Writing M = b * \lfloor \frac{M}{b} \rfloor + M\bmod b, we need (b * \lfloor \frac{M}{b} \rfloor + M\bmod b) \bmod a = ((M \bmod b) \bmod a)

 ((b * \lfloor \frac{M}{b} \rfloor) \bmod a = 0

Hence, we need T = M-M \bmod b to be divisible by a.

- If M < b, all 1 \leq a < b are valid.

- Only the factors of T = M-M \bmod b strictly smaller than b are valid candidates for a

### Subtask 2

We can now try all values of b one by one and compute T = M - M \bmod b. Now, we need to count the number of factors of T strictly less than b. We find all factors of T in O(\sqrt T) time.

The time complexity of this approach is O(N * \sqrt M)

### Subtask 3

Here, the time taken to factorize is too much. But the range of values is limited. If we have list of factors of all numbers from 1 to max(M) in sorted order, all we care about is finding the number of factors of X less than some value Y.

This can be answered by binary searching on the list containing factors of X, for the first element \geq y.

The construction of these lists take O(M*log(M)) time in a sieve style manner, as depicted by following pseudocode

``factors[i] -> list of factors of i
for 1 <= i <= M:
     j = i
     while j <= M:
          factors[j].add(i)
          j += i
``

For answering queries, for each b, we need to do binary search on list containing factors of M-M \bmod b

The time complexity of this approach is O(M*log(M) + N*log(M))

# TIME COMPLEXITY

The time complexity is O(log(M) * (M + \sum N))

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 1e3, maxn = 1e6, maxm = 1e6;
const int maxs = 5e5;
vector<int> v[maxs + 1];
int main()
{
    for(int i = 1; i <= maxs; i++){
        for(int j = i; j <= maxs; j += i){
            v[j].pb(i);
        }
    }
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        ll ans = 0;
        for(int a = 2; a <= min(n, m); a++){
            int x = a * (m / a);
            int l = 0, r = v[x].size() - 1;
            int add = 0;
            while(l <= r){
                int m = (l + r) >> 1;
                if(v[x][m] < a){
                    add = m + 1;
                    l = m + 1;
                }else{
                    r = m - 1;
                }
            }
            ans += add;
        }
        for(int a = m + 1; a <= n; a++){
            ans += a - 1;
        }
        cout << ans << endl;
    }
}
``

Tester's Solution
``import java.util.*;
import java.io.*;
class MODEQ{
    //SOLUTION BEGIN
    int maxM = (int)5e5;
    int[] spf;
    int[][] factors;
    void pre() throws Exception{
        spf = spf(maxM);
        int[] count = new int[1+maxM];
        for(int i = 1; i<= maxM; i++){
            for(int j = i; j<= maxM; j+= i){
                count[j]++;
            }
        }
        factors = new int[1+maxM][];
        for(int i = 1; i<= maxM; i++){
            factors[i] = new int[count[i]];
            count[i] = 0;
        }
        for(int i = 1; i<= maxM; i++){
            for(int j = i; j<= maxM; j+= i){
                factors[j][count[j]++] = i;
            }
        }
    }
    void solve(int TC) throws Exception{
        int N = ni(), M = ni();
        long ans = 0;
        for(int b = 2; b <= N; b++){
            int T = M%b;
            //Find number of a such that M%a == T%a
            //(M-T) is a multiple of a
            //candidates for a are all a such that a < b and a|(M-T)
            if(M == T){
                ans += b-1;
                continue;
            }
            int V = M-T;
            int[] fact = factors[V];
            int lo = 0, hi = fact.length-1;
            while(lo < hi){
                int mid = lo+(hi-lo+1)/2;
                if(fact[mid] < b)lo = mid;
                else hi = mid-1;
            }
            ans += lo+1;
        }
        pn(ans);
    }
    int[] factors(int[] spf, int x){
        int[] factor = new int[]{1};
        while(x > 1){
            int p = spf[x], cnt = 0;
            for(;x%p == 0; x/= p)cnt++;
            int[] tmp = Arrays.copyOf(factor, (1+cnt)*factor.length);
            for(int pw = 1, cur = p; pw <= cnt; pw++, cur *= p)
                for(int i = 0; i< factor.length; i++)
                    tmp[pw*factor.length+i] = factor[i]*cur;
            factor = tmp;
        }
        return factor;
    }
    int[] spf(int max){
        int[] spf = new int[1+max];
        for(int i = 2; i<= max; i++)
            if(spf[i] == 0)
                for(int j = i; j <= max; j += i)
                    if(spf[j] == 0)
                        spf[j] = i;
        return spf;
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
        new MODEQ().run();
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
