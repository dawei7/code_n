# Snakes, Mongooses and the Ultimate Election

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SNELECTP |
| Difficulty Band | Greedy Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Additional Applications of Greedy Algorithms |
| Official Link | [SNELECTP](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA04/problems/SNELECTP) |

---

## Problem Statement

In Snakeland, there are some snakes and mongooses. They are lined up in a row. The information about how exactly they are lined up it is provided to you by a string of length **n**. If the i-th character of this string is 's', then it means that there is a snake at the i-th position, whereas the character 'm' denotes a mongoose.

You might have heard about the age-old rivalry between hares and tortoises, but in Snakeland, the rivalry between snakes and mongooses is much more famous. The snakes and the mongooses want to hold a final poll in which the ultimate winner of this age-old battle will be decided. If the snakes get more votes than the mongooses, they will be the ultimate winners. Similarly, if the mongooses get more votes than snakes, they will be the ultimate winners. Obviously, each animal is loyal to their species, i.e. each snake will vote for the snakes to be the ultimate champions and each mongoose for the mongooses.

Tomorrow's the election day. Before the elections, the mongooses decided to cheat. They planned that each mongoose will eat at most one of its neighbor snakes. Two animals are said to be neighbors of each other if they are consecutive to each other in the row. After this, the elections will be held. The mongooses planned in such a way that the number of snakes eaten is maximized. Can you find out who will win the final poll? Output "snakes", "mongooses" or "tie" correspondingly.

### Input

First line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follow.

The only line of each test case contains a string consisting of characters 's' and 'm'.

### Output

For each test case output a single line containing "snakes", "mongooses" or "tie" correspondingly (without quotes).

### Constraints

- 1 ≤ **T** ≤ 100

- 1 ≤ **|s|** ≤ 100

---

## Examples

**Example 1**

**Input**

```text
4
sm
ssm
sms
ssmmmssss
```

**Output**

```text
mongooses
tie
tie
snakes
```

**Explanation**

**Example 1**. The mongoose will eat the snake. Only the mongoose will be left. So, on the election day, there is one mongoose and zero snakes. So mongooses will win.

**Example 2**. The mongoose will eat the snake at position 2 (1-based indexing). One mongoose and one snake will be left. Hence, there will be a tie.

**Example 3**. The mongoose can eat either the snake to its left or to the right. But, it can eat only one of them. Afterwards, there will be a single snake and mongoose. So, it will result in a tie.

**Example 4**. The mongooses can eat at max two snakes. For example, s*mmm*sss, where * denotes the snakes that were eaten by mongooses. After this, we have four snakes and three mongooses. So, the snakes win.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
sm
```

**Output for this case**

```text
mongooses
```



#### Test case 2

**Input for this case**

```text
ssm
```

**Output for this case**

```text
tie
```



#### Test case 3

**Input for this case**

```text
sms
```

**Output for this case**

```text
tie
```



#### Test case 4

**Input for this case**

```text
ssmmmssss
```

**Output for this case**

```text
snakes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Snakes, Mongooses and the Ultimate Election in Greedy Algorithms](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA04/problems/SNELECTP)

### [](#problem-statement-1)Problem Statement:

In Snakeland, snakes (‘s’) and mongooses (‘m’) are lined up in a row. They will hold an election to decide the winner. Mongooses cheat by eating at most one neighboring snake before the vote.

You need to determine the winner after the mongooses eat the maximum possible number of snakes.

- If **snakes** outnumber mongooses, **snakes** win.

- If **mongooses** outnumber snakes, **mongooses** win.

- If both are equal, it’s a **tie**.

### [](#approach-2)Approach:

- **Observation**:

- Mongooses can eat at most one neighboring snake, either to the left or right, but not both.

- Our goal is to maximize the number of snakes eaten by mongooses before counting votes.

- **Simulating Mongooses Eating Snakes**:

- For each mongoose (`'m'`), check its immediate neighbors (left and right).

- If there’s a snake (`'s'`) next to it that hasn’t been eaten yet, the mongoose will eat that snake.

- This ensures that mongooses eat as many snakes as possible, which may reduce the number of snakes counted in the final election.

- **Counting Remaining Snakes and Mongooses**:

- After mongooses have eaten the maximum possible number of neighboring snakes, count how many snakes and mongooses are left.

- **Determine the Outcome**:

- Compare the final number of mongooses and snakes:

- If the number of mongooses is greater, mongooses win.

- If the number of snakes is greater, snakes win.

- If both numbers are equal, it results in a tie.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` Traversing the string `2 times` → `2*O(N)`

- **Space Complexity:** `O(1)`

</details>
