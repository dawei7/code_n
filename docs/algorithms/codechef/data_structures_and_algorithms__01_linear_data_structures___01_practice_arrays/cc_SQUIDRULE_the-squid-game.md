# The Squid Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SQUIDRULE |
| Difficulty Rating | 970 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [SQUIDRULE](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/SQUIDRULE) |

---

## Problem Statement

*"Let the games begin."*

Squid Game has become a blockbuster hit and the frontman is now finding it difficult to accommodate all the participants in Squid Game 2.0. So, he decided that he will allow only those participants who could solve the following problem.

There are a total of $N$ players who are competing in the Squid Game, numbered from $1$ to $N$. When the $i^{\text{th}}$ player gets eliminated from the game, $A_i$ amount of money is added to the prize pool. The game is played until $N-1$ players get eliminated, and the only player left is declared as the winner. The winner gets all the money present in the prize pool.

You are given an array $A$ consisting of $N$ elements, where $A_i$ denotes the prize money added to the prize pool when the $i^{\text{th}}$ player gets eliminated from the game. Find the maximum prize that the winner can get, given that you can choose any player to be the winner.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$, denoting the number of players.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$, denoting the amount of money added to the prize pool when the $i^{\text{th}}$ ($1 \leq i \leq N$) player dies.

---

## Output Format

For each test case, output in a single line the maximum prize that the winner can get, given that you can choose any player to be the winner.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^4$
- The sum of $N$ across all test cases does not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
3
3 1 2
5
1 1 1 1 1
6
3 6 4 2 5 1
```

**Output**

```text
5
4
20
```

**Explanation**

**Test Case 1:**
- If we choose the first player to be the winner, he will win the game when the second and third players die. Hence, the amount of money won by him will be $1+2 = 3$.
- If we choose the second player to be the winner, he will win the game when the first and third players die. Hence, the amount of money won by him will be $3+2 = 5$.
- If we choose the third player to be the winner, he will win the game when the first and second players die. Hence, the amount of money won by him will be $3+1 = 4$.

Therefore, we can clearly see that the maximum amount of money that can be won by any player is $5$.

**Test Case 2:** Irrespective of who is chosen, the winner will always win an amount of $4$.

**Test Case 3:** If we choose the sixth player to be the winner, the amount won by him will be $3 + 6 + 4 + 2 + 5 = 20$. It can be proven that if we choose any other player to be the winner, the amount is less than $20$. Hence, the maximum amount of money that can be won by any player is $20$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
3 1 2
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
5
1 1 1 1 1
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
6
3 6 4 2 5 1
```

**Output for this case**

```text
20
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-the-squid-gamehttpswwwcodechefcominfi21bproblemssquidrule-1)PROBLEM LINK: [The Squid Game](https://www.codechef.com/INFI21B/problems/SQUIDRULE)

***Setter:***  [Satyam Garg](https://www.codechef.com/users/satty26)

***Editorialist:***   [Arpan Gupta](https://www.codechef.com/users/arpan4775)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#prerequisites-3)PREREQUISITES:

Arrays

#
[](#problem-4)PROBLEM:

Given an array of N Players with an amount A_i associated with each. Whenever a player gets eliminated, the amount associated with him gets added to the pool prize. After N-1 eliminations, find the maximum pool prize that can be achieved.

#
[](#explanation-5)EXPLANATION:

A player i will win maximum prize money only if all **other** players make up the maximum prize and that will be possible if all other players have prize money greater than or equal to the prize money associated with player i.

Let’s assume that player i has the least prize money associated with him. So, the maximum prize money possible after eliminating N-1 players will be (Total prize money – prize money of the player i)

First, find the total prize by iterating over all players and simultaneously finding the minimum element from the given array.

Time Complexity: O(n)

Space Complexity: O(n)

#
[](#solutions-6)SOLUTIONS:

Setter's Solution(C++)
``#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while (t--) {
		int n;
		cin >> n;
		vector<int> v(n);
		int sum = 0;
		int smallest_element = 1e6;
		for (int i = 0; i < n; i++) {
			cin >> v[i];
			sum += v[i];
			smallest_element = min(smallest_element, v[i]);
		}
		cout << sum - smallest_element << "\n";
	}
	return 0;
}
``

For doubts, please leave them in the comment section, I’ll address them.

</details>
