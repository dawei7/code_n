# Chef and Spells

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFSPL |
| Difficulty Rating | 965 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [CHFSPL](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CHFSPL) |

---

## Problem Statement

Chef has three spells. Their powers are $A$, $B$, and $C$ respectively. Initially, Chef has $0$ hit points, and if he uses a spell with power $P$, then his number of hit points increases by $P$.

Before going to sleep, Chef wants to use exactly two spells out of these three. Find the maximum number of hit points Chef can have after using the spells.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $A$, $B$, and $C$.

---

## Output Format

For each test case, print a single line containing one integer — the maximum number of hit points.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A, B, C \leq 10^8$

---

## Examples

**Example 1**

**Input**

```text
2
4 2 8
10 14 18
```

**Output**

```text
12
32
```

**Explanation**

**Example case 1:** Chef has three possible options:
- Use the first and second spell and have $4 + 2 = 6$ hitpoints.
- Use the second and third spell and have $2 + 8 = 10$ hitpoints.
- Use the first and third spell and have $4 + 8 = 12$ hitpoints.

Chef should choose the third option and use the spells with power $4$ and $8$ to have $12$ hitpoints.

**Example case 2:** Chef should use the spells with power $14$ and $18$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 8
```

**Output for this case**

```text
12
```



#### Test case 2

**Input for this case**

```text
10 14 18
```

**Output for this case**

```text
32
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice ](https://www.codechef.com/problems/CHFSPL)

[Contest: Division 3 ](https://www.codechef.com/LTIME98C/problems/CHFSPL)

[Contest: Division 2 ](https://www.codechef.com/LTIME98B/problems/CHFSPL)

[Contest: Division 1 ](https://www.codechef.com/LTIME98A/problems/CHFSPL)

**Author:** [Souradeep](https://www.codechef.com/users/souradeep_adm)

**Tester :** [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Greedy

# PROBLEM:

Chef has three spells. Their powers are A, B, and C respectively. Initially, Chef has 0 hit points, and if Chef uses a spell with power P, then his number of hit points increases by P.

Before going to sleep, Chef wants to use exactly two spells out of these three. Find the maximum number of hit points Chef can have after using the spells.

# EXPLANATION:

Since our goal is to maximize the number of hit points, it is optimal to use those spells with maximum powers. As we need to take exactly two spells, just take the maximum and second maximum power spell.

In another way, our answer is just a maximum of [A+B, B+C, C+A]

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS:

Author
``import java.util.*;
import java.lang.*;
import java.io.*;
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner sc=new Scanner(System.in);
	   // BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	    int t=1;
	    t=sc.nextInt();
	    //int t=Integer.parseInt(br.readLine());
	    while(--t>=0){
	        int x=sc.nextInt();
	        int y=sc.nextInt();
	        int z=sc.nextInt();
	        int g=Math.max(Math.max(x+y,y+z),x+z);
	        System.out.println(g);

	    }

	}
}
``

Tester
``
#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) {
        int a, b, c;
        cin >> a >> b >> c;
        cout << max({a + b, b + c, c + a}) << '\n';
    }
}
``

Editorialist
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
	int a[3];
	cin>>a[0]>>a[1]>>a[2];

	sort(a,a+3);

	cout<<(a[2]+a[1])<<"\n";
}

int main()
{

  // freopen("input.txt","r",stdin);
  // freopen("output.txt","w",stdout);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

``

</details>
