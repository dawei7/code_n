# Mahesh and his lost array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANUMLA |
| Difficulty Rating | 2212 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ANUMLA](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ANUMLA) |

---

## Problem Statement

Mahesh got a beautiful array named **A** as a birthday gift from his beautiful girlfriend Namratha. There are **N** positive integers in that array. Mahesh loved the array so much that he started to spend a lot of time on it everyday. One day, he wrote down all possible subsets of the array. Then for each subset, he calculated the sum of elements in that subset and wrote it down on a paper. Unfortunately, Mahesh lost the beautiful array :(. He still has the paper on which he wrote all subset sums. Your task is to rebuild beautiful array **A** and help the couple stay happy :)

### Input

The first line of the input contains an integer **T** denoting the number of test cases.
First line of each test case contains one integer **N**, the number of elements in **A**.
Second line of each test case contains **2^N** integers, the values written on paper

### Output

For each test case, output one line with **N** space separated integers in non-decreasing order.

### Constraints

- **1** ≤ **T** ≤ **50**

- **1** ≤ **N** ≤ **15**

- **0** ≤ **Values on paper** ≤ **10^9**

- **All input values are valid. A solution always exists**

### Example
`**Input**
2
1
0 10
2
0 1 1 2

**Output**
10
1 1
`

### Explanation
**Test case #2**
For the array [1,1], possible subsets are {}, {1}, {1}, {1,1}, respective sums are 0, 1, 1, 2.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ANUMLA)

[Contest](http://www.codechef.com/COOK51/problems/ANUMLA)

**Author:** [Anudeep Nekkanti](http://www.codechef.com/users/anudeep2011)

**Tester:** [Constantine Sokol](http://www.codechef.com/users/kostya_by)

**Editorialist:** [Florin Chirica](http://www.codechef.com/users/elfus)

### DIFFICULTY:

Easy

### PREREQUISITES:

greedy, heaps (or STL multiset)

### PROBLEM:

You have an unknown set of length N. We take all 2 ^ N subsets of it and sum elements for each subset. Given what we obtained, restore a possible initial set.

### QUICK EXPLANATION

We build our solution step by step. Each step we take smallest element from sums. Suppose we’re at step i and we found element x[i]. We should erase now from sums all sums formed by x[i] and a non-empty subset of  {x[1], x[2], …, x[i – 1]}.

### EXPLANATION

Let’s call all 2^N sums sumSet. Also, let’s call a possible solution valueSet (making sum of all subsets of valueSet, you should obtain sumSet). The problem says there is always a possible solution. We’ll implement sumSet as a multiset from C++. This container allows following things, which will be needed later: find/delete an element and keep the set in increasing order. We’ll note first element from current sum set as sumSet[1], second element as sumSet[2] and so on. Let’s read all numbers from the input and add all of them in multiset sumSet.

Smallest element from sumSet is always 0 (and it corresponds to empty subset). It does not give us any information, so let’s erase it from the set and move on. What’s smallest element now? Is it an element from valueSet? Is it a sum of a subset of valueSet?

There exists at least one element from valueSet equal to smallest element from sumSet. Why? Suppose first element of sumSet is a sum of other elements of valueSet. sumSet[1] = valueSet[k1] + valueSet[k2] + … where k1, k2, … are some indexes.

Since numbers are positive, we get that valueSet[k1] <= sumSet[1], valueSet[k2] <= sumSet[1] and so on. Since sumSet[1] is smallest element possible, we can only get that valueSet[k1] = sumSet[1], valueSet[k2] = sumSet[1] and so on.

This means at least one element from valueSet will have value equal to sumSet[1]. We’ve found one element from valueSet. Let’s add it to valueSet (we build the set incrementally) and erase it from sumSet.

Let’s move now to our new sumSet[1] element (smallest element from sumSet, not deleted yet). We can follow same logic from above and see that sumSet[1] is a new element from valueSet. Let’s add it to valueSet and erase it from sumSet.

We move once again to sumSet[1]. Now, we have a problem. It can be one of following 2 possibilities:

-
`` sum of subset {valueSet[1], valueSet[2]}
``

-
`` a new element of valueSet.
``

Case b) is ideal, because we found one more element of valueSet. What to do with case a)? We know sum valueSet[1] + valueSet[2]. So we can simply erase it from sumSet, before considering sumSet[1]. Then, only case a) is left, so we find valueSet[3]. We erase now valueSet[3] from sumSet (I know, it becomes boring already, I’ll finish in a moment  ).

It’s more tricky now what can be sumSet[1]. It can be one of following: valueSet[3]+valueSet[1], valueSet[3]+valueSet[2], valueSet[3]+valueSet[1]+valueSet[2]. We can fix this by erasing all those elements from sumSet before considering sumSet[1]. Once again, we’re left with valueSet[4].

Let’s note that all sums that should be erased contain a valueSet[3] term and a non-empty subset of {valueSet[1], valueSet[2]}. Sums of subsets of {valueSet[1], valueSet[2]} are already erased in previous steps.

# Generalizing the algorithm

Let’s generalize the algorithm. Suppose you want to calculate valueSet[n]. We need firstly to erase from set a combination of valueSet[n – 1] and a non-empty subset of {valueSet[1], valueSet[2], …, valueSet[n – 2]}. Then, the smallest element is valueSet[n].

We can keep an additional array subsets[] representing all subset sums obtained from {valueSet[1], valueSet[2], …, valueSet[n – 2]}. Then, at step of calculating valueSet[n], we need to erase subsets[j] + valueSet[n – 1] from our sumSet. Now, valueSet[n] is calculated.

The new subset sum list will be the old one plus the one that contains valueSet[n – 1]. So, after we calculate valueSet[n], we update subsets with all values valueSet[n – 1] + subSets[j].

We run this algorithm as long as there is at least one element in sumSet.

# Time Complexity

Each element is added in the multiset once and erased once. Hence, the complexity is O(2 ^ N * log(2 ^ N)) = O(2 ^ N * N).

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Author’s solution](http://www.codechef.com/download/Solutions/COOK51/Setter/ANUMLA.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/COOK51/Tester/ANUMLA.cpp)

</details>
