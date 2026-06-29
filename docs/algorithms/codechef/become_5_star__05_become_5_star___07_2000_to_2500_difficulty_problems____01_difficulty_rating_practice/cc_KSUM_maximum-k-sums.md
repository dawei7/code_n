# Maximum K Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KSUM |
| Difficulty Rating | 2260 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [KSUM](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/KSUM) |

---

## Problem Statement

Chef likes arrays a lot. Today, he found an array **A** consisting of **N** positive integers.

Let **L** denote the sorted (in non-increasing order) list of size **N*(N+1)/2** containing the sums of all possible contiguous subarrays of **A**. Chef is interested in finding the first **K** elements from the list **L**. Can you help him in accomplishing this task?

### Input

There is only a single test case per input file.

The first line of input contains two space separated integer numbers **N** and **K** denoting the size of the array and the number of the maximal sums you need to find.

The following line contains **N** space separated integer numbers denoting the array **A**.

### Output

Output **K** space separated integers where the **ith** integer denotes the **ith** element of **L**.

### Constraints

**
- 1 ≤ N ≤ 105
**
**
- 1 ≤ K ≤ min(N*(N+1)/2, 105)
**
**
- 1 ≤ Ai ≤ 109
**

### Subtasks

- Subtask 1 (47 pts) : **1 ≤ N ≤ 1000, 1 ≤ K ≤ min{N*(N+1)/2, 105}
**

- Subtask 2 (53 pts) : **1 ≤ N ≤ 105, 1 ≤ K ≤ min{N*(N+1)/2, 105}
**

### Example
`
**Input 1**
3 4
1 3 4

**Output 1**
8 7 4 4

**Input 2**
3 3
10 2 7

**Output 2**
19 12 10
`

### Explanation

**Test 1:**

The first **4** elements of it are **[8, 7, 4, 4]**.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/KSUM)

[Contest](http://www.codechef.com/LTIME35/problems/KSUM)

**Author:** [Sunny Aggarwal](http://www.codechef.com/users/ma5termind)

**Tester:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Editorialist:** [Sunny Aggarwal](http://www.codechef.com/users/ma5termind)

### DIFFICULTY:

Easy

### PREREQUISITES:

Sorting, Greedy, Data Structure, Implementation.

### PROBLEM STATEMENT:

Given an array A containing N **positive** integers and an integer K. We are asked to report the largest K values from the list of sums of all possible subarrays of array A.

### EXPLANATION:

**Subtask 1**

Listing sums of all the possible subarrays of A and finding the largest K values will be enough to pass this subtask.

**C++ Code**

`
#define ll long long
void solve(int N, int K, int *arr) {
	vector sum;
	for(int i=1;i<=n;i++) {
		long long int s = 0;
		for(int j=i;j<=n;j++) {
			s += arr[j];
			sum.push_back(s);
		}
	}
	sort(sum.rbegin(), sum.rend());
	for(int i=0; i<=K-1; i++) cout << sum[i] << " ";
	cout << "\n";
}
`

**Time Complexity**

O((\frac{N \times (N+1)}{2})) \times \log{\frac{N \times (N+1)}{2}})

[Complete Code Link](http://ideone.com/dpC3vH)

**Note**

Although the above solution will get passed on first subtask but we can have slight better complexity by maintaining a priority queue for the first K elements instead of sorting all the sums.

[Complete Code Link](http://ideone.com/2dEH71)

### Subtask 2

It is easy to see that the above solution will time out for this subtask.

**Then, how to approach it ?**

It can be noticed that the largest and first value will always be sum of all the elements as it is given that all elements are positive integers. It means the sum is corresponding to the subarray [1 to N] inclusively. Now, we have taken up the range 1...N and we can see that the next possible largest sum will be the maximum of sum of range 2...N and range 1...N-1. Let us assume that the second largest is obtained from the range 1...N-1. Then, the third largest sum will be maximum of sum of range 2...N ( previous range left ), range 2...N-1 and range 1...N-2 ( new ranges ). The above procedure can be run K times to find the largest K values.

**How to implement above idea ?**

Let us maintain a priority queue S ( set can also be used in C++ ). So, whenever we are taking the sum of a range say [L to R] from S, we can simply insert 2 new values to S i.e sum of range [L+1 to R] and [L to R-1] if L != R. Note that along with sum of range we are also maintaining the indices i.e L and R denoting that range in our priority queue.

**C++ Code**

`
#define ll long long
void solve(int N, int K, int *arr) {
	set<pair<ll,pair> S;
	long long int prefix_sum[N+1];
	for(int i=1;i<=n;i++) {
		prefix_sum[i] = prefix_sum[i-1] + arr[i];
	}

	S.insert({prefix_sum[N], {1, N}});
	while( K -- && !S.empty() ) {
		pair<ll,pair> top = *S.begin();
		S.erase( top );
		long long int sum;
		int L, R;
		sum = top.first;
		L = top.second.first;
		R = top.second.second;
		cout << sum <<" ";
		if( L != R ) {
			S.insert({sum-arr[L], {L+1, R}});
			S.insert({sum-arr[R], {L, R-1}});
		}
	}
}

`

### TIME COMPLEXITY:

O(K \times \log{K})

### AUTHOR’S AND TESTER’S SOLUTION:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME35/Setter/KSUM.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME35/Tester/KSUM.cpp).

</details>
