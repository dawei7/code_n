
## Solution

---

### Overview

Solving this problem efficiently requires a couple of key observations.

1. If the number of unique candies is *less than or equal to* half the length of `candyType`, then Alice can eat one of each type of candy and the answer is equal to the *number of unique candies*.
2. Otherwise, the number of candies she can eat is limited to half the length of `candyType`, and so the answer is equal to *half the length of `candyType`*.

In essence, this problem boils down to finding the *number of unique candies*. We then return whichever value is *smaller* out of the *number of unique candies* and *half the length of `candyType`*.

</br>

---

### Approach 1: Brute Force

**Intuition and Algorithm**

One way to find the number of unique candies is to traverse over each element in `candyType`, checking whether or not we've already seen a candy of this same type. We can do this check by iterating over all elements *before* the current element. If any of those are of the same type, then this is not a unique candy. We should keep track of the number of unique candies we find.

```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # We need to count how many unique candies are in the array.
        unique_candies = 0
        # For each candy, we're going to check whether or not we've already
        # seen a candy identical to it.
        for i in range(len(candyType)):
            # Check if we've already seen a candy the same as candyType[i].
            for j in range(0, i):
                # If this candy is the same as previous one, we don't need to
                # check further.
                if candyType[i] == candyType[j]:
                    break
            # Confused? An "else" after a "for" is an awesome Python feature.
            # The code in the "else" only runs if the "for" loop runs without a break.
            # In this case, we know that if we didn't "break" out of the loop, then
            # candyType[i] is unique.
            # https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
            else:
                unique_candies += 1
        # The answer is the minimum out of the number of unique candies, and
        # half the length of the candyType array.
        return min(unique_candies, len(candyType) // 2)
```

**Complexity Analysis**

Let $N$ be the the length of `candyType`.

* Time complexity : $O(N^2)$. We traverse over each of the $N$ elements of $candyType$, and for each, we check all of the elements before it. Checking each item for each item is the classic $O(N^2)$ time complexity pattern.

* Space complexity : $O(1)$. We don't allocate any additional data structures, instead only using constant space variables.

</br>

---

### Approach 2: Sorting

**Intuition and Algorithm**

The previous approach is too inefficient to reliably avoid a `Time Limit Exceeded` (at the time of writing this article), but most importantly, it is unlikely to impress your interviewer!

Is there a more efficient way that we can count the number of unique candies? Yes, there is!

One way is to sort `candyType` first, so that we can then count the number of unique candies by comparing adjacent elements in the sorted array. This removes the need to do repeated traversals.

As a quick warning before we get to the code though, this approach *modifies the input array*. This isn't always a good idea, and is something you should always ask your interviewer about.

> **Interview Tip: In-place Algorithms**
>
> In-place algorithms overwrite the input to save space, but sometimes this can cause problems. Here are a couple of situations where an in-place algorithm might not be suitable.
> 1. The algorithm needs to run in a *multi-threaded* environment, without exclusive access to the array. Other threads might need to read the array too, and might not expect it to be modified.
> 2. Even if there is only a single thread, or the algorithm has exclusive access to the array while running, the array might need to be reused later or by another thread once the lock has been released.
>
> In an interview, you should always check whether or not the interviewer minds you overwriting the input. Be ready to explain the pros and cons of doing so if asked!

```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # We start by sorting candyType.
        candyType.sort()
        # The first candy is always unique.
        unique_candies = 1
        # For each candy, starting from the *second* candy...
        for i in range(1, len(candyType)):
            # This candy is unique if it is different to the one
            # immediately before it.
            if candyType[i] != candyType[i - 1]:
                unique_candies += 1
            # Optimization: We should terminate the loop if unique_candies
            # is now at the maxium she can eat.
            if unique_candies == len(candyType) // 2:
                break
        # Like before, the answer is the minimum out of the number of unique candies, and
        # half the length of the candyType array.
        return min(unique_candies, len(candyType) // 2)
```

If you're using a language that has a built-in *heapify* function, then you can use this to further optimize the space complexity to $O(1)$. Here is an example of using `heapify` in Python.

```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # We start by heapifying candyType.
        heapq.heapify(candyType)
        # We need to save this now, as we're going to be modifying candyType.
        maximum_candies_allowed = len(candyType) // 2
        unique_candies = 0
        # And now, remove elements off the heap until
        while candyType and unique_candies < maximum_candies_allowed:
            # Take a candy off, we'll be checking if it is unique.
            candy = heapq.heappop(candyType)
            # If the next candy is not the same as this one, or there isn't a next
            # candy, then this candy must be unique.
            if not candyType or candyType[0] != candy:
                unique_candies += 1
        # Like before, the answer is the minimum out of the number of unique candies, and
        # half the length of the candyType array.
        return min(unique_candies, maximum_candies_allowed)
```

**Complexity Analysis**

Let $N$ be the the length of `candyType`.

* Time complexity : $O(N \log N)$.

    We start by sorting the $N$ elements in `candyType`, which has a cost of $O(N \log N)$.

    We then perform a single pass through `candyType`, performing an $O(1)$ operation at each step: this has a total cost of $O(N)$.

    This gives us a total of $O(N \log N) + O(N)$. When adding complexities, we only keep the one that is strictly bigger, this leaves us with $O(N \log N)$.

* Space complexity : Dependent on the sorting algorithm implementation, which is generally between $O(1)$ and $O(N)$.

    Python and Java now use Timsort, which requires $O(N)$ space.

    The `heapify` variant for Python is $O(1)$, as it uses Heapsort.

</br>

---

### Approach 3: Using a Hash Set

**Intuition and Algorithm**

> **Explore Card**: Check out our [Explore Card on Hash Tables](https://leetcode.com/explore/learn/card/hash-table/) if you are unfamiliar with them.

Recall that a Set cannot contain duplicates, and attempting to add a duplicate item into a Set will do nothing.

Therefore, the best way to find the number of unique elements is to simply insert all of the `candyType` elements into a Hash Set. After that, the number of unique candies is simply the number of elements in the Hash Set.

```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Count the number of unique candies by creating a set with
        # candyType, and then taking its length.
        unique_candies = len(set(candyType))
        # And find the answer in the same way as before.
        return min(unique_candies, len(candyType) // 2)
```

**Complexity Analysis**

Let $N$ be the the length of `candyType`.

* Time complexity : $O(N)$.

    Adding an item into a Hash Set has an *amortized* time of $O(1)$. Therefore, adding $N$ items requires $O(N)$ time. All of the other operations we use are $O(1)$.

* Space complexity : $O(N)$.

    The worst case for space complexity occurs when all $N$ elements are unique. This will result in a Hash Set containing $N$ elements.