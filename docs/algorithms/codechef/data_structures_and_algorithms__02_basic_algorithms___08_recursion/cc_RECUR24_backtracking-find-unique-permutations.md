# Backtracking - Find Unique Permutations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR24 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR24](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR24) |

---

## Problem Statement

You are given an array $A_1, A_2, \dots, A_N$ of length $N$ that may contain duplicates. Find all possible unique permutations of $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$ - the length of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of unique permutations:
- The first line contains a single integer $M$.
- The next $M$ lines contain $N$ space-separated integers each which will be permutation of $A$.

Note: The permutations must be printed in **lexicographically increasing** order.
Permutatios $a_1,a_2,\ldots,a_N$ is said to be lexicographically smaller than permutation $b_1,b_2,\ldots,b_N$ if there exists a position $i$ where $a_i \lt b_i$ and $a_j = b_j$ for all $j \lt i$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N, A_i \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
3
4 5 5
3
5 25 10
2
6 8
```

**Output**

```text
3
4 5 5 
5 4 5 
5 5 4 
6
5 10 25 
5 25 10 
10 5 25 
10 25 5 
25 5 10 
25 10 5 
2
6 8 
8 6
```

**Explanation**

**Test case $1$:** There are $3$ possible permutations which are $\{[4, 5, 5], [5, 4, 5], [5, 5, 4]\}$.

**Test case $2$:** There are $6$ possible permutations which are $\{[5, 10, 25], [5, 25, 10], [10, 5, 25], [10, 25, 5], [25, 5, 10], [25, 10, 5]\}$.

**Test case $3$:** There are $2$ possible permutations which are $\{[6, 8], [8, 6]\}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem Explanation

We are given an array A, We have to give all unique permutattions of the elements of A.

## [](#approach-2)Approach

We use Recursion and Backtracking to get every permutation from the array. To avoid duplicates being treated as different elements, we store the elements in a map with their frequency. When the function is called, if the map is empty then all the elements have been used, so we push the permutation in our vector of permutations. Otherwise, we iterate in the map and use that elements in the permutations and call the function again with the updated map.

## [](#code-3)Code
``#include <bits/stdc++.h>
using namespace std;
void uniquePermutations(map<int,int>& elementsFreq, vector<int>& currentPermutation, vector<vector<int>>& allPermutations) {
    if (elementsFreq.empty()) {
        allPermutations.push_back(currentPermutation);
        return;
    }
    for (auto element: elementsFreq) {
        int num = element.first, freq = element.second;
        currentPermutation.push_back(num);
        map<int, int> newElementsFreq = elementsFreq;
        if (freq == 1)
            newElementsFreq.erase(num);
        else
            newElementsFreq[num]--;
        uniquePermutations(newElementsFreq, currentPermutation, allPermutations);
        currentPermutation.pop_back();
    }
}
int main() {
	int t;
	cin>>t;
	while(t--){
	    int N;
	    cin>>N;
	    map<int,int> elementsFreq;
	    for (int i=0; i<N; i++) {
	        int x;
	        cin>>x;
	        elementsFreq[x]++;
	    }
	    vector<vector<int>> allPermutations;
        vector<int> currentPermutation;
        uniquePermutations(elementsFreq, currentPermutation, allPermutations);
        cout<<allPermutations.size()<<endl;
        for (auto& permutation: allPermutations) {
            for (int i: permutation)
                cout<<i<<" ";
            cout<<endl;
        }
	}
	return 0;
}
``

</details>
