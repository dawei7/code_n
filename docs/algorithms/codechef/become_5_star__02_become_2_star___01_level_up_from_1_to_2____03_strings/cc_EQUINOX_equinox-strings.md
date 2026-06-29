# Equinox Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQUINOX |
| Difficulty Rating | 1272 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [EQUINOX](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/EQUINOX) |

---

## Problem Statement

Sarthak and Anuradha are very good friends and are eager to participate in an event called *Equinox*. It is a game of words. In this game, $N$ strings $S_1,\ldots, S_N$ are given. For each string $S_i$, if it starts with one of the letters of the word “EQUINOX”, Sarthak gets $A$ points and if not, Anuradha gets $B$ points. The one who has more points at the end of the game wins. If they both the same number of points, the game is a draw..

Print the winner of the game, if any, otherwise print “DRAW”.

###Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains three integers $N$, $A$, $B$.
- $N$ lines follow, each containing a string $S_{i}$.
- All strings are in UPPERCASE.

###Output
- For each test case, print “SARTHAK” (case insensitive) if he has more points than Anuradha, print “ANURADHA” (case insensitive) if she has more points than Sarthak, otherwise print “DRAW” (case insensitive), without the quotes.

###Constraints
- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq A$, $B \leq 10^{9}$
- $1 \leq \left|S_{i}\right| \leq 100$

###Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4 1 3
ABBBCDDE
EARTH
INDIA
UUUFFFDDD
2 5 7
SDHHD
XOXOXOXO
```

**Output**

```text
DRAW
ANURADHA
```

**Explanation**

**Test case $1$:** The strings which start with one of the letters of the word `EQUINOX` are $\{$ `EARTH`, `INDIA`, `UUUFFFDDD` $\}$. Thus, Sarthak gets $1$ point for each of these strings. In total, Sarthak gets $3$ points.
On the other hand, there is one string that does not start with one of the letters of the word `EQUINOX`. Thus, Anuradha gets $3$ points for that string.
Finally, since both of them have equal points, the game results in `DRAW`.

**Test case $2$:** There is only one string that starts with one of the letters of the word `EQUINOX` which is `XOXOXOXO`. Thus, Sarthak gets $5$ point for this string.
There is one string that does not start with one of the letters of the word `EQUINOX`. Thus, Anuradha gets $7$ points for that string.
Finally, Anuradha has the higher score. So she is the winner.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 1 3
ABBBCDDE
EARTH
INDIA
```

**Output for this case**

```text
DRAW
```



#### Test case 2

**Input for this case**

```text
UUUFFFDDD
2 5 7
SDHHD
XOXOXOXO
```

**Output for this case**

```text
ANURADHA
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME95A/problems/EQUINOX)

[Contest Division 2](https://www.codechef.com/LTIME95B/problems/EQUINOX)

[Contest Division 3](https://www.codechef.com/LTIME95C/problems/EQUINOX)

[Practice](https://www.codechef.com/problems/EQUINOX)

**Setter:** [Anshul Garg](https://www.codechef.com/users/skywalker_)

**Tester & Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

Given N words consisting of Uppercase English characters and two integers A and B, two players Sarthak and Anuradha play a game. For each word, if the first character of the word appears in string “EQUINOX”, Sarthak gets A points, otherwise Anuradha gets B points. The person with higher score wins.

# QUICK EXPLANATION

- Simulate the process, maintaining the scores and compare them.

# EXPLANATION

Since this is an easier problem, all we need to do is to simulate the game. Start with scores for both players being zero and consider word one by one.

To check if first characters appears in string EQUINOX, one naive way would be to write 7 if conditions. It works, but too much work for nothing. We can simplify it.

One way would be to us would be to create a string EQUINOX and use the inbuild find function to check whether the character appears in string EQUINOX or not.

Another way would be to make an array or a set.

Following code snippet depict the intended solution

``string EQUINOX = "EQUINOX"
SarthakScore = 0
AnuradhaScore = 0
for word in wordList:
     if word[0] in EQUINOX:
          SarthakScore += A
     else:
          AnuradhaScore += B
``

Don’t forget to use long data type, since the scores can easily go beyond 32 bit integer range.

# TIME COMPLEXITY

The time complexity is O(\sum |S_i|) per test case, since we read that as input.

# SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

const int mod = 1000000007;
#define int long long

string tt = "EQUINOX";

void solve(){
    int n, a, b;
    int ans1 = 0, ans2 = 0; cin >> n >> a >> b;
    for(int i = 0; i < n; i++){
        string s; cin >> s;
        int f = 0;
        for(int j = 0; j < tt.size(); j++){
            if(tt[j] == s[0]) f = 1;
        }
        if(f) ans1 += a;
        else ans2 += b;
    }
    if(ans1 == ans2) cout << "Draw\n";
    else if(ans1 > ans2) cout << "Sarthak\n";
    else cout << "Anuradha\n";
}

signed main(){
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    // #endif
    int t;
    cin >> t;
    while(t--) solve();
}
``

Tester's Solution
``import java.util.*;
import java.io.*;
class EQUINOX{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        long A = nl(), B = nl();
        long sarthak = 0, anuradha = 0;
        String pattern = "EQUINOX";
        for(int i = 0; i< N; i++){
            String word = n();
            if(pattern.contains(word.substring(0,1)))sarthak += A;
            else anuradha += B;
        }
        if(sarthak > anuradha)pn("SARtHak");
        else if(sarthak < anuradha)pn("aNUrAdHA");
        else pn("draW");
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
        new EQUINOX().run();
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
