# ChefTown Parade

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFTOWN |
| Difficulty Rating | 1882 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [CHEFTOWN](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/CHEFTOWN) |

---

## Problem Statement

ChefTown is the biggest city and the capital of ChefLand. There are N beautiful buildings: restaurants, museums, living houses with large kitchens and so on. Every building has its height. For every i (1<=i<=N) there is exactly one building with height i. The buildings are located in a single line from left to right. The height of ith building is H(i). The Mayor of ChefTown wants to organize a parade, where all great chefs will take part. A parade depends of its location. The location of a parade is a segment of consecutive buildings beginning near the building number L and ending near the building number R (1<=L<=R<=N). Any parade won't be interesting if it is not hold on an interesting segment of buildings. The segment of buildings is interesting if following are hold:

- Imagine, that we have a segment [L,R].

- Let K=R-L+1 be the length of this segment, and B be a list of heights of the buildings that belong to this segment.

- Let's sort B in non-decreasing order.

- Segment [L,R] is interesting if B[i]-B[i-1]=1 for every i (2<=i<=K).

Now the Mayor of ChefTown is interested how many ways to organize an interesting parade of length W for ChefTown citizens. Help him and find out the number of different parades of length W, which can be hold in the city. Two parades ([L1,R1] and [L2,R2]) are considered to be different, if L1≠L2 or R1≠R2.

### Input

 Each input file consists of two lines, the first one contains two integers N and W (1<=N<=400000, 1<=W<=N). The second line contains N numbers H(i) (1<=i<=N) - the heights of the buildings.

### Output

For each test case output a single integer - the number of interesting segments of buildings of length W.

---

## Examples

**Example 1**

**Input**

```text
2 1
2 1
```

**Output**

```text
2
```

**Example 2**

**Input**

```text
4 2
1 2 3 4
```

**Output**

```text
3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFTOWN)

[Contest](http://www.codechef.com/SEP12/problems/CHEFTOWN)

# DIFFICULTY

EASY

# PREREQUISITES

Data Structure, Double Ended Queue

# PROBLEM

Given a permutation of numbers from 1 to N, how many segments of length W exist such that

- Suppose the segment S of length W starts from L and ends at R, where R-L+1 = W

- We sort the items in S in increasing order

- Now, S should satisfy S[i] = S[i-1]+1, for i between 2 and K, inclusive (assuming S was 1-based)

# QUICK EXPLANATION

It is easy to see that a segment is valid iff

The largest value in the segment - the smallest value in the segment + 1 = W.

Now, we can find the largest and the smallest value in amortised O(1) time for all the N-W+1 segments and then in one parse, find the number of valid segments. The overall complexity of this algorithm is O(N).

# EXPLANATION

We have to find the smallest value in all N-W+1 segments of size W. To do so, we want to build a Queue with **getMax** capability.

We wish to use a queue to mimic the sliding window behaviour of considering segments, one after the other. And if the queue can efficiently tell us the minimum number inside the queue at any time, we are done. Thus our queue Q should have the following methods

- push: push an item in the queue

- pop: pop an item from the queue in FIFO order

- min: return the minimum value in the queue at this point

Let us implement Q using an internal double ended queue dQ, and an internal simple FIFO queue iQ.

About dQ

- dQ.size is the number of elements in dQ

- dQ.head is the first element in dQ

- dQ.tail is the last element in dQ

- dQ.push_front pushes the element at the head and changes head to this value

- dQ.pop_front pops the element at the head and shifts the head forward

- dQ.push_back pushes the element at the tail and changes the tail to this value

- dQ.pop_back pops the element at the tail and shifts the tail behind

About iQ

- iQ.size is the number of elements in iQ

- iQ.push pushes an element in iQ

- iQ.pop pops an element from iQ in FIFO order

Q.push is implemented as

`
function Q.push(item)
    while dQ.size && dQ.tail > item
        dQ.pop_back()
    dQ.push_back(item)
    iQ.push(item)
`

Q.pop is implemented as

`
function Q.pop()
    retVal = iQ.pop()
    if retVal == dQ.head then dQ.pop_front()
    return retVal
`

Q.min is implemented as

`
function Q.min()
    return dQ.head
`

Now, we make the following observations about Q

- iQ has all the elements inside Q

- dQ has a subset of elements, in Q, in increasing order

- dQ.head has the smallest element in Q

- followed by the next smallest element which was inserted after inserting the smallest element

- so on, till dQ.tail, which has the last element inserted in Q

- If the current item to pop is the smallest item in Q, then we do a iQ.pop() as well as dQ.pop_front(). This ensures that we have the smallest value after the pop operation

- If the last item (or last few items) which was inserted are larger than the current item, then their values are not relevant towards finding the minimum value, since

- They will be popped before popping the currently inserted item (FIFO order)

- They cannot be the smallest value since the current item’s value is smaller

You can work out several examples to see that this data structure works and returns the smallest value in Q at all times.

It remains to show that this is fast enough for this problem.

We will find the smallest values for each segment and store in an array Mi, by using Q as follows

`
Given: A[N]
Let Mi be an array of N-W+1 values
for i in 1 to W, inclusive
    Q.push(A[i])
Mi[1] = Q.min()
for i in W+1 to N, inclusive
    Q.push(A[i])
    Q.pop()
    Mi[i-W] = Q.min()
`

We see that Q.push is being called in a loop, and Q.push iterates over the length of dQ inside. But, if Q.push makes more than 1 comparison over dQ, it also pops items from dQ. Since each item inserted in dQ can only be popped once, there can be at most N pops through all the iterations.

That means that the sum of the number of comparisons made inside Q.push while it is being called in the loop from W+1 to N, will not be more than 2*N. The overall complexity of the algorithm to find the minimum value in each segment remains O(N).

Using the same ideas as above, you can build Ma[N], an array of the maximum values in each segment.

Following this, the result can be calculated as

`
result = 0
for i in 1 to N-W+1, inclusive
    if Ma[i] - Mi[i] + 1 == W then result = result + 1
print result
`

# SETTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Setter/CHEFTOWN.pas)

# TESTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Tester/CHEFTOWN.java)

</details>
