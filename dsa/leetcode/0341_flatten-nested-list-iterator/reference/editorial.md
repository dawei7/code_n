
## Solution

---

### Overview

If you aren't at all familiar with Iterators, then we suggest having a go at [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/). Additionally, the [Solution Article for Peeking Iterator](https://leetcode.com/problems/peeking-iterator/solution/) has a special introduction section that introduces you to what Iterators are.

If you're still having trouble, have a go at writing a function that simply flattens a nested list (i.e. not as an iterator). Then, think about how you could adapt it to be an iterator.

In this article, we cover 5 approaches. Approach 4 is primarily for Java programmers, and Approach 5 is for programmers of languages where generators are supported.

<br/>

---

### Approach 1: Make a Flat List with Recursion

**Intuition**

The simplest way of solving this problem is to flatten the entire input list, in the constructor. Then the actual iterator methods can simply work with this flattened list instead of needing to worry about the input structure.

This approach splits the coding into two parts:

1. A function that the constructor can call to make a flattened list.
2. `next()` and `hasNext()` methods that iterate over a plain list, by keeping track of the current position within it.

The first part is best done with recursion (iteration is more complicated, and if you were going to use it, then you may as well look at approaches 2, 3, and 4 instead). This approach is the only recursive one that works in any programming language (as of the time of writing this article, things are changing!).

To flatten the list recursively, notice that we can look at the input as a tree. The integers are the leaf nodes, and the order they should be returned is from left to right.

![Slide 1](images/slideshow_341_flatten_tree_expansion_Slide1.PNG)

![Slide 2](images/slideshow_341_flatten_tree_expansion_Slide2.PNG)

![Slide 3](images/slideshow_341_flatten_tree_expansion_Slide3.PNG)

![Slide 4](images/slideshow_341_flatten_tree_expansion_Slide4.PNG)

![Slide 5](images/slideshow_341_flatten_tree_expansion_Slide5.PNG)

Therefore, we can use a recursive depth-first search to flatten it.

```text
integers = []

define function flattenList(nestedList):
    for nestedInteger in nestedList:
        if nestedInteger.isInteger():
            append nestedInteger.getInteger() to integers
        else:
            recursively call flattenList on nestedInteger.getList()
```

Here is an animation showing the flattening algorithm.

![Slide 1](images/slideshow_341_flatten_tree_Slide1.PNG)

![Slide 2](images/slideshow_341_flatten_tree_Slide2.PNG)

![Slide 3](images/slideshow_341_flatten_tree_Slide3.PNG)

![Slide 4](images/slideshow_341_flatten_tree_Slide4.PNG)

![Slide 5](images/slideshow_341_flatten_tree_Slide5.PNG)

![Slide 6](images/slideshow_341_flatten_tree_Slide6.PNG)

![Slide 7](images/slideshow_341_flatten_tree_Slide7.PNG)

![Slide 8](images/slideshow_341_flatten_tree_Slide8.PNG)

![Slide 9](images/slideshow_341_flatten_tree_Slide9.PNG)

![Slide 10](images/slideshow_341_flatten_tree_Slide10.PNG)

![Slide 11](images/slideshow_341_flatten_tree_Slide11.PNG)

![Slide 12](images/slideshow_341_flatten_tree_Slide12.PNG)

![Slide 13](images/slideshow_341_flatten_tree_Slide13.PNG)

![Slide 14](images/slideshow_341_flatten_tree_Slide14.PNG)

![Slide 15](images/slideshow_341_flatten_tree_Slide15.PNG)

![Slide 16](images/slideshow_341_flatten_tree_Slide16.PNG)

![Slide 17](images/slideshow_341_flatten_tree_Slide17.PNG)

![Slide 18](images/slideshow_341_flatten_tree_Slide18.PNG)

![Slide 19](images/slideshow_341_flatten_tree_Slide19.PNG)

![Slide 20](images/slideshow_341_flatten_tree_Slide20.PNG)

![Slide 21](images/slideshow_341_flatten_tree_Slide21.PNG)

![Slide 22](images/slideshow_341_flatten_tree_Slide22.PNG)

![Slide 23](images/slideshow_341_flatten_tree_Slide23.PNG)

![Slide 24](images/slideshow_341_flatten_tree_Slide24.PNG)

![Slide 25](images/slideshow_341_flatten_tree_Slide25.PNG)

![Slide 26](images/slideshow_341_flatten_tree_Slide26.PNG)

![Slide 27](images/slideshow_341_flatten_tree_Slide27.PNG)

![Slide 28](images/slideshow_341_flatten_tree_Slide28.PNG)

![Slide 29](images/slideshow_341_flatten_tree_Slide29.PNG)

![Slide 30](images/slideshow_341_flatten_tree_Slide30.PNG)

![Slide 31](images/slideshow_341_flatten_tree_Slide31.PNG)

![Slide 32](images/slideshow_341_flatten_tree_Slide32.PNG)

![Slide 33](images/slideshow_341_flatten_tree_Slide33.PNG)

![Slide 34](images/slideshow_341_flatten_tree_Slide34.PNG)

![Slide 35](images/slideshow_341_flatten_tree_Slide35.PNG)

![Slide 36](images/slideshow_341_flatten_tree_Slide36.PNG)

![Slide 37](images/slideshow_341_flatten_tree_Slide37.PNG)

![Slide 38](images/slideshow_341_flatten_tree_Slide38.PNG)

![Slide 39](images/slideshow_341_flatten_tree_Slide39.PNG)

![Slide 40](images/slideshow_341_flatten_tree_Slide40.PNG)

![Slide 41](images/slideshow_341_flatten_tree_Slide41.PNG)

![Slide 42](images/slideshow_341_flatten_tree_Slide42.PNG)

![Slide 43](images/slideshow_341_flatten_tree_Slide43.PNG)

![Slide 44](images/slideshow_341_flatten_tree_Slide44.PNG)

![Slide 45](images/slideshow_341_flatten_tree_Slide45.PNG)

![Slide 46](images/slideshow_341_flatten_tree_Slide46.PNG)

![Slide 47](images/slideshow_341_flatten_tree_Slide47.PNG)

**Algorithm**

```python
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        def flatten_list(nested_list):
            for nested_integer in nested_list:
                if nested_integer.isInteger():
                    self._integers.append(nested_integer.getInteger())
                else:
                    flatten_list(nested_integer.getList())
        self._integers = []
        self._position = -1 # Pointer to previous returned.
        flatten_list(nestedList)

    def next(self) -> int:
        self._position += 1
        return self._integers[self._position]

    def hasNext(self) -> bool:
        return self._position + 1 < len(self._integers)
```

**Complexity Analysis**

Let $N$ be the total number of *integers* within the nested list, $L$ be the total number of *lists* within the nested list, and $D$ be the maximum nesting depth (maximum number of lists inside each other).

- Time complexity:

    We'll analyze each of the methods separately.

- **Constructor:** $O(N + L)$.

        The constructor is where all the time-consuming work is done.

        For each list within the nested list, there will be one call to `flattenList(...)`. The loop within `flattenList(...)` will then iterate $n$ times, where $n$ is the number of integers within that list. Across all calls to `flattenList(...)`, there will be a total of $N$ loop iterations. Therefore, the time complexity is the number of lists plus the number of integers, giving us $O(N + L)$.

        Notice that the maximum depth of the nesting does not impact the time complexity.

- **next():** $O(1)$.

        Getting the next element requires incrementing `position` by 1 and accessing an element at a particular index of the `integers` list. Both of these are $O(1)$ operations.

- **hasNext():** $O(1)$.

        Checking whether or not there is a next element requires comparing the length of the `integers` list to the `position` variable. This is an $O(1)$ operation.

- Space complexity : $O(N + D)$.

    The most obvious auxiliary space is the `integers` list. The length of this is $O(N)$.

    The less obvious auxiliary space is the space used by the `flattenList(...)` function. Recall that recursive functions need to keep track of where they're up to by putting stack frames on the runtime stack. Therefore, we need to determine what the maximum number of stack frames there could be at a time is. Each time we encounter a nested list, we call `flattenList(...)` and a stack frame is added. Each time we finish processing a nested list, `flattenList(...)` returns and a stack frame is removed. Therefore, the maximum number of stack frames on the runtime stack is the maximum nesting depth, $D$.

    Because these two operations happen one-after-the-other, and either could be the largest, we add their time complexities together giving a final result of $O(N + D)$.

<br/>

---

### Approach 2: Stack

**Intuition**

The downside of Approach 1 is that it creates a new data structure instead of simply iterating over the given one. Instead, we should find a way to step through the integers, one at a time, keeping track of where we're currently up to in `nestedList`.

A better way is to do an iterative depth-first search, based on the following tree traversal algorithm:

```text
define function iterativeDepthFirstSearch(nestedList):
    result = []

    stack = a new Stack
    push all items in nestedList onto stack, in reverse order

    while stack is not empty:
        nestedInteger = pop top of stack
        if nestedInteger.isInteger():
            append nestedInteger.getInteger() to result
        else:
            list = nestedInteger.getList()
            push all items in list onto stack, in reverse order

    return result
```

While we could use this algorithm in the constructor like before, a better way would be to store `stack` on the iterator object and progress the algorithm on each call to `next()` to get the next integer out.

Notice that if the top of the stack is an integer, then we've already found the next integer. Otherwise, if it's a list, then the `else` is adding the list contents to `stack`. On the next loop iteration, the same will happen. We could write an algorithm to get the next integer as follows.

```text
stack = a new Stack
push all items in nestedList onto stack, in reverse order

define function getNextInteger():
    while stack is not empty:
        nestedInteger = pop top off stack
        if nestedInteger.isInteger():
            RETURN nestedInteger.getInteger()
        else:
            list = nestedInteger.getList()
            push all items in list onto stack, in reverse order

```

Notice that the `stack` is shared between calls. This means that `getNextInteger()` will find an integer and return it, while still preserving the state of the stack. We can then call `getNextInteger()` again to get the next integer, and so forth.

To simplify the code a bit, we can change our loop condition so that it checks if the top of the stack is still a list. The loop body should push the contents of the list onto the stack (in reverse). Eventually, there will be an integer on the top of the stack, OR the stack will be empty. Being able to get the next integer to the top of the stack allows the `next()` and `hasNext()` methods to access it.

```text
stack = a new Stack
push all items in nestedList onto stack, in reverse order

define function makeStackTopAnInteger():
    while stack is not empty AND the nestedInteger at top of stack is a list:
        nestedInteger = pop top off stack
        list = nestedInteger.getList()
        push all items in list onto stack, in reverse order
```

**Algorithm**

Let's define a private method called `makeStackTopAnInteger()` that contains the algorithm to make the stack top an integer (as described above). The `makeStackTopAnInteger()` method never *removes* integers.

The `next()` and `hasNext()` methods should call `makeStackTopAnInteger()` before doing anything else. This means that they can then *assume* that either the stack top is an integer, *or* the stack is empty. Then, their definitions are as follows:

- **hasNext():** Returns `true` if the stack still contains items, `false` if not.
- **next():** If the stack still contains items, then it is guaranteed the top is an integer. This integer is popped and returned. If the stack is empty, then the behavior is language-dependent. For example, in Java, a `NoSuchElementException` should be throw.

```python
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0

    def make_stack_top_an_integer(self):
        # While the stack contains a nested list at the top...
        while self.stack and not self.stack[-1].isInteger():
            # Unpack the list at the top by putting its items onto
            # the stack in reverse order.
            self.stack.extend(reversed(self.stack.pop().getList()))
```

**Complexity Analysis**

Let $N$ be the total number of *integers* within the nested list, $L$ be the total number of *lists* within the nested list, and $D$ be the maximum nesting depth (maximum number of lists inside each other).

- Time complexity.

- **Constructor:** $O(N + L)$.

        The worst-case occurs when the initial input nestedList consists entirely of integers and empty lists (everything is in the top-level). In this case, every item is reversed and stored, giving a total time complexity of $O(N + L)$.

- **makeStackTopAnInteger():** $O(\dfrac{L}{N})$ or $O(1)$.

        If the top of the stack is an integer, then this function does nothing; taking $O(1)$ time.

        Otherwise, it needs to process the stack until an integer is on top. The best way of analyzing the time complexity is to look at the total cost across all calls to `makeStackTopAnInteger()` and then divide by the number of calls made. Once the iterator is exhausted `makeStackTopAnInteger()` must have seen every integer at least once, costing $O(N)$ time. Additionally, it has seen every list (except the first) on the stack at least once also, so this costs $O(L)$ time. Adding these together, we get $O(N + L)$ time.

        The amortized time of a single `makeStackTopAnInteger` is the total cost, $O(N + L)$, divided by the number of times it's called. In order to get all integers, we need to have called it $N$ times. This gives us an amortized time complexity of $\dfrac{$\mathcal{O}(N + L)$}{N} =$\mathcal{O}(\dfrac{N}{N} + \dfrac{L}{N})$= O(\dfrac{L}{N})$.

- **next():** $O(\dfrac{L}{N})$ or $O(1)$.

        All of this method is $O(1)$, except for possibly the call to `makeStackTopAnInteger()`, giving us a time complexity the same as `makeStackTopAnInteger()`.

- **hasNext():** $O(\dfrac{L}{N})$ or $O(1)$.

        All of this method is $O(1)$, except for possibly the call to `makeStackTopAnInteger()`, giving us a time complexity the same as `makeStackTopAnInteger()`.

- Space complexity : $O(N + L)$.

    In the worst case, where the top list contains $N$ integers, or $L$ empty lists, it will cost $O(N + L)$ space. Other expensive cases occur when the nesting is very deep. However, it's useful to remember that $D ≤ L$ (because each layer of nesting requires another list), and so we don't need to take this into account.

<br/>

---

### Approach 3: Two Stacks

**Intuition**

Reversing the lists to put them onto the stack can be an expensive operation, and it turns out it isn't necessary.

Instead of pushing every item of a sub-list onto the stack, we can instead associate an index pointer with each sub-list, that keeps track of how far along that sub-list we are. Adding a new sub-list to the stack now becomes an $O(1)$ operation instead of a $O(length of sublist)$ one.

Here is an animation showing this approach.

![Slide 1](images/slideshow_341_flatten_tree_two_stacks_Slide1.PNG)

![Slide 2](images/slideshow_341_flatten_tree_two_stacks_Slide2.PNG)

![Slide 3](images/slideshow_341_flatten_tree_two_stacks_Slide3.PNG)

![Slide 4](images/slideshow_341_flatten_tree_two_stacks_Slide4.PNG)

![Slide 5](images/slideshow_341_flatten_tree_two_stacks_Slide5.PNG)

![Slide 6](images/slideshow_341_flatten_tree_two_stacks_Slide6.PNG)

![Slide 7](images/slideshow_341_flatten_tree_two_stacks_Slide7.PNG)

![Slide 8](images/slideshow_341_flatten_tree_two_stacks_Slide8.PNG)

![Slide 9](images/slideshow_341_flatten_tree_two_stacks_Slide9.PNG)

![Slide 10](images/slideshow_341_flatten_tree_two_stacks_Slide10.PNG)

![Slide 11](images/slideshow_341_flatten_tree_two_stacks_Slide11.PNG)

![Slide 12](images/slideshow_341_flatten_tree_two_stacks_Slide12.PNG)

![Slide 13](images/slideshow_341_flatten_tree_two_stacks_Slide13.PNG)

![Slide 14](images/slideshow_341_flatten_tree_two_stacks_Slide14.PNG)

![Slide 15](images/slideshow_341_flatten_tree_two_stacks_Slide15.PNG)

![Slide 16](images/slideshow_341_flatten_tree_two_stacks_Slide16.PNG)

![Slide 17](images/slideshow_341_flatten_tree_two_stacks_Slide17.PNG)

![Slide 18](images/slideshow_341_flatten_tree_two_stacks_Slide18.PNG)

![Slide 19](images/slideshow_341_flatten_tree_two_stacks_Slide19.PNG)

![Slide 20](images/slideshow_341_flatten_tree_two_stacks_Slide20.PNG)

![Slide 21](images/slideshow_341_flatten_tree_two_stacks_Slide21.PNG)

![Slide 22](images/slideshow_341_flatten_tree_two_stacks_Slide22.PNG)

![Slide 23](images/slideshow_341_flatten_tree_two_stacks_Slide23.PNG)

![Slide 24](images/slideshow_341_flatten_tree_two_stacks_Slide24.PNG)

![Slide 25](images/slideshow_341_flatten_tree_two_stacks_Slide25.PNG)

![Slide 26](images/slideshow_341_flatten_tree_two_stacks_Slide26.PNG)

![Slide 27](images/slideshow_341_flatten_tree_two_stacks_Slide27.PNG)

![Slide 28](images/slideshow_341_flatten_tree_two_stacks_Slide28.PNG)

![Slide 29](images/slideshow_341_flatten_tree_two_stacks_Slide29.PNG)

![Slide 30](images/slideshow_341_flatten_tree_two_stacks_Slide30.PNG)

![Slide 31](images/slideshow_341_flatten_tree_two_stacks_Slide31.PNG)

![Slide 32](images/slideshow_341_flatten_tree_two_stacks_Slide32.PNG)

![Slide 33](images/slideshow_341_flatten_tree_two_stacks_Slide33.PNG)

![Slide 34](images/slideshow_341_flatten_tree_two_stacks_Slide34.PNG)

![Slide 35](images/slideshow_341_flatten_tree_two_stacks_Slide35.PNG)

![Slide 36](images/slideshow_341_flatten_tree_two_stacks_Slide36.PNG)

![Slide 37](images/slideshow_341_flatten_tree_two_stacks_Slide37.PNG)

![Slide 38](images/slideshow_341_flatten_tree_two_stacks_Slide38.PNG)

![Slide 39](images/slideshow_341_flatten_tree_two_stacks_Slide39.PNG)

![Slide 40](images/slideshow_341_flatten_tree_two_stacks_Slide40.PNG)

![Slide 41](images/slideshow_341_flatten_tree_two_stacks_Slide41.PNG)

![Slide 42](images/slideshow_341_flatten_tree_two_stacks_Slide42.PNG)

![Slide 43](images/slideshow_341_flatten_tree_two_stacks_Slide43.PNG)

![Slide 44](images/slideshow_341_flatten_tree_two_stacks_Slide44.PNG)

![Slide 45](images/slideshow_341_flatten_tree_two_stacks_Slide45.PNG)

![Slide 46](images/slideshow_341_flatten_tree_two_stacks_Slide46.PNG)

![Slide 47](images/slideshow_341_flatten_tree_two_stacks_Slide47.PNG)

![Slide 48](images/slideshow_341_flatten_tree_two_stacks_Slide48.PNG)

![Slide 49](images/slideshow_341_flatten_tree_two_stacks_Slide49.PNG)

![Slide 50](images/slideshow_341_flatten_tree_two_stacks_Slide50.PNG)

![Slide 51](images/slideshow_341_flatten_tree_two_stacks_Slide51.PNG)

![Slide 52](images/slideshow_341_flatten_tree_two_stacks_Slide52.PNG)

![Slide 53](images/slideshow_341_flatten_tree_two_stacks_Slide53.PNG)

![Slide 54](images/slideshow_341_flatten_tree_two_stacks_Slide54.PNG)

![Slide 55](images/slideshow_341_flatten_tree_two_stacks_Slide55.PNG)

![Slide 56](images/slideshow_341_flatten_tree_two_stacks_Slide56.PNG)

![Slide 57](images/slideshow_341_flatten_tree_two_stacks_Slide57.PNG)

![Slide 58](images/slideshow_341_flatten_tree_two_stacks_Slide58.PNG)

![Slide 59](images/slideshow_341_flatten_tree_two_stacks_Slide59.PNG)

![Slide 60](images/slideshow_341_flatten_tree_two_stacks_Slide60.PNG)

![Slide 61](images/slideshow_341_flatten_tree_two_stacks_Slide61.PNG)

![Slide 62](images/slideshow_341_flatten_tree_two_stacks_Slide62.PNG)

![Slide 63](images/slideshow_341_flatten_tree_two_stacks_Slide63.PNG)

![Slide 64](images/slideshow_341_flatten_tree_two_stacks_Slide64.PNG)

![Slide 65](images/slideshow_341_flatten_tree_two_stacks_Slide65.PNG)

![Slide 66](images/slideshow_341_flatten_tree_two_stacks_Slide66.PNG)

![Slide 67](images/slideshow_341_flatten_tree_two_stacks_Slide67.PNG)

![Slide 68](images/slideshow_341_flatten_tree_two_stacks_Slide68.PNG)

![Slide 69](images/slideshow_341_flatten_tree_two_stacks_Slide69.PNG)

![Slide 70](images/slideshow_341_flatten_tree_two_stacks_Slide70.PNG)

![Slide 71](images/slideshow_341_flatten_tree_two_stacks_Slide71.PNG)

![Slide 72](images/slideshow_341_flatten_tree_two_stacks_Slide72.PNG)

![Slide 73](images/slideshow_341_flatten_tree_two_stacks_Slide73.PNG)

![Slide 74](images/slideshow_341_flatten_tree_two_stacks_Slide74.PNG)

![Slide 75](images/slideshow_341_flatten_tree_two_stacks_Slide75.PNG)

![Slide 76](images/slideshow_341_flatten_tree_two_stacks_Slide76.PNG)

![Slide 77](images/slideshow_341_flatten_tree_two_stacks_Slide77.PNG)

![Slide 78](images/slideshow_341_flatten_tree_two_stacks_Slide78.PNG)

![Slide 79](images/slideshow_341_flatten_tree_two_stacks_Slide79.PNG)

![Slide 80](images/slideshow_341_flatten_tree_two_stacks_Slide80.PNG)

![Slide 81](images/slideshow_341_flatten_tree_two_stacks_Slide81.PNG)

![Slide 82](images/slideshow_341_flatten_tree_two_stacks_Slide82.PNG)

![Slide 83](images/slideshow_341_flatten_tree_two_stacks_Slide83.PNG)

![Slide 84](images/slideshow_341_flatten_tree_two_stacks_Slide84.PNG)

![Slide 85](images/slideshow_341_flatten_tree_two_stacks_Slide85.PNG)

![Slide 86](images/slideshow_341_flatten_tree_two_stacks_Slide86.PNG)

![Slide 87](images/slideshow_341_flatten_tree_two_stacks_Slide87.PNG)

![Slide 88](images/slideshow_341_flatten_tree_two_stacks_Slide88.PNG)

The *total* time complexity across all method calls for using up the entire iterator remains the same, *but* work is only done when it's necessary, thus improving performance when we only use part of the iterator. This is a desirable property for an iterator.

**Algorithm**

This approach can be implemented as either one stack of pairs/ tuples, or two stacks with one for `NestedInteger`s and the other for indexes. The best decision for this is language-dependent. I tried both for the Java and found that attempting to put `Pair` objects onto a single stack doesn't work well because updating an index count requires popping and then reconstructing the entire `Pair` due to immutability (alternatives such as using length-2 `Lists`s as pairs are possible, but I don't think ideal). Using two stacks is cleaner.

```python
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]

    def make_stack_top_an_integer(self):

        while self.stack:

            # Essential for readability :)
            current_list = self.stack[-1][0]
            current_index = self.stack[-1][1]

            # If the top list is used up, pop it and its index.
            if len(current_list) == current_index:
                self.stack.pop()
                continue

            # Otherwise, if it's already an integer, we don't need
            # to do anything.
            if current_list[current_index].isInteger():
                break

            # Otherwise, it must be a list. We need to increment the index
            # on the previous list, and add the new list.
            new_list = current_list[current_index].getList()
            self.stack[-1][1] += 1 # Increment old.
            self.stack.append([new_list, 0])

    def next(self) -> int:
        self.make_stack_top_an_integer()
        current_list = self.stack[-1][0]
        current_index = self.stack[-1][1]
        self.stack[-1][1] += 1
        return current_list[current_index].getInteger()

    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0
```

**Complexity Analysis**

Let $N$ be the total number of *integers* within the nested list, $L$ be the total number of *lists* within the nested list, and $D$ be the maximum nesting depth (maximum number of lists inside each other).

- Time complexity:

- **Constructor:** $O(1)$.

        Pushing a list onto a `stack` is *by reference* in all the programming languages we're using here. This means that instead of creating a new list, some information about how to get to the existing list is put onto the stack. The list is not traversed, as it doesn't need reversing this time, and we're not pushing the items on one-by-one. This is, therefore, an $O(1)$ operation.

- **makeStackTopAnInteger() / next() / hasNext():** $O(\dfrac{L}{N})$ or $O(1)$.

        Same as Approach 2.

- Space complexity : $O(D)$.

    At any given time, the stack contains only *one* nestedList reference for each level. This is unlike the previous approach, wherein the worst case we need to put almost all elements onto the stack.

    Because there's one reference on the stack at each level, the worst case is when we're looking at the deepest leveled list, giving a space complexity is $O(D)$.

<br/>

---

### Approach 4: Stack of Iterators

**Intuition**

*This approach works best in Java but isn't well suited to other languages. Have a look at Approach 5 if you're looking for an elegant Python and JavaScript approach.*

If you're using Java, a very elegant approach is to maintain a stack of `ListIterators`. This approach is closely based on Approach 3.

Instead of keeping a `Stack` of indexes to keep track of where we are in each `List`, we can simply make each `List` a `ListIterator`, thus keeping a `Stack` of `ListIterator`s. Then, we can use the `next()` and `hasNext()` methods on those `ListIterators`. Internally, the `ListIterator` is storing the index.

A downside to this approach is that for `hasNext()` to work correctly, it needs to know whether or not there are any *integers* remaining (empty lists don't count!). The only way it can do this is to remove items from the `ListIterator` and check whether or not they are an integer. It cannot, however, put the integers back again. Therefore, if it removes an integer it will need to put it into a `peeked` field so that the `next()` function can return that integer. This is the same as in the [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) problem.

A clean design is to have a `setPeeked()` method that is analogous to the `makeStackTopAnInteger()` method. This method should firstly check if `peeked` is empty, and if it is empty, then find the next integer to put in it. This integer is *removed* from the stack (as explained above).

Regardless of the need for `peeked`, this is probably the best design if you're coding in Java.

**Algorithm**

```java
import java.util.NoSuchElementException;

public class NestedIterator implements Iterator<Integer> {

    // This time, our stack will hold list iterators instead of just lists.
    private Deque<ListIterator<NestedInteger>> stackOfIterators = new ArrayDeque();
    private Integer peeked = null;

    public NestedIterator(List<NestedInteger> nestedList) {
        // Make an iterator with the input and put it on the stack.
        // Note that creating a list iterator is an O(1) operation.
        stackOfIterators.addFirst(nestedList.listIterator());
    }

    private void setPeeked() {

        // If peeked is already set, there's nothing to do.
        if (peeked != null) return;

        while (!stackOfIterators.isEmpty()) {

            // If the iterator at the top of the stack doesn't have a next,
            // remove that iterator and continue on.
            if (!stackOfIterators.peekFirst().hasNext()) {
                stackOfIterators.removeFirst();
                continue;
            }

            // Otherwise, we need to check whether that next is a list or
            // an integer.
            NestedInteger next = stackOfIterators.peekFirst().next();

            // If it's an integer, set peeked to it and return as we're done.
            if (next.isInteger()) {
                peeked = next.getInteger();
                return;
            }

            // Otherwise, it's a list. Create a new iterator with it, and put
            // the new iterator on the top of the stack.
            stackOfIterators.addFirst(next.getList().listIterator());
        }
    }

    @Override
    public Integer next() {

        // As per Java specs, throw an exception if there are no further elements.
        if (!hasNext()) throw new NoSuchElementException();

        // hasNext() called setPeeked(), which ensures peeked has the next integer
        // in it. We need to clear the peeked field so that the element is returned
        // again.
        Integer result = peeked;
        peeked = null;
        return result;
    }

    @Override
    public boolean hasNext() {

        // Try to set the peeked field. If any integers are remaining, it will
        // contain the next one to be returned after this call.
        setPeeked();

        // There are elements remaining iff peeked contains a value.
        return peeked != null;
    }
}
```

**Complexity Analysis**

Let $N$ be the total number of *integers* within the nested list, $L$ be the total number of *lists* within the nested list, and $D$ be the maximum nesting depth (maximum number of lists inside each other).

- Time complexity:

- **Constructor:** $O(1)$.

        Same as Approach 3.

- **makeStackTopAnInteger() / next() / hasNext():** $O(\dfrac{L}{N})$ or $O(1)$.

        Same as Approach 3.

- Space complexity : $O(D)$.

    Same as Approach 3.

In practice, this code runs faster than Approach 3, probably because most of the functionality relies on `ListIterator`; an optimized API class. Approach 3 was really just our own implementation of `ListIterator`s.

<br/>

---

### Approach 5: Using a Generator

**Intuition**

*This approach will only work in programming languages that support **generator functions**, for example, **Python**, **JavaScript** and **C#**. At the time of writing this article, **C++** doesn't support it, but it is expected to support them soon.*

In a nutshell, generator functions are a special type of function that can "return" multiple values. When you call a **generator function**, you get back a special object called a **generator**. This **generator** can then be used to get each value from the function, one at a time.

To "return" multiple values from these **generator functions**, a special keyword, `yield`, is used. `yield` behaves similarly to a `return` statement, except that it does not terminate the function. Instead, it pauses the function, and "returns" the `yield`ed value. Then, when we need another value, the function resumes from where it left off. It continues until it gets to another `yield`, just like before. When the function gets to the end (no more code left to run), it stops.

For example in Python, if we have a **generator** `gen`, we can tell it to resume the function and get the next value by calling `next(gen)`.

As an example, the **generators** created by this Python **generator function** can be used to get all numbers from `a` to `b`:

```python
# This is effectively how range works in Python. We're implementing our own
# version of it here to see how generators work.
# Many Python 3 library functions are generators.
def range_generator(a, b):
    current = a
    while current < b:
        # This yield "returns" a value from the function and pauses it
        yield current
        # Once the function is "woken up" by another call to next(...), it will resume
        # by continuing with the next statement (current += 1), until it either
        # hits another yield or reaches the end of the function
        current += 1
    # When we get here, the generator is finished.

# Create a new range_generator object for the numbers 10 to 20.
ten_to_twenty_generator = range_generator(10, 20)

# Get the first 3 values out of the range_generator object we made.
print(next(ten_to_twenty_generator)) # 10
print(next(ten_to_twenty_generator)) # 11
print(next(ten_to_twenty_generator)) # 12

# Here's another example of using the generator with a loop. As we said, it's
# the same as the range function.
# This is a new generator object, not the 10-20 one from above.
for number in range_generator(5, 9):
    print(number)
print("Done!")
# Will print
# 5
# 6
# 7
# 8
# Done
```

End-of-function behaviour for **generators** is language-dependent. For example, in Python, once the end of the function is reached, a `StopIteration` exception is raised. When you use your generator in a loop, e.g. $for number in \text{range}_{generator}(5, 9):$, it will simply stop when it gets this exception. The programmer doesn't need to explicitly handle it.

Now that we know what a **generator** is, we'll use one to implement a `NestedIterator`.

Back in Approach 1, we started by flattening the entire list with the following recursive algorithm:

```python
integers = []
def flatten_list(nested_list):
    for nested_integer in nested_list:
        if nested_integer.isInteger():
            integers.append(nested_integer.getInteger())
        else:
            flatten_list(nested_integer.getList())
```

Something cool about **generator functions** is that they can be recursive.

So, instead of pushing each integer to a list, we could just `yield` them. This way, when we want the next integer, the function will resume from after the `yield` until it finds the next one.

Let's replace the list append with `yield`.

```python
def flatten_list(nested_list):
    for nested_integer in nested_list:
        if nested_integer.isInteger():
            yield nested_integer.getInteger()
        else:
            flatten_list(nested_integer.getList())
```

This has a mistake though; because $\text{flatten}_{list}$ is now a generator function, the recursive call to $\text{flatten}_{list}$ only *creates a new generator*; it doesn't actually `yield` the values from the nested generator.

To fix this, we can loop over each item of the recursive generator and `yield` them instead.

```python
def flatten_list(nested_list):
    for nested_integer in nested_list:
        if nested_integer.isInteger():
            yield nested_integer.getInteger()
        else:
            for integer in flatten_list(nested_integer.getList()):
                yield integer
```

Some languages, such as Python, offer a shorthand for this looping, in Python called `yield from`. Here is its usage.

```python
def flatten_list(nested_list):
    for nested_integer in nested_list:
        if nested_integer.isInteger():
            yield nested_integer.getInteger()
        else:
            yield from flatten_list(nested_integer.getList())
```

Note that, not all languages that support `yield` also support `yield from`. For example, **C#** has `yield`, but no `yield from` equivalent. JavaScript supports it, but instead calls it `yield*`.

**Algorithm**

For this approach, we also need to add a `peeked` field, much like in the [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) problem. This is because the only way to know if there *is* a next value is to take it out of the generator, and generators can only go forwards, not backward.

```python
class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        # Get a generator object from the generator function, passing in
        # nestedList as the parameter.
        self._generator = self._int_generator(nestedList)
        # All values are placed here before being returned.
        self._peeked = None

    # This is the generator function. It can be used to create generator
    # objects.
    def _int_generator(self, nested_list) -> "Generator[int]":
        # This code is the same as Approach 1. It's a recursive DFS.
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                # We always use "yield from" on recursive generator calls.
                yield from self._int_generator(nested.getList())
        # Will automatically raise a StopIteration.

    def next(self) -> int:
        # Check there are integers left, and if so, then this will
        # also put one into self._peeked.
        if not self.hasNext(): return None
        # Return the value of self._peeked, also clearing it.
        next_integer, self._peeked = self._peeked, None
        return next_integer

    def hasNext(self) -> bool:
        if self._peeked is not None: return True
        try: # Get another integer out of the generator.
            self._peeked = next(self._generator)
            return True
        except: # The generator is finished so raised StopIteration.
            return False
```

**Complexity Analysis**

Let $N$ be the total number of *integers* within the nested list, $L$ be the total number of *lists* within the nested list, and $D$ be the maximum nesting depth (maximum number of lists inside each other).

- Time complexity:

- **Constructor:** $O(1)$.

        In the constructor, we only create a generator object. Simply creating a generator object doesn't invoke any code in the generator function itself (only calls to next do).

        Because the time taken to create the generator doesn't vary with the size of the input, the time complexity is $O(1)$.

- **next() / hasNext():** $O(\dfrac{L}{N})$ or $O(1)$.

        Same as approaches 2, 3, and 4.

- Space complexity : $O(D)$.

    We recursively call `_int_generator` within itself for nested lists. Therefore, the runtime stack uses memory proportional to the current depth of the list. Seeing as the largest depth is $D$, the space complexity is $O(D)$.

<br/>