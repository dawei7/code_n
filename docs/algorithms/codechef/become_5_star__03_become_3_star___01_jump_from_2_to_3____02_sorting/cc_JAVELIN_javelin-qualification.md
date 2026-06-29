# Javelin Qualification

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JAVELIN |
| Difficulty Rating | 1538 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [JAVELIN](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/JAVELIN) |

---

## Problem Statement

There are $N$ players with IDs from $1$ to $N$, who are participating in the Javelin throw competition which has two rounds. The first is the qualification round, followed by the final round. The qualification round has gotten over, and you are given the longest distance that each of the $N$ players has thrown as $A_1, A_2, \ldots, A_N$. Now, the selection process for the final round happens in the following two steps:

1) If the longest throw of a player in the qualification round is greater than or equal to the qualification mark of $M$ cm, they qualify for the final round.

2) If after step $1$, less than $X$ players have qualified for the finals, the remaining spots are filled by players who have thrown the maximum distance among the players who have not qualified yet.

You are given the best throws of the $N$ players in the qualification round $A_1, A_2, \ldots, A_N$ and the integers $M$ and $X$. Print the list of the players who will qualify for the finals in increasing order of their IDs.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N, M, X$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

---

## Output Format

- For each test case, print a single line containing $K + 1$ space-separated integers, where $K$ is the number of players qualified.
- First, print the integer $K$, then followed by a space, print $K$ space-separated integers $ID_1, ID_2, \dots, ID_K$ where $ID_i$ denotes the players' *ID* who qualified for the finals.
- You have to print the IDs of the qualified players in increasing order.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq X \leq N \leq 30$
- $5000 \leq A_i \leq 8000$
- $7000 \leq M \leq 8000$
- All $A_i$-s are distinct

---

## Examples

**Example 1**

**Input**

```text
3
3 8000 2
5000 5001 5002
3 5000 2
7999 7998 8000
4 6000 3
5999 5998 6000 6001
```

**Output**

```text
2 2 3
3 1 2 3
3 1 3 4
```

**Explanation**

**Test Case $1$:** Since no player crosses the qualification mark, they are chosen based on the distance thrown. So player $3$ who has thrown the maximum distance gets selected followed by the player $2$. Now since we have got the required number of players, player $1$ isn't selected.

**Test Case $2$:** Since all the players cross the qualification mark, they all are selected.

**Test Case $3$:** The player $3$ and player $4$ cross the qualification mark. So for the third and final spot in the final, the player $1$ is selected since he has the maximum distance thrown amongst the remaining two players.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 8000 2
5000 5001 5002
```

**Output for this case**

```text
2 2 3
```



#### Test case 2

**Input for this case**

```text
3 5000 2
7999 7998 8000
```

**Output for this case**

```text
3 1 2 3
```



#### Test case 3

**Input for this case**

```text
4 6000 3
5999 5998 6000 6001
```

**Output for this case**

```text
3 1 3 4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/JAVELIN)

[Contest: Division 3](https://www.codechef.com/START8C/problems/JAVELIN)

[Contest: Division 2](https://www.codechef.com/START8B/problems/JAVELIN)

[Contest: Division 1](https://www.codechef.com/START8A/problems/JAVELIN)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester :** [Radoslav Dimitrov](https://www.codechef.com/users/radoslav_adm)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N players with IDs from 1 to N, who are participating in the Javelin throw competition which has two rounds. The first is the qualification round, followed by the final round. The qualification round has gotten over, and you are given the longest distance that each of the N players has thrown as A_1, A_2, \ldots, A_N. Now, the selection process for the final round happens in the following two steps:

-

If the longest throw of a player in the qualification round is greater than or equal to the qualification mark of M cm, they qualify for the final round.

-

If after step 1, less than X players have qualified for the finals, the remaining spots are filled by players who have thrown the maximum distance among the players who have not qualified yet.

You are given the best throws of the N players in the qualification round A_1, A_2, \ldots, A_N and the integers M and X. Print the list of the players who will qualify for the finals in increasing order of their IDs.

#
[](#explanation-5)EXPLANATION:

The problem is straightforward, we need to do as the problem statement says. Simply sort the array in decreasing order of the distance remembering the ID of the players with their distance.

Now after that, start traversing the array there are two conditions when a player can be qualified for the finals:

-

If the player’s throw distance is more than the qualification mark M, he simply qualifies for the final.

-

If the player’s throw distance is less than the qualification mark M but the number of players in the final is less than X, the player qualifies for the final.

We can simply push the IDs of the players that are qualified for the finals. Since we need IDs of the qualified players in increasing order, we can sort the array which contains the qualified players ID and print this list.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N*log(N)) per test case

#
[](#solutions-7)SOLUTIONS:

Author
``#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define rb pop_back
#define ti tuple<int, int, int>
#define pii pair<int, int>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define mp make_pair
#define mt make_tuple

using namespace std;

const int maxt = 1000;
const string newln = "\n", space = " ";
const int minm = 5000, maxm = 8000;

int main()
{
    int t, n, m, x, y;
    cin >> t;
    while(t--){
        cin >> n >> m >> x;
        vector<pii> v;
        for(int i = 0; i < n; i++){
            cin >> y;
            v.pb({y, i + 1});
        }
        sort(v.begin(), v.end(), greater<pii>());
        int cnt = 0;
        vector<int> ans;
        for(pii p : v){
            if(p.first >= m){
                ans.pb(p.second); cnt++;
            }else{
                if(cnt < x){
                    ans.pb(p.second); cnt++;
                }else{
                    break;
                }
            }
        }
        sort(ans.begin(), ans.end());
        int sz = ans.size();
        cout << sz << " ";
        for(int i = 0; i < sz; i++){
            cout << ans[i] << (i == sz - 1 ? newln : space);
        }
    }
}
``

Tester
``def solve_case():
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    with_ids = [(x, i + 1) for i, x in enumerate(a)]

    answer = []
    for v, i in sorted(with_ids, reverse=True):
        if len(answer) < k or v >= m:
            answer.append(i)

    print(len(answer), *sorted(answer))

cases = int(input())
for _ in range(cases):
    solve_case()

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
  int n,m,x;
  cin>>n>>m>>x;

  int a[n];

  vector <int> ans;

  for(int i=0;i<n;i++)
  {
    cin>>a[i];
    if(a[i]>=m)
    {
      ans.push_back(i+1);
      a[i]=-1;
    }
  }

  while(ans.size()<x)
  {
    int idx = 0;
    int fi_idx = 0;

    while(idx<n)
    {
      if(a[idx]>a[fi_idx])
        fi_idx = idx;

      idx++;
    }

    ans.push_back(fi_idx+1);
    a[fi_idx] = -1;
  }

  sort(ans.begin(),ans.end());

  cout<<ans.size()<<" ";

  for(auto itr: ans)
    cout<<itr<<" ";

  cout<<endl;
}

int main()
{
  // freopen("input.txt","r",stdin);
  // freopen("output.txt","w",stdout);

  int t;
  cin>>t;

  while(t--)
    solve();
}

``

</details>
