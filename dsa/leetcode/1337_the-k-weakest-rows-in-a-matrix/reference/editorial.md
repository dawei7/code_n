
## Solution

### Overview

We'll use the following grid as our example, with $k = 5$.

![The input grid.](images/input_grid.png)

Let's say the "strength" of a row is the number of `1`'s (soldiers) in it. Because we need to compare rows based on their "strength", let's start by calculating the "strength" of each row. The simplest way of doing this is to loop over each row, and count how many `1`'s there are. We'll put these counts into a new array of length `m` (remember, `m` is the number of rows).

![Calculating the strengths.](images/row_counts.png)

We need to return the `k` rows with the lowest "strength". So, perhaps we should sort the "strengths" we've found and take the first `k` from the sorted list? Doing the sort will give us the following array. The first `k` "strengths" are highlighted.

![Sorting the strengths.](images/sorted_row_counts.png)

Hold on a minute though, the question requires us to return the *indexes* of the lowest "strengths"! Because of the sorting, we no longer know which "strength" was originally at what index. We'll need to keep track of the indexes that went with the "strengths".

We'll go through several different approaches for solving this problem. Some can be more easily implemented using certain programming languages.

<br />

---

### Approach 1: Linear Search and Sorting

**Intuition**

The simplest approach to this problem depends on which programming language you're using. This first approach is recommended for *Python*. It is doable in Java and C++, but requires implementing a [Comparator](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html). This is perhaps too much work, as better options exist for those programming languages.

The first approach we'll look at is multi-tier sorting. Instead of only inserting "strengths" into the list, we'll also insert indexes. We can represent each "strength" and index pair as a `tuple`. We should put the "strength" *first* in each tuple because we'll be sorting based on "strength".

For now, we'll calculate the "strength" of each row using the linear search approach described above (we'll optimize it in a later approach).

Here is the list of tuples you'll get for the above example.

![The generated list of tuples.](images/tuples.png)

Now we can sort the list using Python's built-in sort.

![The sorted list of tuples.](images/sorted_tuples.png)

When told to sort tuples, Python firstly sorts on the first element of the tuple, and then breaks any ties by sorting on the second element. Quite conveniently, this is exactly what we wanted here! Where there is a tie, the lower indexes are first. The only thing left to do is pull the indexes out of the first `k` tuples.

**Algorithm**

```python
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

    # Note that there is a more conscise solution just below. This code
    # avoids the use of advanced language features.

    m = len(mat)
    n = len(mat[0])

    # Calculate the strength of each row.
    strengths = []
    for i, row in enumerate(mat):
        strength = 0
        for j in range(n):
            if row[j] == 0: break
            strength += 1
        strengths.append((strength, i))

    # Sort all the strengths. This will sort firstly by strength
    # and secondly by index.
    strengths.sort()

    # Pull out and return the indexes of the smallest k entries.
    indexes = []
    for i in range(k):
        indexes.append(strengths[i][1])
    return indexes
```

Here is a more Pythonic version of the code, using list comprehensions.

```python
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

    # Build a list of (strength, index) pairs.
    strengths = [(sum(row), i) for i, row in enumerate(mat)]

    # Sort.
    strengths.sort()

    # Pull out and return the indexes of the first k entries.
    return [i for strength, i in strengths[:k]]
```

**Complexity Analysis**

- Time Complexity : $O(m \cdot (n + \log \,m))$.

    For the first phase, we're calculating the "strength" of each row. Calculating the "strength" of a row (with this algorithm) and putting it into the list is $O(n)$ in the worst case, and there are $m$ rows. This gives us $O(n \cdot m)$.

    For the second phase, we are sorting the list (which is of length $m$). Sorting a list using the built-in sort is $O(m \, \log \, m)$.

    To get our final time, we'll add the 2 complexities together. Whether $n \cdot m$ or $m \, \log \,m$ is bigger depends on the relative sizes of $m$ and $n$. This means that we have to add them, giving  $m \cdot n + m \, \log\,m = m \cdot (n + \log \, m))$.

    If $k$ was really small, an optimization would be to use selection sort instead of the built in sort to avoid needing to sort the entire list.

- Space Complexity : $O(m)$.

    Constructing the list requires $O(m)$ space.

<br />

---

### Approach 2: Linear Search and Map

**Intuition**

This approach is recommended for Java and C++. In Python, it offers no advantage over Approach #1.

Another way we can keep track of the indexes is to put them into a `Map`. We'll go with a `HashMap` because more people are familiar with it, but a `TreeMap` could also be used (and has some nice advantages, but doesn't change the overall time complexity). The code in the next section shows both.

Each time we calculate the "strength" of a row, we should insert the index into the `Map` under its "strength". Because multiple indexes could have the same "strengths", the values of the `Map` should be *lists* of indexes, not single values. If we do this to the entire example from above, we get the following:

![Slide 1](images/slideshow_1337_hash_map_Slide1.PNG)

![Slide 2](images/slideshow_1337_hash_map_Slide2.PNG)

![Slide 3](images/slideshow_1337_hash_map_Slide3.PNG)

![Slide 4](images/slideshow_1337_hash_map_Slide4.PNG)

![Slide 5](images/slideshow_1337_hash_map_Slide5.PNG)

![Slide 6](images/slideshow_1337_hash_map_Slide6.PNG)

![Slide 7](images/slideshow_1337_hash_map_Slide7.PNG)

![Slide 8](images/slideshow_1337_hash_map_Slide8.PNG)

![Slide 9](images/slideshow_1337_hash_map_Slide9.PNG)

![Slide 10](images/slideshow_1337_hash_map_Slide10.PNG)

Next, we'll need to sort the keys and iterate over them, pulling indexes out until we have `k` of them. Remember that because of the way we generated the `Map`, the indexes within a list are already sorted. The indexes that you'll need to pull out for the above example ($k = 5$) are highlighted.

![The k items that are returned.](images/pulling_out_k.png)

**Algorithm**

Firstly, here is the solution using a `HashMap`.

```python
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

    m = len(mat)
    n = len(mat[0])

    # Calculate the strength of each row and put them in a dictionary.
    strengths = collections.defaultdict(list)
    for i, row in enumerate(mat):
        strength = 0
        for j in range(n):
            if row[j] == 0: break
            strength += 1
        strengths[strength].append(i)

    # Sort the keys.
    sorted_strengths = sorted(list(strengths.keys()))

    # Pull out and return the indexes of the smallest k entries.
    indexes = []
    for strength in sorted_strengths:
        for index in strengths[strength]:
            indexes.append(index)
            if len(indexes) == k: break
        if len(indexes) == k: break

    return indexes
```

Secondly, here is the solution using a `TreeMap`. The difference between a `HashMap` and a `TreeMap` is that the `TreeMap` maintains the keys in sorted order. Note that this doesn't change the overall time complexity of the algorithm though, because insertion into a `TreeMap` is more expensive (because it's having to do more work to maintain that sorted order). In terms of good coding practice, a `TreeMap` is definitely better here. I haven't provided Python code for this solution, because Python doesn't have a built in `TreeMap`.

```java
class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {

        int m = mat.length;
        int n = mat[0].length;

        // Calculate all the strengths and put them into a TreeMap.
        Map<Integer, List<Integer>> strengths = new TreeMap<>();
        for (int i = 0; i < m; i++) {
            int strength = 0;
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) break;
                strength++;
            }
            if (!strengths.containsKey(strength)) {
                strengths.put(strength, new ArrayList<>());
            }
            strengths.get(strength).add(i);
        }

        int[] indexes = new int[k];
        int i = 0;
        for (int key : strengths.keySet()) {
            for (int index : strengths.get(key)) {
                indexes[i] = index;
                i++;
                if (i == k) break;
            }
            if (i == k) break;
        }

        return indexes;
    }
}
```

**Complexity Analysis**

- Time Complexity : $O(m \cdot (n + \log \,m))$.

    For each of the $m$ rows, we're calculating the "strength", which costs $O(n)$, and then we're inserting it into a `HashMap`, which costs $O(1)$. This part gives us a total of $O(m \cdot n)$.

    Next, we're sorting the $m$ keys, which costs $O(m \, \log \, m)$. We're then pulling the values out of the `Map`, which costs $O(k)$. Overall, this costs $O(m \log m)$ because $k$ is always less than $m$.

    To get our final time, we'll add the 2 complexities together. Whether $n \cdot m$ or $m \, \log \, m$ is bigger depends on the relative sizes of $m$ and $n$. This means that we have to add them, giving $m \cdot n + m \, \log \,m  = m \cdot (n + \log\,m)$.

    Using a `TreeMap` would have had the same time complexity because inserting $m$ values into a tree map costs $O(m \, \log \, m)$, and doesn't require the explicit sorting because values in a TreeMap are already sorted.

- Space Complexity : $O(m)$.

    Constructing the `Map` requires $O(m)$ space, regardless of whether we use a `TreeMap` or `HashMap`.

<br>

---

### Approach 3: Binary Search and Sorting/ Map

**Intuition**

This approach uses **Binary Search**. If you're not familiar with this algorithm, have a look at the [Explore Module on Binary Search](https://leetcode.com/explore/learn/card/binary-search/) and do the first couple of problems.

The way that we calculated the "strength" of each row wasn't very efficient. What we used above was *linear search*, because it scanned through the row until it encountered a 0 (and if the row had been all 1's, it would have had to check the entire row!). Instead, we could find the index of the *first* `0` in each row, and use this to calculate the "strength".

![Link between index of first civilian and strength of row.](images/index_civillian_link.png)

So, let's think through how we could implement a *binary search* to find the first `0` in a given row.

Recall that *binary search* starts by looking at the middle element. It then decides which half of the array the "target" element (in this case the first 0 in the row) must be in and repeats the same process on that half until there's only one element left in the search space.

For example, here is the middle of a really long row. Which half of the array is the "target" in?

![](images/binary_search_example_1.png)

What about this one? You can't actually see the target element, but it's possible to know which half it's in.

![](images/binary_search_example_2.png)

And what about this one?

![](images/binary_search_example_3.png)

If the current "middle" element is a `0`, we know we've gone too far and the solution must be to the left. And if the current "middle" element is a `1`, then we know we haven't gone far enough, and the solution is to the right.

Here's the pseudocode for the binary search algorithm.

```python3
low = 0
high = n
while low < high:
    mid = low + (high - low) // 2
    if row[mid] == 1:
        low = mid + 1
    else:
        high = mid
return low
```

And here's an animation showing the algorithm in action.

![Slide 1](images/slideshow_1337_binary_search_Slide1.PNG)

![Slide 2](images/slideshow_1337_binary_search_Slide2.PNG)

![Slide 3](images/slideshow_1337_binary_search_Slide3.PNG)

![Slide 4](images/slideshow_1337_binary_search_Slide4.PNG)

![Slide 5](images/slideshow_1337_binary_search_Slide5.PNG)

![Slide 6](images/slideshow_1337_binary_search_Slide6.PNG)

![Slide 7](images/slideshow_1337_binary_search_Slide7.PNG)

![Slide 8](images/slideshow_1337_binary_search_Slide8.PNG)

![Slide 9](images/slideshow_1337_binary_search_Slide9.PNG)

![Slide 10](images/slideshow_1337_binary_search_Slide10.PNG)

![Slide 11](images/slideshow_1337_binary_search_Slide11.PNG)

![Slide 12](images/slideshow_1337_binary_search_Slide12.PNG)

![Slide 13](images/slideshow_1337_binary_search_Slide13.PNG)

![Slide 14](images/slideshow_1337_binary_search_Slide14.PNG)

![Slide 15](images/slideshow_1337_binary_search_Slide15.PNG)

**Algorithm**

```python
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

    n = len(mat[0])

    def binary_search(row):
        low = 0
        high = n
        while low < high:
            mid = low + (high - low) // 2
            if row[mid] == 1:
                low = mid + 1
            else:
                high = mid
        return low

    # Calculate the strength of each row using binary search.
    row_strengths = []
    for i, row in enumerate(mat):
        row_strengths.append((binary_search(row), i))

    # Sort all the strengths. This will sort firstly by strength
    # and secondly by index.
    row_strengths.sort()

    # Pull out and return the indexes of the smallest k entries.
    indexes = []
    for i in range(k):
        indexes.append(row_strengths[i][1])
    return indexes
```

**Complexity Analysis**

- Time Complexity : $$O(m \, \log m  n)$$.

    We determined above that Approach #1 and Approach #2 both have the same time complexity. This was $$O(m \cdot n)$$ to calculate the "strengths", and $$O(m \, \log \, m)$$ to get them into sorted order. For this approach though, we calculated the "strengths" using binary search instead of linear search. Calculating each row "strength" cost $$O(\log \,n)$$, and there were $m$ rows to calculate. This is, therefore, $$O(m \, \log \, n)$$. The second part will still be $$O(m \, \log \, m)$$.

    Like before, we don't know whether $m$ or $n$ is bigger. Therefore, we have to add the time complexities, which gives $$O(m \, \log \,n + m \, \log \, m) = O(m \cdot (\log \, n + \log \, m)) = O(m \, \log \, m n)$$.

- Space Complexity : $$O(m)$$.

    Same as above, as we're still relying on the same data structures.

<br />

---

### Approach 4: Binary Search and Priority Queue

**Intuition**

Note: This approach is easier to code in Python than in Java/ C++, because it requires the implementation of a [Comparator](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html).

The previous approaches use $$O(n)$$ space for gathering up row "strength" data. We then throw away $$n - k$$ of these, returning $k$ of them. Is there a way we can reduce this space usage to $$O(k)$$, by only keeping the smallest $k$ we've seen so far?

Problems like this can often be solved using a **Priority Queue**. Recall that a Priority Queue is a data structure that allows us to insert items, and to efficiently remove the *largest* item in the case of a **Max-Priority Queue**, or the *smallest* in the case of a **Min-Priority Queue**.

For this problem, we could start by inserting `k` "strengths" (along with their indexes) into the Priority Queue. After that, we'd only want to insert a "strength"/index pair if it was one of the `k` smallest we've seen so far. We would then also need to remove the largest to bring the total back down to `k`. For this, it makes sense to use a *Max*-Priority Queue. Here is an animation showing this process.

![Slide 1](images/slideshow_1337_priority_queue_Slide1.PNG)

![Slide 2](images/slideshow_1337_priority_queue_Slide2.PNG)

![Slide 3](images/slideshow_1337_priority_queue_Slide3.PNG)

![Slide 4](images/slideshow_1337_priority_queue_Slide4.PNG)

![Slide 5](images/slideshow_1337_priority_queue_Slide5.PNG)

![Slide 6](images/slideshow_1337_priority_queue_Slide6.PNG)

![Slide 7](images/slideshow_1337_priority_queue_Slide7.PNG)

![Slide 8](images/slideshow_1337_priority_queue_Slide8.PNG)

![Slide 9](images/slideshow_1337_priority_queue_Slide9.PNG)

![Slide 10](images/slideshow_1337_priority_queue_Slide10.PNG)

![Slide 11](images/slideshow_1337_priority_queue_Slide11.PNG)

![Slide 12](images/slideshow_1337_priority_queue_Slide12.PNG)

![Slide 13](images/slideshow_1337_priority_queue_Slide13.PNG)

![Slide 14](images/slideshow_1337_priority_queue_Slide14.PNG)

![Slide 15](images/slideshow_1337_priority_queue_Slide15.PNG)

![Slide 16](images/slideshow_1337_priority_queue_Slide16.PNG)

Once we've finished adding all the "strengths", we'll have the `k` smallest "strength"/index pairs in it. If we remove them from the PriorityQueue one-by-one, they'll be sorted from *largest to smallest*. We could either do this and then reverse, or we could iterate backwards over the output array inserting them.

**Algorithm**

Python has a *Min*-Priority Queue called *heapq*. We can convert it into a *Max*-Priority Queue by putting a negative sign in front of all the numbers going into it.

Java's `PriorityQueue` requires a [Comparator](https://docs.oracle.com/javase/8/docs/api/java/util/Comparator.html). We can make it behave as a *Max*-Priority Queue using this.

```python
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low

        # Calculate the strength of each row using binary search.
        # Put the strength/index pairs into a priority queue.
        pq = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)

        # Pull out and return the indexes of the smallest k entries.
        # Don't forget to convert them back to positive numbers!
        indexes = []
        while pq:
            strength, i = heapq.heappop(pq)
            indexes.append(-i)

        # Reverse, as the indexes are around the wrong way.
        indexes = indexes[::-1]

        return indexes
```

**Complexity Analysis**

- Time Complexity : $$O(m \, \log \, nk)$$.

    This approach is very similar to Approach #3. The only difference is that we're putting the "strengths" into a Priority Queue, and storing at most $k$ of them at a time.

    Calculating the strengths is still $$O(m \, \log \, n)$$.

    Inserting an item into a Priority Queue has a cost of $$O(\log\, x)$$, where $x$ is the maximum number of items that will be in the Priority Queue. For this algorithm, the maximum $x$ value is $k$ (not $m$). Therefore, each insertion costs $$log(k)$$. There are $m$ of these insertions, giving a total of $$O(m \, \log \,k)$$.

    Like before, we need to add $$m \, \log \, n + m \, \log \,k$$, and again we can't assume which is bigger out of $$\log \, n$$ and $$\log\,k$$. Therefore, the total time complexity is $$m \, \log \, n + m \, \log \, k = m \cdot (\log \, n + \log \, k) = O(m \,  \log nk)$$.

- Space Complexity : $$O(k)$$.

    We are keeping at most $k$ pieces of "strength" data at a time. Therefore, the space complexity is $$O(k)$$.

<br />

---

### Approach 5: Vertical Iteration

**Intuition**

There's another, completely different, way of looking at the problem which as we'll see, decreases the space usage at the cost of time. Instead of going row-by-row calculating the "strengths", we can instead go column-by-column. Interestingly, we don't actually calculate the row "strengths" at all! This approach was inspired by the code of [lenchen1112](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/discuss/496644/Clean-Python-3-beats-100-without-sort-or-heap) on the discussion forum.

On each cell we pass that is a `0`, we check if the cell to the left was a `1`. If it was, then we're on the first `0` of that row and should add its index to our output list. Once there are `k` indexes in the output list, we simply return the list. The order in which the rows are found using this approach turns out to be the sorted order we want!

Here is an animation showing the algorithm.

One edge case to be careful of is that it is possible some of the `k` rows will contain entirely `1`'s. (e.g. if the whole grid was `1`'s).

![Slide 1](images/slideshow_1337_vertical_algorithm_Slide1.PNG)

![Slide 2](images/slideshow_1337_vertical_algorithm_Slide2.PNG)

![Slide 3](images/slideshow_1337_vertical_algorithm_Slide3.PNG)

![Slide 4](images/slideshow_1337_vertical_algorithm_Slide4.PNG)

![Slide 5](images/slideshow_1337_vertical_algorithm_Slide5.PNG)

![Slide 6](images/slideshow_1337_vertical_algorithm_Slide6.PNG)

![Slide 7](images/slideshow_1337_vertical_algorithm_Slide7.PNG)

![Slide 8](images/slideshow_1337_vertical_algorithm_Slide8.PNG)

![Slide 9](images/slideshow_1337_vertical_algorithm_Slide9.PNG)

![Slide 10](images/slideshow_1337_vertical_algorithm_Slide10.PNG)

![Slide 11](images/slideshow_1337_vertical_algorithm_Slide11.PNG)

![Slide 12](images/slideshow_1337_vertical_algorithm_Slide12.PNG)

![Slide 13](images/slideshow_1337_vertical_algorithm_Slide13.PNG)

![Slide 14](images/slideshow_1337_vertical_algorithm_Slide14.PNG)

![Slide 15](images/slideshow_1337_vertical_algorithm_Slide15.PNG)

![Slide 16](images/slideshow_1337_vertical_algorithm_Slide16.PNG)

![Slide 17](images/slideshow_1337_vertical_algorithm_Slide17.PNG)

![Slide 18](images/slideshow_1337_vertical_algorithm_Slide18.PNG)

![Slide 19](images/slideshow_1337_vertical_algorithm_Slide19.PNG)

![Slide 20](images/slideshow_1337_vertical_algorithm_Slide20.PNG)

![Slide 21](images/slideshow_1337_vertical_algorithm_Slide21.PNG)

![Slide 22](images/slideshow_1337_vertical_algorithm_Slide22.PNG)

![Slide 23](images/slideshow_1337_vertical_algorithm_Slide23.PNG)

![Slide 24](images/slideshow_1337_vertical_algorithm_Slide24.PNG)

![Slide 25](images/slideshow_1337_vertical_algorithm_Slide25.PNG)

![Slide 26](images/slideshow_1337_vertical_algorithm_Slide26.PNG)

![Slide 27](images/slideshow_1337_vertical_algorithm_Slide27.PNG)

![Slide 28](images/slideshow_1337_vertical_algorithm_Slide28.PNG)

![Slide 29](images/slideshow_1337_vertical_algorithm_Slide29.PNG)

![Slide 30](images/slideshow_1337_vertical_algorithm_Slide30.PNG)

![Slide 31](images/slideshow_1337_vertical_algorithm_Slide31.PNG)

![Slide 32](images/slideshow_1337_vertical_algorithm_Slide32.PNG)

![Slide 33](images/slideshow_1337_vertical_algorithm_Slide33.PNG)

![Slide 34](images/slideshow_1337_vertical_algorithm_Slide34.PNG)

![Slide 35](images/slideshow_1337_vertical_algorithm_Slide35.PNG)

![Slide 36](images/slideshow_1337_vertical_algorithm_Slide36.PNG)

![Slide 37](images/slideshow_1337_vertical_algorithm_Slide37.PNG)

![Slide 38](images/slideshow_1337_vertical_algorithm_Slide38.PNG)

![Slide 39](images/slideshow_1337_vertical_algorithm_Slide39.PNG)

![Slide 40](images/slideshow_1337_vertical_algorithm_Slide40.PNG)

![Slide 41](images/slideshow_1337_vertical_algorithm_Slide41.PNG)

![Slide 42](images/slideshow_1337_vertical_algorithm_Slide42.PNG)

![Slide 43](images/slideshow_1337_vertical_algorithm_Slide43.PNG)

![Slide 44](images/slideshow_1337_vertical_algorithm_Slide44.PNG)

![Slide 45](images/slideshow_1337_vertical_algorithm_Slide45.PNG)

![Slide 46](images/slideshow_1337_vertical_algorithm_Slide46.PNG)

![Slide 47](images/slideshow_1337_vertical_algorithm_Slide47.PNG)

![Slide 48](images/slideshow_1337_vertical_algorithm_Slide48.PNG)

![Slide 49](images/slideshow_1337_vertical_algorithm_Slide49.PNG)

![Slide 50](images/slideshow_1337_vertical_algorithm_Slide50.PNG)

![Slide 51](images/slideshow_1337_vertical_algorithm_Slide51.PNG)

![Slide 52](images/slideshow_1337_vertical_algorithm_Slide52.PNG)

![Slide 53](images/slideshow_1337_vertical_algorithm_Slide53.PNG)

![Slide 54](images/slideshow_1337_vertical_algorithm_Slide54.PNG)

![Slide 55](images/slideshow_1337_vertical_algorithm_Slide55.PNG)

![Slide 56](images/slideshow_1337_vertical_algorithm_Slide56.PNG)

![Slide 57](images/slideshow_1337_vertical_algorithm_Slide57.PNG)

![Slide 58](images/slideshow_1337_vertical_algorithm_Slide58.PNG)

![Slide 59](images/slideshow_1337_vertical_algorithm_Slide59.PNG)

![Slide 60](images/slideshow_1337_vertical_algorithm_Slide60.PNG)

![Slide 61](images/slideshow_1337_vertical_algorithm_Slide61.PNG)

![Slide 62](images/slideshow_1337_vertical_algorithm_Slide62.PNG)

![Slide 63](images/slideshow_1337_vertical_algorithm_Slide63.PNG)

![Slide 64](images/slideshow_1337_vertical_algorithm_Slide64.PNG)

![Slide 65](images/slideshow_1337_vertical_algorithm_Slide65.PNG)

![Slide 66](images/slideshow_1337_vertical_algorithm_Slide66.PNG)

![Slide 67](images/slideshow_1337_vertical_algorithm_Slide67.PNG)

![Slide 68](images/slideshow_1337_vertical_algorithm_Slide68.PNG)

![Slide 69](images/slideshow_1337_vertical_algorithm_Slide69.PNG)

![Slide 70](images/slideshow_1337_vertical_algorithm_Slide70.PNG)

![Slide 71](images/slideshow_1337_vertical_algorithm_Slide71.PNG)

**Algorithm**

```python
def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    m = len(mat)
    n = len(mat[0])

    # This code does the same as the animation above.
    indexes = []
    # For each cell, accessed in the order shown in the animation.
    for c, r in itertools.product(range(n), range(m)):
        if len(indexes) == k: break
        # If this is the first 0 in the current row.
        if mat[r][c] == 0 and (c == 0 or mat[r][c - 1] == 1):
            indexes.append(r)

    # If there aren't enough, it's because some of the first k weakest rows
    # are entirely 1's. We need to include the ones with the lowest indexes
    # until we have at least k.
    i = 0
    while len(indexes) < k:
        # If index i in the last column is 1, this was a full row and therefore
        # couldn't have been included in the output yet.
        if mat[i][-1] == 1:
            indexes.append(i)
        i += 1

    return indexes
```

**Complexity Analysis**

- Time Complexity : $O(m \cdot n)$.

    We are visiting each of the first $m \cdot n - 1$ cells at most once, and the last column of $m$ cells at most twice. In big-oh notation, $O(m \cdot (n - 1) + 2 \cdot m) = O(m \cdot n)$. At each of the cells we do a simple $O(1)$ check to determine whether or not it should be added to the output list. The output list doesn't need any further processing, and so does not add anything further to the time complexity. This leaves us with $O(m \cdot n)$.

- Space Complexity : $O(1)$.

    Because the output array is used *only* for gathering up the outputs to return, and these outputs require no further processing, this algorithm is considered to be $O(1)$ space. This is in contrast to the previous approaches that were also using the output array as working memory.

    Another way of looking at it is that if you needed to return the output values one-by-one (i.e. a generator function) for this algorithm, the array would disappear entirely. This is not true of the earlier approaches, which still require it to gather and then sort the values.

<br />