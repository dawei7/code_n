# Gravity Guy

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GRGUY |
| Difficulty Rating | 1568 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [GRGUY](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/GRGUY) |

---

## Problem Statement

Chef likes to play games a lot. Gravity Guy is one such interesting game.

"*Gravity Guy is an arcade side-scrolling game in which the player controls Gravity Guy by tapping the screen to switch gravity. The objective in this game is to run as far as possible while avoiding being trapped by obstacles, falling, or flying off the screen. If hit by obstacles, the game is over.*"

Chef is so addicted to this game that each night he dreams of himself being in the game as Gravity Guy. He has two lanes in front of him represented by two strings of equal length named as **L1** and **L2**. Each of the two lanes consists of some clean blocks represented by **'.'** and some dirty blocks represented by **'#'**.

Chef can start running from the beginning of any of the two lanes and cannot step over any dirty block **( '#' )** encountered during his journey. He has to complete his journey by reaching the end block of any of the two lanes.

Chef can use the following jumps to reach his destination. Considering chef is at **xth** block of some lane.

- He can jump to **x+1th** block of the same lane.

- He can switch gravity quickly and jump to **xth** block of the other lane.

- He can switch gravity and jump to **x+1th** block of the other lane.

You have to tell him whether he can reach his destination or not. If it is possible for him to reach his destination, then Chef is interested in knowing the minimum number of gravity switches required to reach the destination.

### Input

First line of input contains a single integer **T** denoting the number of test cases. Each test case consists of **2** lines. First line of each test case contains a string denoting lane **L1**. Second line of each test case contains a string denoting lane **L2**.

### Output

For each test case, print **"Yes"** (without quotes) in the first line if Chef is able to reach the destination followed by a line containing an integer denoting minimum number of gravity switches required to reach to the destination. Print a single line containing the word **"No"** (without quotes) otherwise.

### Constraints

- **1 ≤ T ≤ 105**

- **1 ≤ |L1| ≤ 2 × 105**, where **|S|** denotes the length of string **S**

- **|L1| = |L2|**

### Subtasks

**Subtask 1 (25 points)**

- Sum of **|L1|** over all test cases in one file it at most **200**.

- Only "Yes"/"No" response will be evaluated.

**Subtask 2 (25 points)**

- Sum of **|L1|** over all test cases in one file it at most **200**.

**Subtask 3 (25 points)**

- Sum of **|L1|** over all test cases in one file it at most **106**.

- Only "Yes"/"No" response will be evaluated.

**Subtask 4 (25 points)**

- Sum of **|L1|** over all test cases in one file it at most **106**.

---

## Examples

**Example 1**

**Input**

```text
3
#...#
.###.
#.#.#.
.#.#.#
#...
#...
```

**Output**

```text
Yes
2
Yes
5
No
```

**Explanation**

**Test case $1$:** Chef will start his journey from $L_2$. He switches gravity and jumps to $L_1$. He continues on $L_1$ till block $4$ and then again switch gravity and jump to block $5$ of $L_2$. Therefore, he requires total $2$ gravity switches to reach the destination.

**Test case $2$:** Chef will start his journey from $L_2$. He switches gravity and jumps to second block of $L_1$. He switches gravity and jumps to third block of $L_2$. He switches gravity and jumps to fourth block of $L_1$. He switches gravity and jumps to fifth block of $L_2$. He switches gravity and jumps to sixth block of $L_1$. Therefore, he requires total $5$ gravity switches to reach the destination.

**Test case $3$:** Chef cannot start his journey as starting block of both the lanes $L_1$ and $L_2$ are dirty and he cannot step over them.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/AUG15/problems/GRGUY)

[Practice](http://www.codechef.com/problems/GRGUY)

**Author:** [Sunny Agarwal](http://www.codechef.com/users/ma5termind)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Simple

### PREREQUISITES:

Greedy, dynamic programming

### PROBLEM:

There are two lanes L_1 and L_2, each containing N blocks, and L_1 is on top of L_2. Chef starts running from the beginning of (any) one of the lanes and must reach the end of any lane. To do so, Chef can use the following jumps (assuming he’s currently at the x th block of some lane):

- Go to the $(x+1)$th block of the same lane.

- Switch gravity and go to the x th block of the other lane.

- Switch gravity and go to the $(x+1)$th block of the other lane.

Some of the blocks are dirty, which means Chef cannot step over them.

You need to know whether Chef can reach the end and if so, what is the minimum number of **gravity switches** necessary.

### QUICK EXPLANATION:

The second kind of jump is not helpful, so we only use the first and third. It’s also not helpful to switch lanes unless there is an obstacle to avoid. With this in mind, there is one obvious optimal path that we should consider (i.e. switch lanes only if necessary):

- There is no path to the end path if and only if there is a column where both lanes contain dirty blocks.

- If there is a lane containing no dirty blocks, then the minimum number of gravity switches is 0.

- Otherwise, start at the lane whose first dirty block appears later. Only switch lanes if the next block in the current lane is dirty. The number of steps taken is the answer.

There’s also a dynamic programming approach: let D_1(x) and D_2(x) be the fastest way to reach the x th block of lanes L_1 and L_2, respectively. Then:

- The answer is \min(D_1(N), D_2(N))

- We have the recurrences:

D_1(x) = \begin{cases}
\infty & \text{if $L_1(x)$ is dirty} \\\
\min(D_1(x-1), D_2(x-1)+1) & \text{otherwise}
\end{cases}

D_2(x) = \begin{cases}
\infty & \text{if $L_2(x)$ is dirty} \\\
\min(D_2(x-1), D_1(x-1)+1) & \text{otherwise}
\end{cases}

We define D_1(0) = D_2(0) = 0 as base cases.

By making two arrays D_1 and D_2 of length N, we can compute these values by increasing x in O(N) time.

### EXPLANATION:

Let’s give some names to the different kinds of jumps.

-
**Forward**: Go to the $(x+1)$th block of the same lane.

-
**Quick switch**: Switch gravity and go to the x th block of the other lane.

-
**Slow switch**: Switch gravity and go to the $(x+1)$th block of the other lane.

The first thing to notice is that “quick switch” is not helpful. Let’s see why this is so, by considering the various possible jumps immediately after doing a quick switch. Let’s assume that Chef is at position L_1(x) (the case L_2(x) is essentially the same).

- If the next jump is a “forward”, then you went from L_1(x) to L_2(x+1) with one gravity switch. But this is just like doing a “slow switch”! If we do a single “slow switch” instead, the number of gravity switches stays the same, and we skipped passing through the block L_2(x) (which is actually better in case L_2(x) is dirty).

- If the next jump is a “slow switch”, then you went from L_1(x) to L_1(x+1) with two gravity switches. But we can instead do a single “forward” move without doing any gravity switches! (and we skipped passing through the block L_2(x) which is helpful as explained in the previous bullet)

- If the next jump is another “quick switch”, then you just went back to your original position while incurring two gravity switches. Clearly, doing two quick switches in a row is just a waste of effort.

Thus, we have shown that forwards and slow switches are the only kinds of jumps we have to consider.

# A greedy approach

The remaining kinds of jumps have the property that each jump takes Chef one column to the right. In fact, we can derive a few more properties of optimal paths:

- It’s not optimal to slow switch if there is no obstacle to avoid. More specifically, if you did a slow switch, then a sequence of k forwards, and another slow switch, but there weren’t any dirty blocks that were avoided in the process, then you can just replace that sequence with a sequence of k+2 forward switches. This saves you two gravity switches

- It’s always better to start at the lane whose first dirty block appears later, or doesn’t appear at all. This is because if you start at the other lane, you are forced to do a slow switch which you could have avoided by simply starting at the other lane.

So we now have the following **greedy** solution to the problem:

- There is no path to the end path if and only if there is a column where both lanes contain dirty blocks.

- If there is a lane containing no dirty blocks, then the minimum number of gravity switches is 0.

- Otherwise, start at the lane whose first dirty block appears later, and simulate the path by trying to do only “forward” steps. Only use “slow switch” if the next block is dirty. The number of steps taken is the answer.

# A dynamic programming approach

Another standard way to approach the problem is to use the ever-powerful **dynamic programming**. For some people this is simpler, because it involves less thinking about the shape of the optimal path.

Let’s define the **distance** of a block to be the minimum number of gravity switches needed to reach that block (in case the block is unreachable, we say the distance is \infty). Then let D_1(x) and D_2(x) be the distances of blocks L_1(x) and L_2(x), respectively.

Notice that the final answer is simply \min(D_1(N), D_2(N)), because we want to reach either L_1(N) or L_2(N) as fast as possible. Now, let’s focus on D_1(x).

If L_1(x) is dirty, then of course there’s no way to reach that cell (you can’t even step on it!), so we immediately know that D_1(x) = \infty. Otherwise, the last move must have been either a “forward” or a “slow switch”.

- If it was a forward, then you arrived at L_1(x-1) to get to L_1(x). The minimum number of gravity switches required for this is D_1(x-1).

- If it was a slow switch, then you arrived at L_2(x-1) to get to L_1(x). The minimum number of gravity switches required for this is D_2(x-1) + 1 (the +1 is due to the last move which uses one gravity switch).

Therefore, we have the following:

D_1(x) = \begin{cases}
\infty & \text{if $L_1(x)$ is dirty} \\\
\min(D_1(x-1), D_2(x-1)+1) & \text{otherwise}
\end{cases}

The case is very similar for D_2(x), i.e.:

D_2(x) = \begin{cases}
\infty & \text{if $L_2(x)$ is dirty} \\\
\min(D_2(x-1), D_1(x-1)+1) & \text{otherwise}
\end{cases}

These formulas enable us to compute D_1(x) and D_2(x) from D_1(x-1) and D_2(x-1) recursively!

But what about the base cases? We can compute D_1(1) and D_2(1) easily by considering that Chef can start at either L_1(1) or L_2(1) without doing any move (as long as the block is not dirty of course!). Thus:

D_1(1) = \begin{cases}
\infty & \text{if $L_1(1)$ is dirty} \\\
0 & \text{otherwise}
\end{cases}

D_2(1) = \begin{cases}
\infty & \text{if $L_2(1)$ is dirty} \\\
0 & \text{otherwise}
\end{cases}

But we can make the base case simpler by **adding a clean block at the beginning of both lanes**! This doesn’t worsen the solution, because you can just start at the same lane you would have started originally, and do a “forward” move, without incurring additional gravity switches. Thus, we define two new blocks L_1(0) and L_2(0) as clean blocks, and define D_1(0) = D_2(0) = 0 as the base cases!

We now have all the ingredients for our solution. First, we build two (0-indexed) arrays, D_1 and D_2, each of length N+1. Then, set D_1[0] = D_2[0] = 0. Next, compute D_1[x] and D_2[x] for 1 \le x \le N in increasing order, based on the recurrences above. Finally, the answer is now \min(D_1[N], D_2[N])! (If this value is infinite, then the answer is `No`)

# Implementation details / optimizations

**Handling \infty**

Notice that the value \infty is used in our arrays D_1 and D_2. But most builtin types (such as `int` or `long`) do not have infinite values. Here are possible ways to handle that:

- Use a dummy value such as “-1” in place of infinity. I don’t recommend this though, because you’ll have to check for the value “-1” all the time (for example, you need to modify the `min` function because infinity should be larger than all other elements).

- Define “infinity” to be some large value. Some possibilities are 10^9, 2^{30}, 2^{60} or the data type’s upper limit. This has the advantage that comparisons of infinity against normal values are correct. However, one should be careful in comparing “infinite” values against each other. Also, be careful in doing arithmetic with this “infinity”, because you might incur overflow!

- Use the “float” or “double” data type which have infinite values.

I prefer the second solution.

**Memory-efficient DP**

The solution above requires us to create two arrays, D_1 and D_2. However, notice that when computing D_1[x] and D_2[x], we only need the values of D_1[x-1] and D_2[x-1]. Therefore, we only need to store the current and previous values of D_1 and D_2, reducing the memory requirements from O(N) to O(1) (disregarding the memory where the input is stored)!

# Sample implementations

Finally, here we provide some implementations of the solution. The DP solutions use a large number for “infinity”, and also use O(1) additional memory.

Python (Greedy approach):

``INF = 1<<30 # some really large number
for cas in xrange(input()):
    L1 = raw_input()
    L2 = raw_input()
    ans = 0
    curr = 0
    for L1x, L2x in zip(L1, L2):
        if L1x == L2x == '#':
            ans = INF
            break

        if L1x == '#':
            if curr == 1:
                ans += 1
            curr = 2
        if L2x == '#':
            if curr == 2:
                ans += 1
            curr = 1

    if ans >= INF:
        print "No"
    else:
        print "Yes"
        print ans
``

C++ (Greedy approach):

``#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define LIM 200011
#define INF LIM<<3

char words[2][LIM];
int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        scanf("%s%s", words[0], words[1]);
        int n = strlen(words[0]);
        int curr = -1, ans = 0;
        for (int i = 0; i < n; i++) {
            bool dirty0 = words[0][i] == '#';
            bool dirty1 = words[1][i] == '#';
            if (dirty0 && dirty1) {
                ans = INF;
                break;
            }
            if (dirty0) {
                if (curr == 0) ans++;
                curr = 1;
            }
            if (dirty1) {
                if (curr == 1) ans++;
                curr = 0;
            }
        }
        if (ans >= INF) {
            printf("No\n");
        } else {
            printf("Yes\n%d\n", ans);
        }
    }
}
``

Python (DP approach):

``INF = 1<<30 # some really large number
for cas in xrange(input()):
    L1 = raw_input()
    L2 = raw_input()
    D1 = D2 = 0
    for L1x, L2x in zip(L1, L2):
        D1, D2 = (
            INF if L1x == '#' else min(D1, D2 + 1),
            INF if L2x == '#' else min(D2, D1 + 1),
        )
    ans = min(D1, D2)
    if ans >= INF:
        print "No"
    else:
        print "Yes"
        print ans
``

C++ (DP approach):

``#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define LIM 200011
#define INF (LIM<<3)

char L[2][LIM];
int D[2];
int nD[2];
int main() {
    int z;
    scanf("%d", &z);
    while (z--) {
        scanf("%s%s", L[0], L[1]);
        int n = strlen(L[0]);
        D[0] = D[1] = 0;
        for (int i = 0; i < n; i++) {
            nD[0] = L[0][i] == '#' ? INF : min(D[0], D[1] + 1);
            nD[1] = L[1][i] == '#' ? INF : min(D[1], D[0] + 1);
            D[0] = nD[0];
            D[1] = nD[1];
        }
        int ans = min(D[0], D[1]);
        if (ans >= INF) {
            printf("No\n");
        } else {
            printf("Yes\n%d\n", ans);
        }
    }
}
``

### Time Complexity:

O(N)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/AUG15/Setter/GRGUY.cpp)

[tester](http://www.codechef.com/download/Solutions/AUG15/Tester/GRGUY.cpp)

</details>
