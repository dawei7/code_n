# Valid String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VSTRING |
| Difficulty Rating | 2194 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [VSTRING](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/VSTRING) |

---

## Problem Statement

Given a binary string $S$ consisting of $0's$ and $1's$, find whether there exists a rightwise  [circular rotation](https://en.wikipedia.org/wiki/Circular_shift) of the string such that every 2 adjacent $1's$ are separated by at most $C$ $0's$.

**Note:** The last occurrence of $1$ in the rotated string won't have any $1$ next to it, i.e, first and the last ones in the string are not considered to be adjacent.

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of two lines of input.
- First line contains two space separated integers $N, C$, length of the string and the upper limit on a number of $0's$ between $2$ adjacent $1's$.
-  Second line contains the binary string $S$.

###Output:
For each testcase, output in a single line "YES" if there exists a rightwise circular rotation of string satisfying the criteria and "NO" if it doesn't exist.

**Note:** The output is case-insensitive ― each letter may be printed in upper case or lower case.

###Constraints
- $1 \leq N \leq 5*10^5$
- $0 \leq C \leq max(0, N - 2)$
- Sum of $N$ over all tests is atmost $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
4 1
1100
4 0
0101
6 1
101001
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Case 1:** In the original configuration maximum number of $0's$ between $2$ adjacent $1's$ is $0$, therefore it satisfies the criteria.

**Case 2:** The $4$ circular rotations of the string S = {"0101", "1010", "0101", "1010"}. In all the cases the maximum number of $0's$ between $2$ consecutive $1's$ is $1$ which doesn't satisfies the criteria.

**Case 3:** The $6$ circular rotations of the string S = {"101001", "110100", "011010", "001101", "100110", "010011"} out of which $second$, $third$ and $fourth$ strings satisfy the criteria.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 1
1100
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
4 0
0101
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
6 1
101001
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START1A/problems/VSTRING)

[Contest Division 2](https://www.codechef.com/START1B/problems/VSTRING)

[Contest Division 3](https://www.codechef.com/START1C/problems/VSTRING)

[Practice](https://www.codechef.com/problems/VSTRING)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

Just observation would do.

# PROBLEM

Given a binary string S and an integer C, you are allowed to perform circular on S any number of times. Does there exist any rotation such that every pair of adjacent ones is separated by at most C zeros.

# QUICK EXPLANATION

Assuming the last character to be adjacent to first, we can find the number of zeros between each pair of adjacent ones in a list. Now, the rotation of binary string is equivalent to deleting at most one element of this list. So if rest of the elements are up to C, then the answer is YES.

# EXPLANATION

For this problem we’ll consider an example first. Assume S = `010001010`. Now we shall consider all rotations of this string and compute the number of zeros between each adjacent pair of ones.

-
`010001010`: The number of zeros between adjacent ones are \{3, 1\}

-
`001000101`: The number of zeros between adjacent ones are \{3, 1\}

-
`100100010`: The number of zeros between adjacent ones are \{2, 3\}

-
`010010001`: The number of zeros between adjacent ones are \{2, 3\}

-
`101001000`: The number of zeros between adjacent ones are \{1, 2\}

-
`010100100`: The number of zeros between adjacent ones are \{1, 2\}

-
`001010010`: The number of zeros between adjacent ones are \{1, 2\}

-
`000101001`: The number of zeros between adjacent ones are \{1, 2\}

-
`100010100`: The number of zeros between adjacent ones are \{3, 1\}

We can see that the list of number of zeros between adjacent ones changes only when some `1` moves from last position to first position. But why does that happen?

It’s because the last and second last occurrence of `1` is no longer adjacent, and additionally, last occurrence of one becomes the first occurrence now, so it is adjacent to second occurrence in rotated string, hence number of zeros between them are added.

### Simple idea, Non-simple implementation

This way, we can actually maintain the queue type structure, and simulate the whole process, where queue supports the following operations

- Add element at beginning

- Remove element from end

- Find maximum of elements in queue

In order to support last operation, there are various methods, like mentioned [here](https://www.geeksforgeeks.org/design-a-queue-data-structure-to-get-minimum-or-maximum-in-o1-time/) or [implementing queue using two stacks](https://www.geeksforgeeks.org/queue-using-stacks/) and using [minimum stack](https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/) approach.

### Can we observe more?

Above approaches were correct, although require too much implementation for an easy problem like this, so let’s observe a bit more.

We saw that list of number of zeros between each pair of adjacent ones got affected only when some `1` moves from last to first. Let’s assume for a moment that last and first character of S are adjacent.

Considering S = `010001010`, now the list of number of zeros between adjacent ones is \{3, 1, 2\}. It is easy to see that all rotations of S have this same list of number of zeros between adjacent ones.

Hence, rotation only affect the number of zeros between last and first occurrence of one, effectively removing it from the list.

So, we can see that if we compute the list of zeros between adjacent ones when S is assumed to be cyclic, we can delete any one element from the list. It can be seen that the new list after deletion shall correspond to a cyclic rotation of original string S.

### Simpler solution, simpler life

So now we have the list of number of zeros between adjacent ones when S is assumed to be cyclic, we know we can delete exactly one element. And we want the remaining elements in list to be up to C. Hence, it is optimal to delete the largest element from the list and check if remaining elements are up to C or not.

It is equivalent to checking whether the second-maximum element of this list is up to C or not. This can all be done with much simpler implementation.

**Genera Note:** There are many such problems where easy idea leads to complicated implementation, but with some more insights, solutions can become a lot more simpler.

# TIME COMPLEXITY

The time complexity is O(N) per test case.

The space complexity is O(N) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

const int maxl = 1e6;

int main()
{
    int t; cin >> t;
    int tl = 0;
    while(t--){
        int n, k; cin >> n >> k; assert(2 * n <= maxl);
        tl += n;
        string s; cin >> s;
        s += s;
        int len = 2 * n, p1 = len + 10, ptr = -1;
        string ans = "nO";
        for(int i = 0; i < len; i++){
            if(s[i] == '1'){
                if(i - p1 - 1 > k){
                    ptr = p1 + 1;
                }
                p1 = i;
            }
            if(i - ptr == n){
                ans = "YeS"; break;
            }
        }
        cout << ans << endl;
    }
    assert(tl <= maxl);
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
		    assert(false);
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
	    freopen("../VSTRING_0.in", "rb", stdin);
	    freopen("../out.txt", "wb", stdout);
    }
#endif
    int T;
    cin >> T;
    forn(tc, T)
    {
	    int N, C;
	    cin >> N >> C;
	    string S;
	    cin >> S;
	    vector<int> v;
	    int act = 0;
 		forn(i, S.size())
	    {
		    if (S[i] == '1')
		    {
			    v.push_back(act);
			    act = 0;
		    }
		    else
		    {
			    ++act;
		    }
	    }
	    if (act > 0)
	    {
		    if (v.empty())
			    v.push_back(act);
		    else
			    v[0] += act;
	    }

	    sort(v.begin(), v.end());
	    v.pop_back();
	    if (v.empty() || v.back() <= C)
		    cout << "YES\n";
	    else
		    cout << "NO\n";
    }
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class VSTRING{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), C = ni();
        String S = n();
        if(S.indexOf('1') == -1){
            pn("YES");
            return;
        }
        int idx = S.indexOf('1');
        S = S.substring(idx) + S.substring(0, idx);
        ArrayList<Integer> list = new ArrayList<>();
        int cnt = 0;
        for(int i = 0; i< S.length(); i++){
            if(S.charAt(i) == '0')cnt++;
            else{
                list.add(cnt);
                cnt = 0;
            }
        }
        list.add(cnt);
        int count = 0;
        for(int x:list)if(x > C)count++;
        pn(count <= 1?"YES":"NO");
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
        new VSTRING().run();
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
