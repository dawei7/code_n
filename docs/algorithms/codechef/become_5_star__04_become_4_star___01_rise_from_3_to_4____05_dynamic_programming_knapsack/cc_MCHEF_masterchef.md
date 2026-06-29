# MasterChef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MCHEF |
| Difficulty Rating | 2016 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming - Knapsack |
| Official Link | [MCHEF](https://www.codechef.com/practice/course/3to4stars/LP3TO405/problems/MCHEF) |

---

## Problem Statement

Chef loves to prepare delicious dishes. He has prepared **N** dishes numbered from **1** to **N** for this year's MasterChef contest. He has presented all the **N** dishes to a panel of judges. Judging panel consists of **M** judges numbered from **1** to **M**. Rating for each dish was decided by voting from all the judges. Rating for the dishes has been given by a **1**-indexed array **A** where **Ai** denotes rating of the **ith** dish.

Some dishes prepared by chef are extraordinary delicious, but unfortunately, some are not. Chef has been given a chance to improve the total rating of his dishes. By total rating of dishes, we mean the sum of the ratings of his dishes. Each of the **M** judges has administrative power to remove some (zero or more) dishes from a specified range. The **ith** judge takes **Ci** rupees for removing each dish of Chef's choice from the dishes numbered from **Li** to **Ri** (both inclusive). Once a dish is removed by any of the **M** judges it will not be considered for calculating total rating of the dishes. Chef has spent a large portion of his money preparing mouth watering dishes and has only **K** rupees left for now. Now chef is worried about maximizing total rating of his dishes by dropping some of the **N** dishes.

Please Help chef by finding the maximum total rating he can achieve such that the total expenditure does not exceed his budget of **K** rupees.

###  Input

- First line of input contains a single integer **T** denoting the number of test cases.

- First line of each test case contains three space separated integers **N**, **K** and **M** denoting the number of dishes prepared by chef, chef's budget, and number of judges in judging panel respectively.

- Next line of each test case contains **N** space separated integers where **ith** integer denotes the rating received by the **ith** dish.

- Next **M** lines of each test case contain three space separated integers each: **L**, **R** and **C**, where the integers in the **ith** line denotes the value of **Li**, **Ri** and **Ci** respectively.

### Output

For each test case, print a single integer in a line corresponding to the answer.

###  Constraints

-  **1 ≤ T ≤ 105**

-  **1 ≤ N,M ≤ 105**

-  **1 ≤ K ≤ 500 **

-  **1 ≤ Li ≤ Ri ≤ N**

-  **1 ≤ Ci ≤ 200**

-  **-109 ≤ Ai ≤ 109**

-  Sum of **N** and **M** over all test cases does not exceed **5*105**

###  Subtasks :

- **Subtask 1 :** Sum of all **N**'s across the test cases in a file does not exceed **5000**. Sum of all **M**'s is also at most **5000**. **(33 points)**.

- **Subtask 2 :** Sum of all **N**'s across the test cases in a file does not exceed **5*105**. Sum of all **M**'s is also at most **5*105**. **( 67 points )**.

---

## Examples

**Example 1**

**Input**

```text
1
5 10 5
10 -2 -5 7 -10
1 1 5
2 4 10
4 4 12
3 4 10
1 5 15
```

**Output**

```text
5
```

**Explanation**

- Chef can drop dish numbered 3rd with rating -5 by paying 10 rupees to the 4th judge, and get the maximum possible total rating of 5.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/MCHEF)

[Contest](http://www.codechef.com/JULY15/problems/MCHEF)

**Author:** [Sunny Aggarwal](http://www.codechef.com/users/ma5termind)

**Tester:** [Mugurel Ionut Andreica](http://www.codechef.com/users/mugurelionut)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

### DIFFICULTY:

Easy-Medium

### PREREQUISITES:

dynamic programming, data structures

### PROBLEM:

Given an array of N elements consisting of both negative and positive elements and M operations. Each operation is of type L, R and K which implies that you can remove any one element within range L to R(both include) by paying K cost (each operation can be used multiple times).

You have a fixed budget C. You have to maximize the total sum of the array such that the expenditure in maximizing sum of elements does not exceed your budget C.

Here, N, M \le 10^5 and C \le 200.

### QUICK EXPLANATION:

First for each element find the minimum cost required to remove it. And then using DP similar to 0-1 Knapsack Problem calculate the maximum possible sum.

For finding minimum cost to remove each element:

-

For **subtask 1**, you can brute force *i.e.* for each operation traverse over all indices it effects and update the value in an array.

-

For solving **subtask 2**, you have to either use STL sets or you can use segment trees.

### EXPLANATION:

================

The most basic observation here is that each operation allows to remove single element only. So, let’s say you want to remove A_i, you can remove it in many ways. Let’s define by set S_i the set of operations which can remove A_i. So S_i = \{\textrm{oper}_j : L_j \le i \le R_j\}. Now you can intuitively/greedily say that for removing A_i you would always choose the operation from set S_i whose cost is minimum.

Now, let’s say for all i, we have found the minimum cost to remove A_i. How we actually do this I will explain later. So our problem now is basically:

You have an array A of size N… For each element A_i there is cost of removal R_i. Remove some elements from A_i to maximize the sum of remaining elements and also total cost of removal shouldn’t exceed C. This is quite similar to [0-1 Knapsack Problem](https://en.wikipedia.org/wiki/Knapsack_problem#0.2F1_knapsack_problem) which can be solved via Dynamic Programming(DP).

So, first step in writing/formalizing any DP problem is to decide some states which defines a sub problem of the problem we are trying to solve. You can do some hit and trial before you reach the correct states. Next step is to break the current problem into smaller sub problems which can help in defining the recursive relation between the DP states. Last step is to decide the base case.

So, here we define \textrm{solve}\hspace{1mm}(i,\hspace{1mm}j) as the answer if our budget is j and our array is formed by the first i elements ie. A_1, A_2, ..., A_i. So our answer will be \textrm{solve}\hspace{1mm}(N,\hspace{1mm}C).

Now let’s try to form recursive relations. You want to reduce your current problem *i.e.* \textrm{solve}\hspace{1mm}(i,\hspace{1mm}j) into smaller sub problems. How can we do that? To reduce current problem in smaller parts, we have to perform some action, which here is to decide whether to remove A_i or not.

Let’s consider case 1, where we will remove A_i. This is only possible if j \ge R_i. Now, \textrm{solve}\hspace{1mm}(i,\hspace{1mm}j) = \textrm{solve}\hspace{1mm}(i-1,\hspace{1mm}j - R_i). Note that we have lost R_i cost on removing A_i and our array is now reduced to first i - 1 elements. Also, in the sum of remaining elements A_i couldn’t contribute anything. (A thought: Will we ever remove A_i if it’s positive, considering removing elements incurs cost?).

Now, case 2, let’s not remove A_i. Now, \textrm{solve}\hspace{1mm}(i,\hspace{1mm}j) = A_i  + \textrm{solve}\hspace{1mm}(i-1,\hspace{1mm}C). Now, A_i is not removed and contributes to the sum of remaining elements. Also, our budget remains same and our array size is now reduced by 1.

So, our recurrence is ready which is basically:

\textrm{solve}\hspace{1mm}(i,\hspace{1mm}j) = \textrm{max}(\hspace{1mm}\textrm{solve}\hspace{1mm}(i-1,\hspace{1mm}j - R_i), \hspace{1mm} A_i + \textrm{solve}\hspace{1mm}(i-1,\hspace{1mm}j)).

Let’s see what are the base cases. The only base case is that if i==0 i.e. there is no array left, the only maximum sum possible is 0.

#### DP Implementation:

This is the last step of completing your DP problem. The best and the easiest way of writing DP is recursively with memoisation. There is no major difference in run time of recurisve and iterative DP.

Now, what is memoisation? It basically is method where you don’t calculate things you’ve already calculated. So you maintain a \textrm{flag} array which is same type of your DP array and intialised to \textrm{false}. Once you have calculated a certain subproblem, you mark it true in the \textrm{flag} array. If you ever reach again a state, which has already been calculated, you return the value currently stored in DP array. Things will get clear from the following implementation:

`

	flag[N][C]  #initialised to false
	DP[N][C]	#array which stores actual answers
	A[N]		#array A
	R[N]		#cost array

	solve(i, j):
    	#base case
        if i<=0:
        	return dp[i][j]=0	#first sets dp[i][j] to 0 and returns it

        if flag[i][j] == true:	#this dp has already been calculated
        	return dp[i][j]

        #case 2: don't remove A[i]
        ret = A[i] + solve(i - 1, j)

        #case 1: remove A[i] if possible
        #tak ret to be the maximum of both cases
        if(j >= R[i])
        	ret = max(ret, solve(i - 1, j - R[i]))

        #mark flag[i][j] true since we have calculated this DP
        flag[i][j] = true

        return dp[i][j] = ret
`

#### Complexity of DP:

Let’s set what is the complexity of such a recursive implementation. Since each possible state is visited once, the complexity of DP is number of states multiplied with transition cost. Transition cost is the complexity required from transfrom from one state to another state.

Here, our total number of states is \textrm{N * C} and transition cost is constant time. So, total complexity is \textrm{O(N * C)}.

#### Calculating minimum cost for removing each element

Now, about the part which we skipped earlier about calculating minimum cost of removing of A_i.

First you initialize all indices of a MIN array to infinity and then for each operation you traverse through all indices which it covers and update the minimum value at each index. Here complexity is \textrm{O(M*N)}, where M is number of operations and N is size of array A. This is enough to pass **Subtask 1**.

For solving **Subtask 2**, interesting observation is that an index i is affected by operations whose left end is before i and right end is after i. Suppose we have a data structure where we can insert/delete elements and find minimum value currently stored in this data structure in sub linear time. Let’s say this structure is S.

So, let’s maintain two vector arrays L and R(means you can store a list of values at each index) and for each operation j insert at index L_j and R_j the cost of this particular operation ie. K_j. Now, when we traverse arrays L and R from left to right, say we are index i, for indices \ge i, values stored in list L[i] are going to effect them, so we add to our structure the values stored at L[i] and the values stored in R[i] are not going to affect indices \ge i, so we remove all values stored at R[i].

What could be this data structure S. If we use [STL set](http://www.cplusplus.com/reference/set/set/), we can insert/delete a object only once, but this is not what we require. There might be two operations with same cost. So instead of storing values, we can store a pair of value and the indices of operations. In this way all operations will be unique and the beginning element of set will always give the minimum value operation.

If you don’t feel enough clarity, see this pseudo code and try to visualize what is happening.

`
	struct oper{
    	int l, r, k;
    };

    oper operarray[M];		//array of operations
    int MIN[N];				//MIN[i] stores minimum cost for removing A[i]
    vector L[N], R[N];
    //arrays as defined in above paragraph
    //except now they store indices of operations instead of their cost

    set < pair < int, int > > iset;
    //first element of pair stores value of operation cost
    //second stores the index of operation

    for i = 1 to M:
    	left = operarray[i].l
        right = operarray[i].r

    	L.push_back(i)
        R[right].push_back(i)

    for i = 1 to N:

    	//add all operations beginning at i
    	for j = 0 to L[i].size() - 1:
        	operindex = L[i][j]		//index of operation beginning here
            cost  = operarray[operindex].k

            //insert in set
    		iset.insert(make_pair(cost, operindex))

        MIN[i] = iset.begin()->first;	//first element of the set

        //remove all operations ending at i
    	for j = 0 to R[i].size() - 1:
        	operindex = R[i][j]		//index of operation beginning here
            cost  = operarray[operindex].k

            //erase from set
    		iset.erase(make_pair(cost, operindex))
`

Set is a STL data structure that inserts and deletes elements in O(\textrm{log (size of set)}). And since it keeps all elements in sorted order, we can find minimum element in constant time.

So total complexity of finding the \textrm{MIN} array is \textrm{O(N log M)}. You can also find \textrm{MIN} array using segment trees where the complexity will be \textrm{O((M + N) log N)}, if we use lazy propagation and make updates.

### COMPLEXITY:

Final complexity after including complexity of DP is \textrm{O(N log M + N C)}.

### AUTHOR’S, TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/JULY15/Setter/MCHEF.cpp)

[tester](http://www.codechef.com/download/Solutions/JULY15/Tester/MCHEF.cpp)

### Problems to Practice:

**Problems based on DP**

- [XORSUB Codechef](http://www.codechef.com/DEC14/problems/XORSUB)

- [DP Domain HackerRank](https://www.hackerrank.com/domains/algorithms/dynamic-programming)

**Problems based on STL**

- SPOJ [WEIRDFN](http://www.spoj.com/problems/WEIRDFN/), [HOMO](http://www.spoj.com/problems/HOMO/), [SUBSEQ](http://www.spoj.com/problems/SUBSEQ/), [HISTOGRA](http://www.spoj.com/problems/HISTOGRA/)

</details>
