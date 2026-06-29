# Restaurant Rating

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RRATING |
| Difficulty Rating | 1851 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [RRATING](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/RRATING) |

---

## Problem Statement

Chef has opened up a new restaurant. Like every other restaurant, critics critique this place. The Chef wants to gather as much positive publicity as he can. Also, he is very aware of the fact that people generally do not tend to go through all the reviews. So he picks out the positive reviews and posts it on the website of the restaurant. A review is represented by an integer which is the overall rating of the restaurant as calculated by that particular review.
A review is considered to be positive if it is among the top one-third of the total reviews when they are sorted by their rating. For example, suppose the ratings given by 8 different reviews are as follows:

2 8 3 1 6 4 5 7

Then the top one-third reviews will be 8 and 7. Note that we considered one-third to be 8/3=2 top reviews according to integer division. (see Notes)

So here is what the Chef wants from you: Given the reviews(ratings) by different critics, the Chef needs you to tell him what is the minimum rating that his website will be displaying. For example in the above case, the minimum rating that will be displayed is 7. Also, different critics keep reviewing the restaurant continuosly. So the new reviews keep coming in. The Chef wants your website ratings to be up-to-date. So you should keep updating the ratings there. At any point of time, the Chef might want to know the minimum rating being displayed. You'll have to answer that query. An interesting thing to note here is that a review might be in the website for some time and get knocked out later because of new better reviews and vice-versa.

Notes: To be precise, the number of reviews displayed website will be floor(n / 3), where n denotes the current number of all reviews.

### Input

First line of the input file consists of a single integer N, the number of operations to follow. The next N lines contain one operation each on a single line. An operation can be of 2 types:

1 x : Add a review with rating 'x' to the exisiting list of reviews (x is an integer)

2 : Report the current minimum rating on the website

### Output

For every test case, output a single integer each for every operation of type 2 mentioned above. If no review qualifies as a positive review, print "No reviews yet".

### Constraints
`
1 ≤ N ≤ 250000
1 ≤ x ≤ 1000000000

`

---

## Examples

**Example 1**

**Input**

```text
10
1 1
1 7
2
1 9
1 21
1 8
1 5
2
1 9
2
```

**Output**

```text
No reviews yet
9
9
```

**Explanation**

Before the first query of the Chef, i.e. the first operation of type 2 in the input, the only ratings were 1 & 7. Thus, there will be total of 2/3 = 0 positive ratings. For the next two, the ratings list now looks like: 1 5 7 8 9 21. Hence, top one-third will have 6/3 = 2 ratings as positive. And lowest displayed rating will be 9. Similarly for the last operation of type 2. Note that there are two ratings of the same value 9 now and only one of them can be in the top reviews. In such a case, you can choose any one of them.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS:

[Practice](http://www.codechef.com/problems/RRATING)

[Contest](http://www.codechef.com/JULY12/problems/RRATING)

### DIFFICULTY:

Easy

### PREREQUISITES:

Heaps

### PROBLEM:

You’re given an online stream of numbers. At any point of time if **K** numbers have already appeared, you need to find out **floor(K/3)**th largest number.

### QUICK EXPLANATION:

Maintain two heaps - one min heap for top **floor(K/3)** numbers and other max heap for all remaining numbers.

### DETAILED EXPLANATION:

We can maintain two different heaps - one min heap for top **1/3th** of votes and

one max heap for all other votes. Once we have this, we can simulate actual

voting itself. The reason is after every vote, at maximum 1 vote moves between

the heaps.

To understand this, let’s say that at some point of time we’ve **x** votes in top heap

and **N - x** votes in other heap. If a new vote comes push it in one of the two halves

by comparing its value to the lowest value in top heap. Now assume it went in top

heap. Number of votes in top heap might be more than **floor( (N+1) / 3)** now in which case we’d need to transfer some numbers to the other heap. But difference

is only of 1 vote as number of votes in top heap <= **1 + floor(N/3)** and hence only 1 vote needs

to goto bottom heap. That one vote has to be the minimum value of this heap.

By similar argument, had the vote gone to bottom heap, again only its topmost value

need to be transfered to top heap, if at all.

At any query, all we have to do is find out the smallest value from top heap and print it.

Complexity of our solution is **O(N log N)** as we take **O(log N)** time per query.

### SETTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/July/Setter/RRATING.cpp).

### TESTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/July/Tester/RRATING.cpp).

### RELATED PROBLEMS:

[Spoj Weird Function](http://www.spoj.pl/problems/WEIRDFN/)

</details>
