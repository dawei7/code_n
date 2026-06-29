# Chef and easy problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFA |
| Difficulty Rating | 1408 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [CHEFA](https://www.codechef.com/practice/course/sorting/SORTINGPRO/problems/CHEFA) |

---

## Problem Statement

Chef and Roma are playing a game. Rules of the game are quite simple.
Initially there are **N** piles of stones on the table.
In each turn, a player can choose one pile and remove it from the table.
Each player want to maximize the total number of stones removed by him.
Chef takes the first turn.

Please tell Chef the maximum number of stones he can remove assuming that both players play optimally.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains a single integer **N** denoting the number of piles.

The second line contains **N** space separated integers **A1**, **A2**, ..., **AN** denoting the number of stones in each pile.

### Output

For each test case, output a single line containg the maximum number of stones that Chef can remove.

### Constraints

- 1 ≤ **Ai** ≤ 109

- Subtask 1 (35 points): **T** = 10, 1 ≤ **N** ≤ 1000

- Subtask 2 (65 points): **T** = 10, 1 ≤ **N** ≤ 105

---

## Examples

**Example 1**

**Input**

```text
2
3
1 2 3
3
1 2 1
```

**Output**

```text
4
3
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
1 2 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem link:

[contest][1]

[practice][2]

### Difficulty :

Cakewalk

### Pre-requisites :

None

### Problem:

You are given N numbers. Two players alternatively choose numbers. Both players want to maximize the score of numbers picked by them. Chef plays first.

Find out maximum score of the Chef if both players play optimally.

### Quick Explanation

Find the sum of alternate numbers starting from the last when the array is sorted in increasing order.

### Explanation

Let us first play this game before we proceed to the final algorithm.

We will first play it for even numbers.

### Game 1:

Let N = 2 and a1 < a2 be two numbers.

if Chef chooses a1 , then Roma will choose a2 and Chef will be left with total sum a1.

If Chef chooses a2 , then Roma will choose a1 and Chef will be left with total sum a2 which is better than a1. Hence the answer will be a2.

In other words, as Chef plays first, he will pick the maximum of the numbers a1 and a2 (i.e. a2).

### Game 2:

Let N = 4 and a1 < a2 < a3 < a4.

Suppose chef chooses any number expect a4, then Roma will select a4 [ as he plays optimally ] . For the remaining two numbers chef takes the maximum one [ as seen above ].

Out of all three possible cases, the maximum sum that Chef can get is a3 + a2.

If Chef chooses a4 , then Roma chooses a3. Chef chooses a2 and Roma chooses a1. Now a4 + a3 > a3 + a2.

Similarly we can prove by induction that in the optimal strategy, both the players should pick the maximum number available for picking.

### Final Algorithm

We will sort the array in increasing order and the answer will be the sum of alternate numbers starting from the last.

How ?

### Proof:

Proof immediately follows from by the assertion that in the optimal strategy, both the players should pick the maximum number available for picking.

### Pseudo Code
``
	Read(N)
	for i in [1,N]
		Read(A[i])
	Sort(A+1,A+N+1)		//Sort all numbers
	for(int i=N ;i>0;i-=2 )
		Answer = Answer + A[i]
	Return Answer

``

### Subtasks

**Subtask 1**:

As we need to sort the array. We can apply any O(N2) eg. selection, insertion, bubble sorting algorithm.

**Subtask 2**:

We need to use O(n log n) sorting algorithm like quick, merge, heap sort.

We can also use O(105) bucket sort Algorithm.

### Some Interesting Readings

[Merge Sort in O(N*log N) time][5]

[Bucket Sort Algorithm in O(Max_Number)][6]

### Setter and Tester Solutions:

[setter][3]

[tester][4]

[1]: [http://www.codechef.com/LTIME16/problems/CHEFA](http://www.codechef.com/LTIME16/problems/CHEFA)

[2]: [http://www.codechef.com/problems/CHEFA](http://www.codechef.com/problems/CHEFA)

[3]: [http://www.codechef.com/download/Solutions/LTIME16/Setter/CHEFA.cpp](http://www.codechef.com/download/Solutions/LTIME16/Setter/CHEFA.cpp)

[4]: [http://www.codechef.com/download/Solutions/LTIME16/Tester/CHEFA.cpp](http://www.codechef.com/download/Solutions/LTIME16/Tester/CHEFA.cpp)

[5]: [http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/mergeSort.htm](http://www.personal.kent.edu/~rmuhamma/Algorithms/MyAlgorithms/Sorting/mergeSort.htm)

[6]: [https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html)

</details>
