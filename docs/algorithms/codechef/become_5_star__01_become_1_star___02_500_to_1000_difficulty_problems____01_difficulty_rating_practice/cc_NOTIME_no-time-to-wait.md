# No Time to Wait

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOTIME |
| Difficulty Rating | 932 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [NOTIME](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/NOTIME) |

---

## Problem Statement

Only $x$ hours are left for the March Long Challenge and Chef is only left with the last problem unsolved. However, he is sure that he cannot solve the problem in the remaining time. From experience, he figures out that he needs exactly $H$ hours to solve the problem.

Now Chef finally decides to use his special power which he has gained through years of intense yoga. He can travel back in time when he concentrates. Specifically, his power allows him to travel to $N$ different time zones, which are $T_1, T_2, \ldots, T_N$ hours respectively behind his current time.

Find out whether Chef can use one of the available time zones to solve the problem and submit it before the contest ends.

### Input
- The first line of the input contains three space-separated integers $N$, $H$ and $x$.
- The second line contains $N$ space-separated integers $T_1, T_2, \ldots, T_N$.

### Output
Print a single line containing the string `"YES"` if Chef can solve the problem on time or `"NO"` if he cannot.

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq N \leq 100$
- $1 \leq x \lt H \leq 100$
- $1 \leq T_i \leq 100$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2 5 3
1 2
```

**Output**

```text
YES
```

**Explanation**

Chef already has $3$ hours left. He can go to the $2$-nd time zone, which is $2$ hours back in time. Then he has a total of $3 + 2 = 5$ hours, which is sufficient to solve the problem.

**Example 2**

**Input**

```text
2 6 3
1 2
```

**Output**

```text
NO
```

**Explanation**

If Chef goes to the $1$-st time zone, he will have $3 + 1 = 4$ hours, which is insufficient to solve the problem.

If he goes to the $2$-nd time zone, he will have $3 + 2 = 5$ hours, which is also insufficient to solve the problem.

Since none of the time travel options can be used to gain sufficient time to solve the problem, Chef is incapable of solving it.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH21A/problems/NOTIME)

[Contest Division 2](https://www.codechef.com/MARCH21B/problems/NOTIME)

[Contest Division 3](https://www.codechef.com/MARCH21C/problems/NOTIME)

[Practice](https://www.codechef.com/problems/NOTIME)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Felipe Mota](https://www.codechef.com/users/fmota)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

There are X hours left for march challenge to end, while Chef needs H hours to complete last problem, with X < H. Check if Chef can solve the problem in at least one timezone. The timezone with their time difference to Chef’s timezone are given.

# QUICK EXPLANATION

Chef can solve the problem if max(T_i) + X >= H where T_i denote time difference from Chef’s timezone.

# EXPLANATION

Let’s see what happens when Chef teleports to a timezone with time Z hours behind Chef’s timezone. The result is that Chef get’s Z more hours to solve the problem.

Hence, Let’s try each timezone one by one and see if Chef can solve the problem in any of them. Chef can solve the problem in timezone T_i behind Chef’s timezone if T_i + X \geq H. Checking each of these condition can be done in O(1) each, which is sufficient to solve the problem.

### Optional observation

Can we solve above problem while checking above condition only once? Yes. Rewriting T_i \geq H-X, we need to check if atleast one T_i \geq H-X holds. Hence, we can pick the timezone with largest T_i and hence, only one comparison would be sufficient.

### Follow up

Let’s assume Chef’s friend selects the timezone in which Chef is transported. Chef’s friend chooses timezone to try to stop Chef from solving the problem. Can Chef still solve the problem?

# TIME COMPLEXITY

The time complexity is O(N) per test case.

The memory complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

const int maxn = 100, maxt = 100, maxx = 99, maxh = 100;

int main()
{
    int n, h, x; cin >> n >> h >> x;
    int maxv = -1;
    int val;
    for(int i = 0; i < n; i++){
        cin >> val;
        maxv = max(maxv, val);
    }
    string ans = "NO";
    if(maxv + x >= h)ans = "YES";
    cout << ans << endl;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
int rint(char nxt){
  char ch=getchar();
  int v=0;
  int sgn=1;
  if(ch=='-')sgn=-1;
  else{
    assert('0'<=ch&&ch<='9');
    v=ch-'0';
  }
  while(true){
    ch=getchar();
    if('0'<=ch && ch<='9')v=v*10+ch-'0';
    else{
      assert(ch==nxt);
      break;
    }
  }
  return v*sgn;
}

int main(){
  int n=rint(' ');
  assert(1<=n&&n<=100);
  int h=rint(' ');
  int x=rint('\n');
  assert(1<=x&&x<h&&h<=100);
  vector<int>t(n);
  bool can=false;
  for(int i=0;i<n;i++){
    t[i]=rint(i==n-1?'\n':' ');
    assert(1<=t[i]&&t[i]<=100);
    can|=(x+t[i]>=h);
  }
  if(can)puts("YES");
  else puts("NO");
  assert(getchar()==EOF);
  return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class NOTIME{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), H = ni(), x = ni();
        boolean canSolve = false;
        for(int i = 0; i< N; i++){
            int timeDiff = ni();
            if(timeDiff+x >= H)canSolve = true;
        }
        pn(canSolve?"YES":"NO");
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = false;
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
        new NOTIME().run();
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
