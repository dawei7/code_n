# Lumpy - The Bus Driver

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUMPYBUS |
| Difficulty Rating | 1708 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [LUMPYBUS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/LUMPYBUS) |

---

## Problem Statement

Lumpy is a bus driver. Today, the conductor is absent so Lumpy has to do the conductor's job as well. There are **N** creatures in the bus. Sometimes the creatures don't carry change and can't pay the exact amount of the fare. Each creature in the bus today has paid an amount
greater than his/her fare. You are given information about the **extra** amount paid by each creature, by an array **A** of size **N**, where **Ai** denotes the extra amount paid by the **i**-th creature, in rupees.

After the end of the trip, Lumpy noticed that he had **P** one rupee coins and **Q** two rupee coins. He wants to pay back the creatures using this money. Being a kind hearted moose, Lumpy wants to pay back as many creatures as he can. Note that Lumpy will
not pay back the **i**-th creature if he can't pay the **exact** amount that the **i**-th creature requires with the coins that he possesses.

Lumpy is busy driving the bus and doesn't want to calculate the maximum number of creatures he can satisfy - He will surely cause an accident if he tries to do so. Can you help him out with this task?

### Input

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

- For each test case, first line consists of three space separated integers **N**, **P** and **Q**.

- Second line consists of **N** space separated integers **A** containing **N** space integers, where **i**-th integer denotes **Ai**.

### Output

- For each test case, output a single line containing an integer corresponding to maximum number of creatures that Lumpy can pay back.

### Constraints

- **1** ≤ **T** ≤ **106**

- **1** ≤ **N** ≤ **105**

- **1** ≤ **Ai** ≤ **109**

- **0** ≤ **P, Q** ≤ **1014**

- Sum of **N** over all the cases does not exceed **106**

### Subtasks

- *Subtask #1 (15 points)*: **P** = 0

- *Subtask #2 (15 points)*: **Q** = 0

- *Subtask #3 (70 points)*: Original constraints

---

## Examples

**Example 1**

**Input**

```text
3
3 3 0
1 2 2
3 2 1
1 2 1
4 5 4
2 3 4 5
```

**Output**

```text
2
3
3
```

**Explanation**

**Example 1**. Lumpy has just **3** one rupee coins.
He can pay creatures numbered **{1, 2}** or creatures numbered **{1, 3}** with these coins. Thus, answer is 2.

 **Example 2**. Lumpy has **2** one rupee coins and **1** two rupee coin.
In the optimal solution, Lumpy can give the two rupee coin to creature **2** and the one rupee coins to creatures **1** and **3**. Thus, answer is 3.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3 0
1 2 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3 2 1
1 2 1
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 5 4
2 3 4 5
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/LUMPYBUS)

[Contest](http://www.codechef.com/LTIME38/problems/LUMPYBUS)

**Author:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Testers:** [Animesh Fatehpuria](https://www.codechef.com/users/animesh_f) [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Easy

### PREREQUISITES:

Greedy

### PROBLEM:

Given is an array A of integers. We have two types of coins: P coins of value 1 and Q coins of value 2. We want to make as many values from the array A as we can using these P+Q coins. We have to report the maximum that we can make.

### EXPLANATION:

Before we talk about subtasks, the simplest thing that comes to our mind is, we will always try to make the smaller values first. This is quite intuitive, but let’s us give a formal argument to it: let us say we try to make values in random order. If using 1s and 2s, we can make a value x, then we can make all other values y such that y \leq x. Why is this so? For some y \leq x, if x and y are of the same parity, then we can simply remove some of the value 2 coins that we used in x. If they are of different parity, we can can first remove a value 1 coin and then remove some value 2 coins. So, the general argument is that if we can make x with coins of values 1s and 2s, we can make numbers smaller than x too. And we should. We can always make more smaller numbers than making a single x. This is the [exchange argument ](http://web.stanford.edu/class/archive/cs/cs161/cs161.1138/handouts/120%20Guide%20to%20Greedy%20Algorithms.pdf) we need for our greedy structure.

But what if x is only made of value 2 coins? In that case, we can’t make smaller values of different parity. We will look at this case later. But it gives us a hint. We need to deal with even and odd numbers separately.

**Subtask 1**

There are no 1 coins. That means we can only make even numbers. We sort all the numbers and try to make the even ones in increasing order till we run out of all the Q coins of value 2.

**Subtask 2**

There are no 2 coins. But we can make everything with coins of value 1. Just that we follow the same thing we did before, we start by making the smallest coin first.

**Subtask 3**

In this subtask we have both the 1s and the 2s. As we saw earlier, we segregate the numbers of the array A into two arrays, even[] and odd[]. Once we have segregated the numbers, we need to sort both the even and the odd arrays; this is because of the same reasoning as before.

Now we start by looking at the smallest coins from the two arrays, even and odd. Let these coins be of values V_e and V_o respectively. We know that odd values require us to use the 1 value coins. So we should try to use our 1 value coins in odd numbers since odd numbers can’t be made with 2 value coins but even numbers can be made with either of the 1s or the 2s. This leads us to a crucial observation. If we can use a 2 value coin, we should do that because we don’t get any benefit by saving them. So, we compare the two values, V_o and V_e, and first make the smaller of the 2. If the V_o was smaller, we move on to the next odd coin, else we move on to the next even coin. This goes on until we run out of all the coins or we are left with just value 2 coins and off numbers. The pseudocode is given below:

``Make_Coins(A[], N):

	odd[oddCount] = getOddNums(A);
	even[evenCount] = getEvenNums(A);
	sort even[] and odd[];

	CountAns = 0; // Answer Counter.

	while (Coins left and Numbers left) {
		Vo = smallest remaining value in odd[];
		Ve = smallest remaining value in even[]; // in case no value remaining,
											     // set to arbitrary high value.

		if (Vo < Ve and Value 1 coins left) {
			// if no value one coins left, we can't make odd numbers.

			Coin2req = Vo / 2;
			if (Coin2req > Q) {
				// we can only use as many coins as are left.
				Coin2req = Q;
			}

			// Subtract value from Vo and also reduce number of 2 coins.
			Vo -= Coin2req * 2;
			Q -= Coin2req;

			// Further calculate how many 1 coins are required.
			Coin1req = Vo;
			if (Coin1req > P) {
				// we can only use as many coins as are left.
				Coin1req = P;
			}

			// Subtract value from Vo and also reduce number of 2 coins.
			Vo -= Coin1req;
			P -= Coin2req;

			// If we managed to make Vo = 0, we can increment our answer counter
			if (Vo == 0) {
				CountAns = CountAns + 1;
				remove Vo from odd[];
			}

		} else if (Ve < Vo and value 1 or value 2 left) {
			//Do same as the case for Vo.

			// If we managed to make Ve = 0, we can increment our answer counter
			if (Ve == 0) {
				CountAns = CountAns + 1;
				remove Ve from even[];
			}
		}
	}

	return CountAns;
``

Sorting takes \mathcal{O}(N\log N) time. Thus, overall complexity is dominated by it. Rest of the procedure is linear.

Please see tester’s/setter’s program for implementation details.

**Binary search based solution**

As we learned above, number of odd coins are more important to consider first. Let us say we decide to make first k smallest odd numbers, we need at least k ones for it. After that, we will find how many even numbers still we make. For that, you can note that the total money remaining to spend on even numbers is $P + 2 * Q - \text{sum of first k smallest odd numbers}. We have to find number of even numbers we can make using this amount of money. This can be done by a binary search over the number of even coins you can make. Overall time complexity will be \mathcal{O}(n log n)$. Please see author’s solution for it.

### COMPLEXITY:

\mathcal{O}(N\log N) per test case.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/LTIME38/Setter/LUMPYBUS.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/LTIME38/Tester/LUMPYBUS.cpp)

[Tester](http://www.codechef.com/download/Solutions/LTIME38/Editorialist/LUMPYBUS.cpp)

</details>
