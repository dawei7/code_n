# Count the Notebooks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOTEBOOK |
| Difficulty Rating | 563 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [NOTEBOOK](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NOTEBOOK) |

---

## Problem Statement

You know that $1$ kg of pulp can be used to make $1000$ pages and $1$ notebook consists of $100$ pages.

Suppose a notebook factory receives $N$ kg of pulp, how many notebooks can be made from that?

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single integer $N$ - the weight of the pulp the factory has (in kgs).

---

## Output Format

For each test case, output the number of notebooks that can be made using $N$ kgs of pulp.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
1
100
50
```

**Output**

```text
10
1000
500
```

**Explanation**

**Test case-1:** $1$ kg of pulp can be used to make $1000$ pages which can be used to make $10$ notebooks.

**Test case-2:** $100$ kg of pulp can be used to make $100000$ pages which can be used to make $1000$ notebooks.

**Test case-3:** $50$ kg of pulp can be used to make $50000$ pages which can be used to make $500$ notebooks.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
100
```

**Output for this case**

```text
1000
```



#### Test case 3

**Input for this case**

```text
50
```

**Output for this case**

```text
500
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START26A/problems/NOTEBOOK)

[Contest Division 2](https://www.codechef.com/START26B/problems/NOTEBOOK)

[Contest Division 3](https://www.codechef.com/START26C/problems/NOTEBOOK)

[Contest Division 4](https://www.codechef.com/START26D/problems/NOTEBOOK)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You know that 1 kg of pulp can be used to make 1000 pages and 1 notebook consists of 100 pages.

Suppose a notebook factory receives N kg of pulp, how many notebooks can be made from that?

#
[](#explanation-5)EXPLANATION:

We are given that 1 notebook contains 100 pages.

Thus, from 1000 pages, we can make \frac{1000}{10} = 10 notebooks.

We are also given that 1 kg of pulp can make 1000 pages. Since 1000 pages can make 10 notebooks, we can make 10 notebooks from 1 kg of pulp.

**Conclusion:** From 1 kg pulp, we can make 10 notebooks. Thus, from N kg pulp, we can make 10 \cdot N notebooks.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define db double
#define el "\n"
#define ld long double
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T=1;
    cin >> T;
    while(T--){

        int n;
        cin>>n;

        cout<<10*n<<'\n';
    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}
``

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    cout<<10*n<<endl;
	}
	return 0;
}
``

</details>
