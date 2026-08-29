"""Project Euler Problem 839: Beans in Bowls.

Mathematical reduction:
Initial beans in bowl n: S_n.
At each step, 1 bean is moved from bowl n to bowl n+1 if S_n > S_{n+1}.
The process terminates at the unique non-descending configuration F = (F_0, F_1, ..., F_{N-1})
that minimizes the total transport cost sum_{i=0}^{N-1} i * (F_i - S_i).

Finding the final configuration F:
- Process bowls 0, 1, ..., N-1 from left to right using a monotonic stack of leveled blocks.
- Each block maintains (count, total_sum).
- When a new bowl is added, while the top of the stack has average less than the previous block,
  the two blocks merge into a single leveled range:
    (count_1 + count_2, total_1 + total_2).
- At the end of the scan, each block of length k and sum w distributes as:
    (k - r) copies of q = floor(w / k), followed by r copies of (q + 1), where r = w mod k.

The total number of moves B(N) is computed directly in O(N) time and O(|stack|) space:
  B(N) = sum_{i=0}^{N-1} i * F_i - sum_{i=0}^{N-1} i * S_i
where sum_{i} i * F_i is evaluated in O(1) per block using arithmetic progression sums.
"""

from __future__ import annotations


def solve(n: int = 10000000) -> int:
    """Compute B(N) in O(N) time and O(1) auxiliary space."""
    stack: list[list[int]] = []
    sum_i_s = 0

    s_curr = 290797
    for i in range(n):
        sum_i_s += i * s_curr

        count = 1
        total = s_curr
        while stack:
            prev_count, prev_total = stack[-1]
            if total * prev_count < prev_total * count:
                stack.pop()
                count += prev_count
                total += prev_total
            else:
                break
        stack.append([count, total])

        s_curr = (s_curr * s_curr) % 50515093

    # Compute sum_i_f from the merged blocks in O(|stack|)
    sum_i_f = 0
    left_idx = 0
    for count, total in stack:
        q = total // count
        r = total % count

        # First count - r elements have value q
        c1 = count - r
        if c1 > 0:
            sum_idx1 = (left_idx + (left_idx + c1 - 1)) * c1 // 2
            sum_i_f += sum_idx1 * q

        # Next r elements have value q + 1
        if r > 0:
            sum_idx2 = ((left_idx + c1) + (left_idx + count - 1)) * r // 2
            sum_i_f += sum_idx2 * (q + 1)

        left_idx += count

    return sum_i_f - sum_i_s


if __name__ == "__main__":
    print(solve())
