# Connecting Soldiers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOKIA |
| Difficulty Rating | 1831 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [NOKIA](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/NOKIA) |

---

## Problem Statement

To protect people from evil,
a long and tall wall was constructed a few years ago.
But just a wall is not safe, there should also be soldiers on it,
always keeping vigil.
The wall is very long and connects the left and the right towers.
There are exactly **N** spots (numbered 1 to **N**) on the wall for soldiers.
The *K*th spot is *K* miles far from the left tower and (**N**+1-*K*) miles from the right tower.

Given a permutation of spots *P* of {1, 2, ..., **N**}, soldiers occupy the **N** spots in that order.
The *P*[*i*]th spot is occupied before the *P*[*i*+1]th spot.
When a soldier occupies a spot, he is connected to his nearest soldier already placed to his left.
If there is no soldier to his left, he is connected to the left tower. The same is the case with right side.
A connection between two spots requires a wire of length equal to the distance between the two.

The realm has already purchased a wire of **M** miles long from Nokia,
possibly the wire will be cut into smaller length wires.
As we can observe, the total length of the used wire depends on the permutation of the spots *P*. Help the realm in minimizing the length of the unused wire. If there is not enough wire, output -1.

### Input

First line contains an integer **T** (number of test cases, 1 ≤ **T** ≤ 10 ). Each of the next **T** lines contains two integers **N M**, as explained in the problem statement (1 ≤ **N** ≤ 30 , 1 ≤ **M** ≤ 1000).

### Output

For each test case, output the minimum length of the unused wire, or -1 if the the wire is not sufficient.

---

## Examples

**Example 1**

**Input**

```text
4
3 8
3 9
2 4
5 25
```

**Output**

```text
0
0
-1
5
```

**Explanation**

In the 1st case, for example, the permutation *P* = {2, 1, 3} will use the exact 8 miles wires in total.

In the 2nd case, for example, the permutation *P* = {1, 3, 2} will use the exact 9 miles wires in total.

To understand the first two cases, you can see the following figures:

In the 3rd case, the minimum length of wire required is 5, for any of the permutations {1,2} or {2,1}, so length 4 is not sufficient.

In the 4th case, for the permutation {1, 2, 3, 4, 5} we need the maximum length of the wire = 20. So minimum possible unused wire length = 25 - 20 = 5.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 8
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3 9
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2 4
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
5 25
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINKS:

[Practice](http://www.codechef.com/problems/NOKIA)

[Contest](http://www.codechef.com/COOK23/problems/NOKIA)

## DIFFICULTY

Simple

## PREREQUISITES

arrays, divide-and-conquer, recursion

## PROBLEM

Given an array A[0…N+1], consider the indices [1…N] as spots for the soldiers and index 0 as the left tower and the index N+1 as the right tower. Initially set A[0] = 1, A[N+1] = 1 and rest all have 0s. Given a permutation P[1…N] of the indices {1, 2,…,N}, we fill them with 1s in that order and find the length of used wire as follows.

**`used_length = 0 for i = 1 to N 	used_length += ( distance from index P[i] to nearest index having 1 to left ); 	used_length += ( distance from index P[i] to nearest index having 1 to right ); 	A[ P[i] ] = 1;`**

You can see that the *used_length* depends on the permutation P and given an integer M, we need to find the minimum length of unused wire. It is same as asking for the maximum possible *used_length* ? M for some permutation P. If M is not sufficient for any permutation P, output -1.

## QUICK EXPLANATION

If you have solved the problem or almost got it yourself, this explanation is for you. If you have not solved it and eager to know how to build the idea from scratch, skip this part and go to the Detailed explanation section below.

There is a simple bruteforce solution and other clever solution. They are explained below.

-

N = 30 is so small that you can generate all possible *used_lengths* for each N = 1 to 30. For a given N, we just need to fix the first position and that partitions the problem in to two independent smaller subproblems and we can merge the answers to these smaller subproblems. If we consider the number of possible *used_lengths* for a given N to be of order O(N2), this requires time O(N5), which is fast enough for N = 30.

-

Given N, we can find the minimum and maximum *used_lengths*.

For minimum, its always better to try partitioning the problem into two equal subproblems.

**minLen[n] = (n+1) + minLen[n/2] + minLen[n-1-n/2]**

For maximum, we just need to place in the order {1,2,3…N}

**maxLen[n] = (n+1) + maxLen[n-1]** , this is same as **maxLen[n] = (n*(n+3))/2**

Now, can you prove that all the values between [ minLen[n], maxLen[n] ] are possible ? An idea is given in tester’s approach.

## DETAILED EXPLANATION

If you haven’t solved this problem yet, take some time now and try different cases on paper. eg. Consider N = 4 and try to find all possible *sum_of_lengths* for different permutations of {1,2,3,4}. You can also take a look at the explanation of sample cases under the problem statement for better understanding.

First lets see an almost bruteforce solution. Consider the array A for N = 9.

Initially A = |, 0, 0, 0, 0, 0, 0, 0, 0, 0, |

and we need to fill the array with 1s in some order. Suppose if we set A[4](http://www.codechef.com/download/Solutions/COOK23/Tester/NOKIA.cpp) = 1,

then A = |, 0, 0, 0, 1, 0, 0, 0, 0, 0, |

and length of wire on left side = 4, length of wire on right side = 6, so we need wire of length 4 + 6 = 10.

Note that if we place the first soldier among N spots at any index, we need wire of length (N+1). Not only that, the first soldier now acts as a barrier between his left and right sides. There will never be a wire which cross this soldier. So we have two independent problems now. If the first solder is placed at index I, then we need (N+1) length wire for this soldier and solve subproblem with (I-1) spots on left side and subproblem with (N-I) spots on right side.

A = |, 0, 0, 0, 1, 0, 0, 0, 0, 0, | is same as solving

A = |, 0, 0, 0, | and |, 0, 0, 0, 0, 0, |

So we can store all possible values for each N = 1 to 30, and for a given N try all possible positions for the first soldier and mix the answers of the two independent subproblems to get all possible values. As the constraint on N is 30, you can just bruteforce each of these steps.

For an alternate simple approach, see point 2 in the quick explanation section.

## SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK23/Setter/NOKIA.c)

## APPROACH

The problem setter used the approach given in the detailed explanation above.

## TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK23/Tester/NOKIA.cpp)

## APPROACH

The problem setter and the tester have independently observed that each of the values between [min, max] can be achieved for some permutation P. This method takes only O(N) time. Here is a rough idea of the proof using induction, in tester’s words.

max[0] = min[0] = 0

max[n] = max[n-1] + n+1

min[n] = min[n/2] + min[n - n/2 - 1] + n+1

Therefore max[n] = n * (n+3) / 2, min[n] = O(n log n).

Here we assume that for k = 1,2,…,n-1, [ min[k], max[k] ] are all possible,

then we should prove [ min[n], max[n] ] are all possible.

From min[n/2] + min[n - n/2 - 1] + n+1 to max[n/2] + max[n - n/2 - 1] + n+1 are all possible by the assumption.

If min[a+1]+min[n-a-2] ? max[a]+max[n-a-1] for all a=n/2, n/2+1, …, n-2, then we can show

[ min[n], max[n] ] are all possible.

L.H.S. = O(n log n), R.H.S = O(n^2), therefore, this is correct for large n.

If you can come with a more intuitive and simple proof, please edit this post and add a section ‘Alternate Proof’.

</details>
