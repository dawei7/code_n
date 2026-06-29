# UEFA Champions League

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | UCL |
| Difficulty Rating | 1633 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [UCL](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/UCL) |

---

## Problem Statement

The UEFA Champions League is the most prestigious annual sports competition in the world. In the group stage of this competition, European football clubs are divided into 8 groups; there are four teams in each group. The teams in each group are ranked based on the matches they play against each other, according to the following rules:
- Based on the results of matches, teams are awarded *points*. Each football match is played between a *home team* and an *away team*. If one of the teams scores more goals than the other, this team gains $3$ points and the other team gains $0$ points. In case of a tie (if both teams score the same number of goals), each of those teams gains $1$ point.
- The *goal difference* of a team is the number of goals it scored minus the number of goals it received, regardless if it scored/received them as the home team or as the away team.
- Between any two teams, the team with more points is ranked higher.
- If they have the same number of points (in case of a tie), the team with higher goal difference is ranked higher.

Each team plays two matches against every other team in its group ― one match as the home team and one match as the away team. You are given the number of goals scored by each team for all twelve matches in one group. Determine the leaders of this group ― the first and second top-ranked team. It is guaranteed that there are no ties for either of these places (for the given results of the matches).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- For each test case, $12$ lines follow. Each of these lines describes the result of one match in the format `HomeTeamName HomeTeamGoals vs. AwayTeamGoals AwayTeamName`, where `HomeTeamName` and `AwayTeamName` are strings and `HomeTeamGoals` and `AwayTeamGoals` are integers denoting the number of goals scored by the respective teams in this match.

### Output
For each scenario, print a single line containing two space-separated strings ― the name of the top-ranked team and the name of the second top-ranked team.

### Constraints
- $1 \le T \le 50$
- the length of the name of each team does not exceed $10$
- the name of each team contains only lowercase English letters
- $0 \le$ number of goals scored by each team $\le 100$

---

## Examples

**Example 1**

**Input**

```text
2
manutd 8 vs. 2 arsenal
lyon 1 vs. 2 manutd
fcbarca 0 vs. 0 lyon
fcbarca 5 vs. 1 arsenal
manutd 3 vs. 1 fcbarca
arsenal 6 vs. 0 lyon
arsenal 0 vs. 0 manutd
manutd 4 vs. 2 lyon
arsenal 2 vs. 2 fcbarca
lyon 0 vs. 3 fcbarca
lyon 1 vs. 0 arsenal
fcbarca 0 vs. 1 manutd
a 3 vs. 0 b
a 0 vs. 0 c
a 0 vs. 0 d
b 0 vs. 0 a
b 4 vs. 0 c
b 0 vs. 0 d
c 0 vs. 0 a
c 0 vs. 0 b
c 1 vs. 0 d
d 3 vs. 0 a
d 0 vs. 0 b
d 0 vs. 0 c
```

**Output**

```text
manutd fcbarca
d b
```

**Explanation**

**Example case 1:** The total number of points and goal difference for each team is as follows:
- `manutd`: $16$ points, goal difference $12$
- `fcbarca`: $8$ points, goal difference $4$
- `manutd`: $5$ points, goal difference $-5$
- `lyon`: $4$ points, goal difference $-11$

**Example case 2:** The total number of points and goal difference for each team is as follows:
- `d`: $7$ points, goal difference $2$
- `b`: $7$ points, goal difference $1$
- `a`: $7$ points, goal difference $0$
- `c`: $7$ points, goal difference $-3$

Note that in this test case, all teams have the same number of points, but teams with higher goal difference are ranked higher.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
manutd 8 vs. 2 arsenal
lyon 1 vs. 2 manutd
fcbarca 0 vs. 0 lyon
fcbarca 5 vs. 1 arsenal
manutd 3 vs. 1 fcbarca
arsenal 6 vs. 0 lyon
arsenal 0 vs. 0 manutd
manutd 4 vs. 2 lyon
arsenal 2 vs. 2 fcbarca
lyon 0 vs. 3 fcbarca
lyon 1 vs. 0 arsenal
fcbarca 0 vs. 1 manutd
```

**Output for this case**

```text
manutd fcbarca
```



#### Test case 2

**Input for this case**

```text
a 3 vs. 0 b
a 0 vs. 0 c
a 0 vs. 0 d
b 0 vs. 0 a
b 4 vs. 0 c
b 0 vs. 0 d
c 0 vs. 0 a
c 0 vs. 0 b
c 1 vs. 0 d
d 3 vs. 0 a
d 0 vs. 0 b
d 0 vs. 0 c
```

**Output for this case**

```text
d b
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/UCL)

[Contest](https://www.codechef.com/COOK104A/problems/UCL)

**Author:** [Erfan alimohammadi](https://www.codechef.com/users/erfaniaa)

**Tester & Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

Given the results of group stage matches in a champions league for one group. You need to determine the team on top of the group’s table and the runner up. The group consists of 4 teams. Hence, 6 matches are held (between each pair).

In a single match, the team with more goals wins. When a team wins it gets 3 points, for a draw it gets 1 point and for losing it gets 0. Teams are sorted in descending order according to points, and in case of a tie according to goal difference (number of goals the team scored - the number of goals it conceded). It’s guaranteed that the group’s top team and the runner up are both unique.

### EXPLANATION:

This a straight forward implementation problem.The best tool to solve it with is map (in C++) or any equivalent structure in any other programming language. If you don’t know it, you must learn about it. In simple words, it creates a structure like a dictionary, which a field containing information about some word. Both the word and the info can be of any standard type or even (custom object but with some conditions I will not be mentioning).

So here we will have maps like:

***map < string , int > points , goals;***

The first map tells the number of points associated with each club name. For example ***points[“barcelona”]*** indicates the number of points associated with the string “barcelona”.

After we read the input, we fix the number of points associated with each team and the number of goals as well. After this, we can sort the 4 teams with any sorting algorithm (or even simple if cases) using the information in the maps.

In my C++ code, I wrote a custom comparator, that compares between two strings according to the data in the maps and then used it along with ***std::sort*** function. Please refer to my code for details.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[**AUTHOR’s solution**](https://pastebin.com/nTiJpumn)

[**TESTER’s solution**](https://pastebin.com/wkQMkVFi)

</details>
