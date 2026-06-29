# Shortest Route

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SHROUTE |
| Difficulty Rating | 1756 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [SHROUTE](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/SHROUTE) |

---

## Problem Statement

### Read problem statements in [Vietnamese](https://www.codechef.com/download/translated/JUNE21/vietnamese/SHROUTE.pdf),

There are $N$ cities in Chefland numbered from $1$ to $N$ and every city has a railway station. Some cities have a train and each city has at most one train originating from it. The trains are represented by an array $A$, where $A_i = 0$ means the $i$-th city doesn't have any train originating from it, $A_i = 1$ means the train originating from the $i$-th city is moving right (to a higher numbered city), and $A_i = 2$ means the train originating from the $i$-th city is moving left (to a lower numbered city).

Each train keeps on going forever in its direction and takes $1$ minute to travel from the current station to the next one. There is a special station at city $1$ which lets travellers instantaneously teleport to any other station that currently has a train. Teleportation and getting on a train once in the city both take $0$ minutes and all trains start at time $0$.

There are $M$ travellers at city $1$, and the $i$-th traveller has destination city $B_i$. They ask Chef to guide them to teleport to a particular station from which they can catch a train to go to their destination in the least time possible. In case it's not possible for a person to reach his destination, print $-1$.

**Note:** The input and output of this problem are large, so prefer using fast input/output methods.

###Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains three lines of input.
- The first line contains two integers $N$, $M$.
- The second line contains $N$ integers $A_1, A_2, \ldots, A_N$.
- The third line contains $M$ integers $B_1, B_2, \ldots, B_M$.

###Output
For each test case, output $M$ space-separated integers $C_1, C_2, \ldots, C_M$, where $C_i$ is the minimum time required by the $i$-th traveller to reach his destination and if the $i$-th traveller can't reach his destination, $C_i = -1$.

###Constraints
- $1 \leq N, M \leq 10^5$
- $0 \leq A_i \leq 2$
- $1 \leq B_i \leq N$
- The sum of $N$ over all test cases is at most $10^6$.
- The sum of $M$ over all test cases is at most $10^6$.

###Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 1
1 0 0 0 0
5
5 1
1 0 0 0 2
4
5 2
2 0 0 0 1
3 1
```

**Output**

```text
4
1
-1 0
```

**Explanation**

**Test Case $1$:** The only person takes the train from station $1$ and hence takes $|5 - 1| = 4$ minutes to reach his destination.

**Test Case $2$:** The only person takes the train from station $5$ and hence takes $|5 - 4| = 1$ minute to reach his destination.

**Test Case $3$:** Since no train passes station $3$, it's impossible for the first person to reach his destination and since the second person is already at station $1$, it takes him $0$ minutes to reach his destination.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 1
1 0 0 0 0
5
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
5 1
1 0 0 0 2
4
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 2
2 0 0 0 1
3 1
```

**Output for this case**

```text
-1 0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE21A/problems/SHROUTE)

[Contest Division 2](https://www.codechef.com/JUNE21B/problems/SHROUTE)

[Contest Division 3](https://www.codechef.com/JUNE21C/problems/SHROUTE)

[Practice](https://www.codechef.com/problems/SHROUTE)

**Setter:** [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia) and [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

None

# PROBLEM

Given an array A of length N representing N cities present in a line where A_i = 0 means no station, A_i = 1 means city i having a train station with train moving to the right, and A_i = 2 means city i having a train station with train moving to the left.

Initially, M travellers are at city 1 and can teleport to any city with a station in 0 minutes. Determine, for each traveller the minimum time required to reach the destination, or determine if it’s not possible for the traveller to reach the destination.

# QUICK EXPLANATION

- Build a list of trains going left and a list of trains right. For traveller at destination p, we need to find the largest positioned train going right at position \leq p and smallest positioned train going left at position \geq p

- The minimum time taken among these two trains is the required minimum time, if both don’t exist, then it’s not possible to reach city p.

- Edge case is when the traveller is at city 1, the time taken is 0 irrespective of train stations.

# EXPLANATION

### Brute force solution

For each traveller, check all train stations, and if a train from that station can reach the traveller’s destination, update the minimum time. This solution works in O(N*M) time and gets time limit exceeded verdict.

### Using Binary Search

For the traveller with destination p, We know, that among trains going right, only the train with the largest positioned train to the left of p matter. If we have a list L of trains going right, our required train’s station is **the largest value \leq p in list L**.

Similarly, for the list of trains R going left, we want to find **smallest value \geq p in list R**

Since list L and R can be built before queries, we can build and sort them beforehand, and binary search in order to find the answer to our queries.

Alternatively, these queries are available as **lower_bound()** and **upper_bound()** methods in C++, and floor/ceiling methods in TreeSet in java.

The time complexity of this solution is O(N*log(N))

### Using precomputation before queries

Let’s compute L_u as the minimum time to reach station u via a train moving towards left, and R_u as the minimum time to reach station u via a train moving right.

Initialliy assuming L_u = R_u = \infin for all u.

For stations with a train going right, we can set R_u = 0, and for all stations with a train going left, we can set L_u = 0.

Now, we can see that train at station u moving right shall reach station u+1 in R_u+1 time, we have update R_u = min(R_u, R_{u-1}+1)

Similarly, we have L_u = min(L_u, L_{u+1}-1)

We can compute R_u in increasing order of u and L_u in decreasing order of u in O(N) time.

The minimum time taken to reach city p is min(L_p, R_p). If both L_p and R_p are \infin, then it’s not possible to reach city p.

### Edge Case

Since the travellers start at city 1 before teleporting, all the travellers having city 1 as the destination do not need to teleport. The minimum time needed is 0 here.

# TIME COMPLEXITY

The time complexity is O(N) or O(N*log(N)) per test case depending upon implementation.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>

# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxtn = 1e6, maxtm = 1e6, maxn = 1e5, maxm = 1e5;
const string newln = "\n", space = " ";
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int t; cin >> t;
    int tn = 0, tm = 0;
    while(t--){
        int n, m; cin >> n >> m;
        tn += n; tm += m;
        int dp[n + 2][2];
        int a[n + 2];
        for(int i = 1; i <= n; i++){
            cin >> a[i];
        }
        dp[0][0] = dp[n + 1][1] = n + 10;
        for(int i = 1; i <= n; i++){
            if(a[i] == 1){
                dp[i][0] = 0;
            }else{
                dp[i][0] = dp[i - 1][0] + 1;
            }
            if(a[n - i + 1] == 2){
                dp[n - i + 1][1] = 0;
            }else{
                dp[n - i + 1][1] = dp[n - i + 2][1] + 1;
            }
        }
        for(int i = 1; i <= m; i++){
            int x; cin >> x;
            int ans = min(dp[x][0], dp[x][1]);
            if(ans > n)ans = -1;
            if(x == 1)ans = 0;
            cout << ans << (i == m ? newln : space);
        }
    }
    assert(tn <= maxtn);
    assert(tm <= maxtm);
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

#ifdef HOME
    #include <windows.h>
#endif

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

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
    if(IsDebuggerPresent())
    {
	    freopen("../in.txt", "rb", stdin);
	    freopen("../out.txt", "wb", stdout);
    }
#endif
    int T = readIntLn(1, 1'000'000);
    int sumN = 0;
    int sumM = 0;
    forn(tc, T)
    {
	    int N = readIntSp(1, 100'000);
	    int M = readIntLn(1, 100'000);
	    vector<int> A(N);
	    set<int> s1;
	    set<int> s2;
	    forn(i, N)
	    {
		    if(i + 1 != N)
			    A[i] = readIntSp(0, 2);
		    else
			    A[i] = readIntLn(0, 2);
		    if (A[i] == 1)
			    s1.insert(i);
		    if (A[i] == 2)
			    s2.insert(i);
	    }
	    forn(i, M)
	    {
		    int Bi = 0;
		    if (i + 1 != M)
			    Bi = readIntSp(1, N);
		    else
			    Bi = readIntLn(1, N);
		    --Bi;
		    int res = -1;
		    if (!s1.empty())
		    {
			    auto b1 = s1.upper_bound(Bi);
			    if (b1 != s1.begin() && (b1 == s1.end() || *b1 != Bi))
			    {
				    --b1;
			    }
			    if (*b1 <= Bi)
				    res = Bi - *b1;
		    }
		    if (!s2.empty())
		    {
			    auto b2 = s2.lower_bound(Bi);
			    if (b2 != s2.end())
			    {
				    if (res == -1)
					    res = *b2 - Bi;
				    else if (res > *b2 - Bi)
					    res = *b2 - Bi;
			    }
		    }
		    if (Bi == 0)
			    res = 0;
		    printf("%d ", res);
	    }
	    printf("\n");
    }
    assert(sumN <= 1'000'000);
    assert(sumM <= 1'000'000);
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class SHROUTE{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), Q = ni(), INF = (int)1e9;
        int[] left = new int[N], right = new int[N];
        Arrays.fill(left, INF);
        Arrays.fill(right, INF);
        for(int i = 0; i< N; i++){
            int x = ni();
            if(x == 1)right[i] = 0;
            if(x == 2)left[i] = 0;
        }
        for(int i = 1; i< N; i++)right[i] = Math.min(right[i], right[i-1]+1);
        for(int i = N-2; i>= 0; i--)left[i] = Math.min(left[i], left[i+1]+1);
        for(int q = 0; q< Q; q++){
            int p = ni()-1;
            int time = Math.min(left[p], right[p]);
            if(time == INF)time = -1;
            if(p == 0)time = 0;
            p(time);
            if(q+1 < Q)p(" ");
            else pn("");
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
        new SHROUTE().run();
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
