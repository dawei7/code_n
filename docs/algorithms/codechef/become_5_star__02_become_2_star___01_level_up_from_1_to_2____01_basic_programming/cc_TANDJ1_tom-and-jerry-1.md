# Tom And Jerry 1

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TANDJ1 |
| Difficulty Rating | 1379 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [TANDJ1](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/TANDJ1) |

---

## Problem Statement

There is a grid of size $10^5 \times 10^5$, covered completely in railway tracks. Tom is riding in a train, currently in cell $(a, b)$, and Jerry is tied up in a different cell $(c, d)$, unable to move. The train has no brakes. It shall move exactly $K$ steps, and then its fuel will run out and it shall stop. In one step, the train must move to one of its neighboring cells, sharing a side. Tom can’t move without the train, as the grid is covered in tracks. Can Tom reach Jerry’s cell after exactly $K$ steps?

**Note:** Tom can go back to the same cell multiple times.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, five integers $a, b, c, d, K$.

---

## Output Format

For each testcase, output in a single line "YES" if Tom can reach Jerry's cell in exactly $K$ moves and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq a, b, c, d \leq 10^5$
- $(a, b) \ne (c, d)$
- $1 \leq K \leq 2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 2 2 2
1 1 2 3 4
1 1 1 0 3
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test Case $1$:** A possible sequence of moves is $(1, 1) \to (1, 2) \to (2, 2)$.

**Test Case $2$:** There is a possible sequence in $3$ moves, but not in exactly $4$ moves.

**Test Case $3$:** A possible sequence of moves is $(1, 1) \to (1, 0) \to (0, 0) \to (1, 0)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 2 2 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
1 1 2 3 4
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
1 1 1 0 3
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1 ](https://www.codechef.com/LTIME96A/problems/TANDJ1)

[Contest Division 2 ](https://www.codechef.com/LTIME96B/problems/TANDJ1)

[Contest Division 3 ](https://www.codechef.com/LTIME96C/problems/TANDJ1)

[Practice ](https://www.codechef.com/problems/TANDJ1)

**Setter:** [Daanish Mahajan ](https://www.codechef.com/users/daanish_adm)

**Tester:** [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY

Cakewalk

# PREREQUISITES

Observation

# PROBLEM

Given a grid of size 10^5 \times 10^5, covered completely in railway tracks. Tom is riding the train and he is initially at cell (a,b) and Jerry in cell (c,d) . You need to **determine** if Tom can ride the train in exactly K moves to reach cell (c,d). In one step, the train must move to one of its neighboring cells, sharing a side. Tom can go back to the same cell multiple times

# QUICK EXPLANATION

Tom can reach Jerry in **total minimum moves**  X where X= abs(c-a) + abs(d-b).

- Tom can reach Jerry in exactly X minimum moves, therefore K needs to greater than equal to X.

- Now, if Tom can reach Jerry in exactly X moves then he can also reach Jerry in exactly X+2, X+4, X+6.... moves.

# EXPLANATION

Why minimum moves required to reach Jerry is X where X=abs(c-a)+abs(d-b)?

The path along the column b i.e abs(c-a) and path along the row c i.e abs(d-b) is the minimum path between (a,b) and (c,d). Therefore, X = abs(c-a)+abs(d-b).

If  Tom can reach Jerry in exactly X moves then he can also reach in exactly X+2, X+4, X+6... But why ?

If Tom can reach Jerry in exactly X moves then he can also reach Jerry in X+2, X+4, X+6... If he wants to reach Jerry in exactly Z moves where Z is integer just greater than X, then he would need minimum 2 other cells to reach Jerry. If he requires 2 cells, then he can repeat the path back and forth and that will basically be **even multiple** of 2. Therefore he can reach Jerry in exactly X+Y, where Y is an even multiple of 2.

Let’s take an example to understand better.

- Let (a,b)=(1,1) and (c,d)=(2,4).

- The minimum path is (1,1) ? (1,2) ? (1,3) ? (1,4) ? (2,4). Therefore X=4. Now let’s try another path that needs exaclty Z moves, where Z is number just greater than X. Try it with Z=5, and you’ll see that there is **no such path** to reach (2,4). Now let’s try with Z=6, here we can see that we have multplie paths like :

-
(1,1) ? (1,2) ? (1,3) ? (1,4) ? (1,3) ? (1,4) ? (2,4).

-
(1,1) ? (1,2) ? (1,3) ? (1,4) ? (1,5) ? (1,4) ? (2,4).

-
(1,1) ? (1,2) ? (1,3) ? (2,3) ? (1,3) ? (2,3) ? (2,4).

- Similarly, we can find that there are multiple such paths to reach (2,4) in exactly Z=6 moves.

Hence, given K we need to check if it is greater than equal to X and also if they have the same parity or not, that can be checked using modulo 2 i.e X%2==K%2.

# TIME COMPLEXITY

The time complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxn = 1e5, maxm = 1e5, maxt = 1e5, maxk = 2e5;
const string newln = "\n", space = " ";

int main()
{
    int t; cin >> t;
    int a, b, c, d, k;
    while(t--){
        cin >> a >> b >> c >> d >> k;
        int dist = abs(c - a) + abs(d - b);
        string ans = (k >= dist && (k - dist) % 2 == 0 ? "YeS" : "nO");
        cout << ans << endl;
    }

``

Tester's Solution
``
#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

void solve() {
    ll a, b, c, d, k;
    cin >> a >> b >> c >> d >> k;
    assert(a != c || b != d);
    ll move = abs(a - c) + abs(b - d);
    if(k >= move && k % 2 == move % 2) {
        cout << "YES\n";
    }else {
        cout << "NO\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) solve();
}
``

Editorialist's Solution
``#include<bits/stdc++.h>
using namespace std;

#define int long long int

void solve()
{
  int a, b, c, d, k;
  cin >> a >> b >> c >> d >> k;
  //minimum moves required
  int X = abs(c - a) + abs(d - b);
  // Checking minimum and parity condition
  if (k >= X && k % 2 == X % 2)
  {
    cout << "YES" << endl;
    return;
  }
  cout << "NO" << endl;

}
int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin >> t;

  while (t--)
    solve();

  return 0;
}

``

</details>
