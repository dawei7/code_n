# Golf

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LKDNGOLF |
| Difficulty Rating | 1256 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LKDNGOLF](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LKDNGOLF) |

---

## Problem Statement

It's a lockdown. You’re bored in your house and are playing golf in the hallway.

The hallway has $N + 2$ tiles numbered from $0$ to $N+1$ from left to right. There is a hole on tile number $x$. You hit the ball standing on tile $0$. When you hit the ball, it bounces at lengths of $k$, i.e. the tiles covered by it are $0, k, 2k, \ldots$, and so on until the ball passes tile $N+1$.

If the ball doesn't enter the hole in the first trial, you try again but this time standing on the tile $N+1$. When you hit the ball, it bounces at lengths of $k$, i.e. the tiles covered by it are $(N + 1), (N + 1 - k), (N + 1 - 2k), \ldots$, and so on until the ball passes tile $0$.

Find if the ball will enter the hole, either in its forward journey or backward journey.

**Note:** The input and output of this problem are large, so prefer using fast input/output methods.

###Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The only line of each test case contains three integers $N, x, k$.

###Output
Output in a single line, the answer, which should be "YES" if the ball enters the hole either in the forward or backward journey and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

###Constraints
- $1 \leq T \leq 10^5$
- $1 \leq x, k \leq N \leq 10^9$

### Subtasks
**Subtask #1 (10 points):** $N \leq 10^2$

**Subtask #2 (90 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 4 2
5 3 2
5 5 2
```

**Output**

```text
YES
NO
NO
```

**Explanation**

In each test case, the tiles covered by the ball for $N = 5$ and $k = 2$ are $\{0, 2, 4, 6\}$ in the forward journey and $\{6, 4, 2, 0\}$ in the backward journey.

Therefore, the answer for the first test case is "YES" since the ball falls in the position of the hole at tile $4$. But the answer for test cases $2$ and $3$ is "NO" since the ball does not fall in the position of the hole.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5 3 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
5 5 2
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MAY21A/problems/LKDNGOLF)

[Contest Division 2](https://www.codechef.com/MAY21B/problems/LKDNGOLF)

[Contest Division 3](https://www.codechef.com/MAY21C/problems/LKDNGOLF)

[Practice](https://www.codechef.com/problems/LKDNGOLF)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester & Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

Basic Maths

# PROBLEM

Given N+2 tiles numbered from 0 to N+1 from left to right, there’s a hole at tile numbered x. A ball starting at tile 0, bounces at length k, visiting tiles 0, k, 2*k \ldots until the ball passes N+1. If the ball doesn’t enter hole, it starts from tile numbered N+1, jumps of length k towards left, visiting tiles (N+1), (N+1-k), (N+1-2*k) \ldots  until it passes tile numbered 0.

Determine whether the ball enters the hole in its forward or backward journey, or not.

# QUICK EXPLANATION

- Ball enters hole in forward journey if x \bmod k = 0

- Ball enters hole in backward journey if x \bmod k = (N+1) \bmod k

# EXPLANATION

### Subtask 1

We can simulate the movement of ball over tiles, starting from position 0 and incrementing position of ball by k at each step.

For reverse pass, we start at position N+1, decrementing the position of ball by k at each step.

Hence, there are at most 2*N iterations, solving the problem in O(N), which is sufficient for subtask 1, but not subtask 2.

### Subtask 2

Let’s see which positions are visited by ball in forward journey. Only those tiles are visited, which are a multiple of k. So if x \bmod k = 0, ball enters hole in forward pass.

We can see that if we could somehow reverse the order of tiles, the backward pass becomes same as forward pass. That way, tile numbered 0 is labelled N+1, tile numbered 1 is numbered N, tile numbered p is labelled (N+1)-p.

This reverse problem is same as forward pass. The ball starts at 0, moving k steps at a time, visiting only those positions which are a multiple of k.

Hence, for position p in original numbering to be visited in backward pass, position (N+1)-p must be a multiple of k, or (N+1-p) \bmod k = 0 \implies (N+1) \bmod k = p \bmod k.

Hence, hole x is visited in backward pass if x \bmod k = (N+1) \bmod k.

Hence, we can check in O(1) whether the ball would be visited in forward or backward journey.

# TIME COMPLEXITY

The time complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 1e5;
const string newln = "\n", space = " ";

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int t; cin >> t;
    int n, x, k;
    while(t--){
        cin >> n >> x >> k;
        string ans = (x % k == 0 || (n + 1 - x) % k == 0) ? "YeS" : "No";
        cout << ans << endl;
    }
}
``

Tester's Solution
``import java.util.*;
import java.io.*;
class LKDNGOLF{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), X = ni(), K = ni();
        pn((X%K == 0 || X%K == (N+1)%K)?"yEs":"nO");
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
        new LKDNGOLF().run();
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
