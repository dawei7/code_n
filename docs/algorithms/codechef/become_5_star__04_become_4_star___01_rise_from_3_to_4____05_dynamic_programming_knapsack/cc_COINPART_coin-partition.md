# Coin Partition

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COINPART |
| Difficulty Rating | 2804 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming - Knapsack |
| Official Link | [COINPART](https://www.codechef.com/practice/course/3to4stars/LP3TO405/problems/COINPART) |

---

## Problem Statement

Chef is a cook. He has a son Chefu and a daughter Chefa. He also has $N$ coins, numbered $1$ through $N$; for each valid $i$, the $i$-th coin has value $V_i$.

Chef wants to give all coins to his two children in the following way: He traverses all coins in a particular order; for each coin, he checks which child currently has less money in total and gives this coin to that child (if both have the same amount of money, Chefu is given the coin).

Chefu is studying computer science, so he knows that this method is not necessarily the most fair way of partitioning the coins, but Chef does not understand why, since he is only a cook.

Now, Chefu wants to take advantage of that and choose the order in which Chef should give out the coins in such a way that the amount of money he gets is maximised. Can you help him?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $V_1, V_2, \dots, V_N$.

### Output
For each test case, print a single line containing $N$ space-separated integers — a permutation of numbers $1$ through $N$ denoting the indices of the coins in the order in which Chef should traverse them. If there is more than one optimal solution, you may print any one.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 500$
- $1 \le V_i \le 500$ for each valid $i$
- the sum of $N$ for all test cases does not exceed $500$

### Subtasks
**Subtask #1 (50 points):** the sum of $N$ for all test cases does not exceed $80$

**Subtask #2 (50 points):** original constraints

### Example Input
```
2
4
5 3 20 9
4
2 2 2 2
```

### Example Output
```
2 4 1 3
1 2 3 4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/elementPART)

[Contest: Division 1](https://www.codechef.com/LTIME64A/problems/elementPART)

[Contest: Division 2](https://www.codechef.com/LTIME64B/problems/elementPART)

**Setter:** [Hasan](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Medium-Hard

### PREREQUISITES:

Pre-computation, Dynamic Programming (Knapsack DP, to be precise), Mathematical proofs.

### PROBLEM:

Given N numbers in  array V, and two sum variables A and B, we iterate over numbers from left to right, if A \leq B, we add current number to A, otherwise we add current number to B.

Our aim is to find a permutation of numbers, such that A is maximized. If multiple permutation satisfies, print any.

### QUICK EXPLANATION

- For every element, say at position i, let us assume it will be the element last added to A. For that to happen, we need A \leq B before adding this element. Find maximum value of A, being A \leq B.

- Say maximum value found is X, then if ith element is last element added to A, then maximum value of A we can achieve is X+v[i]. Find X for every position, and thus, find the element, which will be added last to A.

- Find subset of all numbers, except at chosen position, which sums to X. Put all this numbers in first set, and all other numbers in another set. Now, make permutation of these elements, taking any element from first set, if cA \leq cB and add to cA. Otherwise take any element from second set and add it to cB. Make sure to add chosen element to cA only when first set is empty. cA and cB denote current A and B respectively.

### EXPLANATION

This problem too, has a relatively simple though hard to prove solution. So, whenever i mention observation, try to prove it yourself first. We will first find maximum possible value of A, constructing permutation is shown later.

We can see, that number is added to A if A-B \leq 0, otherwise number is added to B.

First observation is, that at the end, A-B \leq X where X is the element last added. If X is not last number to be added, Just before adding the last element, A-B \leq 0 has to hold.

Suppose we try to keep element V[i] as last element to be added.

Exclude the last element V[i] and make two sets P and Q, first one stores elements which will be added to A and second set stores numbers to be added to B from all elements except V[i]. Clearly, since A-B \leq 0, therefore sum(P) \leq sum(Q) and we need maximum sum(P). Maximum value of C would be sum(P)+V[i].

We take the position which gives maximum value sum(P)+V[i].

So, let’s focus on finding maximum sum§ we can obtain from set of all elements except one element excluded.

We know, that sum of all elements except V[i], is a constant, when V[i] is fixed, say S. So, we need to partition set of all numbers excluding V[i], so that sum(P) \leq S/2 because sum(P)+sum(Q) == S and sum(P) \leq sum(Q) and sum§ is maximum possible.

We use Dynamic Programming here. The problem to find whether there exist a subset of values with sum X is well known and is called Knapsack DP or subset sum problem. A brief explanation in secret box.

Click to view

Given a set of numbers F, we need to answer queries. Can we make a subset of values so that their sum is X. If yes, print the values in subset.

Solution in hidden box. Try to solve this problem, if both number of elements and Maximum value of elements doesn’t exceed 500. Queries to be answered in O(1).

Click to view

First focus on answering whether subset exist or not.

We have one boolean array Z of size sum of all values in array +1. Each positions tell Z[i], whether there exist a subset of numbers, with sum i. We process each element one by one. Initially, only Z[0] is true.

Take an element, say F[i], and for every sum j, if j is reachable earlier, now j+F[i] becomes reachable. We can add numbers one by one, and after that, answer queries. If Z[i] is true, we can make a subset with sum i, otherwise not.

After grasping this much, now let’s find the subset, which actually sums to number given in query. Let’s make another array, say prev. Whenever we mark Z[j+F[i]], we set prev[j+F[i]] = j. Now see what it does is, we come to know, that if we want a subset with sum X and Z[X] is true, First element will be X-prev[X], second element will be prev[X] - prev[prev[X]] and so on until prev[X] becomes 0. Try a few examples and you’ll get it.

Analyzing time complexity, We spend O(N*SUM) time because for every element, we iterate over all sum values.

Now, let’s try another problem with same trick.

Given a set of numbers, what is the largest subset sum you can make, so that it’s value do not exceed X, X given in each query. Idea is similar to previous one, so give it a try, or refer secret box.

Click to view

We do same as we did before. Calculate Z array same way.

After that, make another array, say MX[i], which stores the maximum value j \leq i which is reachable. we can fill it in O(SUM) time. MX[0] = 0 is base case, think of finding MX[i], when MX[i-1] and Z[i] are known.

We know, if i is reachable, MX[i] = i, otherwise, MX[i] = MX[i-1]. So, answer for query for sum X is MX[X]. That’s all.

So, if you have understood the secret box, you know how to select a subset of values, so that their sum doesn’t exceed S/2 as well as sum is maximal possible.

But, This process alone take O(N*SUM) time, and doing this N times have complexity O(N^2*SUM), which is 500^4, which cannot run in time. We have to optimize it.

For that, We maintain a prefix and a suffix knapsack table, say pre[i][j] and suf[i][j] before hand. (I will explain it use soon.)

pre[i][j] means whether we can make a subset of values up to index i, such that their sum is j. suf[i][j] represent whether there exist a subset of values with index above or equal to i, such that their sum is j.

Transition for this table is same as that for problem in hidden box. Just remember,additionally, if pre[i-1][j] is true, pre[i][j] will also be true. Similar for suf too.

Now, Suppose we have fixed V[i] as last element. We need to make subset P out of values in prefix up to i-1 and suffix after i+1.

After making pre and suf tables, let’s fix the element, and notice, if max(sum§) achievable is X for current element, it is of form Y+Z == X, Where Y is sum of elements chosen in prefix and Z is sum of values chosen in prefix.

Also, build two MX array, one for pre[i-1] and one for suf[i+1], say preMX and sufMX.

We need sum§ upto S/2, so, iterate over every i, and try to see maximum value of expression preMX[i] + suf[S/2-i]. Maximum value over all i is maximum sum of P achievable.

After finding max§, take the element having maximum sum(P)+V[i]. This is maximum value of A achievable.

Understand up to here properly, only then the next will make sense.

We know, which element will be added to A at last, so, let us build the subset P, using the prev array we used in hidden box. Here too, make two prev tables, one for prefix and one for suffix. Also, when finding maximum preMX[i]+sufMX[S/2-i], also store i so that we can make a subset from prefix of sum preMX[i] and subset from suffix having sum sufMX[S/2-i]. Uses same idea as we did in hidden box. and combine both sets obtained. This set represent our Set P.

So, Now we reach the final step of solution, that is to build a permutation, so that A = V[i] + sum(P) and B = sum(Q). All Elements not in P are in Q, except the chosen element as the last.

Make position vectors for each value v possible, storing indices i, such that V[i] == v.

We build permutation from left to right, and have two current sum variables cA = cB = 0. If cA \leq cB, we know that element at current position will be added to A, so we can take any element from P, say x, place it at current position (by fetching any position with value x) and increase CA by x. Otherwise, if cA>cB, fetch element from Q, place it at current position and add it to cB.

When set P becomes empty and cA \leq cB, place the chosen element.

This way, we get the required permutation and aha, you deserve 100 points now. But thinking about, “Is there always exist a permutation of elements, such that elements in P are added to A and others are added to B ?”. Let’s prove it.

**Lemma**: Two sets P and Q, where sum(P) \leq sum(Q), prove that there always exist a way to place them in a line, so that if we use the selection procedure as given in problem, Values from set P are added to A and values from set Q are added to B.

**Proof**: Since, we know, under optimal choices, sum(P) \leq sum(Q) and sum(P) + V[i] \geq sum(Q) where V[i] is chosen element.

Let us use mathematical induction to prove that a valid permutation always exist. (explaining small cases for clarity)

Suppose N == 1. This element must be chosen element, thus, both P and Q are empty. Only element is placed at only position.

For N==2, One of the element will be chosen, and second one must be in Q, so that before adding chosen element, ca \leq cb is necessary.

For N==3, Excluding one element (largest one), smallest element in P and middle element in Q. First of all, element in P is placed, then element in Q, and then the chosen element.

General case: Suppose there exist a permutation of N elements. We have to prove that a valid permutation exist of N+1 elements, after adding one element.

See, the added element, will be either in set P, or in set Q, or become the chosen element. Suppose we have final permutation. We try to remove element x from right end one by one. If A-x \leq B, x belonged to set P (or was chosen element). Otherwise, it belonged to Q. we can repeat this procedure.

We will eventually reach the point when A = B = 0. If the elements are inserted in exactly opposite order  (due to proof being right to left), the permutation will give required sets P and Q.

Hence, we can see, that there will always exist a permutation giving sets P and Q, and this completes our proof, and the editorial.

### Time Complexity

For building pre and suf tables, it takes O(N*SUM) time, which is same as O(N^2*MAX), where MAX is maximum value of V[i] permitted. For finding maximum value of sum§ for a fixed element takes O(SUM), we do this N times, so, this step also takes O(N*SUM) that is O(N^2*MAX) time.

Subset can be generated in linear times and permutation from set P and Q can be generated in O(N) or O(N*logN) time, depending upon implementation.

Thus, overall complexity is O(N^2*MAX).

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/LTIME64/setter/COINPART.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/LTIME64/tester/COINPART.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/LTIME64/editorialist/COINPART.java)

**Edit:** Until above links are not working, feel free to refer solution [here](https://ideone.com/uyPkB8).

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
