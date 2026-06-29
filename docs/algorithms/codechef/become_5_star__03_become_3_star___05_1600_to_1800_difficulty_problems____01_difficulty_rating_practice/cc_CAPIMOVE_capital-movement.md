# Capital Movement

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CAPIMOVE |
| Difficulty Rating | 1780 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CAPIMOVE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CAPIMOVE) |

---

## Problem Statement

Chef is playing a video game. In a video game, there's a advanced civilization that has a total of **N** planets under control. All of those planets are connected with **N-1** teleports in such a way, that it's possible to travel between any two planets using those teleports.

There's a chance that some planet gets infected. In this case it takes 24 hours for civilization to find out infection and prevent it from spreading. During this time infection uses teleport one time and infect all the planets that can be achieved in one teleport jump. So, once infection is detected at planet **V**, scientists already know that all planets connected to **V** via teleport are also infected. All the neccessary teleports are disabled right away and medics start working on eliminating the infection.

Each planet has population. Planets are numbered from **1** to **N** and their populations are **P1**, **P2**, ..., **PN**. It is known that all the **Pi** are distinct.

There's a capital among all those planets. The capital is known to have the biggest population.

Once infection is detected at planet **V**, after disabling teleports on planet **V** and all connected to them, government has to establish a new capital if needed in the remaining not-infected planets. So, they list all the planets that are not connected to **V** and are not **V**. Then they pick the planet with biggest population. Your task is to find the number of this planet for every possible **V**.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains one integer **N**.

Next line contains **N** space-separated integers **P1**, **P2**, ..., **PN** denoting the population of each planet.

Next **N-1** lines contain two space-separated integers each **V** and **U** denoting that there's a teleport between planet **V** and **U**.

### Output

For each test case, output a single line containing **N** integers **A1**, **A2**, ..., **AN** separated by a space. Here **Ai** denotes the number of the planet picked to be new capital in case infection starts spreading from the planet **i**. In case infection affects all the planets output **0**.

### Constraints

- **1** ≤ **T** ≤ **5**

- **1** ≤ **N** ≤ **50000**

- **1** ≤ **Pi** ≤ **109**

- All **Pi** are distinct

- **1** ≤ **V** ≤ **N**

- **1** ≤ **U** ≤ **N**

### Subtasks

- **Subtask #1 (20 points): N ≤ 100**

- **Subtask #2 (30 points): N ≤ 10000**

- **Subtask #3 (50 points): No additional constraints**

---

## Examples

**Example 1**

**Input**

```text
1
6
5 10 15 20 25 30
1 3
2 3
3 4
4 5
4 6
```

**Output**

```text
6 6 6 2 6 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](https://www.codechef.com/problems/CAPIMOVE)

[Contest](https://www.codechef.com/JAN17/problems/CAPIMOVE)

**Author:**  [Maksym Bevza](https://www.codechef.com/users/cenadar)

**Tester:**  [Arjun Arul](https://www.codechef.com/users/arjunarul)

**Editorialist:** [Misha Chorniy](https://www.codechef.com/users/mgch)

## Difficulty:

Simple

# Pre-Requisites:

none

## Problem Statement

You are given tree consisting N nodes. Each node i has value P_{i} assigned to it. All values P_{i} are distinct. For each node j find maximal value of node in the graph if to remove nodes adjacent to j and j.

## Explanation

## Subtask 1 and 2

N is less or equal than 10000. For each node will mark all nodes which are adjacent to it as dead(not usable), will find maximum value between non-marked nodes.

``
	for i= 1..N
		//Step 1
		for j=1..N
			alive[j] = 1;	//initialize all marks as ones
		//Step 2
		alive[i] = 0;		//mark itself as dead
		for v is adjacent to i	//mark all adjacent nodes
			alive[v] = 0;	//mark neighbours as dead
		ans[i] = 0;
		//Step 3
		for j=1..N
			if alive[j]==1	//if node j is alive
				ans[i]= max(ans[i],p[j]); //find maximum value

``

How long it works? Obviously, the complexity of first and third step is O(N), how to find the complexity of the second step? Denote D(v) - degree of node v, for vertex i complexity of step 2 is equal to D(i), over all iterations complexity of second step is D(1)+D(2)+…+D(N), what is 2*(N-1) for trees, we see that each edge using exactly two times.

Total complexity of this algorithm is O(N*N+2*(N-2)+N*N) = O(N^2)

First and third steps are slowest in the code above, how to optimize it? We can rewrite that code a bit.

``
	for i=1..N
		alive[i]=1;
	for i=1..N
		alive[i]=0;
		for v is adjacent to i
			alive[v] = 0;
		ans[i]=0;
		for j=1..N
			if alive[j] == 1	//if node j is non-marked
				ans[i] = max(ans[i],p[j]); //update answer
		alive[i]=1;
		for v is adjacent to i
			alive[v] = 1;

``

Now total complexity is O(N+2*(N-2)+N*N+2*(N-2)) = O(N^2), still O(N^2), we can make some observations, basically we have set, where the following operations can be performed:

-
alive_{i}=1 is equivalent to adding in the set value of p_{i}

-
alive_{i}=0 is equivalent to erasing in the set value of p_{i}

## Subtask 3

Let’s use some data structure, namely in our case, the data structure which can add/erase elements, and find the maximal value in the set of these elements, but does this thing in time less than O(N).

``
	for i=1..N
		add(P[i]);
	for i=1..N
		erase(P[i]);
		for v is adjacent to i
			erase(P[v]);
		ans[i] = getMaximalValue();
		add(P[i]);
		for v is adjacent to i
			add(P[v]);

``

What is the best data structure for these things, in most of the modern programming languages exists built-in data structures for such things, in C++ you can use set, Java has Set, Python has similar data structures. If your language doesn’t have built-in data structures, you can read about heaps ([http://pages.cs.wisc.edu/~vernon/cs367/notes/11.PRIORITY-Q.html](http://pages.cs.wisc.edu/~vernon/cs367/notes/11.PRIORITY-Q.html)) and realize it.

Let’s write code with the map in C++, the similar code can be written in Java with Map or in Python with the dictionary.

``
	set < int > S;
	for i=1..N   // Step 0
		S.insert(P[i]);	//Initialize set
	//Adding element P[i] in the set
	for i=1..N
		//Step 1
		S.erase(P[i]);	//Erase value of node i from set
		for v is adjacent to i	//Iterate over neighbours of node i
			S.erase(P[v])	//Erase values of neighbours of i
		//Step 2
		if !S.empty()
			ans[i] = *S.rbegin();	//Value of greatest element
		//Step 3, rollback of the step 1
		S.insert(P[i]);	//Insert value of node i from set
		for v is adjacent to i	//Iterate over neighbours of node i
			S.insert(P[v])	//Insert values of neighbours of i

``

Complexity of adding/erasing of number in such data structures is O(log N), summary complexity of the first steps is O(N log N), the same is for third steps,

Total complexity is O(N log N + N log N + N log N + N log N) = O(N log N)

The overall time complexity of this approach is O(N log N).

## Solution:

Setter’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN17/Setter/CAPIMOVE.cpp)

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/JAN17/Tester/CAPIMOVE.cpp)

**Please feel free to post comments if anything is not clear to you.**

</details>
