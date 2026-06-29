# Mask Policy

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MASKPOL |
| Difficulty Rating | 1064 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MASKPOL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MASKPOL) |

---

## Problem Statement

A city has been infected by a contagious virus.

In a survey, it was found that $A$ out of the $N$ people living in the city are currently infected.
It has been observed that the only way for a person to get infected is if he comes in contact with an already infected person, and both of them are NOT wearing a mask.

The mayor of the city wants to make a new Mask Policy and find out the minimum number of people that will be required to wear a mask to avoid the further spread of the virus.
Help the mayor in finding this number.

Note: The only aim of the mayor is to stop virus spread, not to mask every infected person.

---

## Input Format

- The first line contains $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $N$ and $A$ - the total number of people living in the city and the number of people already affected by the virus respectively.

---

## Output Format

For each test case, output the minimum number of people that will be required to wear a mask so as to curb the virus spread.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 400$
- $1 \leq A \lt N$

---

## Examples

**Example 1**

**Input**

```text
3
2 1
3 2
3 1
```

**Output**

```text
1
1
1
```

**Explanation**

**Test Case #1**: There is $1$ infected person and $1$ uninfected person. We can ask any of them to wear a mask, and no more infections will occur. Hence the answer is $1$.

**Test Case #2**: There are $2$ infected people and $1$ uninfected person. We can ask the uninfected person to wear a mask, and no more infections will occur. Hence the answer is $1$.

**Test Case #3**: There is $1$ infected person and $2$ uninfected people. We can ask the single infected person to wear a mask, and no more infections will occur. Hence the answer is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3 1
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

[Practice](https://www.codechef.com/problems/MASKPOL)

[Contest: Division 3 ](https://www.codechef.com/COOK137C/problems/MASKPOL)

[Contest: Division 2 ](https://www.codechef.com/COOK137B/problems/MASKPOL)

[Contest: Division 1 ](https://www.codechef.com/COOK137A/problems/MASKPOL)

**Author:** [ Nandeesh Gupta](https://www.codechef.com/users/nandeesh_adm)

**Tester :** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N people living in the city out of which A people are infected. People get infected when they came into contact with an infected person and none of them are wearing the mask.

Your goal is to calculate the minimum number of masks needed to prevent any person from getting infected.

#
[](#explanation-5)EXPLANATION:

There are two ways to stop the spread of further infection:

- All the infected people wear a mask.

- All the non-infected people wear a mask.

Since our goal is to minimize the number of masks. Hence the answer will be the minimum of the above two cases.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case

#
[](#solutions-7)SOLUTIONS:

Author's Solution
``#include <iostream>
using namespace std;

int main() {
    int t; cin>>t;
    while(t--){
        int n,a; cin>>n>>a;
        cout<<min(a,n-a)<<'\n';
    }
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
        int n, a;
        cin >> n >> a;
        cout << min(a, n - a) << '\n';
    }
    return 0;
}

``

Editorialist Solution
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
    int n,a;
    cin>>n>>a;

    cout<<min(n-a,a)<<"\n";
}

int main()
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
