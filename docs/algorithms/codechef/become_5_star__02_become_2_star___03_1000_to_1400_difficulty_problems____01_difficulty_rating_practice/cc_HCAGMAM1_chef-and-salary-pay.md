# Chef And Salary Pay

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HCAGMAM1 |
| Difficulty Rating | 1269 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [HCAGMAM1](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/HCAGMAM1) |

---

## Problem Statement

Given the schedule of Chef for $30$ days (A binary string of length $30$ where `'0'` denotes that Chef was on leave and `'1'` denotes Chef was working on that day). Chef gets $X-$ Rs for every day he worked. As working continuously for a long time is hectic so Company introduced the following policy to give a bonus to its employees.

The company will check the longest streak for which an employee has worked and will award $Y-$ Rs for every day of that streak as a bonus. Calculate the salary received by Chef (including the bonus).

**Note:** Rs represents the currency of Chefland, and if there are two or more longest streaks of the same length, only one is counted for the bonus.

---

## Input Format

- The first line contains an integer $T$ denoting the number of test cases. The $T$ test cases then follow.
- The first line of each test case contains $X$ and $Y$.
- Second line contains a binary string (i.e it contains only `‘0’` / `‘1’`), where `'0'` denotes that Chef was on leave and `'1'` denotes Chef was working on that day.

---

## Output Format

- For each testcase, output in a single line answer to the problem. i.e The salary received by Chef (including the bonus).

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X \leq 999$
- $1 \leq Y \leq 999$
- $|S| = 30$

---

## Examples

**Example 1**

**Input**

```text
3
6 3
111100110101100000101100011111
8 2
111010111101001010100100111101
5 6
011101010100101000001101000010
```

**Output**

```text
117
152
78
```

**Explanation**

**Testcase $1$:** Chef's actual pay comes out $17 \cdot 6 = 102-$ Rs and the length of longest continuous working streak comes out $5$ (the last $5$ working days), so bonus reward becomes $5 \cdot 3 = 15-$ Rs. Hence Chef's salary comes out to be $102 + 15 = 117-$ Rs.

**Testcase $2$:** Chef's actual pay comes out $144-$ Rs and the length of longest continuous working streak comes out $4$ (here there are multiple occurrences of the longest working streak, so company selects any one of them), so bonus reward becomes $8-$ Rs. Hence Chef's salary comes out to be $152-$ Rs.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 3
111100110101100000101100011111
```

**Output for this case**

```text
117
```



#### Test case 2

**Input for this case**

```text
8 2
111010111101001010100100111101
```

**Output for this case**

```text
152
```



#### Test case 3

**Input for this case**

```text
5 6
011101010100101000001101000010
```

**Output for this case**

```text
78
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/HCAGMAM1)

[Div1](https://www.codechef.com/START16A/problems/HCAGMAM1)

[Div2](https://www.codechef.com/START16B/problems/HCAGMAM1)

[Div3](https://www.codechef.com/START16C/problems/HCAGMAM1)

**Setter:**  [ Vasu](https://www.codechef.com/users/tm_sky11)

**Tester:**  [ Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

##
[](#difficulty-2)DIFFICULTY:

CAKEWALK

##
[](#prerequisites-3)PREREQUISITES:

None

##
[](#problem-4)PROBLEM:

The schedule of Chef’s job is given by a string S with length 30. S_i = 1 means that chef has worked on that day and S_i=0 means that chef hasn’t worked on that day. Also, Y Rs  bonus will be given in everday on the longest consecutive streak of days that chef has worked (if multiple longest streaks are posssible only one such streak is selected for bonus). We need to find the total salary of chef on that month.

##
[](#explanation-5)EXPLANATION:

-

Let tot be the total number of ones (working days) in S.

-

Let us also find max where max is the maximum length of consecutive ones in S.

-

This can be simply done by looping over the string S, and we keep track of the number of consecutive ones ending at index i, for all 1 \leq i \leq N. The maximum over all these values is equal to max.

-

The total salary will then equal to tot \cdot X + max \cdot Y.

##
[](#time-complexity-6)TIME COMPLEXITY:

O(length(S)) for each testcase.

##
[](#solution-7)SOLUTION:

Editorialist's solution
``

``

Setter's solution
``#include<bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{
    ll t;
    cin>>t;

    while(t--)
    {
        ll x,y;
        cin>>x>>y;

        string s;
        cin>>s;

        ll countd=0;
        ll maxx=0;

        ll count=0;

        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='1')
            {
                countd++;
                count++;
            }
            else
            {
                count=0;
            }

            maxx=max(maxx,count);
        }

        cout<<(countd*x)+(maxx*y)<<endl;
    }
}

``

Tester's solution
``#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  int t;
  cin>>t;
  while(t--){
    int x, y;
    cin>>x>>y;
    string s;
    cin>>s;
    int n = s.size();
    int mx = 0;
    int temp = 0;
    int ans = 0;
    for(int i = 0; i < n; i++){
      if(s[i] == '1'){
        temp++;
        ans += x;
      }else{
        temp = 0;
      }
      mx = max(mx, temp);
    }
    ans += mx * y;
    cout<<ans<<"\n";
  }
  return 0;
}

``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
