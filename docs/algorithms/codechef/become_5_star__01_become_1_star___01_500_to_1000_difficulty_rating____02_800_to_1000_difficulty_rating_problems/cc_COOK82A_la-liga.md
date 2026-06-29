# La Liga

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COOK82A |
| Difficulty Rating | 956 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [COOK82A](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/COOK82A) |

---

## Problem Statement

Today is the final round of La Liga, the most popular professional football league in the world. Real Madrid is playing against Malaga and Barcelona is playing against Eibar. These two matches will decide who wins the league title. Real Madrid is already 3 points ahead of Barcelona in the league standings. In fact, Real Madrid will win the league title, except for one scenario: If Real Madrid loses against Malaga, and Barcelona wins against Eibar, then the La Liga title will go to Barcelona. In any other combination of results, Real Madrid will win the title.

You will be given multiple scenarios for these two games, where in each one you will be given the number of goals each team scored in their respective match. A team wins a match if it scores more than the opponent. In case they score the same number of goals, it's a draw. Otherwise, the team loses the game. You are asked to tell the winner of the La Liga title in each scenario.

### Input

The first line contains a single number **T**, the number of scenarios.
Each scenario is described by four lines. Each line starts with a team name followed by the number of goals this team scored in its corresponding match. (Barcelona plays Eibar and Real Madrid plays Malaga). The names are given in any arbitrary order within a scenario.

### Output

For each scenario, output a single line showing the title winner in case this scenario happens. It should be either "RealMadrid" or "Barcelona".

### Constraints

- 1 ≤ **T** ≤ **500**

- 0 ≤ number of goals scored by a team in a match ≤ **20**

---

## Examples

**Example 1**

**Input**

```text
2
Barcelona 2
Malaga 1
RealMadrid 1
Eibar 0
Malaga 3
RealMadrid 2
Barcelona 8
Eibar 6
```

**Output**

```text
RealMadrid
Barcelona
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
Barcelona 2
Malaga 1
RealMadrid 1
Eibar 0
```

**Output for this case**

```text
RealMadrid
```



#### Test case 2

**Input for this case**

```text
Malaga 3
RealMadrid 2
Barcelona 8
Eibar 6
```

**Output for this case**

```text
Barcelona
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COOK82A)

[Contest](https://www.codechef.com/COOK82/problems/COOK82A)

**Author:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

**Primary Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Secondary Tester:** [Istvan Nagi](https://www.codechef.com/users/iscsi)

**Editorialist:** [Udit Sanghi](https://www.codechef.com/users/mathecodician)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

None

### PROBLEM:

There are 2 matches to be held in the final round of La Liga(a football season/tournament) which determine the winner of the tournament. In order for Barcelona to win the title,it must win its game and Real Madrid must lose its game. Given the goals scored by each of the teams in both the matches, tell who is going to win the title.

### QUICK EXPLANATION:

Store the number of goals scored by each of the team. See who wins the matches between the teams and check if the given condition is true.

### EXPLANATION:

So the first step will idealy be to store the scores of each team.

Now you have the scores of each team. So you need to check -

``1. Barcelona won its game: We can check this if barca > eibar.
2. Real Madrid loses to Malaga: We can check this if real < malaga
``

So if these 2 conditions are true then the answer is ‘Barcelona’ else it is ‘RealMadrid’.

### EDITORIALIST’s, AUTHOR’S AND TESTER’S SOLUTIONS:

**EDITORIALIST’s solution**: [Here] [111](https://pastebin.com/2bYzmYCU)

**AUTHOR’s solution**:  [Here] [222](http://www.codechef.com/download/Solutions/COOK82/Setter/COOK82A.cpp)

**TESTER’s solution**: [Here] [333](http://www.codechef.com/download/Solutions/COOK82/Tester1/COOK82A.cpp)

</details>
