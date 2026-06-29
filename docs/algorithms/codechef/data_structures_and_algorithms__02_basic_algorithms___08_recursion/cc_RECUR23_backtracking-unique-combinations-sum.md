# Backtracking - Unique Combinations Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR23 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR23](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR23) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ and a target sum $B$.

Find the list of all *unique combinations* of the elements of $A$, such that the sum of the chosen elements equals $B$.

Note:
- The same element may be chosen from the array $A$ any number of times.
- Two combinations are unique if the frequency of at least one of the chosen elements is different.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input:
    - The first line of each test case contains two integers $N$ and $B$ - the size of the array and target sum, respectively.
    - The second line contains $N$ space-separated integers - the array $A$.

---

## Output Format

For each test case, output $M+1$ lines, where $M$ is the number of unique combinations:
- The first line contains a single integer $M$.
- The next $M$ lines contains a combination of space-separated elements of $A$ which sums to $B$.

Note:
- Elements in a combination $(C_1, C_2, \ldots, C_k)$ must be printed in non-descending order, i.e., $(C_1\le C_2\le \ldots\le C_k)$.
- The combinations must be printed in lexicographically increasing order.
We say that combination $X$ is lexicographically smaller than $Y$ if either $X$ is a prefix of $Y$ or there exists an index $i$ such that for all $j\lt i$, $X_j = Y_j$ and $X_i\lt Y_i$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 20$
- $1 \leq A_i \leq 20$
- $1 \leq B \leq 20$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
2 3
3 8
2 3 5
3 7
2 3 6
```

**Output**

```text
1
2
3
2 2 2 2
2 3 3
3 5
1
2 2 3
```

**Explanation**

**Test case $1$:** Given $A$ as $[2, 3]$ and $B$ as $2$.

There is only $1$ valid combination which is $\{[2]\}$.

**Test case $2$:** Given $A$ as $[2, 3, 5]$ and $B$ as $8$.

There are $3$ valid combinations which are $\{[2, 2, 2, 2], [2, 3, 3], [3, 5]\}$. Note that all these combinations are sorted and the set of combinations is printed in lexicographically increasing order.

**Test case $3$:** Given $A$ as $[2, 3, 6]$ and $B$ as $7$.

There is only $1$ valid combination which is $\{[2, 2, 3]\}$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem Explanation

We are given an array A and an integer sum, We have to give all unique combinations of the elements of A, such that the sum of the chosen elements is equal to B.

## [](#approach-2)Approach

We use Recursion to get every combinations from the array. If an element is less than or equal to the remaining sum, we use it in the combination and call the function and pass the remaining sum after subtracting the current element. And we call the function once excluding the current element and moving on to the next element. For every element we can be sure that these are the only two choices for making a combination. We push the combinations in a set to make sure the combinations are unique.

## [](#code-3)Code
``#include <bits/stdc++.h>
using namespace std;
void uniqueCombinationsSum(vector<int> &arr, int sum, int n, set<vector<int>> &allCombinations, vector<int> ¤tCombination){
    if(sum==0){
        allCombinations.insert(currentCombination);
    }
    if(sum>=arr[n])
    {
        currentCombination.push_back(arr[n]);
        uniqueCombinationsSum(arr, sum-arr[n], n, allCombinations, currentCombination);
        currentCombination.pop_back();
    }
    if(n+1<arr.size() && sum>=arr[n+1]){
        uniqueCombinationsSum(arr, sum, n+1, allCombinations, currentCombination);
    }
}
int main() {
    int t;
    cin>>t;
    while(t--){
        int n, sum;
        cin>>n>>sum;
        vector<int> arr;
        for(int i=0; i<n; i++){
            int temp;
            cin>>temp;
            arr.push_back(temp);
        }
        vector<int> currentCombination;
        set<vector<int>> allCombinations;
        sort(arr.begin(), arr.end());
        uniqueCombinationsSum(arr, sum, 0, allCombinations, currentCombination);
        cout<<allCombinations.size()<<endl;
        for(auto i: allCombinations){
            for(auto j: i){
                cout<<j<<" ";
            }
            cout<<endl;
        }
    }
}
``

</details>
