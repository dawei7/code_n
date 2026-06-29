# College Life 2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COLGLF2 |
| Difficulty Rating | 1519 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [COLGLF2](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/COLGLF2) |

---

## Problem Statement

Chef has just started watching Game of Thrones, and he wants to first calculate the exact time (in minutes) that it'll take him to complete the series.

The series has $S$ seasons, and the $i^{th}$ season has $E_i$ episodes, each of which are $L_{i,1}, L_{i,2}, \ldots, L_{i,E_i}$ minutes long. Note that these $L_{i,j}$ include the duration of the beginning intro song in each episode. The streaming service that he uses, allows Chef to skip the intro song. The intro song changes slightly each season, and so he wants to watch the intro song in the first episode of each season, but he'll skip it in all other episodes of that season (yes, we know, a sacrilege!). You know that the intro song lasts for $Q_i$ minutes in the $i^{th}$ season.

Find the total time in minutes, that he has to watch.

### Input:

- First line will contain a single integer, $T$, denoting the number of testcases. Then the testcases follow.
- The first line of each testcase will contain a single integer $S$, denoting the total number of seasons.
- The second line contains $S$ space separated integers, $Q_1, Q_2, \ldots, Q_S$, where $Q_i$ denotes the duration of the intro song in the $i^{th}$ season.
- The $i^{th}$ of the next $S$ lines contains $E_i + 1$ space separated integers, where the first integer is $E_i$, denoting the number of episodes in the $i^{th}$ season. That is followed by the duration of each of the $E_i$ episodes, $L_{i,1}, L_{i,2}, \ldots, L_{i,E_i}$.

### Output:
For each testcase, output the answer in a single line.

### Constraints
- $1 \leq T \leq 5$
- $1 \leq S \leq 10^5$
- $2 \leq L_{i,j} \leq 10^5$
- $1 \leq E_i$
- Sum of all $E_i$ in a single testcase is at most $10^5$
- $1 \leq Q_i \lt L_{i,j}$, for all valid $j$.

---

## Examples

**Example 1**

**Input**

```text
1
2
1 2
1 2
2 3 4
```

**Output**

```text
7
```

**Explanation**

**1** in the beginning denotes there is only $1$ test case.

**Testcase 1:**

There are $2$ seasons. The intro song in each of the first season episodes lasts for $1$ minute, and the intro song in the second season episodes lasts for $2$ minutes each.

For the first season, since there is only $1$ episode, Chef will be watching it completely - $2$ minutes.

For the second season, Chef will be watching the first episode completely ($3$ minutes) and will skip the intro song of the second episode ($4 - 2 = 2$ minutes).

So, the total time spent is $2 + (3 + (4 - 2)) = 7$ minutes.

**Example 2**

**Input**

```text
2
1
10
5 11 11 11 11 11
5
10 10 10 10 10
1 11
1 11
1 11
1 11
1 11
```

**Output**

```text
15
55
```

**Explanation**

**2** in the beginning denotes there are $2$ test cases.

**Testcase 1:**

There is only $1$ season having intro song for $10$ minutes.

Chef will have to watch the entire first episode including the intro song and will be skipping the same in further seasons.

So, the total time spent is $(11 + (11 - 10) * 4) = 15$ minutes.

**Testcase 2:**

There are total $5$ seasons. The intro song in every season lasts for $10$ minutes.

For each of the five seasons, since there is only $1$ episode, Chef will be watching all of them completely - $11$ minutes each.

So, the total time spent is $11 * 5 = 55$ minutes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
10
5 11 11 11 11 11
5
10 10 10 10 10
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
1 11
1 11
1 11
1 11
1 11
```

**Output for this case**

```text
55
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START1A/problems/COLGLF2)

[Contest Division 2](https://www.codechef.com/START1B/problems/COLGLF2)

[Contest Division 3](https://www.codechef.com/START1C/problems/COLGLF2)

[Practice](https://www.codechef.com/problems/COLGLF2)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

None

# PROBLEM

Given duration of shows of S seasons, each season having an intro song, Determine the time taken to watch all the episodes, while skipping intro song in each episode except once every season.

# QUICK EXPLANATION

Simply subtract i-th intro song duration (E_i-1) times, as i-th song would be skipped E_i-1 times. Then take the total of all the episode times.

# EXPLANATION

Since this is a simple problem, I’ll explain the solution from two viewpoints for interested readers. It’s perfectly okay to choose any veiwpoint as feels comfortable. Both are essentially same in idea.

### Viewpoint 1

In this view point, we would compute the time spent on each episode. We’d subtract the duration of intro song from all except first episode for all seasons. So we have exact times spent on each episodes. We can take total of these and determine total duration.

### Viewpoint 2

In this viewpoint, we’d focus on computing the time spent viewing the intro song and time spent viewing content in episodes. Since each intro song is watched exactly once, so sum of duration of each intro song determines the total time spent hearing intro songs.

Computing the time spent viewing content is subtracting the duration of intro song from each episode and adding the remaining episode time.

# TIME COMPLEXITY

The time complexity is O(\sum{E_i}) per test case.

The space complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
#define pb push_back
#define ll long long int
#define pii pair<int, int>

using namespace std;

FILE *fp;
ofstream outfile;

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        // char g = getc(fp);
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
            // cout << x << " " << l << " " << r << endl;
            assert(l<=x && x<=r);
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
        // char g=getc(fp);
        assert(g != -1);
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

const int maxt = 5;
const int maxs = 1e5;
const int maxte = 1e5;
const int maxl = 1e5;

int main()
{
    int t = readIntLn(1, maxt);
    while(t--){
        int season = readIntLn(1, maxs);
        vector<int> q; q.clear();
        for(int i = 0; i < season; i++)q.pb(i == season - 1 ? readIntLn(1, maxl - 1) : readIntSp(1, maxl - 1));
        int te = 0;
        ll ans = 0;
        for(int i = 0; i < season; i++){
            int epi = readIntSp(1, maxte);
            te += epi;
            for(int j = 0; j < epi; j++){
                int len = j == epi - 1 ? readIntLn(q[i] + 1, maxl) : readIntSp(q[i] + 1, maxl);
                assert(len > q[i]);
                if(j == 0)ans += len; else ans += len - q[i];
            }
        }
        assert(te <= maxte);
        cout << ans << endl;
    }
    assert(getchar()==-1);
}
``

Tester's Solution
``#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <random>
#include <limits>

#ifdef HOME
#define NOMINMAX
#include <windows.h>
#endif

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T& a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T& a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true) {
	    char g = getchar();
	    if (g == '-') {
		    assert(fi == -1);
		    is_neg = true;
		    continue;
	    }
	    if ('0' <= g && g <= '9') {
		    x *= 10;
		    x += g - '0';
		    if (cnt == 0) {
			    fi = g - '0';
		    }
		    cnt++;
		    assert(fi != 0 || cnt == 1);
		    assert(fi != 0 || is_neg == false);

		    assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
	    }
	    else if (g == endd) {
		    assert(cnt > 0);
		    if (is_neg) {
			    x = -x;
		    }
		    assert(l <= x && x <= r);
		    return x;
	    }
	    else {
		    //assert(false);
	    }
    }
}

string readString(int l, int r, char endd) {
    string ret = "";
    int cnt = 0;
    while (true) {
	    char g = getchar();
	    assert(g != -1);
	    if (g == endd) {
		    break;
	    }
	    // 		if(g == '\r')
	    // 			continue;

	    cnt++;
	    ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
    return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
    return readString(l, r, ' ');
}

int main(int argc, char** argv)
{
#ifdef HOME
    if (IsDebuggerPresent())
    {
	    freopen("../COLGLF2_0.in", "rb", stdin);
	    freopen("../out.txt", "wb", stdout);
    }
#endif
    int T = readIntLn(1, 5);
    forn(tc, T)
    {
	    int S = readIntLn(1, 100'000);
	    int64_t res = 0;
	    vector<int> Q(S);
	    forn(i, S)
	    {
		    if (i + 1 == S)
			    Q[i] = readIntLn(1, 100'000);
		    else
			    Q[i] = readIntSp(1, 100'000);
		    res += Q[i];
	    }
	    forn(i, S)
	    {
		    int E = readIntSp(1, 100'000);
		    int EE;
		    forn(j, E)
		    {
			    if (j + 1 == E)
				    EE = readIntLn(2, 100'000);
			    else
				    EE = readIntSp(2, 100'000);
			    assert(EE > Q[i]);
			    res += EE - Q[i];
		    }
	    }
	    printf("%lld\n", res);
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class COLGLF2{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        long time = 0;
        int S = ni();
        long[] introSong = new long[S];
        for(int i = 0; i< S; i++){
            introSong[i] = nl();
            time += introSong[i];
        }
        for(int i = 0; i< S; i++){
            int E = ni();
            for(int j = 0; j< E; j++)time += nl()-introSong[i];
        }
        pn(time);
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
        new COLGLF2().run();
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

# VIDEO EDITORIAL:

Feel free to share your approach. Suggestions are welcomed as always.

</details>
