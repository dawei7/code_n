# Bench Press

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BENCHP |
| Difficulty Rating | 1611 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [BENCHP](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/BENCHP) |

---

## Problem Statement

In the gym, Chef prefers to lift at least $W$ grams during a bench press and if that's impossible, Chef considers his workout to be incomplete and feels bad.

The rod weighs $W_r$ grams and there are $N$ other weights lying on the floor that weigh $w_1, w_2, ..., w_N$ grams. To maintain balance and to ensure that there is no unnecessary load due to torque, it's important that the weights added to the left side are symmetric to the weights added to the right side. It is not required to use all of the weights. It is also not required to use any weights at all, if Chef feels satisfied lifting only the rod.

For example:

 - $1$ $2$ $2$ $1$ $|$Rod Center$|$ $1$ $1$ $1$ $3$ is a wrong configuration, but

 - $1$ $2$ $3$ $1$ $|$Rod Center$|$ $1$ $3$ $2$ $1$ is a right configuration.

Find whether Chef will be able to collect the required weights to feel satisfied.

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- The first line contains three space-separated integers $N, W, W_r$.
- The second line contains $N$ space-separated integers $w_1, w_2, \ldots, w_N$.

### Output
For each test case, output the answer in a single line: "YES" if Chef will be satisfied after his workout and "NO" if not (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq W \leq 2\cdot 10^5$
- $1 \leq w_i \leq 10^5$
- $1 \leq W_r \leq 2\cdot 10^4$

### Subtasks
**Subtask #1 (30 points):** $w_i = 1$ for all valid $i$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2 5 10 
2 2
7 100 50
100 10 10 10 10 10 90 
6 100 40 
10 10 10 10 10 10
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case 1:** Since the weight of the rod is at least the required weight to be lifted, Chef will feel satisfied after the workout.

**Test case 2:** The configuration having maximum weight is:

$10$ $10$ $|$Rod Center$|$ $10$ $10$

So the maximum total weight Chef can lift is $50 + 4 \cdot 10 = 90$ which is less than the required amount to get satisfied.

**Test case 3:** The configuration having maximum weight is:

$10$ $10$ $10$ $|$Rod Center$|$ $10$ $10$ $10$

So the maximum total weight Chef can lift is $40 + 6\cdot 10 = 100$ which is equal to the required amount to get satisfied.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5 10
2 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
7 100 50
100 10 10 10 10 10 90
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
6 100 40
10 10 10 10 10 10
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME95A/problems/BENCHP)

[Contest Division 2](https://www.codechef.com/LTIME95B/problems/BENCHP)

[Contest Division 3](https://www.codechef.com/LTIME95C/problems/BENCHP)

[Practice](https://www.codechef.com/problems/BENCHP)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester & Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

None

# PROBLEM

Given a rod weighing W_r and N weights, ith weight weighing w_i. In order to maintain balance, Chef can lift rod if and only if on both sides of rod, the sequence of weights is symmetric. Determine if Chef can lift the rod weighing atleast W.

# QUICK EXPLANATION

- If grouping by weight, some weight appear odd number of times, the last one cannot be paired. Calling this last weight as useless weight.

- After discarding useless weights, if the sum of weight of rod and the remaining weights exceed the target weight, Chef can lift rod with weight atleast W, otherwise Chef can’t.

# EXPLANATION

Since we want to check if Chef can lift weight at least W, it is sufficient to determine the maximum weight Chef can lift while maintaining balance, and compare it with W.

Only constraint that stops Chef from adding all weight is the balance. Let’s group the weights by their weight in grams. We can see that weights of different weight do not affect each other.

Say there are C weights of weight G.

- If C is even, we can put C/2 weights on left side and C/2 weights on the right side, thus maintaining balance while adding weight C*G to the total weight.

- If C is odd, we cannot pair the last weight. we can put \lfloor C/2 \rfloor weights on left side and \lfloor C/2 \rfloor weights on the right side, thus maintaining balance while adding weight (C-1)*G to the total weight.

Hence, it is sufficient to count the occurrence of each weight, compute the maximum weight achievable while maintaining balance and compare it with target.

Summary

Can you write expression to avoid writing if condition or ternary operator for handling even and odd case?

Summary

(C-C%2)*G

### Bonus

- Can Chef lift exactly W weight?

- What is the minimum weight greater than W the chef can lift?

# TIME COMPLEXITY

The time complexity is O(N*log(N)) using normal sorting, or O(N+W) using counting sort.

# SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

const int maxw = 2e5, maxwr = 2e4, maxwi = 1e5, maxt = 10, maxn = 1e5;
int f[maxwi + 1];

int main()
{
    int t; cin >> t;
    int n, w, wr;
    while(t--){
        cin >> n >> w >> wr;
        memset(f, 0, sizeof(f));
        int x;
        for(int i = 0; i < n; i++){
            cin >> x;
            f[x]++;
        }
        long long int tot = wr;
        for(int i = 1; i <= maxwi; i++)tot += (long long int)i * 2 * (f[i] / 2);
        string ans = (tot >= w ? "YeS" : "No");
        cout << ans << endl;
    }
}
``

Tester's Solution
``import java.util.*;
import java.io.*;
class BENCHP{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), targetW = ni(), rodW = ni();
        int[] W = new int[N];
        for(int i = 0; i< N; i++)W[i] = ni();
        Arrays.sort(W);
        long maxWeight = rodW;
        for(int i = 0, ii = 0; i< N; i = ii){
            while(ii < N && W[i] == W[ii])ii++;
            int cnt = (ii-i);
            maxWeight += (cnt-cnt%2)*(long)W[i];
        }
        pn(maxWeight >= targetW?"yEs":"nO");
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
        new BENCHP().run();
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
