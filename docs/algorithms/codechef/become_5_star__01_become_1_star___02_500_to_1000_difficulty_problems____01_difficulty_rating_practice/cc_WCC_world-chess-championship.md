# World Chess Championship

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WCC |
| Difficulty Rating | 935 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [WCC](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/WCC) |

---

## Problem Statement

The World Chess Championship $2022$ is about to start. $14$ Classical games will be played between Chef and Carlsen in the championship, where each game has one of three outcomes — it can be won by Carlsen, won by Chef, or it can be a draw. The winner of a game gets $2$ points, and the loser gets $0$ points. If it’s a draw, both players get $1$ point each.

The total prize pool of the championship is $100 \cdot X$. At end of the $14$ Classical games, if one player has **strictly more** points than the other, he is declared the champion and gets $60 \cdot X$ as his prize money, and the loser gets $40 \cdot X$.

If the total points are **tied**, then the defending champion Carlsen is declared the winner. However, if this happens, the winner gets only $55 \cdot X$, and the loser gets $45 \cdot X$.

Given the results of all the $14$ games, output the prize money that Carlsen receives.

The results are given as a string of length $14$ consisting of the characters `C`, `N`, and `D`.
- `C` denotes a victory by Carlsen.
- `N` denotes a victory by Chef.
- `D` denotes a draw.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains one integer $X$, denoting that the total prize pool is $100\cdot X$.
- The second line contains the results of the match, as a string of length $14$ containing only the characters `C`, `N`, and `D`.

---

## Output Format

For each test case, output in a single line the total prize money won by Carlsen.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 10^6$
- $|S| = 14$
- $S$ contains only characters `D`, `C`, `N`.

---

## Examples

**Example 1**

**Input**

```text
4
100
CCCCCCCCCCCCCC
400
CDCDCDCDCDCDCD
30
DDCCNNDDDCCNND
1
NNDNNDDDNNDNDN
```

**Output**

```text
6000
24000
1650
40
```

**Explanation**

**Test case $1$:** Since Carlsen won all the games, he will be crowned the champion and will get $60 \cdot X$ as the prize money which is $60 \cdot 100 = 6000$

**Test case $2$:** Carlsen won $7$ games and drew $7$, so his score is $2 \cdot 7 + 1 \cdot 7 = 21$. Chef lost $7$ games and drew $7$, so his score is $0 \cdot 7 + 1 \cdot 7 = 7$. Since Carlsen has more points, he will be crowned the champion and will get $60 \cdot X$ as the prize money which is $60 \cdot 400 = 24000$

**Test case $3$:** Carlsen and Chef both end up with $14$ points. So, Carlsen is declared the winner, but because the points were tied, he receives $55\cdot X = 55\cdot 30 = 1650$ in prize money.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100
CCCCCCCCCCCCCC
```

**Output for this case**

```text
6000
```



#### Test case 2

**Input for this case**

```text
400
CDCDCDCDCDCDCD
```

**Output for this case**

```text
24000
```



#### Test case 3

**Input for this case**

```text
30
DDCCNNDDDCCNND
```

**Output for this case**

```text
1650
```



#### Test case 4

**Input for this case**

```text
1
NNDNNDDDNNDNDN
```

**Output for this case**

```text
40
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/FEB222A/problems/WCC)

[Contest Division 2](https://www.codechef.com/FEB222B/problems/WCC)

[Contest Division 3](https://www.codechef.com/FEB222C/problems/WCC)

**Setter:** [Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

In a Chess match, The winner of a game gets 2 points, and the loser gets 0 points. If it’s a draw, both players get 1 point each.

The total prize pool of a Chess championship is 100 \cdot X. At the end of 14 classical games, if one player has strictly more points than the other, he is declared the champion and gets 60 \cdot X, and the loser gets 40 \cdot X.

If the total points are tied, then the defending champion Carlsen is declared the winner. However, if this happens, the winner gets only 55 \cdot X, and the loser gets 45 \cdot X.

Given the results of all the 14 games, output the prize money that Carlsen receives.

The results are given as a string of length 14 consisting of the characters `C`, `N`, and `D`.

-
`C` denotes a victory by Carlsen.

-
`N` denotes a victory by Chef.

-
`D` denotes a draw.

#
[](#explanation-5)EXPLANATION:

Observation

Note that if a player wins more matches, he would definitely gain points. Similarly, if both players win the same number of matches, they have the same number of points.

This means that we can calculate the prize money just by comparing the number of wins of both players. The points gained per win do not affect the result.

In this problem, we just need to implement the problem statement. The focus is on our ability to translate the problem statement into functioning error-free code.

Let X denote the number of wins by Carlsen and Y denote the number of wins by Chef. We can calculate these values by a single traversal of the string.

-
**If X > Y:** The number of matches won by Carlsen is strictly greater than that of Chef. Thus he gets 60 \cdot X.

-
**If X = Y:** The total points are tied. Defending champion Carlsen wins 55 \cdot X.

-
**If X <Y:** Carlsen loses and gets 40 \cdot X.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(|S|) as we need to traverse the whole string to calculate the number of wins. Here, since |S| = 14, which is very small, the time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int X;
	    cin>>X;

	    string S;
	    cin>>S;

	    int carlsen = 0;
	    int chef = 0;
	    for(int i = 0; i<14; i++){
	        if(S[i] == 'C')
	            carlsen++;
	        else if(S[i] =='N')
	            chef++;
	    }

	    if(carlsen > chef){
	        cout<<60*X;
	    }
	    else if(carlsen == chef){
	        cout<<55*X;
	    }
	    else{
	        cout<<40*X;
	    }
	    cout<<endl;
	}
	return 0;
}
``

</details>
