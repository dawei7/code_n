# Delivery Man

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TADELIVE |
| Difficulty Rating | 1980 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [TADELIVE](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/TADELIVE) |

---

## Problem Statement

Andy and Bob are the only two delivery men of Pizza-chef store. Today, the store received **N** orders.
It's known that the amount of tips may be different when handled by different delivery man.
More specifically, if Andy takes the **i**th order, he would be tipped **Ai** dollars and if Bob takes this order,
the tip would be **Bi** dollars.

They decided that they would distribute the orders among themselves to maximize the total tip money. One order will be handled by only
one person. Also, due to time constraints Andy cannot take more than **X** orders and Bob cannot take more than
**Y** orders. It is guaranteed that **X** + **Y** is greater than or equal to **N**, which means that all the orders can be handled
by either Andy or Bob.

Please find out the maximum possible amount of total tip money after processing all the orders.

### Input

- The first line contains three integers **N**, **X**, **Y**.

- The second line contains **N** integers. The **i**th integer represents **Ai**.

- The third line contains **N** integers. The **i**th integer represents **Bi**.

### Output

- Print a single integer representing the maximum tip money they would receive.

### Constraints

**All test:**

- **1** ≤ **N** ≤ **105**

- **1** ≤ **X**, **Y** ≤ **N**; **X** + **Y** ≥ **N**

- **1** ≤ **Ai**, **Bi** ≤ **104**

**10 points:**

- **1** ≤ **N** ≤ **20**

**30 points:**

- **1** ≤ **N** ≤ **5000**

**60 points:**

- **1** ≤ **N** ≤ **105**

---

## Examples

**Example 1**

**Input**

```text
5 3 3
1 2 3 4 5
5 4 3 2 1
```

**Output**

```text
21
```

**Explanation**

Bob will take the first three orders (or the first two) and Andy will take the rest (of course).

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/TADELIVE)

[Contest](http://www.codechef.com/LTIME19/problems/TADELIVE)

**Author:** [Tuan Anh](http://www.codechef.com/users/tuananh93)

**Tester:** [Gedi Zheng](http://www.codechef.com/users/stzgd)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Simple

### PREREQUISITES:

greedy

### PROBLEM:

Andy and Bob are pizza delivery guys. They take tips of A[i] and B[i] corresponding to the ith order. Note that

each order will be taken by only one person. Andy can take at most X orders and Bob can take Y.

You have to divide the orders between Andy and Bob such that total tips is maximized. You are also given a constraint that X + Y ? n,

which will guarantee that none of the orders will go unprocessed.

### QUICK EXPLANATION:

Primarily there are three possible solutions depending on the subtasks.

-

For passing the first subtask, you can directly use brute-force solution in which you will try to give each order to either Andy or Bob

while respecting the X and Y condition.

-

For passing the second subtask, you can use a dynamic programming solution having state f(i, j) denoting maximum total tip money

among the first i orders where Andy has taken j orders up to now.

-

For passing third subtask, you can use following greedy strategy. Sort all the orders by D[i] = ]|A[i] - B[i]|.

Process the order one by one in the above sorted order and assign each order to either Andy or Bob greedily depending on relation between

A[i] and B[i].

### EXPLANATION:

Let us start with subtasks in increasing order of difficulty.

# Subtask 1

Try brute force solution by assigning each order to either Andy or Bob. You can implement this method either recursively or using bitmasks.

For understanding about bitmask, you can refer to [this](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=bitManipulation) and [that](http://apps.topcoder.com/forums/?module=Thread&threadID=626172&start=0&mc=14#1034330) link.

**Pseudo Code**

Recursive brute force solution.

`
ans = 0;
// (i, totalTipMoney) signifies that upto now, i orders has been processed,
// and totalTipMoney is amount of total tip money for this particular assignment up to now.
rec(i, andyOrders, bobOrders, totalTipMoney) {
	if (i == N) {
		// i.e. all the orders has been processed
		if (andyOrders <= X && bobOrders <= Y) {
			// if the arrangement is valid.
			ans = max(ans, totalTipMoney);
		}
	} else {
		// try giving this order to Andy
		rec(i + 1, AndyOrders + 1, BobOrders, totalTipMoney + A[i]);
		// try giving this order to Bob
		rec(i + 1, AndyOrders, BobOrders + 1, totalTipMoney + B[i]);
	}
}
// inside main function
rec(0, 0, 0, 0);
// Now ans will be your required answer.
`

Recursive bit mask brute force solution.

`
ans = 0;
// we are iterating over all subsets of size N.
// If current bit of mask is zero, means that current order is given to Andy
// Otherwise it means that order is given to Bob.
for (mask = 0; mask < (1 << N); mask++) {
	cur = 0;
	// cur denotes the total tip money corresponding to this arrangement of orders.
	AndyOrders = 0;
	BobOrders = 0;
	for (i = 0; i < N; i++) {
		if (mask & (1 << i)) {
			cur += A[i]; // Andy takes the order.
			AndyOrders++;
		} else {
			cur += B[i]; // Bob takes the order.
			BobOrders++;
		}
	}
	if (andyOrders <= X && bobOrders <= Y) {
		ans = max(ans, cur);
	}
}
`

**Time Complexity**

For recursive solution, As total number of subsets of size N can be 2^N. (As each item can be either taken or not taken).

So overall time complexity will be O(2^N).

For bitmask solution, As we know total number of subsets of N items can be 2^N. For each subset (represented by mask),

we also execute an inner O(N) loop too. So overall time complexity will be O(2^N * N).

# Subtask 2

We will use a dynamic programming solution. Note that for dynamic programming solution, we need to visualize the process of

assigning orders from left to right. So we should think that we are kind of trying to assign the orders from left to right (ie.

from order 0 to order N - 1).

Assume that we are currently at ith position and we have decided the assignment of orders up to now (

i.e. up to (i - 1)th position).

Now what information do we need to know about the assignment done up to now? Do we really need the information about the exact

assignment of orders?

Or are we only interested in count of orders assigned to Andy and Bob. Note that we only need to know the number of orders

being assigned to Andy. We can find number of orders assigned to Bob easily because we know up to now i - 1 orders has been processed.

So number of orders of Bob will be i - 1 - number of orders of Andy.

So our state of dp solution will be dp(i, j) which denotes that up to first i orders, j of them has been assigned to Andy.

**Base Case**

i is equal to N, then as all the orders has been processed, tip money obtained from the remaining part will be zero.

**Transitions**

Now let us see the transitions. So we are currently at i^th position. For the current order, we will try both the possibilities ie.

we will try to give it to Andy or Bob both depending on whether their count of orders taken has not exceeded from the desired

limit (ie. X for Andy and Y for Bob).

**Pseudo Code**

`
dp(i, j) {
	if (memo[i][j] != -1) {
		return memo[i][j];
	}
	res = 0;
	if (i == N) {
		// all orders are processed.
		res = 0;
	} else {
		// Decide for order i.
		// If can give to Andy, try giving it.
		AndyOrders = j;
		if (AndyOrders + 1 <= X) {
			res = max(res, A[i] + dp(i + 1, j + 1));
		}
		// If can give to Bob, try giving it.
		BobOrders = i - j;
		if (BobOrders + 1 <= Y) {
			res = max(res, B[i] + dp(i + 1, j));
		}
	}
	memo[i][j] = res;
	return res;
}

// inside the main function.
fill the memo array with -1.
ans = dp(0, 0)
// ans will be desired answer.
`

Note that the above explained solution is using forward dp, you can very easily write backward dp too. Some times, backward dp is more

intuitive to understand.

**Backward dp**

f[i][j] = Maximum tip money that can be got in first i order where Andy has taken j orders.

We can make come to f[i][j] from following states.

// give this current order to Andy. Can only be done when j > 0 and j <= X.

f[i - 1][j - 1] + A[i] where j > 0 and j <= X.

// give this current order to Bob. Can only be done when (i - j) > 0 and (i - j) <= Y.

f[i - 1][j] + B[i] where j > 0 and j <= X.

We will simply take the max of these two states to get the answer for f[i][j].

**Pseudo Code**

`
// Asumming one based indexing.
int f[N + 1][X + 1];
for (int i = 1; i <= N; i++) {
	for (int j = 1; j <= X && j <= i; j++) {
		int x = 0;
		if (j <= X) {
			x = f[i - 1][j - 1] + A[i];
		}
		int y = 0;
		if ((i - j) <= Y) }{
			y = f[i - 1][j] + B[i];
		}
		dp[i][j] = max(x, y);
	}
}
int ans = 0;
for (int j = 0; j <= X; i++) {
	ans = max(dp[N][j]);
}
`

# Subtask 3

Let us denote D[i] = |A[i] - B[i]|. Now we will sort all the orders in decreasing order of D.

Now we will process the orders one by one.

We can have following two cases:

-

If A[i] > B[i], then we will try to assign it to Andy if possible (If after the assignment, limit of orders is not crossed).

Otherwise we will assign it to Bob.

-

If B[i] > A[i], then we will try to assign it to Bob if possible. Otherwise we will assign it to Andy.

Note that the condition X + Y >= n guarantees that we will be able to assign the order to one of the persons.

**Proof of the Solution**

Assume that for some i, A[i] > B[i] and you assigned order to Bob, loss encountered due to this assignment is D[i].

Similarly, for some i, B[i] > A[i] and you assigned order to Andy, loss encountered due to this assignment is D[i].

As we want to minimize the loss encountered, it is better to process the orders having high possible losses, because we can

try to reduce the loss in the starting part. There is no point of doing an order which is high loss after an order with less loss.

You can prove it easily by [exchange argument](http://www.cs.cornell.edu/Courses/cs482/2003su/handouts/greedy_exchange.pdf).

Note that this is an intuitive explanation, More formal proof can be made along the similar lines using loss parameter defined above.

**Pseudo Code**

`
// Create D array.
// Sort the orders in the decreasing order of D[i].
totalTipMoney = 0;
for (i = 0; i < n; i++) {
	if (A[i] > B[i]) {
		if (andyOrders + 1 <= X) {
			andyOrders++;
			totalTipMoney += A[i];
		} else {
			bobOrders++;
			totalTipMoney += B[i];
		}
	} else {
		if (bobOrders + 1 <= Y) {
			andyOrders++;
			totalTipMoney += B[i];
		} else {
			andyOrders++;
			totalTipMoney += A[i];
		}
	}
}
// totalTipMoney is our answer.
`

**Time Complexity**

As we are only sorting an array of size n using comparator using D array. We can use Quicksort and mergesort which

take O(n log n) time.

You can use sort function in C++ or Arrays.sort function in Java.

You can O(n^2) selection, insertion, bubble sort etc. to solve Subtask 1 and 2.

Note that in this problem, for sorting A and B using D array will require use of comparators.

For understanding comparators in C++, you can refer to following [article](http://codeforces.com/blog/entry/9604) written by me.

**Problems to Practice**

- [MUL Spoj](http://www.spoj.com/problems/MUL/)

- [COUNTARI Editorial Codechef](http://discuss.codechef.com/questions/3716/countari-editorial)

- [BUYLAND Editorial Codechef](http://discuss.codechef.com/questions/4168/buyland-editorial)

Please add more problems for practice !!

### AUTHOR’S, TESTER’S and Editorialist’s SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/LTIME19/Setter/TADELIVE.cpp)

[tester](http://www.codechef.com/download/Solutions/LTIME19/Tester/TADELIVE.cpp)

[editorialist](http://www.codechef.com/download/Solutions/LTIME19/Editorialist/TADELIVE.cpp)

</details>
