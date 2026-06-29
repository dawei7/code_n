# It is My Serve

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MYSERVE |
| Difficulty Rating | 691 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MYSERVE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MYSERVE) |

---

## Problem Statement

Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player makes $2$ consecutive serves before the service changes. Alice makes the first serve of the match. Therefore the first $2$ serves will be made by Alice, then the next $2$ serves will be made by Bob and so on.

Let's consider the following example match for more clarity:
- Alice makes the $1^{st}$ serve.
- Let us assume, Bob wins this point. (Score is $0$ for Alice and $1$ for Bob)
- Alice makes the $2^{nd}$ serve.
- Let us assume, Alice wins this point. (Score is $1$ for Alice and $1$ for Bob)
- Bob makes the $3^{rd}$ serve.
- Let us assume, Alice wins this point. (Score is $2$ for Alice and $1$ for Bob)
- Bob makes the $4^{th}$ serve.
- Let us assume, Alice wins this point. (Score is $3$ for Alice and $1$ for Bob)
- Alice makes the $5^{th}$ serve.
- And the game continues $\ldots$

After the score reaches $P$ and $Q$ for Alice and Bob respectively, both the players forgot whose serve it is. Help them determine whose service it is.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $P$ and $Q$ — the score of Alice and Bob respectively.

---

## Output Format

For each test case, determine which player's (`Alice` or `Bob`) serve it is.

You may print each character of `Alice` and `Bob` in uppercase or lowercase (for example, `Bob`, `BOB`, `boB` will be considered identical).

---

## Constraints

- $1 \leq T \leq 200$
- $0 \le P, Q \le 10$

---

## Examples

**Example 1**

**Input**

```text
4
0 0
0 2
2 2
4 7
```

**Output**

```text
Alice
Bob
Alice
Bob
```

**Explanation**

- **Test Case 1:** Since no points have been scored yet, this is the first serve of the match. Alice makes the $1^{st}$ serve of the match.
- **Test Case 2:** Two points have been scored yet. Thus, it is the third serve of the match. Bob makes the $3^{rd}$ serve of the match.
- **Test Case 3:** Four points have been scored yet. Thus, it is the fifth serve of the match. Alice makes the $5^{th}$ serve of the match.
- **Test Case 4:** Eleven points have been scored yet. Thus, it is the twelfth serve of the match. Bob makes the $12^{th}$ serve of the match.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 0
```

**Output for this case**

```text
Alice
```



#### Test case 2

**Input for this case**

```text
0 2
```

**Output for this case**

```text
Bob
```



#### Test case 3

**Input for this case**

```text
2 2
```

**Output for this case**

```text
Alice
```



#### Test case 4

**Input for this case**

```text
4 7
```

**Output for this case**

```text
Bob
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME109A/problems/MYSERVE)

[Contest Division 2](https://www.codechef.com/LTIME109B/problems/MYSERVE)

[Contest Division 3](https://www.codechef.com/LTIME109C/problems/MYSERVE)

[Contest Division 4](https://www.codechef.com/LTIME109D/problems/MYSERVE)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

691

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice and Bob are playing a game where every player makes 2 serves with Alice making the initial 2 serves, followed by Bob and so on. On each serve - either Alice or Bob score a point. Given their current scores - P and Q, we have to determine who is currently serving.

#
[](#explanation-5)EXPLANATION:

Hint 1

Note that on each serve - necessarily Alice or Bob have to score a point. There is no draw / tie. What does this tell us about their scores?

Hint 2

If we write down a sequence of the first 20 serves - can it help us identify the logic for solving this problem?

Hint 3

On each serve - Alice or Bob have to score a point.

Hint 3a

What is the sum of the points scored by Alice and Bob?

Hint 3b

Since each serve was equivalent to a point ? it is necessarily true that the total points scored so far are equal to the total serves which have happened so far.

Can you try to solve the problem based on this?

Hint 4

Let’s write down the example of the first 20 serves.

Hint 4a

In the list below, A stands for Alice and B for Bob.

Serves by              - [A  A  B  B  A  A  B  B  A  A  B   B  A   A   B  B   A  A   B  B]

Total points scored- [1   2  3  4   5   6  7  8  9  10 11 12 13 14 15 16 17 18 19 20]

What do we observe?

Hint 4b

Independent of who scores the points - the serve sequence will always run as per the above. So the total points scored can help us identify who is currently serving. How do we do that?

Hint 5

So now, given P and Q, we know that the number of serves finished is P + Q. Now how do we figure out who the next person to serve is?

Hint 5a

Let’s call the two consecutive serves by the same player as their turn. So in the first turn, Alice serves twice. Then in the next turn, Bob serves twice, etc.

Hint 5b

Can we find out how many turns have been completed?

Hint 5c

That’s right. If there have been S serves, there have been floor(S/2) turns.

Hint 5d

Since turns alternate between Alice and Bob, we just need to look at whether floor(S/2) is even or odd.

Hint 6

Full Solution:

Hint 6a

First we calculate total points score as (P + Q)

Hint 6b

We observe that each person has 2 serves ? so the current turn serving is (P + Q) / 2

Hint 6c

Since Alice goes first and Bob goes second, If (P + Q) / 2 is even ? then Alice is serving and if (P + Q) / 2 is odd ? Bob is serving

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
		int x=(a+b)%4/2;
		if(x==0) cout << "Alice\n";
		else cout << "Bob\n";
	}
}
``

Editorialist's Solution
``t=int(input())
for _ in range(t):
    p,q=map(int,input().split())
    total=p+q
    total=total//2
    if total%2==0:
        print("Alice")
    else:
        print("Bob")
``

</details>
