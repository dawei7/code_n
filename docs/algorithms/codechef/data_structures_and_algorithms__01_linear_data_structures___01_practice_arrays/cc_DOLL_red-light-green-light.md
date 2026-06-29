# Red Light, Green Light

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DOLL |
| Difficulty Rating | 984 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [DOLL](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/DOLL) |

---

## Problem Statement

*“You won’t get caught if you hide behind someone.”*

Sang-Woo advises Gi-Hun to hide behind someone to avoid getting shot.

Gi-Hun follows Sang-Woo's advice and hides behind Ali, who saved his life earlier. Gi-Hun and Ali both have the same height, $K$. Many players saw this trick and also started hiding behind Ali.

Now, there are $N$ players standing *between* Gi-Hun and Ali in a straight line, with the $i^{\text{th}}$ player having height $H_i$. Gi-Hun wants to know the minimum number of players who need to get shot so that Ali is visible in his line of sight.

**Note:**
* Line of sight is a straight line drawn between the topmost point of two objects. Ali is visible to Gi-Hun if nobody between them crosses this line.
* Even if there are some players who have the same height as that of Gi-Hun and Ali, Ali will be visible in Gi-Hun's line of sight.
* Gi-Hun and Ali have the same height.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$, denoting the total number of players between Gi-Hun and Ali and the height of both of them respectively.
- The second line of each test case contains $N$ space-separated integers, denoting the heights of the players between Gi-Hun and Ali.

---

## Output Format

For each test case, output in a single line the minimum number of players who need to get shot so that Ali is visible in Gi-Hun's line of sight.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq 10^6$
- $1 \leq H_i \leq 10^6$ for every $1 \leq i \leq N$.
- The sum of $N$ across all test cases does not exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4 10
2 13 4 16
5 8
9 3 8 8 4
4 6
1 2 3 4
```

**Output**

```text
2
1
0
```

**Explanation**

**Test Case 1:** Gi-Hun and Ali have height $10$. For Ali to be visible to Gi-Hun, the second person (with height $13$) and the fourth person (with height $16$) need to get shot. Hence, the minimum number of players who need to get shot is $2$.

**Test Case 2:** Gi-Hun and Ali have height $8$. For Ali to be visible to Gi-Hun, the first person (with height $9$) needs to get shot. Hence, the minimum number of players who need to get shot is $1$.

**Test Case 3:** Nobody needs to get shot because everyone is shorter than Gi-Hun and Ali.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 10
2 13 4 16
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 8
9 3 8 8 4
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4 6
1 2 3 4
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-red-light-green-lighthttpswwwcodechefcominfi21bproblemsdoll-1)PROBLEM LINK: [ Red Light, Green Light](https://www.codechef.com/INFI21B/problems/DOLL)

***Setter:***  [ Reyaan Jagnani](https://www.codechef.com/users/reyaan44)

***Editorialist:***   [Arpan Gupta](https://www.codechef.com/users/arpan4775)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#prerequisites-3)PREREQUISITES:

Arrays

#
[](#problem-4)PROBLEM:

Gi-Hun and Ali both have a height K and there are N people standing between these two with height A_i. A line of sight is a straight line drawn between the topmost point of two objects. Find the minimum number of players that need to be removed such that there is no other player blocking the line of sight between Gi-Hun and Ali. Players having the same height as of Gi-Hun and Ali don’t block the line of sight.

#
[](#explanation-5)EXPLANATION:

Since both Gi-Hun and Ali have the same height, therefore all players having a height greater than K will block the line of sight and needs to be removed.

So for an i_{th} person, if the height is greater than K, we will eliminate this person.

Time Complexity: O(n)

Space Complexity: O(n)

#
[](#solutions-6)SOLUTIONS:

Setter's Solution(C++)
``#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        int arr[n];
        int ans = 0;
        for(int i=0; i<n; i++)
        {
            cin>>arr[i];
        }
        for(int i=0; i<n; i++)
        {
            if(arr[i]>k) ans++;
        }
        cout<<ans<<endl;
    }
    return 0;
}
``

Setter's Solution(Python)
``T=int(input())
for _ in range(T):
    N,K=list(map(int,input().split()))
    A=list(map(int,input().split()))
    ans=0
    for i in range(N):
        if (A[i]>K):
            ans=ans+1

    print(ans)
``

For doubts, please leave them in the comment section, I’ll address them.

</details>
