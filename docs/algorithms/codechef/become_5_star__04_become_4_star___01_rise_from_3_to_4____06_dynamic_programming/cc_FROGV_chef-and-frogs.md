# Chef and Frogs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FROGV |
| Difficulty Rating | 1668 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [FROGV](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/FROGV) |

---

## Problem Statement

Nobody knows, but $N$ frogs live in Chef's garden.

Now they are sitting on the X-axis and want to speak to each other. One frog can send a message to another one if the distance between them is less or equal to $K$.

Chef knows all $P$ pairs of frogs, which want to send messages. Help him to define can they or not!

**Note** : More than $1$ frog can be on the same point on the X-axis.

### Input

-   The first line contains three integers $N$, $K$ and $P$.
-   The second line contains $N$ space-separated integers $A_1$, $A_2$, ..., $A_N$ denoting the x-coordinates of frogs".
-   Each of the next $P$ lines contains two integers $A$ and $B$ denoting the numbers of frogs according to the input.

### Output

For each pair print "Yes" without a brackets if frogs can speak and "No" if they cannot.

### Constraints

-   $1 \le N, P \le 10^5$
-   $0 \le A_i, K \le 10^9$
-   $1 \le A, B \le N$

---

## Examples

**Example 1**

**Input**

```text
5 3 3
0 3 8 5 12
1 2
1 3
2 5
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

- For pair $(1, 2)$ frog $1$ can directly speak to the frog $2$ as the distance between them is $3 - 0 = 3 \le K$ .

- For pair $(1, 3)$ frog $1$ can send a message to frog $2$, frog $2$ can send it to frog $4$ and it can send it to frog $3$.

- For pair $(2, 5)$ frogs can't send a message under current constraints.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/FROGV)

[Contest](http://www.codechef.com/JULY14/problems/FROGV)

**Author:** [Dmytro Berezin](http://www.codechef.com/users/berezin)

**Tester:** [Shang Jingbo](http://www.codechef.com/users/jingbo_adm) and [Gerald Agapov](http://www.codechef.com/users/gerald)

**Editorialist:** [Devendra Agarwal](http://www.codechef.com/users/devuy11)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

Basic Dynamic Programming

### PROBLEM:

Given Frog’s location on the X axis and they can communicate their message to another frog only if the distance are less than or equal to K , now you need to answer if given two frogs can communicate or not. **Assumption** : Frog’s are cooperative in nature and will transfer the message without editing it  .

### Quick Explanation

Find for each frog the maximum distance which his message can reach. Two Frogs can only communicate if their maximum distance of communication are same.

**Reason**

You can easily proof by contradiction. Let us assume that there are two frogs 1 and 2 which can communicate but their maximum distances are different. You can easily contradict this , proof is left as an exercise for the reader.

### Explanation

Only Challenge left is to calculate the maximum distance which each frog can message.

The First point to note is that one of the optimal strategy of each frog(say f) will be to send message to it’s nearest frog(say f1) and then it will be the responsibility of the nearest frog to carry it further.

One Line Proof : Frog’s reachable from the f in the direction of f1 is also reachable from f1.

Another point to note is that the frog on the extreme positive side of X axis(i.e Maximum A[i] , say A[j]) can communicate till A[j] + K.

Using these observation , one can use a simple dp to calculate the maximum distance . But how ?

Sort A[i]'s but do not loose the index of frog’s while sorting. Let the sorted array be Frog[] . Now if Frog[i] can communicate to Frog[i+1] , then Frog[i] can communicate as mcuh distance as Frog[i+1] can communicate.

**Pseudo Code**

``Pre-Compute ( A , K ):
	sort(A,A+N);		//Sorted in Decreasing Order of X .
	Max_Distance[A[0].ind]=A[0].v+K;
	for(int i=1;i<N;i++)
		if((A[i-1].x-A[i].x)<=K)
			Max_Distance[A[i].ind] = Max_Distance[A[i-1].ind];
		else
			Max_Distance[A[i].ind] = A[i].x + K;

Answer ( x , y ):
	if ( Max_Distance[x] == Max_Distance[y] ):
		return "Yes"
	else
		return "No"
``

**Complexity**:

O(N*log(N)), N * logN for sorting N integers.

### AUTHOR’S and TESTER’S SOLUTIONS:

Author’s solution to be uploaded soon.

[Tester’s solution](http://www.codechef.com/download/Solutions/2014/July/Tester/FROGV.cpp)

</details>
