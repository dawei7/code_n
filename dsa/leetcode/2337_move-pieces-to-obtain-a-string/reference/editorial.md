[TOC]

## Solution

---

### Overview

We are given two strings, `start` and `target`, both of the same length $n$. These strings consist only of the characters `'L'`, `'R'`, and `'_'`.

Let's look at an example with a `start` string of $"R_{L}"$ and a `target` string of $"L_{R}"$. To achieve this transformation, `'L'` would need to move leftward and `'R'` would need to move rightward, but neither can "jump over" the other due to the step-by-step movement rules that only allow moves into adjacent blank spaces. This restriction inherently prevents characters from crossing each other, making the transformation impossible. Therefore, we return `false`.

---

### Approach 1: Brute Force (Memory Limit Exceeded)

#### Intuition

A natural first thought to solve this problem is to explore all possible ways to move the pieces. We generate all possible states of the `start` string by making valid moves and checking if any of these states match the `target` string.

To implement this logic, we start by initializing a queue to store the current states (`stateQueue`) of the `start` string. To avoid repetitive lookups for the same state, we use a set to keep track of visited states (`visitedStates`).

Once we have the `visitedStates` and `stateQueue` ready, we begin by pushing the initial `start` string into the queue. For each state, we check if it matches the `target` string. If it does, we return `true` because we have found a valid transformation sequence. If the current state does not match the `target`, we generate new states by moving `'L'` to the left and `'R'` to the right, ensuring that each move is valid according to the rules. We then push each new valid state into the queue and mark it as visited. If the queue is exhausted and we haven't found a matching state, we return `false` because no valid transformation sequence exists.

Due to the worst-case scenario where all possible states (which can be up to $n^2$ unique states) need to be stored in the visited states set, this solution results in a memory limit exceeded error.

<details>
<summary>Explanation of the Total Number of Unique States (Click Here)</summary>
The total number of unique states depends on the number of blank spaces available, as more blank spaces allow for more possible movements. Consider a string of length $n$ with $n-2$ blank spaces, represented as: <code>_…_L_…_R_…_</code>.

- The character <code>'L'</code> can move to any position <code>i</code> with $0 \leq i < n - 1$.
- For each position of <code>'L'</code>, the character <code>'R'</code> can move to $n - 1 - i$ positions (any position to the right of <code>'L'</code>).

This gives the total number of states as:

$$
\begin{aligned}
 (n - 1) + (n - 2) + (n - 3) + \ldots + (n - (n - 1)) = $\mathcal{O}(n^2)$
\end{aligned}
$$
</details>

#### Algorithm

- Initialize an unordered set `visitedStates` to track states that have already been visited and avoid cycles.
- Initialize a queue `stateQueue` and push the `start` state into the queue.

- While `stateQueue` is not empty:
  - Extract the front of the queue into `currentState`.
  - If `currentState` matches `target`, return `true`.

  - For each position in `currentState` from index `1` to the end:
- If $\text{currentState}[position]$ is `'L'` and the position to its left is `'_'`:
      - Swap `'L'` with `'_'` to simulate moving `'L'` left.
      - If the new state has not been visited:
- Push the new state into the queue.
- Mark the state as visited by inserting it into `visitedStates`.
      - Restore `currentState` to its original form by swapping back.
- If $currentState[position - 1]$ is `'R'` and the position to its right is `'_'`:
      - Swap `'R'` with `'_'` to simulate moving `'R'` right.
      - If the new state has not been visited:
- Push the new state into the queue.
- Mark the state as visited by inserting it into `visitedStates`.
      - Restore `currentState` to its original form by swapping back.

- If the process completes without finding a valid transformation sequence, return `false`.

#### Implementation

```python
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # To keep track of visited states to avoid cycles
        visited_states = set()

        # Queue for current state
        state_queue = []
        # Start with the initial state
        state_queue.append(start)

        while state_queue:
            current_state = state_queue.pop(0)

            # If we reach the target state, return true
            if current_state == target:
                return True

            for position in range(1, len(current_state)):
                # Try moving 'L' to the left
                if (
                    current_state[position] == "L"
                    and current_state[position - 1] == "_"
                ):
                    current_state = list(current_state)
                    current_state[position], current_state[position - 1] = (
                        current_state[position - 1],
                        current_state[position],
                    )
                    current_state = "".join(current_state)
                    if current_state not in visited_states:
                        # Add the new state to the queue
                        state_queue.append(current_state)
                        # Mark the new state as visited
                        visited_states.add(current_state)
                    # Restore the state
                    current_state = list(current_state)
                    current_state[position], current_state[position - 1] = (
                        current_state[position - 1],
                        current_state[position],
                    )
                    current_state = "".join(current_state)

                # Try moving 'R' to the right
                if (
                    position < len(current_state) - 1
                    and current_state[position] == "R"
                    and current_state[position + 1] == "_"
                ):
                    current_state = list(current_state)
                    current_state[position], current_state[position + 1] = (
                        current_state[position + 1],
                        current_state[position],
                    )
                    current_state = "".join(current_state)
                    if current_state not in visited_states:
                        # Add the new state to the queue
                        state_queue.append(current_state)
                        # Mark the new state as visited
                        visited_states.add(current_state)
                    # Restore the state
                    current_state = list(current_state)
                    current_state[position], current_state[position + 1] = (
                        current_state[position + 1],
                        current_state[position],
                    )
                    current_state = "".join(current_state)

        # If no valid transformation sequence is found, return false
        return False
```

#### Complexity Analysis

Let $n$ be the size of the `start` and `target` strings.

- Time complexity: $O(n^2)$

    The algorithm explores all possible states. In the worst case, each character in the string can be swapped with its adjacent character, leading to $n$ possible swaps per state. Since each state can generate up to $n$ new states, and the algorithm explores all possible states, the time complexity is $O(n^2)$.

- Space complexity: $O(n^2)$

    The space complexity is dominated by the space required to store the states in the `visitedStates` set and the `stateQueue`. In the worst case, all possible states (which can be up to $n^2$ unique states) need to be stored in the `visitedStates` set. The `stateQueue` can also grow to store up to $n$ states at any given time during the traversal.

    Therefore, the space complexity is $O(n^2)$.

---

### Approach 2: Using Queue

#### Intuition

Instead of generating all possible moves, we can focus on the fundamental rules that govern whether a transformation is possible. The `'L'` pieces can only move left, and the `'R'` pieces can only move right. This means that for any valid transformation:

1. The relative order of `'L'`s and `'R'`s must remain unchanged since they cannot pass through each other.
2. An `'L'` in the `start` string must be at the same position or to the right of its target position.
3. An `'R'` in the `start` string must be at the same position or to the left of its target position.

This observation allows us to drastically simplify our approach. Rather than trying different combinations of moves, we can simply extract the positions of all `'L'` and `'R'` pieces from both strings and compare them in order. By storing these positions in queues (one for the `start` string and one for the `target` string), we maintain the relative ordering of pieces while ignoring the underscores.

The actual implementation becomes a matter of comparing corresponding pieces from both queues. For each pair of pieces:

1. First, verify they are the same type (both `'L'` or both `'R'`).
2. Then, depending on the piece type, check if their positions satisfy our movement constraints:
   - `'L'` pieces in the `start` must not be to the left of their target positions.
   - `'R'` pieces must not be to the right of their target positions.

To implement this concept, start by creating two queues to store character-position pairs. Next, populate these queues by iterating through both the `start` and `target` strings, recording only the non-underscore characters along with their positions. Once the queues are populated, compare their sizes to ensure they match, as this confirms that both strings contain the same number of pieces. Then, process both queues simultaneously, comparing each pair of front characters to verify that they are of the same type (both `'L'` or both `'R'`) and that their positions allow for valid moves according to the rules. Specifically, for `'L'` pieces, ensure that the start position is not to the left of the target position, and for `'R'` pieces, ensure that the start position is not to the right of the target position.

This way we transform what would be a quadratic-complexity problem of move generation into a linear-time solution that simply validates position constraints.

#### Algorithm

- Initialize two queues, `startQueue` and `targetQueue`, to store the non-underscore characters and their indices from `start` and `target`.

- Traverse the `start` and `target` strings:
  - If a character in `start` is not an underscore (`'_'`), add it along with its index to `startQueue`.
  - If a character in `target` is not an underscore, add it along with its index to `targetQueue`.

- Check if the sizes of `startQueue` and `targetQueue` are different:
  - If they are, return `false` because the number of movable pieces must match.

- While `startQueue` is not empty:
  - Dequeue the front element from both `startQueue` and `targetQueue`.
  - Compare the character and movement rules:
- If the characters don't match, return `false`.
- If the character is `'L'` (must only move left), check if its index in `start` is less than its index in `target`. If so, return `false`.
- If the character is `'R'` (must only move right), check if its index in `start` is greater than its index in `target`. If so, return `false`.

- Return `true` if all characters and their movement rules are valid, indicating that `start` can be transformed into `target`.

#### Implementation

```python
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Queue to store characters and indices from both strings
        start_queue = []
        target_queue = []

        # Record non-underscore characters and their indices
        for i in range(len(start)):
            if start[i] != "_":
                start_queue.append((start[i], i))
            if target[i] != "_":
                target_queue.append((target[i], i))

        # If number of pieces don't match, return false
        if len(start_queue) != len(target_queue):
            return False

        # Compare each piece's type and position
        while not len(start_queue) == 0:
            start_char, start_index = start_queue.pop(0)
            target_char, target_index = target_queue.pop(0)

            # Check character match and movement rules
            if (
                start_char != target_char
                or (start_char == "L" and start_index < target_index)
                or (start_char == "R" and start_index > target_index)
            ):
                return False

        return True
```

#### Complexity Analysis

Let $n$ be the size of the `start` and `target` strings.

- Time complexity: $O(n)$

    The algorithm iterates through both strings once, which takes $O(n)$ time. Pushing elements into the queues and popping elements from the queues also take $O(n)$ time in total. Therefore, the overall time complexity is $O(n)$.

- Space complexity: $O(n)$

    The space complexity is determined by the space used by the two queues. In the worst case, if all characters in the strings are non-underscore, both queues will store $n$ elements each. Thus, the space complexity is $O(n)$.

---

### Approach 3: Two pointer

#### Intuition

Instead of using additional data structures like queues or generating possible states, we can directly compare both strings by scanning them simultaneously using two pointers. These pointers will help us compare the corresponding `'L'` and `'R'` pieces. When we encounter underscores, we can simply skip over them because they don't affect the validity of the transformation.

What really matters is the relative positions of the `'L'` and `'R'` pieces and whether they can move to their target positions according to the movement rules. Each time we find an `'L'` or `'R'` in both strings (after skipping underscores), we can immediately check if the movement is possible based on their positions:

- `'L'` pieces can only move left, so their position in the `start` string must be greater than or equal to their position in the `target` string.
- `'R'` pieces can only move right, so their position in the `start` string must be less than or equal to their position in the `target` string.

To implement this, we use two pointers, `startIndex` and `targetIndex`, to traverse the `start` and `target` strings respectively. By making a single pass through the strings, we validate two key aspects:

1. Character Matching: Ensure that the sequence of `'L'` and `'R'` pieces is identical in both strings.
2. Position Constraints: Check that `'L'` pieces don't need to move right and `'R'` pieces don't need to move left.

By checking these conditions as we go, we can achieve the same validation as a more complex queue-based approach, but with constant space complexity and cleaner code.

The algorithm is visualized below:

![Slide 1](images/slideshow_2337_two_pointer_slide1.png)

![Slide 2](images/slideshow_2337_two_pointer_slide2.png)

![Slide 3](images/slideshow_2337_two_pointer_slide3.png)

![Slide 4](images/slideshow_2337_two_pointer_slide4.png)

![Slide 5](images/slideshow_2337_two_pointer_slide5.png)

![Slide 6](images/slideshow_2337_two_pointer_slide6.png)

![Slide 7](images/slideshow_2337_two_pointer_slide7.png)

![Slide 8](images/slideshow_2337_two_pointer_slide8.png)

![Slide 9](images/slideshow_2337_two_pointer_slide9.png)

![Slide 10](images/slideshow_2337_two_pointer_slide10.png)

![Slide 11](images/slideshow_2337_two_pointer_slide11.png)

![Slide 12](images/slideshow_2337_two_pointer_slide12.png)

![Slide 13](images/slideshow_2337_two_pointer_slide13.png)

![Slide 14](images/slideshow_2337_two_pointer_slide14.png)

![Slide 15](images/slideshow_2337_two_pointer_slide15.png)

![Slide 16](images/slideshow_2337_two_pointer_slide16.png)

![Slide 17](images/slideshow_2337_two_pointer_slide17.png)

![Slide 18](images/slideshow_2337_two_pointer_slide18.png)

![Slide 19](images/slideshow_2337_two_pointer_slide19.png)

![Slide 20](images/slideshow_2337_two_pointer_slide20.png)

![Slide 21](images/slideshow_2337_two_pointer_slide21.png)

![Slide 22](images/slideshow_2337_two_pointer_slide22.png)

![Slide 23](images/slideshow_2337_two_pointer_slide23.png)

![Slide 24](images/slideshow_2337_two_pointer_slide24.png)

> For a more comprehensive understanding of the two-pointer technique, check out the [Two Pointer Explore Card 🔗](https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/). This resource provides an in-depth look at the two-pointer approach, explaining its key concepts and applications with a variety of problems to solidify understanding of the pattern.

#### Algorithm

- Initialize `startLength` as the length of the `start` string.
- Initialize two pointers, `startIndex` and `targetIndex`, both set to `0`, to traverse the `start` and `target` strings.

- While either `startIndex` or `targetIndex` is less than `startLength`:
  - Skip underscores in the `start` string by incrementing `startIndex` until a non-underscore character is found or the end of the string is reached.
  - Skip underscores in the `target` string by incrementing `targetIndex` until a non-underscore character is found or the end of the string is reached.
  - If one string is fully traversed and the other is not, return `false` as both strings should be exhausted simultaneously.
  - If the characters at $\text{start}[startIndex]$ and $\text{target}[targetIndex]$ do not match, return `false` as the transformations are invalid.
  - If the character is `'L'` in `start`, ensure $startIndex \ge targetIndex$ (left pieces can only move left); otherwise, return `false`.
  - If the character is `'R'` in `start`, ensure $startIndex \le targetIndex$ (right pieces can only move right); otherwise, return `false`.

- Increment both `startIndex` and `targetIndex` to move to the next characters.

- If the loop ends without returning `false`,  all conditions for a valid transformation are satisfied; return `true`.

#### Implementation

```python
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_length = len(start)
        # pointers for start string and target string
        start_index, target_index = (0, 0)

        while start_index < start_length or target_index < start_length:
            # skip underscores in start
            while start_index < start_length and start[start_index] == "_":
                start_index += 1

            # skip underscores in target
            while target_index < start_length and target[target_index] == "_":
                target_index += 1

            # if one string exhausted, both strings should be exhausted
            if start_index == start_length or target_index == start_length:
                return (
                    start_index == start_length and target_index == start_length
                )

            # check if the pieces match and follow movement rules
            if (
                start[start_index] != target[target_index]
                or (start[start_index] == "L" and start_index < target_index)
                or (start[start_index] == "R" and start_index > target_index)
            ):
                return False

            start_index += 1
            target_index += 1

        # if all conditions satisfied, return true
        return True
```

#### Complexity Analysis

Let $n$ be the size of the `start` and `target` strings.

- Time complexity: $O(n)$

    The algorithm iterates through both strings once, skipping underscores and comparing characters. Each character is processed at most once, resulting in a linear time complexity.

- The inner `while` loops that skip underscores run in constant time for each character, so they do not increase the overall time complexity.
- The main `while` loop runs until both indices reach the end of the strings, which takes $O(n)$ time in the worst case.

- Space complexity: $O(1)$

    The space complexity is constant because the algorithm uses a fixed amount of extra space regardless of the input size.

- The only additional space used is for the indices `startIndex` and `targetIndex`, which are single integer variables.
- No additional data structures are used that grow with the input size.

---