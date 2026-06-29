# Good Program

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NIBBLE |
| Difficulty Rating | 593 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [NIBBLE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NIBBLE) |

---

## Problem Statement

In computing, the collection of **four bits** is called a **nibble**.

Chef defines a program as:
- **Good**, if it takes exactly $X$ nibbles of memory, where $X$ is a positive integer.
- **Not Good**, otherwise.

Given a program which takes $N$ **bits** of memory, determine whether it is **Good** or **Not Good**.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first and only line of each test case contains a single integer $N$, the number of bits taken by the program.

---

## Output Format

For each test case, output $\texttt{Good}$ or $\texttt{Not Good}$ in a single line.
You may print each character of $\texttt{Good}$ or $\texttt{Not Good}$ in uppercase or lowercase (for example, $\texttt{GoOd}$, $\texttt{GOOD}$, $\texttt{good}$ will be considered identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
8
17
52
3
```

**Output**

```text
Good
Not Good
Good
Not Good
```

**Explanation**

**Test case 1:** The program requires $8$ bits of memory. This is equivalent to $\frac{8}{4} = 2$ nibbles. Since $2$ is an integer, this program is good.

**Test case 2:** The program requires $17$ bits of memory. This is equivalent to $\frac{17}{4} = 4.25$ nibbles. Since $4.25$ is not an integer, this program is not good.

**Test case 3:** The program requires $52$ bits of memory. This is equivalent to $\frac{52}{4} = 13$ nibbles. Since $13$ is an integer, this program is good.

**Test case 4:** The program requires $3$ bits of memory. This is equivalent to $\frac{3}{4} = 0.75$ nibbles. Since $0.75$ is not an integer, this program is not good.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8
```

**Output for this case**

```text
Good
```



#### Test case 2

**Input for this case**

```text
17
```

**Output for this case**

```text
Not Good
```



#### Test case 3

**Input for this case**

```text
52
```

**Output for this case**

```text
Good
```



#### Test case 4

**Input for this case**

```text
3
```

**Output for this case**

```text
Not Good
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME105A/problems/NIBBLE)

[Contest Division 2](https://www.codechef.com/LTIME105B/problems/NIBBLE)

[Contest Division 3](https://www.codechef.com/LTIME105C/problems/NIBBLE)

[Contest Division 4](https://www.codechef.com/LTIME105D/problems/NIBBLE)

**Setter:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#problem-3)PROBLEM:

In computing, the collection of **four bits** is called a **nibble**.

Chef defines a program as:

-
**Good**, if it takes exactly X nibbles of memory, where X is a positive integer.

-
**Not Good**, otherwise.

Given a program that takes N **bits** of memory, determine whether it is **Good** or **Not Good**.

#
[](#explanation-4)EXPLANATION:

I have two questions for you:

-
N is multiple of 4.

-
N is not a multiple of 4

Can you guess what happens in the first case?

- As N is a multiple of 4, there won’t be any remainder left and hence it requires exactly some X nibbles. Such types of programs are **Good**.

Second Case?

- In this case, there will be some remainder left which will require a nibble but it won’t be able to fill the nibble completely. Hence such types of programs are **Not Good**.

You can print as required by the problem.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1) per test case.

#
[](#solutions-6)SOLUTIONS:

Setter
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
        if(n%4==0) cout<<"Good";
        else cout<<"Not Good";
        cout<<endl;
    }
	return 0;
}

``

Tester
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
  int n;
  cin>>n;

  cout<<((n%4==0)?"Good":"Not Good")<<"\n";
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
