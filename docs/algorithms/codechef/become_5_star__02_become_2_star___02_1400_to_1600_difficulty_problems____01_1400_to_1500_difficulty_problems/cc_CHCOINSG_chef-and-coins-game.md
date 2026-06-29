# Chef and Coins Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHCOINSG |
| Difficulty Rating | 1442 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CHCOINSG](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CHCOINSG) |

---

## Problem Statement

Chef is playing a game with his friend Misha. They have a pile containg **N** coins. Players take alternate turns, removing some coins from the pile. On each turn, a player can remove either one coin or coins equal to some prime power (i.e. **px** coins, where **p** - prime number and **x** - positive integer). Game ends when the pile becomes empty. The player who can not make a move in his turn loses.

Chef plays first. Your task is to find out who will win the game, provided that both of the player play optimally.

### Input

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The only line of each test case contains one integer **N**.

### Output

- For each test case, output a single line containing one word - the name of the winner of the game. Print "Chef" (without quotes) if Chef wins the game, print "Misha" (without quotes) otherwise.

### Constraints

- **1** ≤ **T** ≤ **1000**

- **1** ≤ **N** ≤ **109**

### Subtasks

**Subtask #1 (20 points): **

- **1** ≤ **N** ≤ **10**

**Subtask #2 (30 points): **

- **1** ≤ **N** ≤ **104**

**Subtask #3 (50 points): **No additional constraints.

---

## Examples

**Example 1**

**Input**

```text
2
1
8
```

**Output**

```text
Chef
Chef
```

**Explanation**

**Example case 1.** Chef will remove the only coin from the pile and will win the game.

**Example case 2.** Chef will remove all 8 coins from the pile and win the game. Chef can remove 8 coins because 8 is a prime power, as 8 = 23.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
Chef
```



#### Test case 2

**Input for this case**

```text
8
```

**Output for this case**

```text
Chef
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/JUNE16/problems/CHCOINSG)

[Practice](http://www.codechef.com/problems/CHCOINSG)

**Author:** [Vasya Antoniuk](http://www.codechef.com/users/dpraveen)

**Testers:** [Istvan Nagy](http://www.codechef.com/users/iscsi)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Simple

### PREREQUISITES:

finding pattern, game theory, understanding of winning and losing positions

### PROBLEM:

You have a pile containing n coins.

Two players play following game alternately. Each player in its turn can remove any prime power number of coins from the pile, i.e. p^x, s.t. p is a prime and x \geq 0. The player who can’t make his move loses the game. Find who wins the game.

### QUICK EXPLANATION:

Second player will win iff N \, \% \, 6 = 0, otherwise first player will win.

### EXPLANATION:

**Solution based on finding pattern**

We can find a pattern by writing a slow code to find the winner of the game for small numbers, say \leq 100. You can just implement the basic definition of winning/losing position in the game theory by writing a simple dp.

**More formal solution**

Let us try to see what happens for the game on some small examples.

For n = 1, first player will win.

For n = 2, 3, 5, first player will win as these numbers are prime.

For n = 4, the first player will also win as 4 = 2^2.

For n = 6, player can not remove 6 coins in his first turn, as 6 is not a prime power. Hence, whatever number of coins first player removes, he will end up with 1, 2, \dots, 5 coins, all of which are a wining positions for the other person. Hence, n = 6 is losing position for first player.

You can notice that numbers from n = 7 to 11, are also winning positions, as the first player can make a move such that remaining number of coins in the pile are equal to 6, which is a losing position.

For n = 12, the first player can win if he can move to some losing position, i.e. he could remove either 6 or 12 coins. He can’t remove any of these as they are not prime powers. So n = 12 is a losing position.

Similarly any multiple of 6 is a losing position, as you can’t make a move from n = 6 * k to any losing position, as you have to remove coins equal to some multiple of 6. A multiple of 6 can’t be a prime power, as 6 = 2 * 3.

### Time Complexity:

\mathcal{O}(1) - Just check whether N \, \% 6 \, = 0 or not.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](http://www.codechef.com/download/Solutions/JUNE16/Setter/CHCOINSG.cpp)

[Tester](http://www.codechef.com/download/Solutions/JUNE16/Tester/CHCOINSG.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/JUNE16/Editorialist/CHCOINSG.py)

</details>
