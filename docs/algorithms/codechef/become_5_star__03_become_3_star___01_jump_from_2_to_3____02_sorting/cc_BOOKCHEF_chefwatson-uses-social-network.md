# ChefWatson uses Social Network

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BOOKCHEF |
| Difficulty Rating | 1610 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [BOOKCHEF](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/BOOKCHEF) |

---

## Problem Statement

Chef Watson uses a social network called ChefBook, which has a new feed consisting of posts by his friends. Each post can be characterized by **f** - the identifier of the friend who created the post, **p** - the popularity of the post(which is pre-calculated by ChefBook platform using some machine learning algorithm) and **s** - the contents of the post which is a string of lower and uppercase English alphabets.

Also, Chef has some friends, which he has marked as *special*.

The algorithm used by ChefBook for determining the order of posts in news feed is as follows:

- Posts of *special* friends should be shown first, irrespective of popularity. Among all such posts the popular ones should be shown earlier.

- Among all other posts, popular posts should be shown earlier.

Given, a list of identifiers of Chef's *special* friends and a list of posts, you have to implement this algorithm for engineers of ChefBook and output the correct ordering of posts in the new feed.

### Input

First line contains **N**, number of *special* friends of Chef and **M**, the number of posts. Next line contains **N** integers **A1, A2, ..., AN** denoting the identifiers of *special* friends of Chef. Each of the next **M** lines contains a pair of integers and a string denoting **f**, **p** and **s**, identifier of the friend who created the post, the popularity of the post and the contents of the post, respectively.

### Output

Output correct ordering of posts in news feed in **M** lines. Output only the contents of a post.

### Constraints

- **1** ≤ **N, M** ≤ **103**

- **1** ≤ **Ai, f, p** ≤  **105**

- **1** ≤ **length(s)** ≤  **100**

- It is guaranteed that no two posts have same popularity, but the same friend might make multiple posts.

---

## Examples

**Example 1**

**Input**

```text
2 4
1 2
1 1 WhoDoesntLoveChefBook
2 2 WinterIsComing
3 10 TheseViolentDelightsHaveViolentEnds
4 3 ComeAtTheKingBestNotMiss
```

**Output**

```text
WinterIsComing
WhoDoesntLoveChefBook
TheseViolentDelightsHaveViolentEnds
ComeAtTheKingBestNotMiss
```

**Explanation**

Friends $1$ and $2$ are special. Among them, friend $2$'s post has more popularity. Thus, the first two posts of the feed would be of friend $2$ and $1$ respectively.
From remaining friends, i.e., friends $3$ and $4$, friend $4$'s post has more popularity. Thus, it would be shown earlier in the feed.
The final ordering of posts is $2\rightarrow 1\rightarrow 4\rightarrow 3$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/BOOKCHEF)

[Contest](http://www.codechef.com/COOK75/problems/BOOKCHEF)

**Author and Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

**Tester:** [Kamil Debowski](http://www.codechef.com/users/errichto)

### DIFFICULTY:

cakewalk

### PREREQUISITES:

basic programming, [sorting](https://en.wikipedia.org/wiki/Sorting_algorithm)

### PROBLEM:

You are given list of N *special* friends of Chef and M posts in ChefBook, where each post has f - the Id of friend who created the post, p - the popularity of the post and c - the contents of the post.

BookChef uses following algorithm to show posts in feed of Chef:

- First posts of *special* friends are shown. Popular posts are shown first.

- All other posts are shown after posts of *special* friends and are arranged in decreasing order of popularity.

Your task is to output the contents of posts in correct order.

### EXPLANATION:

================

The idea is very simple. Break down posts into two types: posts by *special* friends and posts by others. For each type, sort the posts in decreasing order of popularity and then output the contents. You need to know any basic sorting algorithm. Also, you need to maintain a structure for storing posts information which can be

``struct
``

in C++,

``tuple
``

in Python or even

``list
``

available in most programming languages. Next is you need sort an array of this structure according to one of the specific fields, for which you need to write a custom compare function.

To avoid writing custom compare function, you can do things a little intelligently. You must notice that once we’ve separated posts based on whether they’re from *special* friends or not, we don’t need to maintain the Id of the friend who created the post. In C++, if we sort a

``pair <T1, T2>
``

, it’s sorted in increasing order of first element. So, we can maintain a list of

``pair< int, string >
``

where first element is the popularity and second is the content of the post. We maintain two different lists for each type.

Shown below is the pseudo code along with some C++ constructs. You can read setter’s and tester’s solutions for example implementations.

``//Array for marking Ids of special friends. Special[i] is 1 if friend with Id i is special
bool Special[MAXID]

scan(T)
for test = 0 to T - 1:
	scan(N, M)

	pair<int, string> listSpecial, listNormal;

	for i = 0 to N - 1
		scan(x)
		Special[x] = 1

	for i = 0 to M - 1
		scan(f, p, s)
		if Special[f]:
			listSpecial.push_back( {p, s} )
		else:
			listNormal.push_back( {p, s} )

	sort(listSpecial)
	sort(listNormal)

	reverse(listSpecial)
	reverse(listNormal)

	for i in listSpecial:
		print i.second
	for i in listNormal:
		print i.second
``

### COMPLEXITY:

================

O(N + M \text{log} M) to read special friends and then sort the two lists of posts. Since, we can check whether each friend is special or not in O(1), the complexity is not affected by these operations.

### AUTHOR’S, TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/COOK75/Setter/BOOKCHEF.py)

[tester](http://www.codechef.com/download/Solutions/COOK75/Tester/BOOKCHEF.cpp)

</details>
