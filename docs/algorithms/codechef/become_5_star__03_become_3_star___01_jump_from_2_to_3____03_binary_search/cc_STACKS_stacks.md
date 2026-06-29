# Stacks

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STACKS |
| Difficulty Rating | 1799 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Binary Search |
| Official Link | [STACKS](https://www.codechef.com/practice/course/2to3stars/LP2TO303/problems/STACKS) |

---

## Problem Statement

As every other little boy, Mike has a favorite toy to play with. Mike's favorite toy is a set of **N** disks. The boy likes to compose his disks in stacks, but there's one very important rule: the disks in a single stack must be ordered by their radiuses in a **strictly** increasing order such that the top-most disk will have the smallest radius.

For example, a stack of disks with radii (5, 2, 1) is valid, while a stack of disks with radii (3, 4, 1) is not.

Little Mike has recently come up with the following algorithm after the order of disks are given:

- First, Mike initiates an empty set of disk stacks.

- Then, Mike processes the disks in the chosen order using the following pattern:

- If there is at least one stack such that Mike can put the current disk on the top of the stack without making it invalid, then he chooses the stack with the smallest top disk radius **strictly** greater than the radius of the current disk, and puts the current disk on top of that stack.

- Otherwise, Mike makes a new stack containing only the current disk.

For example, let's assume that the order of the disk radii is (3, 4, 5, 1, 1, 2). Here's how the set of the top stack disks will appear during the algorithm's run:

- In the beginning of the algorithm, the set of disk stacks is empty. After processing the first disk, the set of top stack disks is {3}.

- We cannot put the second disk on the only stack that we have after processing the first disk, so we make a new stack. After processing the second disk, the set of top stack disks is {3, 4}.

- We cannot put the third disk on any of the available stacks, so we make a new stack. After processing the third disk, the set of top stack disks is {3, 4, 5}.

- The fourth disk has radius 1, so it can be easily put on any of the available stacks. According to the algorithm, we choose the stack with the top disk radius equal to 3. After processing the fourth disk, the set of top stack disks is {1, 4, 5}.

- The fifth disk has radius 1, so there are two stacks we can put it on. According to the algorithm, we choose the stack with the top disk radius equal to 4. After processing the fifth disk, the set of top stack disks is {1, 1, 5}.

- The sixth disk has radius 2, so there is only one stack we can put it on. The final set of top stack disks is {1, 1, 2}.

Mike is really excited about his new algorithm, but he has so many disks that it seems impossible to simulate the algorithm manually.

You are given an array **A** of **N** integers denoting the radii of Mike's disks. The disks are already ordered by Mike. Your task is to find the set of the stack top disk radii after the algorithm is done.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of a test description contains a single integer **N**.

The second line of the description contains **N** integers denoting **A1, ... , AN**.

### Output

For each test case, output a single line. The line should start with a positive integer **S** denoting the number of stacks after the algorithm is done. This should be followed by **S** integers on the same line denoting the stacks' top disk radii in **non-decreasing order**.

If there are multiple correct answers, you are allowed to output any of them.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 105

- 1 ≤ **Ai** ≤ 109

---

## Examples

**Example 1**

**Input**

```text
3
6
3 4 5 1 1 2
10
3 2 9 5 2 9 4 14 7 10
8
14 5 13 19 17 10 18 12
```

**Output**

```text
3 1 1 2
5 2 2 4 7 10 
4 5 10 12 18
```

**Explanation**

**Test case $1$:** This case is already explained in the problem statement.

**Test case $2$:** After processing the first disk, the set of top stack disks are $[3]$. The second disk can be placed on the first stack. Thus, top stack disks are $[2]$. The next $3$ disks can be stacked together. Thus, the top stack disks are $[2, 2]$. The next two disks can be stacked together to get $[2, 2, 4]$. The next two disks can be stacked together to get $[2, 2, 4, 7]$. The last disk can be put on top of the fifth stack. The final stack top are $[2, 2, 4, 7, 10]$. Thus, $5$ stacks are needed.

**Test case $3$:** After processing the first disk, the set of top stack disks are $[14]$. The second disk can be placed on the first stack. Thus, top stack disks are $[5]$. The next disk can be placed on second stack to get $[5, 13]$. The next $2$ disks can be stacked together. Thus, the top stack disks are $[5, 13, 17]$. The next disk can be placed on second stack to get $[5, 10, 17]$. The next disk can be placed on fourth stack to get $[5, 10, 17, 18]$. The last disk can be put on top of the third stack. The final stack top are $[5, 10, 12, 18]$. Thus, $4$ stacks are needed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
3 4 5 1 1 2
```

**Output for this case**

```text
3 1 1 2
```



#### Test case 2

**Input for this case**

```text
10
3 2 9 5 2 9 4 14 7 10
```

**Output for this case**

```text
5 2 2 4 7 10
```



#### Test case 3

**Input for this case**

```text
8
14 5 13 19 17 10 18 12
```

**Output for this case**

```text
4 5 10 12 18
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

###
[](#problem-link-1)PROBLEM LINK:

[Practice](http://www.codechef.com/problems/STACKS)

[Contest](http://www.codechef.com/COOK62/problems/STACKS)

**Author:** [Kanstantsin Sokal](http://www.codechef.com/users/kostya_by)

**Tester:** [Jingbo Shang](http://www.codechef.com/users/shangjingbo)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

###
[](#difficulty-2)DIFFICULTY:

Simple

###
[](#prerequisites-3)PREREQUISITES:

binary search, data structures

###
[](#problem-4)PROBLEM:

Mike likes to compose his disks in stacks, but there’s one very important rule: The disks in a single stack must be ordered by their radiuses in a **strictly** increasing order such that the top-most disk will have the smallest radius.

Mike initiates an empty set of disk stacks. Mike processes the disks in the given order A_1, A_2, ..., A_N using the following pattern:

- If there is at least one stack such that Mike can put the current disk on the top of the stack without making it invalid, then he chooses the stack with the smallest top disk radius strictly greater than the radius of the current disk, and puts the current disk on top of that stack.

- Otherwise, Mike makes a new stack containing only the current disk.

Your task is to output the set of the stack top disk radii after the algorithm is done in non-decreasing order.

###
[](#quick-explanation-5)QUICK EXPLANATION:

======================

We build our solution incrementally and at each step we maintain an sorted array S storing the top radii of all the stacks present. Using binary search, we can find the correct stack for a new disk. After replacing the top radii of such a stack, array S still remains sorted.

###
[](#explanation-6)EXPLANATION:

================

We are going to build our solution incrementally. That is, at each step we’ll store the stacks we already have formed and then find the correct position for a disk and put it there.

Now, from the example, given in the problem statement, it should be pretty clear that we need not store all the radii present in a stack. Since, we just need to output the top radii, and also where a new disk goes also depends on the top radii, we can just store the top radii of each of the stack currently formed.

Let’s say we have an array S_1, S_2, ..., S_k which currently stores the top radii of all stacks currently formed in sorted order. And now, we want to insert a new disk with radius x into this structure. So, we need to find smallest S_j(*i.e.* smallest j, since S is sorted) such that S_j > x. And we update S_j = x. We know that S_{j-1} \le x and S_{j+1} \gt x, so array S still remains sorted after the update. So, at each step we apply binary search to find such an index j and update the value x. If there is no such index found, we just create a new entry at the end of the array.

``A[N] = input
S[N]
current_size = 0

for i=0 to N-1:
	// find the first idx in the sorted array S, such that S[idx] > a[i].
	// this can be done using a simple binary search.
	int idx = binarySearch(size, a[i]);

	S[idx] = A[i]

	if(idx==size) size++;

for i=0 to size-1:
	print S[i]

//searches for first index idx such that S[idx] > val
int binarySearch(size, val):
	int lo = 0, hi = size - 1;
	int ans = size;
	while (lo <= hi) {
		int mid = (lo + hi) / 2;
		if (a[mid] > x) {
			ans = mid;
			hi = mid - 1;
		}
		else {
			lo = mid + 1;
		}
	}
	return ans;
}
``

You can also use built-in function \text{upper\_bound} instead of binary search. Also, we can solve this problem using [multiset](http://www.cplusplus.com/reference/set/multiset/). We just have to perform simulation. So, first, let’s try to write our algorithm in pseudo code first and then we’ll try to think about what kind of data structure do we need to implement that algorithm efficiently:

``A[N] = input
Data Structure DS;

for i=0 to N-1:
	x = Find in DS smallest number greater than A[i]

	if no such number:
		DS.insert(A[i])
	else:
		//we place A[i] on the stack with top radii x
		DS.delete(x)
		DS.insert(A[i])

print DS in sorted order
``

Now, we just need to think what kind of data structure DS is. It should efficiently insert values, delete values and for a given value find smallest number greater than value. If you know STL, [set](http://www.cplusplus.com/reference/set/set/) is such a data structure which keeps its elements sorted and can insert, delete, find operations in O(\text{log}(size)). But, set doesn’t keep duplicates, while we need to keep duplicates, so we use [multiset](http://www.cplusplus.com/reference/set/multiset/). A multiset allows duplicate values.While deleting in a multiset, if you delete by value, all occurences of value are deleted. So, we should first find a value, which will return an iterator and then we’ll delete by iterator.

``A[N] = input
multiset <int> myset;
multiset <int>::iterator it;

for i=0 to N-1:
	//here we first insert and then we find smallest number greater than A[i]
	myset.insert(A[i])

	it = myset.find(A[i])
	//right now, it points to A[i]

	//since multiset keeps elements ordered
	//so, next element should be the element we are looking for
	//also, sets have bidirectional iterators and can be incremented/decremented easily
	it++;

	//no such element present
	if it == myset.end():
		DS.insert(A[i])
	else:
		myset.erase(it)

//traverse over multiset to print values
//values inside multiset are already sorted
for(it=myset.begin(); it!=myset.end(); it++)
	print (*it)
``

###
[](#complexity-7)COMPLEXITY:

================

O(N \text{log} N), since each operation on multiset takes O(\text{log}N), or in case of binary search, it takes O(\text{log}N) at each step.

###
[](#problems-to-solve-8)PROBLEMS TO SOLVE:

================

Problems involving binary search:

[STRSUB](https://www.codechef.com/MARCH15/problems/STRSUB)

[ASHIGIFT](https://www.codechef.com/LTIME22/problems/ASHIGIFT)

[STETSKLX](https://www.codechef.com/AUG15/problems/STETSKLX)

Problems involving STL containers:

[Running Median](https://www.hackerrank.com/challenges/median)

[ANUMLA](https://www.codechef.com/COOK51/problems/ANUMLA)

###
[](#authors-testers-solutions-9)AUTHOR’S, TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/COOK62/Setter/STACKS.cpp)

[tester](http://www.codechef.com/download/Solutions/COOK62/Tester/STACKS.cpp)

</details>
