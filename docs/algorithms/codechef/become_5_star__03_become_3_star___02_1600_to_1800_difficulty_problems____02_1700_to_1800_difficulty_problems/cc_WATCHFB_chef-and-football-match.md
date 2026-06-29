# Chef and Football Match

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WATCHFB |
| Difficulty Rating | 1700 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [WATCHFB](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/WATCHFB) |

---

## Problem Statement

Chef and his son Chefu want to watch a match of their favourite football team playing against another team, which will take place today.

Unfortunately, Chef is busy in the kitchen preparing lunch, so he cannot watch the match. Therefore, every now and then, Chef asks Chefu about the current scores of the teams and Chefu tells him the score. However, Chefu sometimes does not specify the teams along with the score — for example, he could say "the score is 3 to 6", and there is no way to know just from this statement if it was their favourite team or the other team that scored 6 goals; in different statements, the order of teams may also be different. Other times, Chefu specifies which team scored how many goals.

Chef asks for the score and receives a reply $N$ times. There are two types of replies:
- `1 A B`: their favourite team scored $A$ goals and the other team scored $B$ goals
- `2 A B`: one team scored $A$ goals and the other scored $B$ goals

Chef is asking you to help him determine the score of his favourite team after each of Chefu's replies. After each reply, based on the current reply and all previous information (but without any following replies), tell him whether it is possible to certainly determine the number of goals scored by his favourite team.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The following $N$ lines describe Chefu's replies in the format described above.

### Output
For each of Chefu's replies, print a single line containing the string `"YES"` if it is possible to determine the score of Chef's favourite team after this reply or `"NO"` if it is impossible.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^4$
- $0 \le A, B \le 10^9$
- the sum of $N$ over all test cases does not exceed $10^5$
- there is at least one valid sequence of scored goals consistent with all replies

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
6
2 0 1
1 3 1
2 2 4
2 5 6
2 8 8
2 9 10
```

**Output**

```text
NO
YES
YES
NO
YES
NO
```

**Explanation**

**Example case 1:**
- Reply 1: Chef cannot know who scored the first goal.
- Reply 2: Chefu told Chef that their favourite team has scored $3$ goals so far.
- Reply 3: Chef can conclude that his favourite team has scored $4$ goals, since it already scored $3$ goals earlier.
- Reply 4: the favourite team could have scored $5$ or $6$ goals, but there is no way to know which option is correct.
- Reply 5: since there is a tie, Chef knows that his favourite team has scored $8$ goals.
- Reply 6: again, Chef cannot know if his favourite team has scored $9$ or $10$ goals.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/WATCHFB)

[Contest](https://www.codechef.com/LTIME76B/problems/WATCHFB)

**Author:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester & Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### PROBLEM EXPLANATION

Chef and his son Chefu want to watch a match of their favourite football team playing against another team.

Chef asks Chefu for the score N times and each time he received a reply.

There are two types of replies:

-
`1 A B` : their favorite team scored A goals and the other team scored B goals

-
`2 A B` : one team scored A goals and the other scored B goals without specifying who scored A and who scored B.

After each reply, based on the current reply and all previous information (but without any following replies), tell Chef whether it is possible to certainly determine the number of goals scored by his favourite team.

### DIFFICULTY:

Easy

### PREREQUISITES:

None

### EXPLANATION:

We need to handle all possible cases in this problem.

First, let’s keep track of the scores Chefu replied with to the last question (they would be 0-0 at the beginning). Also, we need to distinguish at each point of time if we really know the mapping between the scores and the teams or not.

Let’s start processing replies one by one then:

- If the score told is a draw (our previous queries don’t really matter) the answer is **YES**.

-
**ELSE** If the reply was of the first type, the answer is **YES** and we definitely know the score-to-team mapping from this moment on.

-
**ELSE** If we don’t know the score-to-team mapping at this moment and first two conditions are not met, then definitely we won’t get any information with the new reply so the answer is **NO**.

-
**ELSE** If we already know the mapping between the last recorded scores and the teams (min_p,max_p) with min_p being the score of the team with fewer goals. If on the current reply (min_c,max_c) the team with fewer goals min_c didn’t reach the team with most goals on the previous reply max_p (In short min_c < max_p) then we know for fact that the team who scored min_p on previous reply and min_c on current one are the same team.

-
**ELSE** In any other case, the answer is **NO**. And we should mark that we don’t know the mapping for processing future replies until we get some reply that points out the mapping.

### AUTHOR’S AND TESTER’S SOLUTIONS:

**EDITORIALIST’s solution**: Can be found [here](https://pastebin.com/FpxRbyTg)

</details>
