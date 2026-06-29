# Forest Gathering

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FORESTGA |
| Difficulty Rating | 1829 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [FORESTGA](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/FORESTGA) |

---

## Problem Statement

Chef is the head of commercial logging industry that recently bought a farm containing **N** trees. You are given initial height of the i-th tree by **Hi** and the rate of growth of height as **Ri** meters per month. For simplicity, you can assume that all the trees are perfect cylinders of equal radius. This allows us to consider only the height of trees when we talk about the amount of wood.

In Chef's country, laws don't allow one to cut a tree partially, so one has to cut the tree completely for gathering wood. Also, laws prohibit cutting trees of heights (strictly) lower than **L** meters.

Today Chef received an order of **W** meters (of height) of wood. Chef wants to deliver this order as soon as possible. Find out how minimum number of months he should wait after which he will able to fulfill the order. You can assume that Chef's company's sawing machines are very efficient and take negligible amount of time to cut the trees.

### Input

There is a single test case per test file.

The first line of the input contains three space separated integers **N**, **W** and **L** denoting the number of trees in the farm, the amount of wood (in meters) that have to be gathered and the minimum allowed height of the tree to cut.

Each of next **N** lines contain two space separated integers denoting **Hi** and **Ri** respectively.

### Output

Output a single integer denoting the number of months that have to pass before Chef will be able to fulfill the order.

### Constraints

- **1** ≤ **N** ≤ **105**

- **1** ≤ **W**, **L** ≤ **1018**

- **1** ≤ **Hi**, **Ri** ≤ **109**

### Subtasks

- **Subtask #1 [40 points]:** **1 ≤ ** **N**, **W**, **L** ≤ **104**

- **Subtask #2 [60 points]:** No additional constraints

---

## Examples

**Example 1**

**Input**

```text
3 74 51
2 2
5 7
2 9
```

**Output**

```text
7
```

**Explanation**

After **6** months, heights of each tree will be **14**, **47** and **56** respectively. Chef is allowed to cut only the third tree, sadly it is not enough to fulfill an order of 74 meters of wood.

After **7** months, heights of each tree will be **16**, **54** and **65** respectively. Now Chef is allowed to cut second and third trees. Cutting both of them would provide him **119** meters of wood, which is enough to fulfill the order.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/MAY16/problems/FORESTGA)

[Practice](http://www.codechef.com/problems/FORESTGA)

**Author:** [Maksym Bevza](http://www.codechef.com/users/cenadar)

**Tester:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

**Translators:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666) (Russian), [Team VNOI](http://www.codechef.com/users/vnoi) (Vietnamese) and [Hu Zecong](http://www.codechef.com/users/huzecong) (Mandarin)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Easy

### PREREQUISITES:

Binary search

### PROBLEM:

There are N trees. The initial height of the i th tree is H_i meters, and the height increases R_i meters per month.

A tree with height lower than L cannot be cut. What is the fewest number of months before the Chef can cut W meters of height of wood?

### QUICK EXPLANATION:

Binary search the answer.

However, in some languages, you need to take care of some overflow issues. These will be addressed below.

### EXPLANATION:

The most straightforward solution for this that I can think of is to just loop through the number of months, say t, and then check if there is enough wood after this number of months. Checking is simple: For each tree, we know that after t months its height is H_i + R_it, so if this height is \ge L, then we can add this height to the total amount of height of wood we can cut. Then we just compare the total wood we have with W.

The following C++ code illustrates this:

``#include <stdio.h>
#define N 100111
#define ll long long

int n;
ll H[N];
ll R[N];
ll W, L;

bool can_cut(ll time) {
    ll total_cut = 0;
    for (int i = 0; i < n; i++) {
        ll height = H[i] + R[i] * time;
        if (height >= L) total_cut += height;
    }
    return total_cut >= W;
}

int main() {
    scanf("%d%lld%lld", &n, &W, &L);
    for (int i = 0; i < n; i++) {
        scanf("%lld%lld", &H[i], &R[i]);
    }
    ll time = 0;
    while (!can_cut(time)) time++;
    printf("%lld\n", time);
}
``

Unfortunately, this doesn’t work for the second subtask because the answer can be very large. Indeed, it can reach up to 10^{18}-1, and there’s not enough time to even loop up to 10^{12}!

We need to find an insight that will improve our solution. Here’s the key insight: **If there’s enough wood at time t, then there’s enough wood at time t+1**, and indeed for every t' such that t' > t. In other words, the amount of wood only increases with time.

This simple fact actually allows us to use **binary search** to find the answer! Because suppose we know that the answer lies in the range [t_L,t_R]. Let t_M be a time somewhere within [t_L,t_R]. Then:

- If there’s enough wood at time t_M, then the answer is in [t_L,t_M].

- If there isn’t enough wood at time t_M, then the answer is in [t_M+1,t_R].

Thus, if we choose t_M to be roughly in the middle of the range [t_L,t_R], then checking once on t_M will **reduce the range’s size by roughly half.** Thus, if A is the size of the range where the solution can be, then there will just be O(\log A) checks before the range becomes of size 1, at which point we already know the answer!

The following pseudocode shows how to do it.

``t_L = -1
t_R = 10^18

while t_R - t_L > 1:
    t_M = (t_L + t_R) / 2
    if can_cut(t_M):
        t_R = t_M
    else:
        t_L = t_M

print t_R
``

Note that t_L and t_R in this binary search is slightly different; the range containing the solution is *not* [t_L,t_R], rather it is (t_L,t_R] (or \{t_L+1,t_L+2,\ldots,t_R-1,t_R\}), and the solution maintains the invariant that `can_cut(t_L) == false` and `can_cut(t_R) == true`.

Since `can_cut` runs in O(N) time, and \log_2 10^{18} \le 64 so `can_cut` is only called a few times, this solution runs fast enough for the time limit!

# Pitfalls

While mathematically correct, the solution above suffers from some pitfalls. One common mistake might be setting the bounds, especially the lower bound. Notice that in the pseudocode above I set `t_L = -1`. This is because a solution of 0 is possible! This is when the amount of wood is enough to begin with, so we don’t even need to wait.

The next possible source of error is **arithmetic overflow**. Notice that we’re dealing with large integers here; large enough to potentially overflow 64-bit integers. (In some languages such as Python, this doesn’t occur.) There are a few places where overflow may occur:

- If `time` is large enough, then `H[i] + R[i] * time` may overflow. To fix this, you can replace the statement `if (H[i] + R[i] * time >= L)` with `if (time >= (L - H[i]) / R[i])`. Notice that there’s no multiplication.

-
`total_cut` may overflow. To fix this, return `true` as soon as `total_cut` exceeds `W`. This is to avoid further increases in `total_cut` which may trigger overflow.

An additional technique to further defend against overflow is to **dynamically find the upper bound** by doubling. In other words, we add an initial step where we try to find a suitably small upper bound, but using just a few steps. Here’s a pseudocode:

``t_L = -1

// compute t_R by doubling
t_R = 1
while !can_cut(t_R):
    t_R *= 2

// now, binary search
while t_R - t_L > 1:
    t_M = (t_L + t_R) / 2
    if can_cut(t_M):
        t_R = t_M
    else:
        t_L = t_M

print t_R
``

Using this, we can be sure that `t_R` is at most twice the solution, so our upper bound isn’t that far off.

### Time Complexity:

O(N \log \text{ans})

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](http://www.codechef.com/download/Solutions/MAY16/Setter/FORESTGA.py)

[Tester](http://www.codechef.com/download/Solutions/MAY16/Tester/FORESTGA.py)

</details>
