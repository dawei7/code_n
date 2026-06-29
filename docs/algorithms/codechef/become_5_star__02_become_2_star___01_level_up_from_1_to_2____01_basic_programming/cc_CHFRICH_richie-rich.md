# Richie Rich

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFRICH |
| Difficulty Rating | 878 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [CHFRICH](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CHFRICH) |

---

## Problem Statement

Chef aims to be the richest person in Chefland by his new restaurant franchise. Currently, his assets are worth $A$ billion dollars and have no liabilities. He aims to increase his assets by $X$ billion dollars per year.

Also, all the richest people in Chefland are not planning to grow and maintain their current worth.

To be the richest person in Chefland, he needs to be worth at least $B$ billion dollars. How many years will it take Chef to reach his goal if his value increases by $X$ billion dollars each year?

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, three integers $A$, $B$, $X$.

### Output
For each test case, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 21\ 000$
- $100 \leq A < B \leq 200$
- $1 \leq X \leq 50$
- $X$ divides $B - A$

### Subtasks
**Subtask #1 (100 points):** Original constraints

---

## Examples

**Example 1**

**Input**

```text
3
100 200 10
111 199 11
190 200 10
```

**Output**

```text
10
8
1
```

**Explanation**

**Test Case $1$:** Chef needs to increase his worth by $200 - 100 = 100$ billion dollars and his increment per year being $10$ billion dollars, so it will take him $\frac{100}{10} = 10$ years to do so.

**Test Case $2$:** Chef needs to increase his worth by $199 - 111 = 88$ billion dollars and his increment per year being $11$ billion dollars, so it will take him $\frac{88}{11} = 8$ years to do so.

**Test Case $3$:** Chef needs to increase his worth by $200 - 190 = 10$ billion dollars and his increment per year being $10$ billion dollars, so it will take him $\frac{10}{10} = 1$ year to do so.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 200 10
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
111 199 11
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
190 200 10
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1 ](https://www.codechef.com/LTIME97A/problems/CHFRICH)

[Contest Division 2 ](https://www.codechef.com/LTIME97B/problems/CHFRICH)

[Contest Division 3 ](https://www.codechef.com/LTIME97C/problems/CHFRICH)

[Practice ](https://www.codechef.com/problems/CHFRICH)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [ Felipe Mota ](https://www.codechef.com/users/fmota)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

# DIFFICULTY

Cakewalk

# PREREQUISITES

Maths

# PROBLEM:

Chef aims to be the richest person in Chefland by his new restaurant franchise. Currently, his assets are worth A billion dollars and have no liabilities. He aims to increase his asset by X billion dollars per year.

How much minimum time will it take Chef to be the richest person given he should be worth at least B billion dollars to meet the target.

# QUICK EXPLANATION:

Currently, Chef has A billion dollars and he needs at least B billion dollars to become the richest person. Hence the amount that Chef need is  :

Amt=B-A

Now, every year Chef increases its asset by X billion dollars. Hence the minimum time that Chef needs to increase its asset by Amt billion dollars is:

time = \left \lceil{\frac{Amt}{x}}\right \rceil

This is the minimum time that Chef needs to become the richest person in Chefland.

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS:

Setter
````

Tester
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int a,b,x;
  cin>>a>>b>>x;

  int diff=b-a;

  int ans=diff/x;
  if(diff%x)
    ans++;

  cout<<ans<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}
``

</details>
