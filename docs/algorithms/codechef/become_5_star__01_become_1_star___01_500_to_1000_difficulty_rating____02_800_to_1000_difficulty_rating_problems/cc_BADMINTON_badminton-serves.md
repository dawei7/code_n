# Badminton Serves

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BADMINTON |
| Difficulty Rating | 869 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [BADMINTON](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/BADMINTON) |

---

## Problem Statement

Chef is playing badminton today. The service rules of this singles game of badminton are as follows:
1. The player who starts the game serves from the **right** side of their court.
2. Whenever a player wins a point, they serve next.
3. If the server has won an **even** number of points during a game, then they will serve from the **right** side of the service court for the subsequent point.

Chef will be the player who begins the game.

Given the number of points $P$ obtained by Chef at the end of the game, please determine how many times Chef served from the **right** side of the court.

Please see the sample cases below for explained examples.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line containing one integer $P$, the points obtained by Chef.

---

## Output Format

For each test case, output in a single line the number of times Chef served from the **right** side of the court.

---

## Constraints

- $1 \leq T \leq 10^3$
- $0 \leq P \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
2
9
53
746
```

**Output**

```text
2
5
27
374
```

**Explanation**

**Test case $1$**: Chef obtained $2$ points at the end of the game. This means he served two times from the right side of the court, once when his score was $0$ and once again when his score was $2$.

**Test case $2$**: Chef obtained $9$ points at the end of the game. This means he served $5$ times from the right side of the court. The points when he had to serve from right were: $0,2,4,6,8$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
9
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
53
```

**Output for this case**

```text
27
```



#### Test case 4

**Input for this case**

```text
746
```

**Output for this case**

```text
374
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[https://www.codechef.com/START24C/problems/BADMINTON](https://www.codechef.com/START24C/problems/BADMINTON)

Setter: [Utkarsh Gupta ](https://www.codechef.com/users/utkarsh_25dec)

Tester: [Aryan Chaudhary ](https://www.codechef.com/users/aryanc403)

Editorialist: [Rishabh Gupta ](https://www.codechef.com/users/rishabhdevil)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is playing badminton today. The service rules of this singles game of badminton is as follows:

- The player who starts the match serves from **right** side of their court.

- If the server has won an even number of points during a game, then they shall serve from the **right** side of the service court for the subsequent point.

Chef will be the player who begins the match.

Given the number of points P, obtained by Chef at the end of the game, please determine how many times did the Chef serve from **right** side of the court.

#
[](#explanation-5)EXPLANATION:

For each of the even number less than or equal to P, chef gets to serve once. And the total even numbers \leq P are \lfloor P/2 \rfloor + 1.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

 Setter's Solution
``#include<iostream>
int main(){
    int n,t; std::cin>>t; while(t--){
	std::cin>>n;
	std::cout<<(n/2)+1<<'\n';
    }
    return 0;
}
``

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;

int main()
{
   ios_base::sync_with_stdio(0);
   cin.tie(0); cout.tie(0);
   #ifndef ONLINE_JUDGE
   freopen("input.txt" , "r" , stdin) ;
   freopen("output.txt" , "w" , stdout) ;
   #endif

   int t;
   cin >> t ;
   while(t--){
       int n;
       cin>>n;
       cout<<1 +  n/2<<endl ;
   }

   return 0;

}
``

</details>
