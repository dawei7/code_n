# Rock Paper Scissors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ROPASCI |
| Difficulty Rating | 2013 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ROPASCI](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ROPASCI) |

---

## Problem Statement

There are $N$ players standing in a line, indexed $1$ to $N$ from left to right. They all play a game of Rock, Paper, Scissors. Each player has already decided which move they want to play. You are given this information as a string $S$ of length $N$, i.e,

- $S_i$ is equal to $\verb+R+$ if player $i$ will play Rock.
- $S_i$ is equal to $\verb+P+$ if player $i$ will play Paper.
- $S_i$ is equal to $\verb+S+$ if player $i$ will play Scissors.

Let $W(i, j)$ denote the move played by the winner if players $i, i+1, \ldots, j$ compete in order from left to right. That is,
- First, players $i$ and $i+1$ play a game
- The winner of this game plays against player $i+2$
- The winner of the second game plays against player $i+3$

$\vdots$

- The winner of the first $j-i-1$ games plays against player $j$, and the move played by the winner of this game is declared to be $W(i, j)$.

If $i = j$, then player $i$ is considered to be the winner and $W(i, i) = S_i$.

Your task is to find the value of $W(i,N)$ for all $i$ from $1$ to $N$.

**Note** :
If a person with index $i$ and index $j$ ($i \lt j$) play against each other, then:
- If $S_i \neq S_j$, the winner is decided by classical rules, i.e, rock beats scissors, scissors beats paper, and paper beats rock.
- If $S_i = S_j$, the player with lower index (in this case, $i$) wins.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, the number of players.
- The second line of each test case contains the string $S$ of length $N$, denoting the moves chosen by the players.

---

## Output Format

For each test case, print a single line containing a string of length $N$, whose $i$-th character is $W(i, N)$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 5\cdot 10^5$
- $S_i$ is either $\verb+R+$, $\verb+P+$ or $\verb+S+$
- Sum of $N$ over all test cases doesn't exceed $5 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
1
S
4
SSPR
```

**Output**

```text
S
RRPR
```

**Explanation**

**Test Case 1.** $W(1,1) = \verb+S+$ as there is only one player.

**Test Case 2.**

For $W(1,4)$ the game is played as follows  :
- Player $1$ and $2$ compete, player $1$ wins.
- Player $1$ and $3$ compete, player $1$ wins.
- Player $1$ and $4$ compete, player $4$ wins.

Hence, we print $W(1,4) = S_4 = \verb+R+$

For $W(3,4)$ the game is played as follows  :
- Player $3$ and $4$ compete, player $3$ wins.

Hence, we print $W(3,4) = S_3 = \verb+P+$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
S
```

**Output for this case**

```text
S
```



#### Test case 2

**Input for this case**

```text
4
SSPR
```

**Output for this case**

```text
RRPR
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/DEC21A/problems/ROPASCI)

[Contest Division 2](https://www.codechef.com/DEC21B/problems/ROPASCI)

[Contest Division 3](https://www.codechef.com/DEC21C/problems/ROPASCI)

[Practice](https://www.codechef.com/problems/ROPASCI)

**Setter:** [Nishant Shah](https://www.codechef.com/users/nishant_adm)

**Tester:** [Lavish Gupta](https://www.codechef.com/users/lavish315)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

There are N players standing in a line, indexed 1 to N from left to right. They all play a game of Rock, Paper, Scissors. Each player has already decided which move they want to play. You are given this information as a string S of length N, i.e,

-
S_i is equal to \verb+R+ if player i will play Rock.

-
S_i is equal to \verb+P+ if player i will play Paper.

-
S_i is equal to \verb+S+ if player i will play Scissors.

Let W(i, j) denote the move played by the winner if players i, i+1, \ldots, j compete in order from left to right. That is,

- First, players i and i+1 play a game

- The winner of this game plays against player i+2

- The winner of the second game plays against player i+3

\vdots

- The winner of the first j-i-1 games plays against player j, and the move played by the winner of this game is declared to be W(i, j).

If i = j, then player i is considered to be the winner and W(i, i) = S_i.

Your task is to find the value of W(i,N) for all i from 1 to N.

#
[](#quick-explanation-5)QUICK EXPLANATION

- Considering position p, if q is the first position where p-th person loses, then W(p, N) = W(q, N).

- If no such q exists, person at position p wins all games, hence W(p, N) = A_p in that case.

#
[](#explanation-6)EXPLANATION

The brute force solution for this problem would be to consider each start point and simulate all games one by one. There are a total of N games, and each game may require N steps, so a total O(N^2) time is required to simulate this, which is not fast enough.

Let’s just consider computing W(p, N) for some p. Two cases are possible for a person at position p.

- Person at position p wins all games. In this case, W(p, N) = A_p, since p-th person win the last game.

- Person at position p loses to the person at position q.

In the second case, now q-th person starts playing subsequent games. Once q-th person starts playing, it does not matter whether we were computing W(q, N) or W(p, N). The answer only depends on subsequent games. We can prove that if q-th person is the first person to which p-th person loses, then W(q, N) = W(p, N) holds.

Hence, in order to compute W(p, N) quickly, we need W(q, N) computed for q \gt p. We can ensure this by solving the problem in the decreasing order of p.

We also need to compute quickly for each position, the smallest position q where the person at position p loses. It roughly translates to finding the first position of some character after position p.

Since there are only three distinct characters in the string, we can keep an ordered set of positions of each character. Alternatively, since we are iterating from right to left, we can maintain three variables, the last seen position of each charcacter. As soon as we process position p, we update the value of variable representing character A_p with p.

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(N) per test case.

#
[](#solutions-8)SOLUTIONS

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

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

const int MAX_T = 100000;
const int MAX_N = 500000;
const int MAX_SUM_LEN = 500000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

int get_res(int a , int b)
{
    if(a == b)
        return a ;
    if(a > b)
        return get_res(b , a) ;
    if(a == 0 && b == 1)
        return 1 ;
    if(a == 1 && b == 2)
        return 2 ;
    return 0 ;
}

void solve()
{
    string str ;
    int n = readIntLn(1 , MAX_N) ;
    str = readStringLn(n , n);

    sum_len += n;
    max_n = max(max_n , n) ;

    int dp[n][3] ;
    int arr[n] ;
    string s = "RPS" ;

    for(int i = 0 ; i < n ; i++)
    {
        for(int j = 0 ; j < 3 ; j++)
            if(str[i] == s[j])
                arr[i] = j ;
    }

    for(int i = n-1 ; i >= 0 ; i--)
    {
        for(int j = 0 ; j < 3 ; j++)
        {
            if(i == n-1)
                dp[i][j] = get_res(j , arr[i]) ;
            else
                dp[i][j] = dp[i+1][get_res(j , arr[i])] ;
        }
    }
    string ans;
    for(int i = 0 ; i < n ; i++)
    {
        if(i == n-1)
            ans += s[arr[i]] ;
        else
            ans += s[dp[i+1][arr[i]]] ;
    }
    cout << ans << endl ;
    return ;

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("inputf.txt", "r" , stdin);
    freopen("outputf.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;
    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(sum_len <= MAX_SUM_LEN) ;
    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class ROPASCI{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), A = 26;
        char[] S = n().toCharArray();
        int[] nxt = new int[A];
        Arrays.fill(nxt, N);
        char[] ans = new char[N];
        for(int i = N-1; i>= 0; i--){
            char win = win(S[i]);
            if(nxt[win-'A'] == N)ans[i] = S[i];
            else ans[i] = ans[nxt[win-'A']];
            nxt[S[i]-'A'] = i;
        }
        pn(new String(ans));
    }
    //who wins against ch
    char win(char ch){
        switch(ch){
            case 'R': return 'P';
            case 'P': return 'S';
            case 'S': return 'R';
            default: return ' ';
        }
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
        new ROPASCI().run();
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
