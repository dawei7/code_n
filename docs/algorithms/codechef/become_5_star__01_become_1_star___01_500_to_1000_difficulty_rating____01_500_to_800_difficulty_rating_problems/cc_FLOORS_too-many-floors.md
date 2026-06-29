# Too many Floors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLOORS |
| Difficulty Rating | 717 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [FLOORS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOORS) |

---

## Problem Statement

Chef and Chefina are residing in a hotel.

There are $10$ floors in the hotel and each floor consists of $10$ rooms.

- Floor $1$ consists of room numbers $1$ to $10$.
- Floor $2$ consists of room numbers $11$ to $20$.
$\ldots$
- Floor $i$ consists of room numbers $10 \cdot (i-1) + 1$ to $10 \cdot i$.

You know that Chef's room number is $X$ while Chefina's Room number is $Y$.
If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X, Y$, the room numbers of Chef and Chefina respectively.

---

## Output Format

For each test case, output the number of floors Chef needs to travel to reach Chefina's room.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 100$
- $X \neq Y$

---

## Examples

**Example 1**

**Input**

```text
4
1 100
42 50
53 30
81 80
```

**Output**

```text
9
0
3
1
```

**Explanation**

**Test Case $1$:** Since Room $1$ is on $1^{st}$ floor and Room $100$ is on $10^{th}$ floor, Chef needs to climb $9$ floors to reach Chefina's Room.

**Test Case $2$:** Since Room $42$ is on $5^{th}$ floor and Room $50$ is also on $5^{th}$ floor, Chef does not need to climb any floor.

**Test Case $3$:** Since Room $53$ is on $6^{th}$ floor and Room $30$ is on $3^{rd}$ floor, Chef needs to go down $3$ floors to reach Chefina's Room.

**Test Case $4$:** Since Room $81$ is on $9^{th}$ floor and Room $80$ is on $8^{th}$ floor, Chef needs to go down $1$ floors to reach Chefina's Room.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 100
```

**Output for this case**

```text
9
```



#### Test case 2

**Input for this case**

```text
42 50
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
53 30
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
81 80
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

[Contest Division 1](https://www.codechef.com/LTIME109A/problems/FLOORS)

[Contest Division 2](https://www.codechef.com/LTIME109B/problems/FLOORS)

[Contest Division 3](https://www.codechef.com/LTIME109C/problems/FLOORS)

[Contest Division 4](https://www.codechef.com/LTIME109D/problems/FLOORS)

**Setter:** [utkarsh_adm](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

717

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef and Chefina are in a hotel where each of the 10 floors has 10 rooms. Chef’s room is X and Chefina’s room is Y. We have the output the difference in floors between Chef and Chefina

#
[](#explanation-5)EXPLANATION:

Note that the rooms are numbered sequentially from 1 to 10 on the 1st floor, 11 to 20 on the 2nd floor and so on.

Hint 1

Given the room numbers X and Y, we need to be able to identify their floor numbers. What does the room number sequence from [10 * (i - 1) + 1] to [10 * i] tell us?

Hint 2

How do we identify the floors that Chef and Chefina are staying on?

Hint 2a

Given any room number - we know that it lies between [10 * (i - 1) + 1] to [10 * i] for some i. We now need to find what that ‘i’ is - that will give us the floor number.

Hint 2b

If we divide the room number by 10, what will that give us? A number between [(i - 1) + 1/10] and [ i ].

Hint 2c

If we round up the above division to the nearest integer, [ (i - 1) + 1/10] will round up to [(i - 1) + 1] = [ i ].

Hence we will get the floor number. Note that this is true for any of the rooms in that floor. For eg. take the 6th room - [10 * (i-1) + 6]. When you divide it by 10, we get [ (i-1) + 6/10 ], and rounding this up, we get [ (i-1) + 1 ] = [ i ] again.

Hint 3

What do we do after finding their floors?

Hint 3a

Now we just need to calculate the floor numbers for both Chef and Chefina and subtract them. However, is that sufficient or are we missing something?

Hint 3b

If we just output (Chef’s floor - Chefina’’s floor), we are making a mistake. What is the mistake?

Hint 3c

We don’t know whether Chef is on a higher floor or Chefina

Hint 3d

Consider the case when Chef is in room 45, and Chefina is in room 65. We would be outputting -2. But the answer should actually be 2. So we should take the *absolute difference* between their floors.

Hint 4

Full Solution:

Hint 4a

Chef’s floor number is math.ceil [X/10] and Chefina’s floor number is math.ceil [Y/10]

Hint 4b

We need to output the absolute value of the difference in their floors - i.e. abs (math.ceil [X/10] - math.ceil [Y/10])

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
const int N=2e5+5;
int n;
ll a[N];
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;
	while(t--){
		int a,b;cin >> a >> b;
		int c=abs((a-1)/10-(b-1)/10);
		cout << c << '\n';
	}
}
``

Editorialist's Solution
``t=int(input())
for _ in range(t):
    X,Y = map(int,input().split())
    X = ((X-1)//10)
    Y = ((Y-1)//10)
    print(abs(X-Y))
``

</details>
