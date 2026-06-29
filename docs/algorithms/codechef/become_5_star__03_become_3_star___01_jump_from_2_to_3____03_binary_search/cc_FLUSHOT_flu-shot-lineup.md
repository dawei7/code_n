# Flu Shot Lineup

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLUSHOT |
| Difficulty Rating | 1692 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [FLUSHOT](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/FLUSHOT) |

---

## Problem Statement

A new strain of flu has broken out. Fortunately, a vaccine was developed very quickly and is now being administered to the public. Your local health clinic is administering this vaccine, but the waiting line is very long.

For safety reasons, people are not allowed to stand very close to each other as the flu is not under control yet. However, many people were not aware of this precaution. A health and safety official recently examined the line and has determined that people need to spread out more in the line so that they are at least T units away from each other. This needs to be done as quickly as possible so we need to calculate the minimum distance D such that it is possible for every person to move at most D units so the distance between any two people is at least T. Specifically, D should be the minimum value such that there are locations x'i so that |xi - x'i| ≤ D for each person i and |x'i - x'j| ≥ T for any two distinct people i,j. Furthermore, since nobody can move past the receptionist we must also have that x'i ≥ 0.

The location of each person is given by the number of meters they are standing from the receptionist. When spreading out, people may move either forward or backward in line but nobody may move past the location of the receptionist.

### Input

The first line of input contains a single integer K ≤ 30 indicating the number of test cases to follow. Each test case begins with a line containing an integer N (the number of people) and a floating point value T (the minimum distance that should be between people). The location of each person i is described by single floating point value xi which means person i is xi meters from the receptionist. These values appear in non-decreasing order on the following N lines, one value per line.

Bounds: 1 ≤ N ≤ 10,000 and T and every xi is between 0 and 1,000,000 and is given with at most 3 decimals of precision.

### Output

For each test case, you should output the minimum value of D with exactly 4 decimals of precision on a single line.

---

## Examples

**Example 1**

**Input**

```text
3
2 4
1
2
2 2
1
2
4 1
0
0.5
0.6
2.75
```

**Output**

```text
2.0000
0.5000
1.4000
```

**Explanation**

**Test case $1$:** To maintain a distance of $4$ units, the first person can move to location $0$ and the second can move to location $4$. The maximum distance a person has to move is $2$.

**Test case $2$:** To maintain a distance of $2$ units, the first person can move to location $0.5$ and the second person can move to location $2.5$. The maximum distance a person has to move is $0.5$.

**Test case $3$:** To maintain a distance of $1$ unit, the first person does not move, the second moves to location $1$, the third moves to location $2$, and the fourth moves to location $3$. The corresponding distances moved by each of them is $0, 0,5, 1.4,$ and $0.25$ respectively. Thus, the maximum distance moved by any person is $1.4$ moved by the third person.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/FLUSHOT/)

[Contest](http://www.codechef.com/JAN11/problems/FLUSHOT/)

### DIFFICULTY

EASY

### EXPLANATION

The problem can be solved with a binary search approach. Given a value D, we can efficiently determine if there is a way to move each person with distance at most D or not. The idea is that we can assume that the left-most person moved as far left as they can. Then, the second person moves as far left as they can up to distance D or until they are T units next to the first person. Basically, the first person moves to x’ _ 1 := max(0, x _ 1-D) and every subsequent person i moves to x’ _ i := max(x’_ {i-1}+T, x _ i-D). If this max ever moves someone more than D units to the right, then we report that distance D is not sufficient. Otherwise, we report that distance D is ok. Of course, if

distance D suffices then any distance D’ >= D will also work so the binary search approach will succeed.

The output precision was chosen to be 4 decimals because the input precision was 3 decimals and one can argue that the solution is always

an integer multiple of 0.0005. It’s a fun exercise.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/January/Setter/Flushot.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2011/January/Tester/Flushot.cpp).

</details>
