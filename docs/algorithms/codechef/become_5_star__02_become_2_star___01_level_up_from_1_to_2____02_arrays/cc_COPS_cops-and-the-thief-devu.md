# Cops and the Thief Devu

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COPS |
| Difficulty Rating | 1242 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [COPS](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/COPS) |

---

## Problem Statement

There are 100 houses located on a **straight line**. The first house is numbered 1 and the last one is numbered 100. Some **M** houses out of these 100 are occupied by cops.

Thief Devu has just stolen PeePee's bag and is looking for a house to hide in.

PeePee uses fast 4G Internet and sends the message to all the cops that a thief named Devu has just stolen her bag and ran into some house.

Devu knows that the cops run at a maximum speed of **x** houses per minute in a straight line and they will search for a maximum of **y** minutes. Devu wants to know how many houses are safe for him to escape from the cops. Help him in getting this information.

### Input

First line contains **T**, the number of test cases to follow.

First line of each test case contains 3 space separated integers: **M**, **x** and **y**.

For each test case, the second line contains **M** space separated integers which represent the house numbers where the cops are residing.

### Output

For each test case, output a single line containing the number of houses which are safe to hide from cops.

### Constraints

- 1 ≤ **T** ≤ 104

- 1 ≤ **x, y, M** ≤ 10

---

## Examples

**Example 1**

**Input**

```text
3
4 7 8
12 52 56 8
2 10 2
21 75
2 5 8
10 51
```

**Output**

```text
0
18
9
```

**Explanation**

**Test case $1$:** Based on the speed, each cop can cover $56$ houses on each side. These houses are:
- Cop in house $12$ can cover houses $1$ to $11$ if he travels left and houses $13$ to $68$ if he travels right. Thus, this cop can cover houses numbered $1$ to $68$.
- Cop in house $52$ can cover houses $1$ to $51$ if he travels left and houses $53$ to $100$ if he travels right. Thus, this cop can cover houses numbered $1$ to $100$.
- Cop in house $56$ can cover houses $1$ to $55$ if he travels left and houses $57$ to $100$ if he travels right. Thus, this cop can cover houses numbered $1$ to $100$.
- Cop in house $8$ can cover houses $1$ to $7$ if he travels left and houses $9$ to $64$ if he travels right. Thus, this cop can cover houses numbered $1$ to $64$.

Thus, there is no house which is not covered by any of the cops.

**Test case $2$:** Based on the speed, each cop can cover $20$ houses on each side. These houses are:
- Cop in house $21$ can cover houses $1$ to $20$ if he travels left and houses $22$ to $41$ if he travels right. Thus, this cop can cover houses numbered $1$ to $41$.
- Cop in house $75$ can cover houses $55$ to $74$ if he travels left and houses $76$ to $95$ if he travels right. Thus, this cop can cover houses numbered $55$ to $95$.

Thus, the safe houses are house number $42$ to $54$ and $96$ to $100$. There are $18$ safe houses.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 7 8
12 52 56 8
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2 10 2
21 75
```

**Output for this case**

```text
18
```



#### Test case 3

**Input for this case**

```text
2 5 8
10 51
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/COPS)

[Contest](http://www.codechef.com/COOK60/problems/COPS)

**Author:** [Devendra Agarwal](http://www.codechef.com/users/devuy11)

**Tester:** [Surya Kiran](http://www.codechef.com/users/adurysk)

**Editorialist:** [Amit Pandey](http://www.codechef.com/users/amitpandeykgp)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

There are 100 houses in a lane, numbered from 1 to 100. **N** cops are positioned in some houses. A cop’s running speed is h houses per second and he can run for at max t secs. Find number of houses where a thief can hide such that he won’t be caught by any of the cops.

### QUICK EXPLANATION:

For each house and each cop, we can check whether the cop can reach the house or not by checking whether distance between them is less than or equal to maximum distance a cop can travel (h * t). If some cop can reach a house, then the house is unsafe otherwise it is safe.

The editorial explains three methods of finding number of safe houses having time complexities of \mathcal{O}(H N), \mathcal{O}(H \, log N) and \mathcal{O}(H + N) respectively, where H denotes number of houses (is fixed to 100 in our problem) and N denotes the number of cops.

### Explanation

For a particular house, we want to find out whether this house can be checked by some cop or not. We know that a cop can cover a maximum of h * t inter-house distances in t secs. So, if the distance between the thief’s hiding house and cop’s house is less than or equal to h * t, then the cop can catch the thief. We just need to check whether the current house can be reached by any of the cops or not. If yes, then it is not safe otherwise it is safe.

So, we can describe the solution succinctly as follows.

`
ans = 0
for each house from 1 to 100:
    safe = true
    for each cop houses from 1 to N:
       if (the cop can reach the house)
          safe = false
    if (safe) ans += 1
`

Clearly the above implementation of the problem will take \mathcal{O}(100 * N) time.

### Faster Solution

Let us say thief is currently at house p and we want to check whether he will be safe in this house or not. If we can find the nearest cops in both directions of the lane from current house, then we just need to check whether these nearest cops in either direction can reach the house p in time or not.

We will describe a method for finding nearest cop in forward direction faster than \mathcal{O}(N) time. Backward direction can be handled similarly.

Let us can create a sorted array of houses of cops. We want to find the first element in the array having value \geq p. This can be done by using binary search over the array. Time complexity of this will be \mathcal{O}(N) per search operation in array.

You can also find the same thing using \mathtt{lower}_\mathtt{bound} in *set* in C++. *set* maintain a balanced binary search tree underneath it, which takes \mathcal{O}(log N) time for each \mathtt{lower}_\mathtt{bound} query.

So, this solution runs in \mathcal{O}(100 * log N) time. Can we make it faster?

### Even Faster Solution

We have to find nextCopHouse/prevCopHouse information for each house faster. Let us see how can find nextCopHouse information faster. Let us make a boolean array isCop of size 100 where isCop[i] denotes that there is a cop in i-th house or not.

Now, we go from house number 100 to 1 and update the nextCopHouse information by maintaining the position of latest house having cop in it.

`
latestHouseHavingCop = -1;
for house p from 100 to 1:
    if (there is a cop in the house):
        latestHouseHavingCop = p;
    nextCopHouse[p] = latestHouseHavingCop;
`

Time complexity of this solution is \mathcal{O}(N + 100).

### AUTHOR’S, TESTER’S SOLUTIONS:

[setter’s solution](http://www.codechef.com/download/Solutions/COOK60/Setter/COPS.cpp)

[tester’s solution](http://www.codechef.com/download/Solutions/COOK60/Tester/COPS.cpp)

</details>
