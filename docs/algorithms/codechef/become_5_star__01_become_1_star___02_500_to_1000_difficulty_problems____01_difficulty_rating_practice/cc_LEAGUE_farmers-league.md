# Farmers League

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LEAGUE |
| Difficulty Rating | 883 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [LEAGUE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/LEAGUE) |

---

## Problem Statement

A football league of $N$ teams is taking place, where each team plays other teams once in [single round robin](https://en.wikipedia.org/wiki/Round-robin_tournament) fashion. A team gets $3$ points for winning a game and $0$ for losing (assume that no games end in a draw/tie). What is the **maximum** possible difference of points between the winning team and the second-placed team?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing a single integer $N$.

---

## Output Format

For each test case, output in a single line the maximum difference of points between first and second place.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
2
3
4
9
```

**Output**

```text
3
3
6
12
```

**Explanation**

**Test case $1$:** There will only be one match played between the two teams, therefore one team wins by $3$ points.

**Test case $2$:** Let the three teams be A, B, C. If team A wins both the games against team B and team C, then team A will win by $3$ points since one of team B and team C will win the game between them.

**Test case $3$:** Let the four teams be A, B, C, D. One possibility is for A to win all its games, and then B beats C, C beats D, D beats B. This way, the winner has $9$ points and second place has $3$ points, making a difference of $6$.

**Test case $4$:** It can be shown that it's not possible to achieve a difference higher than $12$ when $9$ teams play. One way of achieving this is for the winner to score $24$ points and second place to score $12$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
9
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 3](https://www.codechef.com/COOK141C/problems/LEAGUE)

[Contest Division 4](https://www.codechef.com/COOK141D/problems/LEAGUE)

**Setter and Editorialist :**  [Yashodhan Agnihotri](https://www.codechef.com/users/zappelectro)

#
[](#difficulty-2)DIFFICULTY:

883

#
[](#prerequisites-3)PREREQUISITES:

None.

#
[](#problem-4)PROBLEM:

Find the maximum number of points by which a team can win a N-team league, if each team plays every other team in round robin fashion. Teams get 3 points for a win and 0 points for a loss. (Assume there are no draws).

#
[](#explanation-5)EXPLANATION:

The answer can mainly be gathered with the following hints.

Winning team wins all

This is necessary to maximise the points of the winner team. Therefore the total number of points of the winning team will be 3*(N-1).

Other teams perform similarly

If the second placed team performs similar to other teams apart from team A(winning team), that helps in minimizing the total points.

So, the second placed team will play a total of N-2 games with teams other than the winning team. If they win half games and lose halfgames, that will help in keeping their points total to a minimum. So, points gathered will be ceil((N-2)/2)*3. Ceil function is used so that in case N is odd, second placed team will win one game more than the last placed team (as you can check for N=3).

Final Answer

Final Answer will be the difference of the points total of the first and the second placed teams.

\therefore ans = 3*(N-1) - ceil((N-2)/2)*3 = 3*(N/2)

If using C++, be sure to use 64 bit integer to avoid unnecessary overflow errors.

#
[](#solutions-6)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		int64_t ans = (n - 1) * 3 - ceil((double)(n - 2) / 2) * 3;
		cout << ans << "\n";
	}
	return 0;
}
``

For doubts, please leave them in the comment section, I’ll address them.

</details>
