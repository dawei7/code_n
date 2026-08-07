[TOC]

## Solution

---
### Overview

We are asked to design a _**Zigzag Iterator**_ for two vectors, so that we could output the elements in an alternative way.

>The **_follow-up_** question is that what if we are given `k` vectors, instead of two?

Since this is a design problem, it would be more interesting to tackle the problem while taking into account the follow-up question all at once.

In this article, we will present two approaches which can be easily extended to `k` vectors.

---
### Approach 1: Two-Pointers

**Intuition**

We are asked to iterate the elements, while alternating the vectors.
One can imagine this as iterating over a two-dimension matrix, where each row represents an input vector.

>The idea is that we can employ _**two pointers**_ for iteration: one pointed to the vector (denoted as $p_{vec}$), and the other pointed to the element within the vector (denoted as $p_{elem}$).

![two pointers](images/281_two_pointers.png)

As we can see from the above graph, the vector pointer ($p_{vec}$) will move in the _zigzag_ way (more precisely **_cyclic_** way), _i.e._ once it reaches the last vector, it will start all over from the first vector.

The element pointer ($p_{elem}$) increments, only when the vector pointer finishes a _cycle_.

We give the priority to the vector pointer, _i.e._ we move the vector pointer _first_, then the element pointer.

**Algorithm**

With the above-mentioned two pointers, one should have all the elements needed to implement the function of `next()`.

To implement the function of `hasNext()`, we can keep **_account_** of the number of elements we output so far.
Once it reaches the total number of elements in the input, we would know that there is no more element to output.

Here are some sample implementations based on the above ideas.

```python
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.p_elem = 0   # pointer to the index of element
        self.p_vec = 0    # pointer to the vector
        # variables for hasNext() function
        self.total_num = len(v1) + len(v2)
        self.output_count = 0

    def next(self) -> int:
        iter_num = 0
        ret = None

        # Iterate over the vectors
        while iter_num < len(self.vectors):
            curr_vec = self.vectors[self.p_vec]
            if self.p_elem < len(curr_vec):
                ret = curr_vec[self.p_elem]

            iter_num += 1
            self.p_vec = (self.p_vec + 1) % len(self.vectors)
            # increment the element pointer once iterating all vectors
            if self.p_vec == 0:
                self.p_elem += 1

            if ret is not None:
                self.output_count += 1
                return ret

        # no more element to output
        raise Exception

    def hasNext(self) -> bool:
        return self.output_count < self.total_num

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
```

**Complexity Analysis**

Let $K$ be the number of input vectors, although it is always two in the setting of the problem.
This variable becomes relevant, once the input becomes $K$ vectors.

- Time Complexity:

- For the `next()` function, at most it will take us $K$ iterations to find a valid element output. Hence, its time complexity is $\mathcal{O}(K)$.

- For the `hasNext()` function, its time complexity is $\mathcal{O}(1)$.

- Space Complexity:

- For the `next()` function, we keep the references to all the input vectors in the variable `self.vectors`.
    As a result, we would need $\mathcal{O}(K)$ space for $K$ vectors.
    In addition, we used some constant-space variables such as the pointers to the vector and the element.
    Hence, the overall space complexity for this function is $\mathcal{O}(K)$.

- *Note:* we did not copy the input vectors, but simply keep references to them.

---
### Approach 2: Queue of Pointers

**Intuition**

The above approach is not the most efficient when the input vectors are not of equal size.
For instance, for the input vectors of `[1], [2, 3, 4, 5]`, we would waste some computing cycles to alternate the vector pointer, once we consume all the elements from the shorter vector.
The problem exacerbates when the number of input vectors grows.

>One idea to alleviate the above problem is to keep a **_queue_** of pointers to the input vectors as shown in the following graph.

![queue of pointers](images/281_queue.png)

The queue functions in the following ways:

- Initially, each input vector will have a corresponding pointer in the queue.

- At each invocation of `next()` function, we _**pop**_ out a pointer from the queue. With the pointer to the chosen vector, we further output an element from the vector.

- If the vector still has some elements left, we _**append**_ another pointer pointed to the vector at the end of the queue.
    In this way, we _alternate_ the order of vectors.

- If all the elements in the chosen vector are already outputted, we will NOT append another pointer. As a result, the vector would be out of the scope of the iteration. Later we won't waste any effort to iterate over the vectors that are exhausted.

- As to the `hasNext()` function, as long as there are still some pointers left in the queue, we would still have more elements to output.

**Algorithm**

One could use the `Iterator` object (in Java or C++) as the pointer to the vector.
Some of you might argue that we might be building a _iterator_ with a built-in iterator.
This has certain truth in it.

>However, the key point here is that we could simply use some _index_ and _integer_ to implement the role of _pointer_ in the above idea.

There are several advantages of using the _queue_ of pointers, as one will see from the implementations later:

- First of all, we would achieve a constant time complexity for the `next()` function.

- The logics of implementation is much simplified and thus easy to read.

```python
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.queue = deque()
        for index, vector in enumerate(self.vectors):
            # <index_of_vector, index_of_element_to_output>
            if len(vector) > 0:
                self.queue.append((index, 0))

    def next(self) -> int:

        if self.queue:
            vec_index, elem_index = self.queue.popleft()
            next_elem_index = elem_index + 1
            if next_elem_index < len(self.vectors[vec_index]):
                # append the pointer for the next round
                # if there are some elements left
                self.queue.append((vec_index, next_elem_index))

            return self.vectors[vec_index][elem_index]

        # no more element to output
        raise Exception

    def hasNext(self) -> bool:
        return len(self.queue) > 0
```

**Complexity Analysis**

Let $K$ be the number of input vectors, although it is always two in the setting of the problem.
This variable becomes relevant, once the input becomes $K$ vectors.

- Time Complexity: $\mathcal{O}(1)$

- For both the `next()` function and the `hasNext()` function, we have a constant time complexity, as we discussed before.

- Space Complexity: $\mathcal{O}(K)$

- We use a queue to keep track of the _pointers_ to the input vectors in the variable `self.vectors`.
    As a result, we would need $\mathcal{O}(K)$ space for $K$ vectors.

- Although the size of queue will reduce over time once we exhaust some shorter vectors, the space complexity for both functions is still $\mathcal{O}(K)$.

---