# Musical Rods

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MUSROD |
| Difficulty Rating | 2160 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MUSROD](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MUSROD) |

---

## Problem Statement

You have $N$ rods with you. The $i$-th rod has a length of $A_i$ and a beauty of $B_i$.

You'd like to arrange these rods side-by-side in some order on the number line, starting from $0$.

Let $x_i$ be the starting position of the $i$-th rod in an arrangement. The beauty of this arrangement is
$$
\sum_{i=1}^N x_i\cdot B_i
$$

What is the maximum beauty you can attain?

Note that the left endpoint of the first rod you place **must** be $0$, and you cannot leave any space between rods.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single integer $N$, the number of rods.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$
    - The third line of each test case contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$

---

## Output Format

- For each test case print on a new line the answer: the maximum value of $\sum_{i=1}^N x_i B_i$ if the order of rods is chosen optimally.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_{i} \leq 10^4$
- $1 \leq B_{i} \leq 10^4$
- The sum of $N$ across all testcases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
2
1 2
4 6
4
2 8 9 11
25 27 100 45
```

**Output**

```text
8
2960
```

**Explanation**

**Test case $1$:** Place the second rod followed by the first one. This makes $x_2 = 0$ and $x_1 = 2$, giving us a beauty of $2\cdot 4 + 0\cdot 6 = 8$, which is the maximum possible.

**Test case $2$:** Place the rods in the order $[2, 4, 3, 1]$. This gives us $x = [28, 0, 19, 8]$, and the beauty is $28\cdot 25 + 0\cdot 27 + 19\cdot 100 + 8\cdot 45 = 2960$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
4 6
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
4
2 8 9 11
25 27 100 45
```

**Output for this case**

```text
2960
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MUSROD)

[Contest: Division 1](https://www.codechef.com/START67A/problems/MUSROD)

[Contest: Division 2](https://www.codechef.com/START67B/problems/MUSROD)

[Contest: Division 3](https://www.codechef.com/START67C/problems/MUSROD)

[Contest: Division 4](https://www.codechef.com/START67D/problems/MUSROD)

***Author:*** [Kunj Rakesh Patel](https://www.codechef.com/users/kunjrp_1402)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2160

#
[](#prerequisites-3)PREREQUISITES:

Sorting, exchange arguments

#
[](#problem-4)PROBLEM:

Given the length A_i and beauty B_i of N rods, arrange them in some order to maximize \sum_{i=1}^N x_i B_i where x_i is the starting position of rod i.

#
[](#explanation-5)EXPLANATION:

Let’s find the optimal order of rods: computing the answer given this order is easy to do.

First, try to solve the problem for N = 2, i.e, you have one rod with parameters (A_1, B_1) and another with parameters (A_2, B_2). How would you determine the optimal order here?

Answer

There are only two possible orders.

The beauties of these two orders are A_1B_2 and A_2B_1 respectively, so the answer is whichever of them is higher.

In particular, notice that rod 1 is placed before rod 2 if and only if A_1B_2 \geq A_2B_1, i.e, \frac{A_1}{B_1} \geq \frac{A_2}{B_2}

A natural generalization of the above observation to N rods would be to sort them in descending order of \frac{A_i}{B_i}.

Indeed, this is optimal, and isn’t hard to prove.

Proof

Consider some arrangement of rods which is *not* sorted in descending order of \frac{A_i}{B_i}.

Then, there must be an index i such that 1 \leq i \lt N and \frac{A_i}{B_i} \lt \frac{A_{i+1}}{B_{i+1}}.

If we swap the places of these two, the beauty increases by A_{i+1}B_i - A_iB_{i+1} \gt 0 so our initial arrangement couldn’t have been optimal.

This gives us a pretty simple solution: sort the rods in decreasing order of \frac{A_i}{B_i}, then use this order to compute the final answer.

As an aside, what we did above is something called an *exchange argument*, which sometimes can be [quite useful](https://codeforces.com/blog/entry/63533).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
#include <iostream>
#define ull  long long int
#define ll long long int
using namespace std;
#define maxlen 100

bool sortVec(const vector<ull> l, const vector<ull> r){
    if (l[1]*r[0] == l[0]*r[1]) return l[0] < r[0];
	else if (l[1]*r[0] > l[0]*r[1])return false;
	else return true;
}

void solve (ll k){
	ull n;
	cin>>n;
	vector<vector<ull>> rods(n, vector<ull>(2,0));
	ull sum = 0;
	for (ull i = 0; i < n; i++){
		cin>>rods[i][0];
		sum+=rods[i][0];
	}
	for (ull i = 0; i < n; i++){
		cin>>rods[i][1];
	}

	//cout<<"here"<<"\n";
	sort(rods.begin(), rods.end(), sortVec);
	//cout<<"here"<<"\n";
	ull pos = 0;
	ull ans = 0;
	for (ull i = 0; i < n; i++){
        //cout<<pos<<" "<<rods[i][1]<<" "<<ans<<"\n";
		ans += pos*rods[i][1];
		pos += rods[i][0];
	}
	cout<<ans<<"\n";

}

int main(){
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
    int t;
	cin>>t;
	for(int k=1;k<=t;k++){
		solve(k);
	}
	return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
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

bool custom(pair<int, int>& a, pair<int, int>& b) {
    return a.first*b.second > a.second*b.first;
}

int main() {
	int t;
	t = readIntLn(1, 1000);
	while(t--) {
	    int n;
	    n = readIntLn(1, 100000);
	    vector<int> a(n), b(n);
	    for(int i = 0; i < n - 1; i++) a[i] = readIntSp(1, 10000);
	    a[n - 1] = readIntLn(1, 10000);
	    for(int i = 0; i < n - 1; i++) b[i] = readIntSp(1, 10000);
	    b[n - 1] = readIntLn(1, 10000);
	    vector<pair<int, int>> v(n);
	    for(int i = 0; i < n; i++) v[i].first = a[i], v[i].second = b[i];
	    sort(v.begin(), v.end(), custom);
	    long long int ans = 0, cur = 0;
	    for(int i = 0; i < n; i++) {
	        ans += (cur*v[i].second);
	        cur += v[i].first;
	    }
	    cout << ans << "\n";
	}
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ind = [i for i in range(n)]
    ind.sort(key = lambda x: -a[x]/b[x])
    ans = prv = 0
    for i in ind:
        ans += b[i] * prv
        prv += a[i]
    print(ans)
``

</details>
