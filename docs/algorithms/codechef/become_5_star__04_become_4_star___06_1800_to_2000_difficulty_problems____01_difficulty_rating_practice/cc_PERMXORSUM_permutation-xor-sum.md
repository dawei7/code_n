# Permutation XOR Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMXORSUM |
| Difficulty Rating | 1998 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [PERMXORSUM](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/PERMXORSUM) |

---

## Problem Statement

For a permutation $P$ of integers from $1$ to $N$, let's define its value as $(1 \oplus P_1) + (2 \oplus P_2) + \ldots + (N \oplus P_N)$.

Given $N$, find the maximum possible value of the permutation of integers from $1$ to $N$.

As a reminder, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)

---

## Input Format

The first line of the input contains a single integer $T$ $-$ the number of test cases. The description of test cases follows.

The only line of each test case contains a single integer $N$.

---

## Output Format

For each test case, output the maximum possible value of the permutation of integers from $1$ to $N$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$.

---

## Examples

**Example 1**

**Input**

```text
5
1
2
3
4
29012022
```

**Output**

```text
0
6
6
20
841697449540506
```

**Explanation**

For $N = 1$, the only such permutation is $P = (1)$, its value is $1 \oplus 1 = 0$.

For $N = 2$, the permutation with the best value is $P = (2, 1)$, with value $1 \oplus 2 + 2 \oplus 1 = 6$.

For $N = 3$, the permutation with the best value is $P = (2, 1, 3)$, with value $1 \oplus 2 + 2 \oplus 1 + 3 \oplus 3 = 6$.

For $N = 4$, the permutation with the best value is $P = (2, 1, 4, 3)$, with value $1 \oplus 2 + 2 \oplus 1 + 3 \oplus 4 + 4 \oplus 3 = 20$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
20
```



#### Test case 5

**Input for this case**

```text
29012022
```

**Output for this case**

```text
841697449540506
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME104A/problems/PERMXORSUM)

[Contest Division 2](https://www.codechef.com/LTIME104B/problems/PERMXORSUM)

[Contest Division 3](https://www.codechef.com/LTIME104C/problems/PERMXORSUM)

***Author:*** [Lokesh Singh](https://www.codechef.com/users/lucky_21)

***Tester:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

#
[](#difficulty-2)DIFFICULTY:

Easy - Medium

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N, find the maximum possible value of the permutation of integers from 1 to N where value of a permutation P is defined as:

1 \oplus P_1 + 2 \oplus P_2 + \ldots + N \oplus P_N.

#
[](#explanation-5)EXPLANATION:

Hint 1

Solve for N as even and odd separately.

Hint 2

Find the upper bound for the answer.

Hint 3

Prove that a construction exists such that we can achieve the upper bound for all N.

Solution

Suppose a number x \in [1, N] has binary representation B_{x, hsb}, B_{x, hsb-1}, \ldots , B_{x,0} where hsb = \lfloor log_2 N \rfloor + 1 and B_{x, i} represents i^{th} bit of x and B_{x, i} \in \{0, 1\}.

- For N even:

\sum_{x=1}^{N} B_{x, i} \leq \frac{N}{2},  \forall i \in [0, hsb]. This means, there’s a possibility of arrangement in which a number having a bit set for some position i, is paired with a number having the bit unset at that position and if we can get this done for all the bits over all numbers, our answer will be maximum **since none of the set bits gets canceled**.

So upper bound on the answer is 2 \cdot \sum_{i = 1}^{N} i = N \cdot (N + 1).

Construction for the optimal permutation

Start pairing the elements starting from N. Suppose you are at any non paired element x, pair it with the closest non paired value y such that x \oplus y = x + y, i.e, none of the bits are lost and it can be proved that for every x such a y exists.

For example: Optimal permutation for N = 8 is

``6 5 4 3 2 1 8 7
``

- For N odd:

\sum_{x=1}^{N} B_{x, i} \leq \frac{N}{2} + 1,  \forall i \in [0, hsb]. For the values of i where \sum_{x=1}^{N} B_{x, i} = \frac{N}{2} + 1, atmost \frac{N}{2} set bits can be paired with \frac{N}{2} unset bits, implying atleast 1 set bit will get canceled. For other bit positions, atmax all the bits can be paired.

So upper bound on the answer is 2 \cdot (\sum_{i = 1}^{N} i  - \sum_{i = 0}^{hsb} f(i)), where:

f(i)=
\begin{dcases}
  2^i,& \text{if } \sum_{x=1}^{N} B_{x, i} = \frac{N}{2} + 1\\
  0,              & \text{otherwise}
\end{dcases}

Construction for the optimal permutation

Start pairing the elements starting from N. Suppose you are at any non paired element x, pair it with the closest non paired value y such that x \oplus y = x + y, i.e, none of the bits are lost and if such a y doesn’t exist, have P_x = x, i.e, pair the element with itself. It can be proved that there exists only one index where this happens.

For example: Optimal permutation for N = 11 is

``2 1 *3* 11 10 9 8 7 6 5 4 3 2 1
``

Here P_3 = 3.

Hence we are able to find a construction achieving the upper bound, thereby making it our answer.

#
[](#complexity-analysis-6)COMPLEXITY ANALYSIS:

Maximum computation time is taken to calculate \sum_{i = 0}^{hsb} f(i) which can be calculated in two ways:

- Make a frequency array F where F_i represents the number of elements in the range [1, N] having their i^{th} bit set. This can be done in  \mathcal {O}(sumN \log_2 maxN) where sumN represents the sum of N overall tests and maxN represents the maximum of N over all tests. This will pass subtask 1.

- The same can also be calculated in (\log_2 N)^2 using combinatorics and even better in  \log_2 N with additional use of prefix sums. So the total complexity is  \mathcal {O}(T \log_2 N).

Observation that makes the code way simple

Only the first consecutive set bits of N matter. See editorialist code for reference.

#
[](#solutions-7)SOLUTIONS:

Setter's Solution
``/**
 *    Coded by : lucky_21
 *               --------Lokesh Singh
**/

#include<bits/stdc++.h>
using namespace std;

#define     F           first
#define     S           second
#define     pb          push_back
#define     lb          lower_bound
#define     ub          upper_bound
#define     vi          vector<int>
#define     all(x)      x.begin(),x.end()
#define     fix         fixed<<setprecision(10)
#define     rep(i,a,b)  for(int i=int(a);i<=int(b);i++)
#define     repb(i,b,a) for(int i=int(b);i>=int(a);i--)
#define     FastIO      ios_base::sync_with_stdio(0),cin.tie(0)

typedef double db;
typedef long long ll;

const int N=2e5+5;
const int mod=1e9+7;

void solve(){
    int n;
    cin>>n;
    ll ans=1ll*n*(n+1);
    for(int b=0;b<30;b++){
        int p=(1<<b);
        int t=n/2/p*p;
        int m=n%(2*p);
        t+=max(0,m-p+1);
        if(t==n/2+1){
            ans-=2*p;
        }
    }
    cout<<ans<<'\n';
}

signed main(){
    FastIO;
    int t;
    cin>>t;
    while(t--) solve();
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt;
    cin >> tt;
    while (tt--) {
        int n;
        cin >> n;
        long long ans = 0;
        for (int i = 0; i < 30; i++) {
            int cnt = 0;
            if (n >= (1 << i)) {
                cnt += max(0, n % (1 << (i + 1)) + 1 - (1 << i));
                cnt += n >> (i + 1) << i;
            }
            if (cnt * 2 <= n) {
                cnt = cnt * 2;
            } else {
                cnt = (n - cnt) * 2;
            }
            ans += (long long) cnt << i;
        }
        cout << ans << '\n';
    }
    return 0;
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);

	int t; cin >> t;
	int n;
	while(t--){
		cin >> n;
		ll ans = (ll)n * (n + 1);
		ll p2 = 1;
		while(n != 0){
			if(n & 1)ans -= 2 * p2;
			else break;
			p2 *= 2; n /= 2;
		}
		cout << ans << endl;
	}

	return 0;
}
``

</details>
