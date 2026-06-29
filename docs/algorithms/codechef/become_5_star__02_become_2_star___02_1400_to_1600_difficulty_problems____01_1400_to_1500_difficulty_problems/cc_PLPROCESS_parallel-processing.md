# Parallel Processing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PLPROCESS |
| Difficulty Rating | 1425 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [PLPROCESS](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/PLPROCESS) |

---

## Problem Statement

There are $N$ tasks waiting in line to be executed. The execution time for the $i^{th}$ task is $A_i$ seconds.

Chef has **two processors** to execute these $N$ tasks. Both these processors work simultaneously. Each processor executes the assigned tasks one by one.

Chef assigns a **prefix** of these tasks to the first processor and the remaining tasks to the second processor.

For example, if there are $3$ tasks, Chef can do one of the following:
- Assign no task to the first processor. This means, the second processor will execute tasks $1, 2$ and $3$.
- Assign task $1$ to the first processor. This means, the second processor will execute tasks $2$ and $3$.
- Assign tasks $1$ and $2$ to the first processor. This means, the second processor will execute task $3$.
- Assign tasks $1, 2$ and $3$ to the first processor. Thus, second processor would execute no tasks.

Find the **minimum** time in which all the tasks can be executed.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$, the number of tasks waiting to be executed.
- The second line of each test case contains $N$ space separated positive integers $A_1, A_2, \ldots, A_N$ denoting the execution time for each task.

---

## Output Format

For each test case, output in a single line, the minimum time in which all tasks can be executed.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$
- The sum of $N$ over all test cases is not more than $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
4 2 3
6
1 1 1 1 1 1
1
5
```

**Output**

```text
5
3
5
```

**Explanation**

**Test Case 1:** Chef assigns task $1$ to the first processor and tasks $2$ and $3$ to the second processor. The first processor takes $4$ seconds to execute task $1$. The second processor takes $2+3 = 5$ seconds to execute tasks $2$ and $3$. Thus, atleast $5$ seconds are required to execute all tasks.

**Test Case 2:** Chef assigns tasks $1, 2$ and $3$ to the first processor. Processes $4, 5$ ad $6$ are executed by second processor.

**Test Case 3:** Chef assigns task $1$ to the first processor. No task is executed by second processor.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
4 2 3
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
6
1 1 1 1 1 1
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
1
5
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME105A/problems/PLPROCESS)

[Contest Division 2](https://www.codechef.com/LTIME105B/problems/PLPROCESS)

[Contest Division 3](https://www.codechef.com/LTIME105C/problems/PLPROCESS)

[Contest Division 4](https://www.codechef.com/LTIME105D/problems/PLPROCESS)

**Setter:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Prefix Sum

#
[](#problem-4)PROBLEM:

There are N tasks waiting in line to be executed. The execution time for the i^{th} task is A_i seconds.

Chef has **two processors** to execute these N tasks. Both these processors work simultaneously. Each processor executes the assigned tasks one by one.

Chef assigns a **prefix** of these tasks to the first processor and the remaining tasks to the second processor.

#
[](#explanation-5)EXPLANATION:

Suppose there is only one processor so it makes sense that the total amount of time taken to execute N tasks will be a summation of all the times required by every task. Let’s say this value is S, i.e

S = \sum_{i=1}^{N}A

Now, suppose we introduced another processor, and now let’s do as the problem says i.e. assign some prefix to the processor 1 and the remaining task to the processor 2.

Let’s say the time required to complete the task that was given to processor 1 is T_1. Hence the processor 2 will be able to complete the task in S-T_1.

Now since the processors are running in parallel, hence the total time required to complete all tasks will be a maximum of T_1 and S-T_1.

Now the question arises, Which prefix do I need to assign to processor 1?

- It’s quite simple, just assign every possible prefix to the processor 1 and check which prefix assignment is giving us the minimum time to complete all the remaining tasks. You can maintain a prefix sum array to efficiently perform the calculations.

Finally, output the minimum time that you can achieve.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) per test case

#
[](#solutions-7)SOLUTIONS:

Author
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
        int a[n];
        long long int sum = 0;
        for(int i = 0; i<n; i++){
            cin>>a[i];
            sum += a[i];
        }

        long long int ans = sum;
        long long int curr = 0;
        for(int i = 0; i<n-1; i++){
            curr += a[i];
            ans = min(ans, max(curr, sum-curr));
        }
        cout<<ans<<endl;
	}
	return 0;
}

``

Tester
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int n;
  cin>>n;

  int a[n];
  int pref[n];

  for(int i=0;i<n;i++)
  {
    cin>>a[i];
    pref[i] = (i>0)?pref[i-1]+a[i]:a[i];
  }

  int ans = pref[n-1];

  for(int i=0;i<n;i++)
  {
    int rem_sum = pref[n-1]-pref[i];
    rem_sum = max(0ll,rem_sum-pref[i]);
    ans = min(ans,pref[i]+rem_sum);
  }

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
