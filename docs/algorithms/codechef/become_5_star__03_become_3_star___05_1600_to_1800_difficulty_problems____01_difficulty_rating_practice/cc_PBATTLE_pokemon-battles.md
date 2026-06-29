# Pokemon Battles

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PBATTLE |
| Difficulty Rating | 1739 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [PBATTLE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/PBATTLE) |

---

## Problem Statement

There are $N$ Pokemon trainers numbered from $1$ to $N$. Each trainer has **one** Pokemon. All the trainers have arrived to participate in a contest.
There are two battle arenas, one in ground and other in water. Each Pokemon may have different power in both the arenas.
When two Pokemon fight in an arena, the Pokemon having higher power in that arena wins. It is guaranteed that all Pokemon have **distinct** powers in the same arena to avoid any ties.

The *strength* of a Pokemon trainer is determined to be the number of other Pokemon his Pokemon can defeat in **at least one** arena.

It is known that only the Pokemon trainers with the **highest** *strength* will qualify for the next round (multiple trainers may have the same strength). Find the number of Pokemon trainers who will qualify for the next round.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains a single integer $N$, denoting the number of Pokemon trainers.
    - The second line will contain $N$ space-separated integers, $A_{1},A_{2},\ldots,A_{N}$, where $A_{i}$ denotes the power of the Pokemon of $i^{th}$ trainer in the ground arena.
    - The third line will contain $N$ space-separated integers, $B_{1},B_{2},\ldots,B_{N}$, where $B_{i}$ denotes the power of the Pokemon of $i^{th}$ trainer in the water arena.

---

## Output Format

For each test case, output on a new line the number Pokemon trainers who will qualify for the next round.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^{5}$
- $1 \leq A_i, B_i \leq 10^{9}$
- The elements of array $A$ are distinct.
- The elements of array $B$ are distinct.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^{5}$.

---

## Examples

**Example 1**

**Input**

```text
4
2
1 2
3 4
2
1 2
2 1
3
1 2 3
1 4 2
5
2 3 5 4 1
4 2 1 5 6
```

**Output**

```text
1
2
2
3
```

**Explanation**

**Test case 1:** The second trainer's Pokemon can defeat the first trainer's Pokemon in both arenas so his strength is $1$. Similarly, the first trainer's Pokemon can not defeat the second trainer's Pokemon in any arena so his strength will be $0$. Hence, only the second trainer will qualify.

**Test case 2:** The second trainer's Pokemon can defeat the first trainer's Pokemon in ground arena so his strength is $1$ and the first trainer's Pokemon can defeat the second trainer's Pokemon in water arena so his strength will also be $1$. Hence both of them will qualify.

**Test case 4:** The maximum strength possible is $4$. There are $3$ trainers with strength $4$:
- Trainer $3$: Trainer $3$'s pokemon has ground power equal to $5$, so, it can defeat all other $4$ pokemons in the ground arena. Thus, the trainer's strength is $4$.
- Trainer $4$: Trainer $4$'s pokemon has ground power equal to $4$. It can beat the pokemons having ground power less than $4$. These belong to trainers $1, 2,$ and $5$. Similarly, it has water power equal to $5$. Thus, it can also beat trainer $3$'s pokemon which has water power $1$. Thus, total strength of this trainer is $4$.
- Trainer $5$: Trainer $5$'s pokemon has water power equal to $6$, so, it can defeat all other $4$ pokemons in the water arena. Thus, the trainer's strength is $4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
3 4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
1 2
2 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
1 2 3
1 4 2
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
5
2 3 5 4 1
4 2 1 5 6
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

[Practice](https://www.codechef.com/problems/PBATTLE)

[Contest: Division 1](https://www.codechef.com/SEP221A/problems/PBATTLE)

[Contest: Division 2](https://www.codechef.com/SEP221B/problems/PBATTLE)

[Contest: Division 3](https://www.codechef.com/SEP221C/problems/PBATTLE)

[Contest: Division 4](https://www.codechef.com/SEP221D/problems/PBATTLE)

***Author:*** [Ayush Rusiya](https://www.codechef.com/users/ayushrusiya47)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1739

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

N Pokemon trainers participate in a tournament. Each of them has one Pokemon, with a power of A_i on land and B_i in the water.

Trainer i can defeat trainer j if A_i \gt A_j or B_i \gt B_j. The strength of a trainer is the number of other trainers this trainer can defeat.

All the values of A_i are distinct, as are the values of B_i. Find the number of trainers with maximum strength.

#
[](#explanation-5)EXPLANATION:

First, note that the maximum possible strength is \leq N-1, since a trainer can only defeat the other N-1 trainers at best.

In fact, the maximum strength will always be exactly N-1.

Proof

Since all the A_i are distinct, consider the trainer with highest A_i value — without loss of generality, less this be A_1.

Now, trainer 1 can beat every other trainer on the ground, and thus has a strength of N-1. So, there is always a trainer with strength N-1, as required.

Now that we know the maximum strength, all that remains is counting: we need to count the number of trainers with strength N-1. Of course, doing this with brute force in \mathcal{O}(N^2) is too slow so we need to be better.

For a trainer to have a strength of N-1, he must be able to defeat every other trainer, either on land or in water.

Suppose we sort the pairs of (A_i, B_i) so that A_1 \lt A_2 \lt \ldots \lt A_N. Now, note that trainer i can surely defeat any trainer j with j \lt i on land, so we don’t have to care about B_j for j \lt i.

So, for trainer i to have a strength of N-1, B_i must be larger than all of B_{i+1}, B_{i+2}, \ldots, B_N — all of these trainers beat trainer i on land, so they *must* lose in the water for i to have a strength of N-1.

Note that the condition on B_i can be rephrased as B_i \gt \max(B_{i+1}, B_{i+2}, \ldots, B_N).

This gives us a rather simple algorithm:

- Sort the pairs (A_i, B_i) in increasing order of A_i.

- Iterate i in decreasing order, from N to 1. Keep a variable mx to denote the current maximum value of B_i.

- At position i, if B_i \gt mx, add 1 to the answer.

- Then, set mx \gets \max(mx, B_i).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per test case.

#
[](#code-7)CODE:

Setter's code (Python)
``# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a=[(a[i],b[i]) for i in range(n)]

    a.sort(key=lambda x:x[0])

    ans=1
    curr_max=a[-1][1]
    for i in range(n-2,-1,-1):
        if a[i][1]>curr_max:
            ans+=1
            curr_max=a[i][1]

    print(ans)
``

Tester's code (C++)
``// Jai Shree Ram

#include<bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
template <class T> using Tree = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
#define ook order_of_key
#define fbo find_by_order

#define rep(i,a,n)     for(int i=a;i<n;i++)
#define ll             long long
#define int            long long
#define pb             push_back
#define all(v)         v.begin(),v.end()
#define endl           "\n"
#define x              first
#define y              second
#define gcd(a,b)       __gcd(a,b)
#define mem1(a)        memset(a,-1,sizeof(a))
#define mem0(a)        memset(a,0,sizeof(a))
#define sz(a)          (int)a.size()
#define pii            pair<int,int>
#define hell           1000000007
#define elasped_time   1.0 * clock() / CLOCKS_PER_SEC

template<typename T1,typename T2>istream& operator>>(istream& in,pair<T1,T2> &a){in>>a.x>>a.y;return in;}
template<typename T1,typename T2>ostream& operator<<(ostream& out,pair<T1,T2> a){out<<a.x<<" "<<a.y;return out;}
template<typename T,typename T1>T maxs(T &a,T1 b){if(b>a)a=b;return a;}
template<typename T,typename T1>T mins(T &a,T1 b){if(b<a)a=b;return a;}

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
                cerr << l << ' ' << r << ' ' << x << '\n';
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
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

int sum = 0;

int solve(){
 		int n = readIntLn(2,1e5);
 		sum += n;
 		assert(sum <= 2e5);
 		vector<int> a = readVectorInt(n,1,1e9);
 		vector<int> b = readVectorInt(n,1,1e9);

 		auto check_distinct = [&](auto a){
 			set<int> st;
 			for(auto i:a)st.insert(i);
 			assert(sz(st) == sz(a));
 		};
 		check_distinct(a);
 		check_distinct(b);

 		vector<int> ord(n);
 		iota(all(ord),0);
 		sort(ord.begin(),ord.end(),[&](auto &i,auto &j){
 			return  a[i] < a[j];
 		});

 		Tree<int> tr;
 		vector<int> res(n);
 		for(int i = n - 1; i >= 0; i--){
 			res[ord[i]] = i + tr.ook(b[ord[i]]);
 			tr.insert(b[ord[i]]);
 		}
 		int mx = *max_element(all(res));
 		cout << count(all(res),mx) << endl;
 return 0;
}
signed main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    #ifdef SIEVE
    sieve();
    #endif
    #ifdef NCR
    init();
    #endif
    int t = readIntLn(1,1000);
    while(t--){
        solve();
    }
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [(a[i], b[i]) for i in range(n)]
    c.sort()
    ans, mx = 0, 0
    for i in reversed(range(n)):
        if c[i][1] > mx:
            ans += 1
        mx = max(mx, c[i][1])
    print(ans)
``

</details>
