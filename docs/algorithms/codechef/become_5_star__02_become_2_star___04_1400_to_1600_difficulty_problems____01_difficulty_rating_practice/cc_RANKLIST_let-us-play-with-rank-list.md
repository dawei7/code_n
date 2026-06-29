# Let us play with rank list

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RANKLIST |
| Difficulty Rating | 1543 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [RANKLIST](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/RANKLIST) |

---

## Problem Statement

A **rank list** is a list of ranks of persons in a programming contest. Note that some of the persons might be having same rank. {1, 2}, {1, 2, 2} and {1, 1, 2, 3, 4, 4} are few examples of rank lists whereas {1, 3}, {0, 2}, {1, 2, 4} are not rank lists.
Also note that a rank list need not to be sorted e.g. {2, 2, 1} and {3, 3, 2, 1} are valid rank lists.

Mathematically, a **rank list** is an array of numbers when sorted will have the starting element as 1 and difference between any two consecutive elements less than or equal to 1.

A rank list is said to be an **ideal rank list** if no two persons gets equal rank in it.

You can convert any rank list into an ideal rank list by applying following operations. In a single operation, you can change value of any one element of the rank list to any value.

Chandan now wonders about minimum number of operations needed to convert a rank list of size **n** with sum of its element equal to **s** in to an ideal rank list. Please help Chandan find this minimum number of operations needed to create an ideal rank list.

Note that you are guaranteed that values of **n, s** will be given in such a way that there will exist a valid rank list.

### Input
First line of input will give an integer **T** denoting number of test cases.
Then for next **T** lines, each line will contain two space separated integers **n, s**.

### Output
For each test case, print a single line containing a single integer corresponding to the answer of the problem.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **n** ≤ **10^5**

- **1** ≤ **s** ≤ **10^10**

---

## Examples

**Example 1**

**Input**

```text
4
1 1
3 6
3 5
3 3
```

**Output**

```text
0
0
1
2
```

**Explanation**

**Example case 1.**
Only possible rank list in this case is {1}, As it is already an ideal rank list, hence you need zero operations.

**Example case 2.**
Only possible rank list in this case is {1 2 3}, As it is already an ideal rank list, hence you need zero operations.

**Example case 3.**
One of the possible rank list is {1 2 2}, You can convert it into an ideal rank list by changing any 2 to 3 i.e. {1, 2, 3}, hence you need one operations.

**Example case 4.**
Only possible rank list is {1 1 1}, You can convert it into an ideal rank list by changing a 1 to 2 and another 1 to 3 i.e. {1, 2, 3}, hence you need two operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3 6
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3 5
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
3 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/RANKLIST)

[Contest](http://www.codechef.com/FEB15/problems/RANKLIST)

**Author:** [Chandan Boruah](http://www.codechef.com/users/chandubaba)

**Tester:** [Pushkar Mishra](http://www.codechef.com/users/pushkarmishra)

**Editorialist:** [Florin Chirica](http://www.codechef.com/users/elfus)

### PROBLEM

Let’s define a ranklist as a sequence of numbers between 1 and x of length n, such as ALL numbers between 1 and x must appear in the sequence at least once. An operation can change one element in what value you want. Your goal is to create a sequence containing all numbers between 1 and n exactly once by using minimal number of operations.

### QUICK EXPLANATION

Let’s iterate a number x meaning that all numbers between 1 and x appear in the ranklist. The cost of *any* ranklist with values between 1 and x is n - x. We need to determine if numbers between 1 and x are enough to create a sum s. Let’s note that a ranklist defined by x can create all sums between minSum and maxSum, where minSum = x * (x + 1) / 2 + (n - x) and maxSum = x * (x + 1) / 2 + (n - x) * x.

### EXPLANATION

To solve this problem, we need to make two observations. They seem pretty easy and intuitive, but after we make them, the problem is solved.

**Observation 1**

A ranklist containing elements between 1 and x (no element greater than x) will need n - x operations to be transformed into a sequence of numbers between 1 and n, no matter how sequence looks like.

We already have all elements between 1 and x (from the definition of a ranklist). However, we need to also have elements x + 1, x + 2, …, n - 1, n. Those do not appear (since all are greater than x), so we have to make some operations to get them. We can keep exactly one position which contains a value i, for each i between 1 and x. Rest of n - x positions must be modified. We’ll put in the remaining n - x positions values x + 1, x + 2, …, n - 1 and n. So cost of a ranklist containing elements between 1 and x becomes n - x.

**Observation 2**

A ranklist containing elements between 1 and x (no element greater than x) can generate all sums s, such as minSum <= s <= maxSum. More, all sums that can be generated by this ranklist are the ones that are between minSum and maxSum.

Let’s find out who is minSum. We are forced to place x elements: 1 2 … x. The rest of them we can complete them with 1s. So minSum = (1 + 2 + … + x) + (n - x) = x * (x + 1) / 2 + (n - x). maxSum can be obtained by completing the first x elements 1 2 … x and the rest of them with x value (the maximum we’re allowed to use). So we get maxSum = (1 + 2 + … + x) + (n - x) * x = x * (x + 1) / 2 + (n - x) * x.

Obviously, no sum s can be less than minSum or greater than maxSum (because those values are the minimum/maximum one can get). Let’s proof now that each sum s which has minSum <= s <= maxSum can be obtained. The idea is to see how those n - x terms can vary: they can be from 1 1 1 … 1 1 1 to x x x … x x x. Suppose we obtained a configuration corresponding to a sum s. Unless s is equal to maxSum, we can always obtain s + 1 as well. If s equal to maxSum, then all terms are equal to x. Otherwise, at least one term isn’t x. Since it isn’t x, we can increment it. Now, the obtained sum is s + 1 and it’s obtained assuming that s is different from maxSum.

**Putting the observations together**

In fact, those 2 observations are enough to solve the problem. The key that puts them together is that we can iterate x from 1 to n. Let’s see for a fixed x if a sum s can be obtained. For the given x, we can calculate minSum and maxSum and if minSum <= x <= maxSum, then sum s can be obtained and a ranklist containing only values between 1 and x is valid. The cost to transform this ranklist into 1 2 … n is n - x. So, for all valid ranklists (those who can give sum s), we keep minimum of n - x and we’re done.

**Time Complexity**

Since we iterate the x variable from 1 to n, the complexity is O(n).

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Tester’s solution](http://www.codechef.com/download/Solutions/FEB15/Tester1/RANKLIST.cpp)

[Setter’s solution](http://www.codechef.com/download/Solutions/FEB15/Setter/RANKLIST.cpp)

</details>
