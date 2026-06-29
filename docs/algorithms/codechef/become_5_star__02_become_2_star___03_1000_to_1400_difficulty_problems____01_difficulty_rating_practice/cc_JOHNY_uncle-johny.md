# Uncle Johny

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JOHNY |
| Difficulty Rating | 1093 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [JOHNY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/JOHNY) |

---

## Problem Statement

Vlad enjoys listening to music. He lives in Sam's Town. A few days ago he had a birthday, so his parents gave him a gift: MP3-player! Vlad was the happiest man in the world! Now he can listen his favorite songs whenever he wants!

Vlad built up his own playlist. The playlist consists of **N** songs, each has a **unique** positive integer length. Vlad likes all the songs from his playlist, but there is a song, which he likes more than the others. It's named "Uncle Johny".

After creation of the playlist, Vlad decided to sort the songs in increasing order of their lengths. For example, if the lengths of the songs in playlist was {1, 3, 5, 2, 4} after sorting it becomes {1, 2, 3, 4, 5}. Before the sorting, "Uncle Johny" was on **K**-th position (1-indexing is assumed for the playlist) in the playlist.

Vlad needs your help! He gives you all the information of his playlist. Your task is to find the position of "Uncle Johny" in  the sorted playlist.

### Input
The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains one integer **N** denoting the number of songs in Vlad's playlist. The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the lenghts of Vlad's songs.
The third line contains the only integer **K** - the position of "Uncle Johny" in the initial playlist.

### Output
For each test case, output a single line containing the position of "Uncle Johny" in the sorted playlist.

### Constraints
1 ≤ **T** ≤ 1000

1 ≤ **K** ≤ **N** ≤ 100

1 ≤ **Ai** ≤ 109

---

## Examples

**Example 1**

**Input**

```text
3
4
1 3 4 2
2
5
1 2 3 9 4
5
5
1 2 3 9 4 
1
```

**Output**

```text
3
4
1
```

**Explanation**

In the example test there are **T**=3 test cases.

**Test case 1**

In the first test case **N** equals to 4, **K** equals to 2, **A** equals to {1, 3, 4, 2}. The answer is **3**, because {1, 3, 4, 2} -> {1, 2, 3, 4}. **A2** now is on the **3**-rd position.

**Test case 2**

In the second test case **N** equals to 5, **K** equals to 5, **A** equals to {1, 2, 3, 9, 4}. The answer is **4**, because {1, 2, 3, 9, 4} -> {1, 2, 3, 4, 9}. **A5** now is on the **4**-th position.

**Test case 3**

In the third test case **N** equals to 5, **K** equals to 1, **A** equals to {1, 2, 3, 9, 4}. The answer is **1**, because {1, 2, 3, 9, 4} -> {1, 2, 3, 4, 9}. **A1** stays on the **1**-th position.

### Note

["Uncle Johny"](http://www.last.fm/music/The+Killers/_/Uncle+Johny) is a real song performed by The Killers.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 3 4 2
2
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5
1 2 3 9 4
5
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
5
1 2 3 9 4
1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/JOHNY)

[Contest](http://www.codechef.com/NOV13/problems/JOHNY)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

None

### PROBLEM:

Given an unsorted array of unique elements, find the position of a specified elements in array’s sorted form.

### QUICK EXPLANATION:

Count the number of elements in an unsorted array which are smaller than the given element.

### EXPLANATION:

Since the length of all songs is unique, if we count the number of songs which have length less than the length of “Uncle Johny”, we know its position in sorted array.

Constraint on the value of N in this problem is very low so many contestants sorted the array and then did binary search for the length of “Uncle Johny” song in the sorted array. This approach also passes well within time limit.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be uploaded soon

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/November/Tester1/JOHNY.cpp) and [here](http://www.codechef.com/download/Solutions/2013/November/Tester2/JOHNY.py)

</details>
