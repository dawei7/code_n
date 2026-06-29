# The Ball And Cups

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TAVISUAL |
| Difficulty Rating | 1306 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [TAVISUAL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/TAVISUAL) |

---

## Problem Statement

At the end of a busy day, The Chef and his assistants play a game together. The game is not just for fun but also used to decide who will have to clean the kitchen. The Chef is a Game Master, so his concern is how to manage the game but not how to win the game like his assistants do.

The game requires players to find the only ball under one of the **N** cups after their positions are changed in a special way. At the beginning of the game, The Chef places **N** cups in a row and put a ball under the **C**-th cup from the left (the cups are numbered from **1** to **N**). All players can see the initial position of the ball. Then Chef performs **Q** flip operations. Each flip operation is defined by two integers **L** and **R** such that **1 ≤ L ≤ R ≤ N** and consists in reversing the segment **[L, R]** of cups. Namely, Chef swaps **L**-th and **R**-th cups, **(L+1)**-th and **(R−1)**-th cups, and so on. After performing all the operations Chef asks his assistants to choose a cup that they think the ball is under it. Who can guess the position of the ball will win the game, and of course, the others will have to clean the kitchen.

The Chef doesn't want to check all the **N** cups at the end of the game. He notes down the value of **C** and the pairs **(L, R)** and asked you, the mastered programmer, to determine the cup that contains the ball.

### Input

The first line of the input contains a single integer **T**, denoting the number of test cases. The description of **T** test cases follows. The first line of each test case contains three space-separated integers **N**, **C** and **Q**, denoting the total number of cups, the initial position of the ball and the number of flip operations Chef will perform. Each of the following **Q** lines contains two space-separated integers **L** and **R**, denoting the ends of the segment of the current flip operation.

### Output

For each test case output on a separate line the final position of the ball.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **N** ≤ **100000** (**105**)

- **1** ≤ **C** ≤ **N**

- **1** ≤ **Q** ≤ **10000** (**104**)

- **1** ≤ **L** ≤ **R** ≤ **N**

---

## Examples

**Example 1**

**Input**

```text
1
5 2 3
1 4
3 5
1 5
```

**Output**

```text
1
```

**Explanation**

The row of cups at the beginning of the game and after each flip is shown below. Here **'-'** means an empty cup and **'B'** is the cup that hides the ball, the segment of flip is marked bold.
``
**-B--**-
--**B--**
**----B**
B----
``

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/TAVISUAL)

[Contest](http://www.codechef.com/COOK32/problems/TAVISUAL)

### DIFFICULTY

CAKEWALK

### PREREQUISITES

Ad Hoc

### PROBLEM

**N** cups are arranged in a line. There is a ball under one of the cups. You know initially which cup it was under.

Several operations of the following type are performed

**Flip the order of the cups starting from Lth position and ending at Rth position, inclusive**

Output the position of the ball after all the operations.

### QUICK EXPLANATION

The cups are numbered **1 to N** from left to right. For some given L and R, if the ball is currently at position x, such that

`L ? x ? R`

Then the new position of the ball is going to be

`L + R - x`

We will see why this is so below. The problem can thus be solved by the following snippet of code

`
Let x be the initial position of the ball

for each operation [L, R]
    if L ? x ? R
        x = L + R - x
`

### EXPLANATION

If **x** lies between **L** and **R**, let us derive the expression for the new position of **x**.

For this, we will imagine that we have a number line and each one of **L**, **R** and **x** are points on this number line. We will mark these points as **‘L’**, **‘R’** and **‘x’** respectively.

`
                   L            R
<----------0-------L--------x---R--------------->
                            x
`

**Step 1: Shift everything to the range [0, R-L]**

This can be performed by subtracting **L** from all the positions.

`
           L                 R
<----------0--------(x-L)---(R-L)--------------->
                     x
`

**Step 2: Flip all positions to the range [-R+L, 0]**

This can be performed by multiplying all the positions with **-1**.

`
             R                   L
<-----------(L-R)---(L-x)--------0-------------->
                     x
`

**Step 3: Shift back to the range [0, R-L]**

This can be performed by adding **R-L** to all the positions.

`
           R                 L
<----------0--------(R-x)---(R-L)--------------->
                     x
`

**Step 4: Shift back to the range [L, R]**

This can be performed by adding **L** to all the positions.

`
                   R                  L
<----------0-------L--------(L+R-x)---R--------->
                             x
`

Hence, we can solve the problem by finding the new position after each operation. Note that we do not need to perform any change if **x** does not fall within the boundaries of an operation.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK32/Setter/TAVISUAL.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK32/Tester/TAVISUAL.cpp).

</details>
