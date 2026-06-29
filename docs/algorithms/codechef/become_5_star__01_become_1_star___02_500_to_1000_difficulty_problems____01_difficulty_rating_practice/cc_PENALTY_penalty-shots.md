# Penalty Shots

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PENALTY |
| Difficulty Rating | 925 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [PENALTY](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/PENALTY) |

---

## Problem Statement

It's the soccer match finals in Chefland and as always it has reached the penalty shootouts.
Each team is given $5$ shots to make and the team scoring a goal on the maximum number of shots wins the game. If both the teams' scores are equal, then the game is considered a draw and we would have $2$ champions.

Given ten integers $A_1, A_2, \ldots, A_{10}$, where the odd indexed integers($A_1, A_3,$ $A_5,$ $A_7, A_9$) represent the outcome of the shots made by team $1$ and even indexed integers($A_2, A_4, A_6, A_8, A_{10}$) represent the outcome of the shots made by team $2$ (here $A_i = 1$ indicates that it's a goal and $A_i = 0$ indicates a miss), determine the winner or find if the game ends in a draw.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains ten space-separated integers $A_1, A_2, \ldots, A_{10}$.

---

## Output Format

For each test case, print a single line containing one integer - $0$ if the game ends in a draw or $1$ if the first team wins or $2$ if the second team wins.

---

## Constraints

- $1 \leq T \leq 1024$
- $0 \leq A_i \leq 1$

---

## Examples

**Example 1**

**Input**

```text
4
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
1 0 1 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 0
```

**Output**

```text
0
2
1
1
```

**Explanation**

**Test case $1$:** No team scores any goal, so the game ends in a draw.

**Test case $2$:** The second team is able to score in their final shot, while the first team has scored 0 goals and hence the second team wins.

**Test case $3$:** The first team is successfully able to make their first $2$ shots count and whereas the second team has not scored any goals. Therefore the first team wins.

**Test case $4$:** Team $2$ misses their final shot and hence team $1$ wins the game with the final score of $5 - 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 0 0 0 0 0 0 0 0 0
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
0 0 0 0 0 0 0 0 0 1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
1 0 1 0 0 0 0 0 0 0
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
1 1 1 1 1 1 1 1 1 0
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice ](https://www.codechef.com/problems/PENALTY)

[Contest: Division 3 ](https://www.codechef.com/START8C/problems/PENALTY)

[Contest: Division 2 ](https://www.codechef.com/START8B/problems/PENALTY)

[Contest: Division 1 ](https://www.codechef.com/START8A/problems/PENALTY)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester :** [Radoslav Dimitrov](https://www.codechef.com/users/radoslav_adm)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given ten integers A_1, A_2, \ldots, A_{10}, where the odd indexed integers(A_1, A_3, A_5, A_7, A_9) represent the outcome of the shots made by team 1 and even indexed integers(A_2, A_4, A_6, A_8, A_{10}) represent the outcome of the shots made by team 2 (here A_i = 1 indicates that it’s a goal and A_i = 0 indicates a miss), determine the winner or find if the game ends in a draw.

#
[](#explanation-5)EXPLANATION:

We can simply count the number of goals for each team and then we can easily determine the winner (or the game ends in a draw).

How to count the number of goals for each team?

-

Simply do as the problem statement says. If the shot number is odd and there is a goal in this shot we can increment the count of goals of Team 1.

-

Similarly, if the shot number is even and there is a goal in this shot we can increment the count of goals of Team 2.

Finally, check which team has more goals and output that team. If the number of goals is the same output 0 which means the game ended in a draw.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case

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

const int maxt = 1024;
const string newln = "\n", space = " ";

int main()
{
    int t; cin >> t;
    while(t--){
        int c[2]; c[0] = c[1] = 0;
        for(int i = 0; i < 10; i++){
            int x; cin >> x;
            c[i & 1] += x;
        }
        int ans = 0;
        if(c[0] > c[1])ans = 1;
        else if(c[0] < c[1]) ans = 2;
        cout << ans << endl;
    }
}
``

Tester
``def solve_case():
    x = [int(x) for x in input().split()]

    balanace = 0
    for i, x in enumerate(x):
        if i & 1:
            balanace += x
        else:
            balanace -= x

    if balanace == 0:
        print(0)
    elif balanace < 0:
        print(1)
    else:
        print(2)

cases = int(input())
for _ in range(cases):
    solve_case()

``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
  int a[10];

  for(int i=0;i<10;i++)
    cin>>a[i];

  int player_a = 0;
  int player_b = 0;

  for(int i=0;i<10;i++)
  {
    if(a[i]==1)
    {
      if(i%2==0)
        player_a++;
      else
        player_b++;
    }
  }

  if(player_b==player_a)
    cout<<0<<endl;
  else if(player_a>player_b)
    cout<<1<<endl;
  else
    cout<<2<<endl;
}

int main()
{

  int t;
  cin>>t;

  while(t--)
    solve();
}

``

</details>
