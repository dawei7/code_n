# Candies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CANDIES3 |
| Difficulty Rating | 2329 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CANDIES3](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CANDIES3) |

---

## Problem Statement

Chef gave you an infinite number of candies to sell. There are $N$ customers, and the budget of the $i^{th}$ customer is $A_i$ rupees, where $1 \leq A_i \leq M$.

You have to choose a price $P$, to sell the candies, where $1 \leq P \leq M$.
The $i^{th}$ customer will buy **exactly** $\lfloor{\frac{A_i}{P}} \rfloor$ candies.
Chef informed you that, for each candy you sell, he will reward you with $C_P$ rupees, as a bonus. Find the **maximum** amount of bonus you can get.

Note:
- We are not interested in the profit from selling the candies (as it goes to Chef), but only the amount of bonus. Refer the samples and their explanations for better understanding.
- $\lfloor x \rfloor$ denotes the largest integer which is not greater than $x$. For example, $\lfloor 2.75 \rfloor = 2$ and $\lfloor 4 \rfloor = 4$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$, the number of customers and the upper limit on budget/price.
    - The second line contains $N$ integers - $A_1, A_2, \ldots, A_N$, the budget of $i^{th}$ person.
    - The third line contains $M$ integers - $C_1, C_2, \ldots, C_M$, the bonus you get per candy, if you set the price as $i$.

---

## Output Format

For each test case, output on a new line, the maximum amount of bonus you can get.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N, M \leq 10^5$
- $1 \leq A_i \leq M$
- $1 \leq C_j \leq 10^6$
- The elements of array $C$ are not necessarily non-decreasing.
- The sum of $N$ and $M$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5 6
3 1 4 1 5
1 4 5 5 8 99
1 2
1
4 1
```

**Output**

```text
20
4
```

**Explanation**

**Test case $1$:**
- If we choose $P = 1$, the number of candies bought by each person is $[\lfloor{\frac{3}{1}} \rfloor, \lfloor{\frac{1}{1}} \rfloor, \lfloor{\frac{4}{1}} \rfloor, \lfloor{\frac{1}{1}} \rfloor, \lfloor{\frac{5}{1}} \rfloor]$. Thus, our bonus is $(3 + 1 + 4 + 1 + 5) \cdot 1 = 14$.
- If we choose $P = 2$, the number of candies bought by each person is $[\lfloor{\frac{3}{2}} \rfloor, \lfloor{\frac{1}{2}} \rfloor, \lfloor{\frac{4}{2}} \rfloor, \lfloor{\frac{1}{2}} \rfloor, \lfloor{\frac{5}{2}} \rfloor]$. Thus our bonus is $(1 + 0 + 2 + 0 + 2) \cdot 4 = 20$.
- If we choose $P = 3$, the number of candies bought by each person is $[\lfloor{\frac{3}{3}} \rfloor, \lfloor{\frac{1}{3}} \rfloor, \lfloor{\frac{4}{3}} \rfloor, \lfloor{\frac{1}{3}} \rfloor, \lfloor{\frac{5}{3}} \rfloor]$. Thus our bonus is $(1 + 0 + 1 + 0 + 1) \cdot 5 = 15$.
- If we choose $P = 4$, the number of candies bought by each person is $[\lfloor{\frac{3}{4}} \rfloor, \lfloor{\frac{1}{4}} \rfloor, \lfloor{\frac{4}{4}} \rfloor, \lfloor{\frac{1}{4}} \rfloor, \lfloor{\frac{5}{4}} \rfloor]$. Thus our bonus is $(0 + 0 + 1 + 0 + 1) \cdot5 = 10$.
- If we choose $P = 5$, the number of candies bought by each person is $[\lfloor{\frac{3}{5}} \rfloor, \lfloor{\frac{1}{5}} \rfloor, \lfloor{\frac{4}{5}} \rfloor, \lfloor{\frac{1}{5}} \rfloor, \lfloor{\frac{5}{5}} \rfloor]$. Thus our bonus is $(0 + 0 + 0 + 0 + 1) \cdot 8 = 8$.
- If we choose $P = 6$, the number of candies bought by each person is $[\lfloor{\frac{3}{6}} \rfloor, \lfloor{\frac{1}{6}} \rfloor, \lfloor{\frac{4}{6}} \rfloor, \lfloor{\frac{1}{6}} \rfloor, \lfloor{\frac{5}{6}} \rfloor]$. Thus our bonus is $(0 + 0 + 0 + 0 + 0) \cdot 99 = 0$.

Thus, the answer is $20$.

**Test case $2$:**
- If we choose $P = 1$, the number of candies bought by each person is $[\lfloor{\frac{1}{1}} \rfloor]$. Thus, our bonus is $1 \cdot 4 = 4$.
- If we choose $P = 2$, the number of candies bought by each person is $[\lfloor{\frac{1}{2}} \rfloor]$. Thus, our bonus is $0 \cdot 1 = 0$.

Thus, the answer is $4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 6
3 1 4 1 5
1 4 5 5 8 99
```

**Output for this case**

```text
20
```



#### Test case 2

**Input for this case**

```text
1 2
1
4 1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CANDIES3)

[Contest: Division 1](https://www.codechef.com/START74A/problems/CANDIES3)

[Contest: Division 2](https://www.codechef.com/START74B/problems/CANDIES3)

[Contest: Division 3](https://www.codechef.com/START74C/problems/CANDIES3)

[Contest: Division 4](https://www.codechef.com/START74D/problems/CANDIES3)

***Author:*** [frtransform](https://www.codechef.com/users/frtransform)

***Testers:*** [nishant403](https://www.codechef.com/users/nishant403), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

[Harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)#Partial_sums)/sieve-like methods, prefix sums/binary search

#
[](#problem-4)PROBLEM:

You have an array A, where 1 \leq A_i \leq M for each i denotes the budget of the i-th customer.

There are infinitely many candies; whose price you can choose to be between 1 and M (every candy has the same price).

The i-th customer will buy as many candies as their budget allows.

You also have an array C of length M, where C_i denotes the bonus you receive for each candy of price i bought.

Find the maximum possible bonus if the price is chosen appropriately.

#
[](#explanation-5)EXPLANATION:

Suppose we fix the price of the candy, P.

Of course, we can always look at each element of A and figure out how much each person will buy, but that’s too slow.

Let’s look at a different perspective.

How many people will buy exactly k candies when the price is P?

It’s not hard to see that this is exactly the number of people whose A_i lies in the range [kP, (k+1)\cdot P-1].

If we were able to quickly count the number of people whose A_i lies in this range (say, in \mathcal{O}(1)), then we could iterate over every possible value of k and add k\cdot\text{count} to the number of candies we sell.

Computing this count quickly is fairly simple.

How?

If we sort the A_i, finding the number of elements in a given range is a simple exercise in binary searching, and can be done in \mathcal{O}(\log N).

In fact, we can utilize the constraints to do even better.

Notice that A_i \leq M.

So, let \text{freq} be an array of length M, where \text{freq}[r] denote the number of people with A_i = r.

Then, what we want is \text{freq}[kP] + \text{freq}[kP+1] + \ldots + \text{freq}[kP+k-1].

This is a range sum on \text{freq}, which can be computed in \mathcal{O}(1) using prefix sums.

Now, notice that for a fixed P, we don’t need to check too many values of k.

In particular, we can stop as soon as M\lt kP, because A_i \leq M anyway.

This means we need to check for each k from 1 to \left\lfloor \frac{M}{P}\right\rfloor.

Each check is done in \mathcal{O}(1).

Doing this for every P from 1 to M brings our overall time complexity to

\mathcal{O}\left (\sum_{P=1}^M \left\lfloor \frac{M}{P}\right\rfloor\right )

which is, [rather famously](https://codeforces.com/blog/entry/95287), equal to \mathcal{O}(M\log M).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(M\log M) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
#include "stdio.h"

using namespace std;

#define SZ(s) ((int)s.size())
#define all(x) (x).begin(), (x).end()
#define lla(x) (x).rbegin(), (x).rend()
#define bpc(x) __builtin_popcount(x)
#define bpcll(x) __builtin_popcountll(x)
#define MP make_pair
#define endl '\n'

mt19937 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

typedef long long ll;
const int MOD = 1e9 + 7;
const int N = 1e6 + 3e2;

int sumn = 0, summ = 0;
void solve(){
    int n, m;
    cin >> n >> m;

    sumn += n;
    summ += m;

    vector<int> c(m + 1), cnt(m + 1, 0);
    while (n--){
        int x;
        cin >> x;
        assert(1 <= x && x <= m);
        cnt[x]++;
    }

    for (int i = 1; i <= m; i++){
        cin >> c[i];
        assert(1 <= c[i] && c[i] <= 1000000);
    }

    for (int i = 2; i <= m; i++) cnt[i] += cnt[i - 1];

    long long ans = 0;
    for (int p = 1; p <= m; p++){
        long long candies = 0;
        for (int x = 1; x <= m / p; x++){
            int l = x * p, r = min(m, (x + 1) * p - 1);
            candies += (ll)(cnt[r] - cnt[l - 1]) * x;
        }
        ans = max(ans, candies * c[p]);
    }

    cout << ans << endl;
}

int main(){
    clock_t startTime = clock();
    ios_base::sync_with_stdio(false);

#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
#endif

    int test_cases = 1;
    cin >> test_cases;

    assert(1 <= test_cases && test_cases <= 10000);

    for (int test = 1; test <= test_cases; test++){
        // cout << (solve() ? "YES" : "NO") << endl;
        solve();
    }

    assert(sumn <= 100000);
    assert(summ <= 100000);

    cerr << "Time: " << int((double) (clock() - startTime) / CLOCKS_PER_SEC * 1000) << " ms" << endl;

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

const int MAX_T = 1e4;
const int MAX_N = 1e5;
const int MAX_SUM_N = 1e5;
const int MAX_C = 1e6;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int sum_m = 0;
int max_n = 0;
int max_m = 0;
int max_ans = 0;

void solve()
{
    int n,m;
    n = readIntSp(1,MAX_N);
    max_n = max(max_n, n);
    sum_n += n;
    assert(sum_n <= MAX_SUM_N);

    m = readIntLn(1,MAX_N);
    max_m = max(max_m, m);
    sum_m += m;
    assert(sum_m <= MAX_SUM_N);

    int a[n];
    for(int i=0;i<n;i++) {
        if(i != n - 1) {
            a[i] = readIntSp(1 , m);
        } else {
            a[i] = readIntLn(1 , m);
        }
    }

    int c[m];
    for(int i=0;i<m;i++) {
        if(i != m - 1) {
            c[i] = readIntSp(1 , MAX_C);
        } else {
            c[i] = readIntLn(1 , MAX_C);
        }
    }

    vector<int> fre(m + 1 , 0);
    for(int i=0;i<n;i++) {
        fre[a[i]]++;
    }

    vector<int> fre_pref_sum(m + 1 , 0);
    for(int i=1;i<=m;i++) {
        fre_pref_sum[i] = fre[i] + fre_pref_sum[i - 1];
    }

    int ans = 0;
    int ans_ind = -1;

    //iterate over P
    for(int p=1;p<=m;p++) {

        // A[i]/p is bounded by M/p
        int cur_sum = 0;

        for(int i=1;i<=(m/p);i++) {
            //how many values in a provide answer i (i.e. (A[j]/p) = i)
            int min_val = (p * i);
            int max_val = min(m , (p * (i + 1)) - 1);

            int val_count = fre_pref_sum[max_val] - fre_pref_sum[min_val - 1];
            cur_sum += i * val_count;
        }

        int cur_ans = cur_sum * c[p - 1];
        ans = max(ans , cur_ans);

        if(ans == cur_ans) {
            ans_ind = p;
        }
    }

    cerr << "Optimal p : " << ans_ind << " for given m : " << m << '\n';

    max_ans = max(max_ans , ans);

    cout << ans << '\n';
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
    cerr<<"Sum of lengths A : " << sum_n << '\n';
    cerr<<"Maximum length A : " << max_n << '\n';
    cerr<<"Sum of lengths B : " << sum_m << '\n';
    cerr<<"Maximum length B : " << max_m << '\n';
    cerr<<"Maximum answer : " << max_ans << '\n';
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
	n, m = map(int, input().split())
	a = list(map(int, input().split()))
	c = list(map(int, input().split()))
	pref = [0]*(m+1)
	for x in a: pref[x] += 1
	for i in range(1, m+1): pref[i] += pref[i-1]
	ans = 0
	for x in range(1, m+1):
		val = 0
		for y in range(x, m+1, x):
			R = min(m, y+x-1)
			val += y//x * (pref[R] - pref[y-1])
		ans = max(ans, val*c[x-1])
	print(ans)
``

</details>
