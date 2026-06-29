# Racing Horses

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HORSES |
| Difficulty Rating | 1231 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [HORSES](https://www.codechef.com/practice/course/1to2stars/LP1TO204/problems/HORSES) |

---

## Problem Statement

Chef is very fond of horses. He enjoys watching them race. As expected, he has a stable full of horses. He, along with his friends, goes to his stable during the weekends to watch a few of these horses race. Chef wants his friends to enjoy the race and so he wants the race to be close. This can happen only if the horses are comparable on their skill i.e. the difference in their skills is less.

There are **N** horses in the stable. The skill of the horse **i** is represented by an integer **S[i]**. The Chef needs to pick 2 horses for the race such that the difference in their skills is *minimum*. This way, he would be able to host a very interesting race. Your task is to help him do this and report the minimum difference that is possible between 2 horses in the race.

### Input:

First line of the input file contains a single integer **T**, the number of test cases.

Every test case starts with a line containing the integer **N**.

The next line contains **N** space separated integers where the **i**-th integer is **S[i]**.

### Output:

For each test case, output a single line containing the minimum difference that is possible.

### Constraints:
`
1 ≤ **T** ≤ 10
2 ≤ **N** ≤ 5000
1 ≤ **S[i]** ≤ 1000000000

`

---

## Examples

**Example 1**

**Input**

```text
1
5
4 9 1 32 13
```

**Output**

```text
3
```

**Explanation**

The minimum difference can be achieved if we pick horses with skills 1 and 4 for the race.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](http://www.codechef.com/problems/HORSES)

[Contest](http://www.codechef.com/SEP12/problems/HORSES)

[Video Editorial](https://youtu.be/MfmYDH7kR04)

# DIFFICULTY

CAKEWALK

# PREREQUISITES

[Sorting](http://en.wikipedia.org/wiki/Sorting), [Quick Sort](http://en.wikipedia.org/wiki/Quicksort)

# PROBLEM

You are given a list of integers. Find the pair of integers whose value is closest among all the pair of integers in this list.

# QUICK EXPLANATION

You can sort the integers and then consider all `(N-1)` consecutive pairs of integers. One of these pairs is surely the closest. Their difference is the answer.

# EXPLANATION

First, let us consider the complexity of a naive brute force solution.

If we consider each possible pair of integers, we will end up with an **`O(N*N)`** solution - given there are **`N`** integers.

For a file with `T` test cases, the over all complexity is **`O(N\*N\*T)`**. This will mean about **`250 million`** calculations. This will be too slow to pass within **3 seconds** on the CodeChef servers.

As with any brute force solutions, this solution is doing a lot of extra work. It is considering the difference between several pairs of integers that can be ignored.

Consider the case where the list of integers - we will call it **`A`** - is **sorted**.

**Lemma:**

The closest pair of integers is one of the N-1 pairs, which appear consecutively in **`A`**

Alternately, if **`A[i]`** and **`A[j]`** are the closest pair of integers, then `i` is equal to `j-1`.

**Proof:**

We will use **[Proof by Contradiction](http://en.wikipedia.org/wiki/Proof_by_contradiction)**.

Let us assume that the pair of closest integers is **`A[i]`** and **`A[j]`** and `i < (j-1)`

- Consider **`A[k]`** ? `k > i` and `k <= (j-1)`

- Since **`A`** is sorted, **`A[k]`** `>=` **`A[i]`** and **`A[k]`** `<=` **`A[j]`**

- From `(2)` we get **`A[k] - A[i]`** `>=` **`0`**

- Adding **`A[j] - A[k]`** on both the sides in `(3)` we get

**`A[j] - A[i]`** `>=` **`A[j] - A[k]`**

Hence, **`A[k]`** and **`A[j]`** are either a better or an equally good choice for pair of closest integers.

This means, at least one of the assumptions is false.

- Either **`A[i]`** and **`A[j]`** are not the closest integers

- Or, `i` is equal to `j-1`

**Approach:**

Now, we just need to sort the numbers efficiently and consider the consecutive pairs in one parse. Sorting can be done in place using the [Quick Sort](http://en.wikipedia.org/wiki/Quicksort) algorithm, which sorts in **`O(N log N)`** time. Quick Sort is available in the standard library in almost all languages.

The rest can be resolved in a single parse. The code will look like

`Sort A
minval = infinity
for i = 1 to N-1, inclusive
	if minval > A[i] - A[i-1] then minval = A[i] - A[i-1]
print minval
`

# SETTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Setter/HORSES.cpp)

# TESTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Tester/HORSES.c)

### Video Editorial

</details>
