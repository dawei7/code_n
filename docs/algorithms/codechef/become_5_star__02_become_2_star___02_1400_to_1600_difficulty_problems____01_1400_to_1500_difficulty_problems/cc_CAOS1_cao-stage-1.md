# CAO Stage-1

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CAOS1 |
| Difficulty Rating | 1488 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CAOS1](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CAOS1) |

---

## Problem Statement

### Problem Statement

**Past**

In the year of 2048, the Virtual Reality Massively Multiplayer Online Role-Playing Game (VRMMORPG), **Code Art Online (CAO)**, is released. With the Chef Gear, a virtual reality helmet that stimulates the user's five senses via their brain, players can experience and control their in-game characters with their minds.

On August the 2nd, 2048, all the players log in for the first time, and subsequently discover that they are unable to log out. They are then informed by Code Master, the creator of CAO, that if they wish to be free, they must reach the second stage of the game.

Kirito is a known star player of CAO. You have to help him log out.

**Present**

*Stage 1*

A map is described by a 2D grid of cells. Each cell is either labelled as a **#** or a **^**. **#** denotes a wall. A monster exists in a cell if the cell is not a wall and the cell is a **centre of Prime-Cross (CPC)**.

- Let **L** be the number of contiguous **^** to the left of **X**, in the same row as **X**.

- **R** be the number of contiguous **^** to the right of **X**, in the same row as **X**.

- **T** be the number of contiguous **^** above **X**, in the same column as **X**.

- **B** be the number of contiguous **^** below **X**, in the same column as **X**.

A cell **X** is said to be a **CPC** if there exists a prime number **P** such that **P ≤ minimum of [L, R, T, B]**.

**Note:** While computing **L, R, T, B** for a cell **X**, you should not count the **^** of the cell **X**.

Given a map, you have to tell Kirito the number of cells where monsters exist.

**Future**

If you are done with this task, go help Kirito with Stage 2 :-)

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. Each case starts with a line containing two space separated integers **R, C** denoting the number of rows and columns in the map respectively. The next **R** lines contain **C** characters each, describing the map.

### Output

For each test case, output a single line containing the number of cells where monsters exist.

### Constraints

- 1 ≤ **T** ≤ 100

- 1 ≤ **R** ≤ 50

- 1 ≤ **C** ≤ 50

---

## Examples

**Example 1**

**Input**

```text
2
5 5
^^^^^
^^^^^
^^^^#
^^^^^
^^^^^
5 7
^^#^^^^
^^#^#^#
#^^^^^^
^^#^^#^
^^^^^^^
```

**Output**

```text
0
1
```

**Explanation**

**Example case 1.** There is no cell for which minimum of L, R, T, B is greater than some prime P.

**Example case 2.** The cell at [3, 4], (1-based indexing) is the only CPC.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5
^^^^^
^^^^^
^^^^#
^^^^^
^^^^^
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
5 7
^^#^^^^
^^#^#^#
#^^^^^^
^^#^^#^
^^^^^^^
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link:

[Practice](http://www.codechef.com/problems/CAOS1)

[Contest](http://www.codechef.com/SEPT13/problems/CAOS1)

# Difficulty:

Cakewalk

# Pre-requisites:

None

# Problem:

Given a matrix whose each entry is either ‘^’ or ‘#’, find the number of CPCs. A cell is CPC if it is filled with ‘^’, and there exists a prime P such that there are P or more consecutive '^'s on each of its four sides(i.e. left, right, top bottom).

# Explanation:

It is easy to see that since 2 is the smallest Prime, for a cell to be CPC, it is necessary and sufficient that

2 ? min(L, R, T, B)

Therefore, all you were supposed to do was to check the number of consecutive '^'s on each of its four sides is at least 2.

``
bool check-CPC(int i, int j) // 1 ? i ? n, 1 ? j ? m
    if mat[i][j] != '^'
        return false
    if i-2 < 1 or j-2 < 1 or i+2 > n or j+2 > m
        return false
    for (int x=-2; x<=2; x++)
        if mat[i+x][j] != '^' or mat[i][j+x] != '^'
            return false
    return true

``

We could also calculate the exact values of L, R, T, B and then check if its minimum is at least 2, but that will be covered in CAOS2 editorial.

# Setter’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/September/Setter/CAOS1.cpp)

# Tester’s Solution:

- Mahbub’s

``
(http://www.codechef.com/download/Solutions/2013/September/Tester/Tester1/CAOS1.cpp)
 2. Sergey's

``

([http://www.codechef.com/download/Solutions/2013/September/Tester/Tester2/CAOS1.cpp](http://www.codechef.com/download/Solutions/2013/September/Tester/Tester2/CAOS1.cpp))

# Editorialist’s Solution:

Can be found [here](http://www.codechef.com/download/Solutions/2013/September/Editorialist/CAOS1.cpp)

</details>
