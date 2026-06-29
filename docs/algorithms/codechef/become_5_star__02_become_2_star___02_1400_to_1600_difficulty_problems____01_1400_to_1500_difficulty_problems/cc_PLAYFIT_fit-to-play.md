# Fit to Play

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PLAYFIT |
| Difficulty Rating | 1419 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [PLAYFIT](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/PLAYFIT) |

---

## Problem Statement

Rayne Wooney has been one of the top players for his football club for the last few years. But unfortunately, he got injured during a game a few months back and has been out of play ever since.

He's got proper treatment and is eager to go out and play for his team again. Before doing that, he has to prove to his fitness to the coach and manager of the team. Rayne has been playing practice matches for the past few days. He's played N practice matches in all.

He wants to convince the coach and the manager that he's improved over time and that his injury no longer affects his game. To increase his chances of getting back into the team, he's decided to show them stats of any 2 of his practice games. The coach and manager will look into the goals scored in both the games and see how much he's improved. If the number of goals scored in the 2nd game(the game which took place later) is greater than that in 1st, then he has a chance of getting in. Tell Rayne what is the maximum improvement in terms of goal difference that he can show to maximize his chances of getting into the team. If he hasn't improved over time, he's not fit to play. Scoring equal number of goals in 2 matches will not be considered an improvement. Also, he will be declared unfit if he doesn't have enough matches to show an improvement.

**Note:** Large input data. Use faster I/O methods. Prefer scanf,printf over cin/cout.

---

## Input Format

- The first line of the input contains a single integer $T$, the number of test cases.
- Each test case begins with a single integer $N$, the number of practice matches Rayne has played.
- The next line contains $N$ integers. The $i^{th}$ integer, $g_i$, on this line represents the number of goals Rayne scored in his $i^{th}$ practice match. The matches are given in chronological order i.e. $j > i$ means match number $j$ took place after match number $i$.

---

## Output Format

For each test case output a single line containing the maximum goal difference that Rayne can show to his coach and manager. If he's not fit yet, print "UNFIT".

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 100000$
- $0 \leq g_i \leq 1000000$ (Well, Rayne's a legend! You can expect him to score so many goals!)

---

## Examples

**Example 1**

**Input**

```text
3
6
3 7 1 4 2 4
5
5 4 3 2 1
5
4 3 2 2 3
```

**Output**

```text
4
UNFIT
1
```

**Explanation**

In the first test case, Rayne can choose the first and second game. Thus he gets a difference of 7-3=4 goals. Any other pair would give him a lower improvement.
In the second test case, Rayne has not been improving in any match. Thus he's declared UNFIT.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
3 7 1 4 2 4
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
5
5 4 3 2 1
```

**Output for this case**

```text
UNFIT
```



#### Test case 3

**Input for this case**

```text
5
4 3 2 2 3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/PLAYFIT/)

[Contest](http://www.codechef.com/APRIL12/problems/PLAYFIT/)

### DIFFICULTY

EASY

### EXPLANATION

This was one of the simple problems of this month. A lot of you were able to solve it easily. The constraints of the problem were such that only O(n) solution could pass. The problem could be stated simply as: Find 2 numbers ai and aj such that aj-ai is maximum. (1 <= i < j <= N) A couple of approaches to this problem: Approach 1: Store the numbers in an array a. Take 2 additional arrays b & c. b[i]=maximum over all ax (for all x such that i<=x<=n) c[i]=minimum over all ax (for all x such that 1<=x<=i) Both these arrays can be computed in O(n) time and space. Clearly, answer will be max(b[i]-c[i]) for all i. This can be found in O(n) too. Approach 2: Take a variable ‘minm’ which denotes the minimum value encountered so far. Let ‘ans’ denote the maximum difference achieved so far. Read the numbers one by one. Let current value be cur. ans=max(ans,cur-minm) minm=min(minm,cur); Finally, the answer would be in ‘ans’.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/April/Setter/PLAYFIT.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/April/Tester/PLAYFIT.c).

</details>
