# Soccer League

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | M3 |
| Difficulty Rating | 1906 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Graphs |
| Official Link | [M3](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/M3) |

---

## Problem Statement

The new season of the Bytelandian Premier League (BPL) has started!

In the BPL, any two soccer teams play with each other exactly once. In each match, the winner earns 3 points and the loser earns no point. There is no draw (if the match is level after the two halves, two teams will take part in a penalty shootout to decide the winner).

At the end of the league, the winner is the team having the largest number of points. In case there are more than one team which has the largest number of points, these teams will be co-champions of the league.

The league has been running for some time. Now, the following problem has arisen: we would like to know if a specific team still has a chance of winning the league.

### Input

The first line contains T (about 20), the number of test cases. Then T test cases follow. Each test case has the following form.

The first line of the test case contains a number N (1 <= N <= 140), the number of teams in the league.

The i-th line in the next N lines contains N numbers ai1, ai2, ..., ain. The number aij gives the status of the match between the i-th team and the j-th team:

- aij = 1 if the i-th team wins,

- aij = 0 if the i-th team loses,

- aij = 2 if the match has not taken place yet.

The input data is such that if i!=j, then aij + aji = 1 or aij = aji = 2. Moreover, aii = 0 for all i.

### Output

For each test case, print a binary string of length N, in which the i-th character is 1 if the i-th team still has a chance to be a champion of the league, and 0 otherwise.

---

## Examples

**Example 1**

**Input**

```text
3
3
0 0 0 
1 0 1 
1 0 0 
4
0 1 1 0 
0 0 2 0 
0 2 0 0 
1 1 1 0 
5
0 2 2 1 0 
2 0 1 1 0 
2 0 0 1 0 
0 0 0 0 1 
1 1 1 0 0
```

**Output**

```text
010
0001
11001
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
0 0 0
1 0 1
1 0 0
4
```

**Output for this case**

```text
010
```



#### Test case 2

**Input for this case**

```text
0 1 1 0
0 0 2 0
0 2 0 0
1 1 1 0
5
```

**Output for this case**

```text
0001
```



#### Test case 3

**Input for this case**

```text
0 2 2 1 0
2 0 1 1 0
2 0 0 1 0
0 0 0 0 1
1 1 1 0 0
```

**Output for this case**

```text
11001
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Soccer League](https://www.codechef.com/practice/course/3to4stars/LP3TO403/problems/M3)

### [](#problem-statement-1)Problem Statement

The new season of the Bytelandian Premier League (BPL) has started!

In the BPL, any two soccer teams play with each other exactly once. In each match, the winner earns 3 points and the loser earns no point. There is no draw (if the match is level after the two halves, two teams will take part in a penalty shootout to decide the winner).

At the end of the league, the winner is the team having the largest number of points. In case there are more than one team which has the largest number of points, these teams will be co-champions of the league.

The league has been running for some time. Now, the following problem has arisen: we would like to know if a specific team still has a chance of winning the league.

### [](#approach-2)Approach

The problem is solved by analyzing the results of matches. The number of wins (`wins[i]`) and unplayed matches (`unplayed[i]`) for each team is tracked. The highest current score (`score`) is determined by iterating over the results of all matches. Then, it is checked whether adding the maximum potential points from unplayed matches allows a team to equal or surpass the current highest score. If a team cannot potentially achieve the highest score, it is marked as having no chance (0). Otherwise, it is marked as having a chance (1).

The logic also considers the scenario where unplayed matches between top teams might increase the score further if they directly impact the current leading teams’ wins. This ensures a thorough assessment of all possibilities for championship contention.

### [](#time-complexity-3)Time Complexity

The time complexity is O(n^2), as the code iterates over all n \times n match results in the league.

### [](#space-complexity-4)Space Complexity

The space complexity is O(n), as arrays `wins` and `unplayed` are used to store data for n teams.

</details>
