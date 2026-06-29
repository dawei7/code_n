# Minimal Inversions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MININV |
| Difficulty Rating | 1918 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [MININV](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/MININV) |

---

## Problem Statement

Initially, Chef had an array $A$ of length $N$. Chef performs the following operation on $A$ **at most** once:
- Select $L$ and $R$ such that $1 \le L \le R \le N$ and set $A_i := A_i + 1$ for all $L \le i \le R$.

Determine the **maximum** number of *inversions* Chef can decrease from the array $A$ by applying the operation **at most** once.
More formally, let the final array obtained after applying the operation **at most** once be $B$. You need to determine the **maximum** value of $inv(A) - inv(B)$ (where $inv(X)$ denotes the number of *inversions* in array $X$).

**Note:** The number of *inversions* in an array $X$ is the number of pairs $(i, j)$ such that $1 \le i \lt j \le N$ and $X_i \gt X_j$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

---

## Output Format

For each test case, output the **maximum** value of $inv(A) - inv(B)$ which can be obtained after applying at most one operation.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le N \le 10^5$
- $1 \le A_i \le N$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
5
4 2 3 1 5
6
1 2 3 4 5 6
4
2 1 1 1
```

**Output**

```text
2
0
3
```

**Explanation**

**Test case $1$:** The initial array $A$ is $[4, 2, 3, 1, 5]$ which has $5$ inversions. We can perform operation on $L = 3, R = 4$. The resultant array will be $[4, 2, 4, 2, 5]$ which has $3$ inversions. Therefore we reduce the number of inversion by $2$ which is the maximum decrement possible.

**Test case $2$:** The initial array $A$ is $[1, 2, 3, 4, 5, 6]$ which has $0$ inversions. In this case, we do not need to apply any operation and the final array $B$ will be same as the initial array $A$. Therefore the maximum possible decrement in inversions is $0$.

**Test case $3$:** The initial array $A$ is $[2, 1, 1, 1]$ which has $3$ inversions. We can perform operation on $L = 2, R = 4$. The resultant array will be $[2, 2, 2, 2]$ which has $0$ inversions. Therefore we reduce the number of inversion by $3$ which is the maximum decrement possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
4 2 3 1 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
6
1 2 3 4 5 6
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
4
2 1 1 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MININV)

[Contest: Division 1](https://www.codechef.com/START74A/problems/MININV)

[Contest: Division 2](https://www.codechef.com/START74B/problems/MININV)

[Contest: Division 3](https://www.codechef.com/START74C/problems/MININV)

[Contest: Division 4](https://www.codechef.com/START74D/problems/MININV)

***Author:*** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [nishant403](https://www.codechef.com/users/nishant403), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Frequency tables

#
[](#problem-4)PROBLEM:

You have an array A. **Exactly** once, you can choose a subarray [L, R] and increase all its elements by 1.

Suppose the final array is B. Find the maximum value of inv(A) - inv(B).

#
[](#explanation-5)EXPLANATION:

Let’s analyze what choosing subarray [L, R] does for the number of inversions, and whether this tells us anything about what choices of L and/or R can possibly be optimal.

Analysis

Let’s denote the prefix [1, L-1] by P, the subarray [L, R] by M, and the suffix [R+1, N] by S.

Now, consider some pair (i, j). Let’s do a bit of casework.

- If i\not\in M and j\not\in M, A_i and A_j both don’t change, so this pair’s contribution to the number of inversions doesn’t change.

- If i\in M and j\in M, both values increase by 1 so once again, its contribution to the number of inversions doesn’t change.

- If i\in M and j\in S, then only A_i increases by 1.

- If (i, j) was already an inversion (i.e, initially A_i \gt A_j), it continues to remain one.

- If A_i = A_j initially, this pair creates a new inversion

- If A_i \lt A_j initially, this pair continues to not be an inversion

- If i\in P and j \in M, then only A_j increases by 1.

- If A_i \leq A_j, this pair continues to not be an inversion.

- If A_i \gt A_j+1, this pair continues to be an inversion.

- If A_i = A_j+1, this pair stops being an inversion.

From this, we see that the only way to *reduce* inversions is between P and M; while interactions between M and S are bad because they can increase the number of inversions.

In particular, it’d be nice if P and M were as large as possible, while S was as small as possible.

This is easy to achieve: simply choose R = N always, so the suffix S will be empty!

However, we can’t yet say anything about L.

Now that we’ve fixed R to always be N, we need to find which value of L is optimal.

Checking each one in \mathcal{O}(N) (or worse) is obviously too slow.

Instead, let’s be a bit smarter.

Suppose we (somehow) knew the answer for [L, N] (that is, you know how many inversions it reduces).

Can we then compute the answer for [L+1, N]?

Yes we can!

Recall from our previous analysis that the only reductions in inversions come from pairs (i, j) such that A_i = A_j+1.

When moving from L to L+1, we’re essentially moving the element A_{L+1} from the subarray M to the subarray P. So,

- if P contains x occurrences of A_{L+1}+1, these x positions were originally reduced inversions with position L+1, but they are no longer reduced. So, decrease the current answer by x.

- On the other hand, if there are y occurrences of A_{L+1}-1 in M, these y positions now are reduced inversions with position L+1, so increase the current answer by y.

We need to be able to quickly compute x and y. Note that they’re both frequencies.

So, maintain two frequency tables: one corresponding to P and one corresponding to M.

When moving from L to L+1, update the frequencies appropriately: this takes one operation in each table, after which both x and y can be obtained in \mathcal{O}(N) by just looking at the appropriate frequency table.

This allows us to move from [L, N] to [L+1, N] in \mathcal{O}(1) time; updating the answer along the way.

So, start from L = 1 (for which computing the answer is trivial), and then increase L till N; each time computing the answer for that suffix.

The final answer is the maximum among everything computed.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << "L: " << l << ", R: " << r << ", Value Found: " << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

int sumN = 0;

void solve()
{
    int n = readIntLn(1, 1e5);
    vector<int> a = readVectorInt(n, 1, n);
    vector<int> pfreq(n + 2), sfreq(n + 2);
    for(int i = 0; i < n; i++)
        pfreq[a[i]]++;
    int ans = 0, cur = 0;
    for(int i = n - 1; i >= 0; i--)
    {
        // changing a[i] to a[i] + 1
        cur -= sfreq[a[i] - 1];
        cur += pfreq[a[i] + 1];
        ans = max(ans, cur);
        sfreq[a[i]]++;
        pfreq[a[i]]--;
    }
    cout << ans << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T = readIntLn(1, 1e5);
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    assert(sumN <= 2e5);
    readEOF();
    return 0;
}
``

Tester's code (C++)
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

#define int long long

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_N = 2e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int sum_ans = 0;

void solve()
{
    int n;
    n = readIntLn(1, MAX_N);

    sum_n += n;
    assert(sum_n <= MAX_SUM_N);
    max_n = max(max_n,n);

    int a[n];
    for(int i=0;i<n;i++) {
        if(i != n - 1) {
            a[i] = readIntSp(1 , n);
        } else {
            a[i] = readIntLn(1 , n);
        }
    }

   vector<int> before(n+2,0),after(n+2,0);

    for(int i=0;i<n;i++) {
        before[a[i]]++;
    }

   int result = 0;
   int cur_change = 0;
   int best_ind = -1;

    for(int i=n-1;i>=0;i--) {
        cur_change -= after[a[i]];

        after[a[i] + 1]++;
        before[a[i]]--;

        cur_change += before[a[i] + 1];

        result = max(result , cur_change);

        if(result == cur_change) {
            best_ind = i;
        }
    }

    sum_ans += result;

    cerr << "N : " << n << " best ind : " << best_ind << '\n';

    cout << result << '\n';
}

signed main()
{
    int t = 1;
    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Maximum N : " << max_n << '\n';
    cerr<<"Sum of N : " << sum_n << '\n';
    cerr<<"Sum of answer : " << sum_ans << '\n';
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	pref_freq = [0]*(n+2)
	suf_freq = [0]*(n+2)
	for x in a: pref_freq[x] += 1
	ans = 0
	cur = 0
	for i in reversed(range(1, n)):
		cur -= pref_freq[a[i]] * suf_freq[a[i]-1] + pref_freq[a[i]+1] * suf_freq[a[i]]
		suf_freq[a[i]] += 1
		pref_freq[a[i]] -= 1
		cur += pref_freq[a[i]] * suf_freq[a[i]-1] + pref_freq[a[i]+1] * suf_freq[a[i]]
		ans = max(ans, cur)
	print(ans)
``

</details>
