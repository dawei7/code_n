[TOC]

## Solution

---

### Approach: Simulation

#### Intuition

To calculate the greatest common divisor (GCD) of every pair of adjacent nodes in a linked list, we maintain two pointers, `node1` and `node2`, initially pointing to the first and second nodes, respectively.

As we iterate through the list, we need to compute the GCD of the values stored in `node1` and `node2`. The most efficient method for finding the GCD of two numbers is the renowned [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm). This algorithm is based on the principle that the GCD of two numbers also divides their difference.

In simple terms, the Euclidean algorithm works by repeatedly replacing the larger number by the remainder of the division of the larger number by the smaller number, until one of the numbers becomes zero. The non-zero number at this stage is the GCD of the original pair of numbers.

> Many programming languages offer built-in implementations of this algorithm, which you can utilize in your solution. For instance, Python has a built-in `math.gcd()` function, while C++ provides the `std::gcd()` function in the `<numeric>` header. If such a function is not available in your programming language, or if you prefer to implement it manually, you can write a custom GCD method using the following pseudo-code:

Recursive Way:
```
function gcd(a, b)
  if b = 0
    return a
  else
    return gcd(b, a mod b)
```

Iterative Way:
```
function gcd(a, b)
  while b ≠ 0
    t := b
    b := a mod b
    a := t
  return a
```

After computing the GCD, we create a new node with the GCD value and insert it between `node1` and `node2` as follows:
1. Set `node1`'s next pointer to the new node.
2. Set the new node's next pointer to `node2`.
3. Disconnect the direct link between `node1` and `node2`.

Next, we move `node1` and `node2` to the next pair of nodes and continue the process.

The below slideshow demonstrates the algorithm in action:

![Slide 1](images/slideshow_slideshow_slide1.png)

![Slide 2](images/slideshow_slideshow_slide2.png)

![Slide 3](images/slideshow_slideshow_slide3.png)

![Slide 4](images/slideshow_slideshow_slide4.png)

![Slide 5](images/slideshow_slideshow_slide5.png)

![Slide 6](images/slideshow_slideshow_slide6.png)

![Slide 7](images/slideshow_slideshow_slide7.png)

![Slide 8](images/slideshow_slideshow_slide8.png)

#### Algorithm

Main method `insertGreatestCommonDivisors`:

- If the list contains only one node (`head.next` is `null`), return the `head` as no insertion is needed.
- Initialize `ListNode` variables `node1` and `node2` to `head` and `head.next` respectively, to traverse the linked list.
- While `node2` is not `null`:
  - Calculate the GCD's of the values in `node1` and `node2`.
  - Create a new `ListNode` `gcdNode` with the calculated GCD value.
  - Update `node1.next` to `gcdNode`.
  - Update `gcdNode.next` to `node2`.
  - Set `node1` to `node2` and `node2` to `node2.next`, respectively. This essentially moves `node1` and `node2` to the next pair of nodes in the list.
- Return the modified `head` of the list as our answer.

Helper method `calculateGCD(a, b)`:

- While `b` is greater than `0`:
  - Set a variable `temp` to `b`.
  - Set `b` to `a%b` and `a` to `temp`, respectively.
- Return `a`.

> Note: We have used a custom method to calculate the GCD for completeness. In an interview, clarify with your interviewer if built-in GCD methods are acceptable.

#### Implementation

```python
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Helper method to calculate the greatest common divisor using the Euclidean algorithm
        def _calculate_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        # If the list contains only one node, return the head as no insertion is needed
        if not head.next:
            return head

        # Initialize pointers to traverse the list
        node1 = head
        node2 = head.next

        # Traverse the linked list
        while node2:
            gcd_value = _calculate_gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)

            # Insert the GCD node between node1 and node2
            node1.next = gcd_node
            gcd_node.next = node2

            # Move to the next pair of nodes
            node1 = node2
            node2 = node2.next

        return head
```

#### Complexity Analysis

Let $n$ be the number of nodes in the linked list.

- Time complexity: $O(n \cdot \log(\min(a,b)))$

    The algorithm traverses the list, visiting each node exactly once. This takes linear time.

    The GCD is calculated using the Euclidean algorithm, which has a time complexity of $O(\log(\min(a, b)))$, where $a$ and $b$ are numbers whose GCD is being calculated.

    Thus, the overall time complexity of the algorithm is $O(n \cdot \log(\min(a,b)))$.

- Space complexity: $O(1)$

    The iterative implementation of the GCD method has a space complexity of $O(1)$.

---