# Fibonacci Search

| | |
|---|---|
| **ID** | `search_09` |
| **Category** | searching |
| **Complexity (required)** | $O(\log N)$ Time, $O(1)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 1/10 |
| **Wikipedia** | [Fibonacci search technique](https://en.wikipedia.org/wiki/Fibonacci_search_technique) |

## Problem statement

Given a sorted array `arr` and a `target` value.
Find the index of the `target` in the array. If the `target` is not present, return `-1`.
Optimize the search for environments where **division operators** (`/` or `//`) and **bitwise shifts** (`>>`) are not supported or are incredibly expensive, and you can ONLY use addition and subtraction.

**Input:** A sorted array `arr` and a `target` value.
**Output:** An integer representing the index.

## When to use it

- Purely a hardware/systems-level optimization technique.
- Used on extremely old microprocessors or specialized embedded systems (like ASICs) where division logic gates do not physically exist on the silicon chip.
- Also optimizes CPU cache performance because the array is split into unequal chunks (~= 61\% and 39\%), which occasionally aligns better with physical memory pages than exactly 50\%.

## Approach

**1. The Division Problem:**
Binary Search uses `mid = (left + right) / 2`.
This requires division. How can we split an array without division?

**2. The Fibonacci Sequence:**
Recall the sequence: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34...`
A fundamental property of the sequence is F_k = F_{k-1} + F_{k-2}.
If an array has length 13, we can mathematically split it perfectly into two chunks of length 8 and 5!
If we eliminate the chunk of size 5, we are left with an array of size 8. But 8 is also a Fibonacci number! We can split it again into 5 and 3!
We can recursively shrink the array using ONLY subtraction: F_{k-1} = F_k - F_{k-2}!

**3. The Algorithm:**
1. Generate Fibonacci numbers until we find F_k that is \ge N (the length of the array).
2. Set an `offset = -1`. This represents the start of our currently active array chunk.
3. Our "midpoint" (probe) is simply calculated as: `i = min(offset + F_{k-2}, N-1)`. We are cutting off a chunk of size F_{k-2} from the left.
4. Compare `arr[i]` with the `target`:
   - **Match:** Return `i`.
   - **Target is smaller:** The target is in the left chunk (size F_{k-2}). We shift our Fibonacci numbers down by TWO: F_k = F_{k-2}.
   - **Target is larger:** The target is in the right chunk (size F_{k-1}). We shift our Fibonacci numbers down by ONE: F_k = F_{k-1}. Crucially, we update our `offset` to `i`, effectively slicing off the entire left chunk!
5. Loop until F_k drops to 1.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for search_09: Fibonacci Search.

Sorted array; uses Fibonacci numbers to split the range.
Always shrinks by at least one Fibonacci number, so the loop
runs in O(log n) time. The split is by index, not value.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    # Initialise the smallest Fibonacci >= n.
    fib2, fib1 = 0, 1
    fib = fib1 + fib2
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if data[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif data[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and offset + 1 < n and data[offset + 1] == target:
        return offset + 1
    return -1
```

</details>

## Walk-through

`arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`. `target = 60`. Length 10.

1. Generate Fibonacci: `0, 1, 1, 2, 3, 5, 8, 13`.
   - F_k = 13, F_{k-1} = 8, F_{k-2} = 5.
   - `offset = -1`.
2. **Loop 1:**
   - `i = min(-1 + 5, 9) = 4`. `arr[4] = 50`.
   - `50 < 60`. Target is in the right half!
   - `offset = 4`.
   - Shift down by 1: F_k = 8, F_{k-1} = 5, F_{k-2} = 3.
3. **Loop 2:**
   - `i = min(4 + 3, 9) = 7`. `arr[7] = 80`.
   - `80 > 60`. Target is in the left half!
   - `offset = 4` (Unchanged).
   - Shift down by 2: F_k = 3, F_{k-1} = 2, F_{k-2} = 1.
4. **Loop 3:**
   - `i = min(4 + 1, 9) = 5`. `arr[5] = 60`.
   - `60 == 60`! Match found!

Result: `5`. ✓
*(Notice how we successfully performed a divide-and-conquer search without executing a single `/` or `%` or `*` or `>>` operator!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Average** | $O(\log N)$ | $O(1)$ |
| **Worst** | $O(\log N)$ | $O(1)$ |

The Fibonacci numbers grow exponentially. Specifically, F_k ~= 1.618^k.
Because the size of the active array strictly shrinks by the golden ratio at every step, the number of iterations required is strictly bounded by $O(\log N)$.
Space complexity is $O(1)$ because we only track three integers to maintain the active Fibonacci state.

## Variants & optimizations

- **Golden-Section Search (`search_05` note):** The Fibonacci Search algorithm applied to mathematical Unimodal functions instead of arrays, used to find the absolute minimum/maximum of a curve without using calculus.

## Real-world applications

- **Late 1950s Mainframes:** The IBM 650 (the first mass-produced computer) had an agonizingly slow drum-memory architecture where division took orders of magnitude longer than addition. Fibonacci Search was invented specifically to optimize sorting and searching on these machines.

## Related algorithms in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — The division-based algorithmic counterpart.
- **[dynamic_01 - Fibonacci Numbers](../dynamic/dp_01_fibonacci.md)** — The dynamic programming algorithm used to generate the numbers.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
