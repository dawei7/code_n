# Walk

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WALK |
| Difficulty Rating | 1247 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [WALK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/WALK) |

---

## Problem Statement

Chef and his girlfriend are going to have a promenade. They are walking along the straight road which consists of segments placed one by one. Before walking Chef and his girlfriend stay at the beginning of the first segment, they want to achieve the end of the last segment.

There are few problems:

-  At the beginning Chef should choose constant integer - the velocity of moving. It can't be changed inside one segment.

-  The velocity should be decreased by at least 1 after achieving the end of some segment.

-  There is exactly one shop on each segment. Each shop has an attractiveness. If it's attractiveness is **W** and Chef and his girlfriend move with velocity **V** then if **V** < **W** girlfriend will run away into the shop and the promenade will become ruined.

 Chef doesn't want to lose her girl in such a way, but he is an old one, so you should find the minimal possible velocity at the first segment to satisfy all conditions.

### Input

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a single integer **N** denoting the number of segments. The second line contains **N** space-separated integers **W1**, **W2**, ..., **WN** denoting the attractiveness of shops.

### Output

- For each test case, output a single line containing the minimal possible velocity at the beginning.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **N** ≤ **10^5**

- **1** ≤ **Wi** ≤ **10^6**

---

## Examples

**Example 1**

**Input**

```text
2
5
6 5 4 3 2
5
3 4 3 1 1
```

**Output**

```text
6
5
```

**Explanation**

**Example case 1.**

 If we choose velocity 6, on the first step we have 6 >= 6 everything is OK, then we should decrease the velocity to 5 and on the 2nd segment we'll receive 5 >= 5, again OK, and so on.

**Example case 2.**

 If we choose velocity 4, the promanade will be ruined on the 2nd step (we sould decrease our velocity, so the maximal possible will be 3 which is less than 4).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
6 5 4 3 2
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
5
3 4 3 1 1
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/WALK)

[Contest](http://www.codechef.com/MARCH14/problems/WALK)

**Author:** [Dmytro Berezin](http://www.codechef.com/users/berezin)

**Tester:** [Mahbubul Hasan](http://www.codechef.com/users/white_king)

**Editorialist:** [Jingbo Shang](http://www.codechef.com/users/shangjingbo)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Programming

### PROBLEM:

Given a sequence of numbers **W[0…N-1]**, find out a number **S**, such that **S - i >= W[i]** holds for all **0 <= i < N**.

### EXPLANATION:

It is easy to find out the choice of decreasing speed is to decrease it by 1 after each segment. So we can have the above problem.

After some transformations, the requirement is that **S >= W[i] + i** holds for all **0 <= i < N**. Therefore, simply let **S** be the maximum of **W[i]+i** is the best choice.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/2014/March/Setter/WALK.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2014/March/Tester/WALK.cpp).

</details>
