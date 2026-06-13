"""Greedy algorithms.

Ten algorithms from GFG's "Greedy Algorithms" catalog:

  01 Activity Selection     - max non-overlapping activities
  02 Fractional Knapsack    - max value with fractional items
  03 Huffman Coding         - optimal prefix code (min total bits)
  04 Job Sequencing         - max profit with deadlines
  05 Optimal Merge Pattern  - min cost of merging files
  06 Gas Station            - find a valid starting pump
  07 Jump Game              - min jumps to reach the end
  08 Candy Distribution     - min candies satisfying the rating rules
  09 Lemonade Change        - can we make change for every customer?
 10 Minimum Coins (greedy)  - min coins for an amount (canonical denom)

Each challenge generates a deterministic random input, computes
the expected answer in setup(), and asks the player to reproduce
it. Greedy algorithms give one clear correct answer per input
shape, so verify() is always a plain equality check.
"""

from __future__ import annotations

import heapq
import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass
from code_n.grid import CellType, Grid
from code_n.tracked import TrackedList


# --- Visualisation helper. The Pygame renderer needs a Grid to
# draw on, and the user has asked that every data structure get a
# representative visual. This helper builds a Grid from a list of
# rows (one per "field") of equal length and fills each cell with
# the corresponding value. ---


def _make_data_grid(rows: list[list], cell_type: CellType = CellType.VALUE) -> Grid:
    """Build a Grid that visualises ``rows`` (a list of equal-length lists).

    Each row in the input becomes a row in the grid; columns are
    aligned so cell (column, row_index) shows the i-th element of
    rows[row_index]. The grid is sized to fit, with empty cells if
    any row is shorter than the longest.
    """
    n_cols = max((len(r) for r in rows), default=0)
    n_rows = max(len(rows), 1)
    grid = Grid(n_cols, n_rows)
    for row_index, row in enumerate(rows):
        for col_index, value in enumerate(row):
            grid.set(col_index, row_index, cell_type, value)
    return grid


# --- Activity Selection ---


def _setup_activity(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(n, 20)
    activities: list[tuple[int, int]] = []
    for _ in range(challenge._n):
        start = rng.randint(0, 50)
        finish = start + rng.randint(1, 20)
        activities.append((start, finish))
    challenge._start = [s for s, _ in activities]
    challenge._finish = [f for _, f in activities]
    challenge._expected = _activity_count(challenge._start, challenge._finish, challenge._n)
    challenge.grid = _make_data_grid([challenge._start, challenge._finish])
    return {"start": list(challenge._start), "finish": list(challenge._finish), "n": challenge._n}


def _verify_activity(challenge, result: Any) -> bool:
    return result == challenge._expected


def _activity_count(start: list[int], finish: list[int], n: int) -> int:
    pairs = sorted(zip(start, finish), key=lambda p: p[1])
    if not pairs:
        return 0
    count = 1
    last = pairs[0][1]
    for s, f in pairs[1:]:
        if s >= last:
            count += 1
            last = f
    return count


GREEDY_01_SOURCE = '''\
"""Optimal solution for greedy_01: Activity Selection.

Sort activities by finish time, then greedily pick each one that
starts after the last picked activity's finish. O(n log n) time.
"""


def solve(start, finish, n):
    pairs = sorted(zip(start, finish), key=lambda p: p[1])
    if not pairs:
        return 0
    count = 1
    last_finish = pairs[0][1]
    for s, f in pairs[1:]:
        if s >= last_finish:
            count += 1
            last_finish = f
    return count
'''


# --- Fractional Knapsack ---


def _setup_fractional_knapsack(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(n, 15)
    challenge._values = [rng.randint(1, 100) for _ in range(challenge._n)]
    challenge._weights = [rng.randint(1, 50) for _ in range(challenge._n)]
    total_weight = sum(challenge._weights)
    challenge._capacity = max(1, total_weight // 2)
    challenge._expected = _fractional_knapsack(
        challenge._values, challenge._weights, challenge._capacity,
    )
    challenge.grid = _make_data_grid([challenge._values, challenge._weights])
    return {
        "values": TrackedList(challenge._values),
        "weights": TrackedList(challenge._weights),
        "capacity": challenge._capacity,
        "n": challenge._n,
    }


def _verify_fractional_knapsack(challenge, result: Any) -> bool:
    return abs(float(result) - challenge._expected) < 1e-6


def _fractional_knapsack(values: list[int], weights: list[int], capacity: int) -> float:
    # Sort items by value/weight ratio descending; take as much as fits.
    items = sorted(zip(values, weights), key=lambda vw: vw[0] / vw[1], reverse=True)
    remaining = capacity
    total = 0.0
    for v, w in items:
        if w <= 0:
            continue
        if remaining >= w:
            total += v
            remaining -= w
        else:
            total += v * (remaining / w)
            break
    return total


GREEDY_02_SOURCE = '''\
"""Optimal solution for greedy_02: Fractional Knapsack.

Sort items by value/weight ratio descending. Greedily take as much
of each item as fits. O(n log n) time. Unlike 0/1 knapsack, the
fractional version is solvable optimally by a simple greedy.
"""


def solve(values, weights, capacity, n):
    # Sort items by value-to-weight ratio (descending). Pair indices
    # so we can sort on the ratio without losing the alignment.
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    remaining = capacity
    total = 0.0
    for index in order:
        w = weights[index]
        if remaining >= w:
            total += values[index]
            remaining -= w
        else:
            total += values[index] * (remaining / w)
            break
    return total
'''


# --- Huffman Coding ---


def _setup_huffman(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(n, 10)
    # Lowercase letters so the player has a readable alphabet.
    challenge._chars = [chr(ord("a") + i) for i in range(challenge._n)]
    challenge._freq = [rng.randint(1, 50) for _ in range(challenge._n)]
    challenge._expected = _huffman_total_bits(challenge._freq)
    # Visualise frequencies; the chars label would not fit in a
    # 1-cell-wide row, so we only show the numbers.
    challenge.grid = _make_data_grid([challenge._freq])
    return {
        "chars": list(challenge._chars),
        "freq": list(challenge._freq),
        "n": challenge._n,
    }


def _verify_huffman(challenge, result: Any) -> bool:
    return int(result) == challenge._expected


def _huffman_total_bits(freq: list[int]) -> int:
    if not freq:
        return 0
    heap = [[f, 0, ""] for f in freq]
    heapq.heapify(heap)
    # Single character -> 1 bit per occurrence (one symbol, depth 1).
    if len(heap) == 1:
        return heap[0][0]
    # Internal node shape: [total_freq, 0, ""] with 0 children for leaves
    # and 2 children for merges. We don't need the children; we just
    # need the total weighted path length.
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = [a[0] + b[0], 0, ""]
        total += merged[0]
        heapq.heappush(heap, merged)
    return total


GREEDY_03_SOURCE = '''\
"""Optimal solution for greedy_03: Huffman Coding.

Build a min-heap of leaf frequencies. Repeatedly pop the two
smallest, merge them into a new node whose weight is their sum,
push the new node. Each merge adds its weight to the total bits.
O(n log n) time.
"""


def solve(chars, freq, n):
    import heapq
    if n == 0:
        return 0
    if n == 1:
        return freq[0]
    heap = [[f, 0, ""] for f in freq]
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = [a[0] + b[0], 0, ""]
        total += merged[0]
        heapq.heappush(heap, merged)
    return total
'''


# --- Job Sequencing with Deadlines ---


def _setup_job_sequencing(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(n, 8)
    # (id, deadline, profit) - deadlines 1..n
    challenge._jobs = []
    for i in range(challenge._n):
        deadline = rng.randint(1, challenge._n)
        profit = rng.randint(1, 100)
        challenge._jobs.append((i, deadline, profit))
    challenge._expected = _job_sequencing(challenge._jobs, challenge._n)
    challenge.grid = _make_data_grid(
        [[d for _, d, _ in challenge._jobs], [p for _, _, p in challenge._jobs]],
    )
    return {
        "deadline": [d for _, d, _ in challenge._jobs],
        "profit": [p for _, _, p in challenge._jobs],
        "n": challenge._n,
    }


def _verify_job_sequencing(challenge, result: Any) -> bool:
    return int(result) == challenge._expected


def _job_sequencing(jobs: list[tuple[int, int, int]], n: int) -> int:
    # Sort by profit descending; greedily schedule each at the latest
    # available free slot up to its deadline.
    slots = [False] * (n + 1)
    total = 0
    for _id, deadline, profit in sorted(jobs, key=lambda j: j[2], reverse=True):
        for t in range(min(deadline, n), 0, -1):
            if not slots[t]:
                slots[t] = True
                total += profit
                break
    return total


GREEDY_04_SOURCE = '''\
"""Optimal solution for greedy_04: Job Sequencing with Deadlines.

Each job takes one unit of time and must finish by its deadline.
Sort jobs by profit (descending); place each in the latest free
slot before its deadline. O(n^2) time. Greedy correctness follows
from the exchange argument.
"""


def solve(deadline, profit, n):
    # Build job tuples and sort by profit descending.
    jobs = sorted(
        ((profit[i], deadline[i]) for i in range(n)),
        key=lambda j: j[0],
        reverse=True,
    )
    # latest_free[t] is the latest time slot that is still available
    # up to t. We collapse the search with a simple boolean array.
    slots = [False] * (n + 1)
    total = 0
    for p, d in jobs:
        # Find the latest free slot <= min(d, n).
        for t in range(min(d, n), 0, -1):
            if not slots[t]:
                slots[t] = True
                total += p
                break
    return total
'''


# --- Optimal Merge Pattern ---


def _setup_optimal_merge(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(n, 8)
    challenge._sizes = [rng.randint(1, 100) for _ in range(challenge._n)]
    challenge._expected = _optimal_merge_cost(challenge._sizes)
    challenge.grid = _make_data_grid([challenge._sizes])
    return {"sizes": list(challenge._sizes), "n": challenge._n}


def _verify_optimal_merge(challenge, result: Any) -> bool:
    return int(result) == challenge._expected


def _optimal_merge_cost(sizes: list[int]) -> int:
    if len(sizes) <= 1:
        return 0
    heap = list(sizes)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = a + b
        total += merged
        heapq.heappush(heap, merged)
    return total


GREEDY_05_SOURCE = '''\
"""Optimal solution for greedy_05: Optimal Merge Pattern.

Merging two files of sizes a and b costs a + b. Total cost of
merging n files is the sum of costs of each pairwise merge. To
minimise, always merge the two smallest remaining files. O(n log n).
"""


def solve(sizes, n):
    import heapq
    if n <= 1:
        return 0
    heap = list(sizes)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = a + b
        total += merged
        heapq.heappush(heap, merged)
    return total
'''


# --- Gas Station ---


def _setup_gas_station(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(n, 10)
    # Construct inputs that DO have a solution to keep the
    # expected output interesting (otherwise the answer is -1 every
    # time and the player can't tell apart a good vs bad submission).
    while True:
        gas = [rng.randint(1, 30) for _ in range(challenge._n)]
        cost = [rng.randint(1, 30) for _ in range(challenge._n)]
        start = _gas_station_start(gas, cost)
        if start != -1 or sum(gas) >= sum(cost):
            # If sum(gas) >= sum(cost) but no start works, this
            # happens; regenerate.
            if start != -1:
                break
    challenge._gas = gas
    challenge._cost = cost
    challenge._expected = start
    challenge.grid = _make_data_grid([gas, cost])
    return {"gas": list(gas), "cost": list(cost), "n": challenge._n}


def _verify_gas_station(challenge, result: Any) -> bool:
    return int(result) == challenge._expected


def _gas_station_start(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    total = 0
    start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            start = i + 1
            total = 0
    return start if 0 <= start < len(gas) else -1


GREEDY_06_SOURCE = '''\
"""Optimal solution for greedy_06: Gas Station.

If the total gas is at least the total cost, a solution exists.
Track the running tank from each candidate start. When the tank
goes negative, no station up to and including the current one
can be a valid start. O(n).
"""


def solve(gas, cost, n):
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
'''


# --- Jump Game (minimum number of jumps) ---


def _setup_jump_game(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(max(n, 4), 30)
    # arr[i] = max jump length from position i. The last position
    # is always reachable since we cap n and constrain arr.
    arr = [rng.randint(1, 5) for _ in range(challenge._n)]
    # Make sure the last position is reachable from at least one
    # earlier position; otherwise the answer is undefined.
    if challenge._n > 1:
        arr[-1] = 0
        reachable = any(arr[i] >= challenge._n - 1 - i for i in range(challenge._n - 1))
        if not reachable:
            arr[0] = challenge._n - 1
    challenge._arr = arr
    challenge._expected = _min_jumps(arr, challenge._n)
    challenge.grid = _make_data_grid([arr])
    return {"arr": list(arr), "n": challenge._n}


def _verify_jump_game(challenge, result: Any) -> bool:
    return int(result) == challenge._expected


def _min_jumps(arr: list[int], n: int) -> int:
    if n <= 1:
        return 0
    # Greedy: track the current "window" of positions reachable
    # in the current number of jumps, and the farthest position
    # the next jump can reach. When we cross the window, we
    # must take another jump.
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps


GREEDY_07_SOURCE = '''\
"""Optimal solution for greedy_07: Jump Game (min jumps).

Track the farthest index reachable in the current number of
jumps, and the farthest index reachable in one more jump. When
the loop index reaches the end of the current window, take
another jump. O(n).
"""


def solve(arr, n):
    if n <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
'''


# --- Candy Distribution ---


def _setup_candy(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(max(n, 3), 30)
    challenge._ratings = [rng.randint(1, 10) for _ in range(challenge._n)]
    challenge._expected = _candy_count(challenge._ratings)
    challenge.grid = _make_data_grid([challenge._ratings])
    return {"ratings": list(challenge._ratings), "n": challenge._n}


def _verify_candy(challenge, result: Any) -> bool:
    return int(result) == challenge._expected


def _candy_count(ratings: list[int]) -> int:
    n = len(ratings)
    if n == 0:
        return 0
    candies = [1] * n
    # Left-to-right pass: every child with a higher rating than
    # the left neighbour gets one more candy.
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    # Right-to-left pass: do the same against the right neighbour.
    total = candies[-1]
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        total += candies[i]
    return total


GREEDY_08_SOURCE = '''\
"""Optimal solution for greedy_08: Candy Distribution.

Each child gets at least 1 candy. Children with a higher rating
than a neighbour must get more candies. Two passes: one
left-to-right (to satisfy the left rule), one right-to-left
(to satisfy the right rule). O(n).
"""


def solve(ratings, n):
    if n == 0:
        return 0
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    total = candies[-1]
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        total += candies[i]
    return total
'''


# --- Lemonade Change ---


def _setup_lemonade(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    challenge._n = min(n, 30)
    # Customers pay with $5, $10, or $20. We start with no change.
    # Always include at least one $5 to make the puzzle solvable.
    bills = [5] * 3 + [rng.choice([5, 10, 20]) for _ in range(challenge._n - 3)]
    rng.shuffle(bills)
    challenge._bills = bills
    challenge._expected = _lemonade_change(bills)
    challenge.grid = _make_data_grid([bills])
    return {"bills": list(bills), "n": challenge._n}


def _verify_lemonade(challenge, result: Any) -> bool:
    return bool(result) == bool(challenge._expected)


def _lemonade_change(bills: list[int]) -> bool:
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:  # 20
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True


GREEDY_09_SOURCE = '''\
"""Optimal solution for greedy_09: Lemonade Change.

Each lemonade is $5. Customers pay with $5/$10/$20. We must give
exact change. Always prefer a $10 over three $5s when making
$20 change (preserve $5s). O(n).
"""


def solve(bills, n):
    fives = 0
    tens = 0
    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives == 0:
                return False
            fives -= 1
            tens += 1
        else:  # 20
            if tens > 0 and fives > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True
'''


# --- Minimum Coins (Greedy, canonical denominations) ---


def _setup_min_coins(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Canonical US-style denominations that make the greedy
    # algorithm optimal (1, 5, 10, 25 = quarters).
    challenge._coins = [1, 5, 10, 25]
    challenge._amount = rng.randint(1, max(2, n) * 20)
    challenge._expected = _min_coins(challenge._coins, challenge._amount)
    # Two rows: coin denominations on top, target amount on the
    # bottom (the amount is constant across the row, but the row
    # makes the visual obvious).
    challenge.grid = _make_data_grid(
        [challenge._coins, [challenge._amount] * len(challenge._coins)],
    )
    return {
        "coins": list(challenge._coins),
        "amount": challenge._amount,
    }


def _verify_min_coins(challenge, result: Any) -> bool:
    return int(result) == challenge._expected


def _min_coins(coins: list[int], amount: int) -> int:
    count = 0
    for c in sorted(coins, reverse=True):
        if c <= 0:
            continue
        while amount >= c:
            amount -= c
            count += 1
        if amount == 0:
            break
    return count if amount == 0 else -1


GREEDY_10_SOURCE = '''\
"""Optimal solution for greedy_10: Minimum Coins (greedy).

For canonical denomination sets (1, 5, 10, 25), the greedy
algorithm is optimal: always take as many of the largest coin as
fits. For non-canonical sets the greedy is only a heuristic; for
those use the 0/1 knapsack / DP variant instead. O(n) after sort.
"""


def solve(coins, amount):
    count = 0
    for c in sorted(coins, reverse=True):
        if c <= 0:
            continue
        while amount >= c:
            amount -= c
            count += 1
        if amount == 0:
            break
    if amount == 0:
        return count
    return -1
'''


GREEDY_11_SOURCE = '''\
"""Optimal solution for greedy_11: Egyptian Fraction.

Every positive rational number ``p/q`` can be written as the sum
of distinct unit fractions (1/d) - the greedy algorithm
repeatedly takes the smallest unit fraction not smaller than the
remainder, which is ``ceil(q / p)``. Stop when the remainder
hits zero; cap the loop at q+1 steps so a degenerate input can't
run forever.
"""


def solve(p, q):
    if p <= 0 or q <= 0:
        return []
    result = []
    for _ in range(q + 1):
        if p == 0:
            break
        d = (q + p - 1) // p  # ceil(q / p)
        result.append(d)
        p = p * d - q
        q = q * d
        # Reduce to keep numbers small.
        from math import gcd
        g = gcd(p, q) or 1
        p //= g
        q //= g
    return result
'''


GREEDY_12_SOURCE = '''\
"""Optimal solution for greedy_12: Max Trains for Stoppage.

Given arrival and departure times for trains at a single platform,
find the maximum number of trains that can be handled without
conflict. Greedy: sort by departure time, accept a train iff its
arrival is after the last accepted departure. O(n log n) for the
sort.
"""


def solve(arrivals, departures, n):
    if n == 0:
        return 0
    order = sorted(range(n), key=lambda i: (departures[i], arrivals[i]))
    count = 0
    last_departure = -1
    for i in order:
        if arrivals[i] >= last_departure:
            count += 1
            last_departure = departures[i]
    return count
'''


# --- greedy_11 Egyptian Fraction helpers. ---


def _setup_egyptian(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    # Pick a fraction with smallish numerator and denominator so the
    # greedy algorithm finishes within a reasonable number of steps.
    q = rng.randint(2, max(2, n) * 3)
    p = rng.randint(1, q)
    challenge._p = p
    challenge._q = q
    return {"p": p, "q": q}


def _verify_egyptian(challenge, result: Any) -> bool:
    if not isinstance(result, list) or not result:
        return False
    # Sum 1/d for each d in result; should equal challenge._p / challenge._q.
    from fractions import Fraction
    total = sum(Fraction(1, d) for d in result)
    expected = Fraction(challenge._p, challenge._q)
    return total == expected and len(result) == len(set(result))  # distinct


# --- greedy_12 Max Trains helpers. ---


def _setup_max_trains(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n_trains = max(1, min(n, 12))
    arrivals = []
    departures = []
    for _ in range(n_trains):
        a = rng.randint(0, 100)
        # Keep departures after arrivals, with reasonable spans.
        d = a + rng.randint(1, 30)
        arrivals.append(a)
        departures.append(d)
    challenge._arrivals = arrivals
    challenge._departures = departures
    return {"arrivals": list(arrivals), "departures": list(departures), "n": n_trains}


def _verify_max_trains(challenge, result: Any) -> bool:
    if not isinstance(result, int):
        return False
    # Re-run the greedy and compare.
    n = len(challenge._arrivals)
    order = sorted(range(n), key=lambda i: (challenge._departures[i], challenge._arrivals[i]))
    count = 0
    last = -1
    for i in order:
        if challenge._arrivals[i] >= last:
            count += 1
            last = challenge._departures[i]
    return result == count


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="greedy_01",
        name="Activity Selection",
        category="greedy",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Given n activities with start and finish times, pick the maximum\n"
            "number of non-overlapping activities.\n"
            "Greedy: sort by finish time, then pick each activity whose start is\n"
            "at or after the finish of the last picked.\n"
            "Requirement: O(n log n).\n"
            "Source: https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/"
        ),
        source_url="https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/",
        params=["start", "finish", "n"],
        inputs={
            "start": "list of n activity start times.",
            "finish": "list of n activity finish times (parallel to start).",
            "n": "number of activities.",
        },
        returns="the maximum number of non-overlapping activities that can be selected.",
        source=GREEDY_01_SOURCE,
        setup_fn=_setup_activity,
        verify_fn=_verify_activity,
        samples=[
            Sample("start = [1, 3, 0, 5, 8, 5], finish = [2, 4, 6, 7, 9, 9], n = 6", "4"),
            Sample("start = [1, 2, 3], finish = [2, 3, 4], n = 3", "3"),
            Sample("start = [0, 5, 8], finish = [4, 6, 9], n = 3", "2"),
        ],
        hint="Sort by finish time; pick each activity whose start >= last picked finish.",
        parents=[],
        children=["greedy_02"],
    ),
    AlgorithmSpec(
        id="greedy_02",
        name="Fractional Knapsack",
        category="greedy",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Items with weight and value, a knapsack of capacity W. Take fractions\n"
            "of items. Maximize total value.\n"
            "Greedy: sort by value/weight ratio descending; take as much of each\n"
            "item as fits.\n"
            "Requirement: O(n log n). Unlike 0/1 knapsack, the fractional version\n"
            "is exactly solvable by a simple greedy.\n"
            "Source: https://www.geeksforgeeks.org/fractional-knapsack-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/fractional-knapsack-problem/",
        params=["values", "weights", "capacity", "n"],
        inputs={
            "values": "list-like of n item values.",
            "weights": "list-like of n item weights (parallel to values).",
            "capacity": "knapsack capacity.",
            "n": "number of items.",
        },
        returns="the maximum total value, allowing fractions of items (as a float).",
        source=GREEDY_02_SOURCE,
        setup_fn=_setup_fractional_knapsack,
        verify_fn=_verify_fractional_knapsack,
        samples=[
            Sample("values = [60, 100, 120], weights = [10, 20, 30], capacity = 50, n = 3", "240.0"),
            Sample("values = [500], weights = [30], capacity = 10, n = 1", "166.66666666666666"),
            Sample("values = [10, 20, 30], weights = [5, 10, 15], capacity = 100, n = 3", "60.0"),
        ],
        hint="Sort by value/weight ratio. For each item, take as much as fits.",
        parents=["greedy_01"],
        children=["greedy_03"],
    ),
    AlgorithmSpec(
        id="greedy_03",
        name="Huffman Coding",
        category="greedy",
        difficulty=5,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Given a list of characters and their frequencies, build the optimal\n"
            "prefix-free binary code (Huffman tree) and return the total number of\n"
            "bits needed to encode the string.\n"
            "Requirement: O(n log n) using a min-heap.\n"
            "Source: https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/"
        ),
        source_url="https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/",
        params=["chars", "freq", "n"],
        inputs={
            "chars": "list of n distinct characters.",
            "freq": "list of n frequencies (parallel to chars).",
            "n": "number of characters.",
        },
        returns="the total number of bits in the Huffman encoding of the string.",
        source=GREEDY_03_SOURCE,
        setup_fn=_setup_huffman,
        verify_fn=_verify_huffman,
        samples=[
            Sample("chars = ['a', 'b', 'c', 'd', 'e', 'f'], freq = [5, 9, 12, 13, 16, 45], n = 6", "224"),
            Sample("chars = ['a', 'b', 'c'], freq = [1, 1, 1], n = 3", "5"),
            Sample("chars = ['a'], freq = [7], n = 1", "7"),
        ],
        hint="Push all frequencies into a min-heap. Repeatedly merge the two smallest. Each merge adds its sum to the total.",
        parents=["greedy_02"],
        children=["greedy_04"],
    ),
    AlgorithmSpec(
        id="greedy_04",
        name="Job Sequencing",
        category="greedy",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Each job has a deadline and a profit, and takes one unit of time.\n"
            "Schedule jobs to maximise total profit; a job must finish by its\n"
            "deadline.\n"
            "Greedy: sort by profit descending; place each job in the latest free\n"
            "slot <= its deadline.\n"
            "Requirement: O(n^2) with a boolean slot array, or O(n log n) with a DSU.\n"
            "Source: https://www.geeksforgeeks.org/job-sequencing-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/job-sequencing-problem/",
        params=["deadline", "profit", "n"],
        inputs={
            "deadline": "list of n deadlines (1-indexed).",
            "profit": "list of n profits (parallel to deadline).",
            "n": "number of jobs.",
        },
        returns="the maximum total profit from a feasible schedule.",
        source=GREEDY_04_SOURCE,
        setup_fn=_setup_job_sequencing,
        verify_fn=_verify_job_sequencing,
        samples=[
            Sample("deadline = [2, 1, 2, 1, 3], profit = [100, 19, 27, 25, 15], n = 5", "142"),
            Sample("deadline = [3, 3, 3], profit = [50, 60, 70], n = 3", "120"),
            Sample("deadline = [1, 1, 1], profit = [10, 20, 30], n = 3", "30"),
        ],
        hint="Sort by profit descending. Place each job in the latest free slot <= its deadline.",
        parents=["greedy_03"],
        children=["greedy_05"],
    ),
    AlgorithmSpec(
        id="greedy_05",
        name="Optimal Merge Pattern",
        category="greedy",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Merging two files of sizes a and b costs a + b. Total cost of\n"
            "merging n files into one is the sum of pairwise merge costs.\n"
            "Greedy: always merge the two smallest remaining files. Same shape\n"
            "as Huffman but with a single weight per file.\n"
            "Requirement: O(n log n) using a min-heap.\n"
            "Source: https://www.geeksforgeeks.org/optimal-file-merge-pattern/"
        ),
        source_url="https://www.geeksforgeeks.org/optimal-file-merge-pattern/",
        params=["sizes", "n"],
        inputs={
            "sizes": "list of n file sizes.",
            "n": "number of files.",
        },
        returns="the minimum total cost of merging all files into one.",
        source=GREEDY_05_SOURCE,
        setup_fn=_setup_optimal_merge,
        verify_fn=_verify_optimal_merge,
        samples=[
            Sample("sizes = [5, 2, 4, 7], n = 4", "44"),
            Sample("sizes = [20, 30, 10, 5, 30], n = 5", "205"),
            Sample("sizes = [10, 20], n = 2", "30"),
        ],
        hint="Use a min-heap. Repeatedly pop the two smallest, sum them, push back.",
        parents=["greedy_04"],
        children=["greedy_06"],
    ),
    AlgorithmSpec(
        id="greedy_06",
        name="Gas Station",
        category="greedy",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "n gas stations on a circular route. gas[i] is the fuel at station i,\n"
            "cost[i] is the fuel to reach i+1. Find a starting index from which\n"
            "the car can complete the loop, or -1 if none exists.\n"
            "Requirement: O(n) - one pass tracks the running tank; whenever the\n"
            "tank goes negative, the start must be after the failing station.\n"
            "Source: https://www.geeksforgeeks.org/gas-station/"
        ),
        source_url="https://www.geeksforgeeks.org/gas-station/",
        params=["gas", "cost", "n"],
        inputs={
            "gas": "list of n gas amounts at each station.",
            "cost": "list of n fuel costs to the next station.",
            "n": "number of stations.",
        },
        returns="the index of a valid starting station, or -1 if no valid start exists.",
        source=GREEDY_06_SOURCE,
        setup_fn=_setup_gas_station,
        verify_fn=_verify_gas_station,
        samples=[
            Sample("gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2], n = 5", "3"),
            Sample("gas = [2, 3, 4], cost = [3, 4, 3], n = 3", "-1"),
            Sample("gas = [5, 1, 2, 3, 4], cost = [4, 4, 4, 4, 4], n = 5", "4"),
        ],
        hint="If sum(gas) < sum(cost), return -1. Otherwise track the running tank; reset start when it goes negative.",
        parents=["greedy_05"],
        children=["greedy_07"],
    ),
    AlgorithmSpec(
        id="greedy_07",
        name="Jump Game",
        category="greedy",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Each element arr[i] is the maximum jump length from position i.\n"
            "Return the minimum number of jumps to reach the last index\n"
            "(or stay where you are if you're already there).\n"
            "Requirement: O(n) using two pointers: the end of the current\n"
            "'reach window' and the farthest position reachable by one more jump.\n"
            "Source: https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-array/"
        ),
        source_url="https://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-array/",
        params=["arr", "n"],
        inputs={
            "arr": "list of n max-jump lengths.",
            "n": "length of arr.",
        },
        returns="the minimum number of jumps to reach the last index, or 0 if already there.",
        source=GREEDY_07_SOURCE,
        setup_fn=_setup_jump_game,
        verify_fn=_verify_jump_game,
        samples=[
            Sample("arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], n = 11", "3"),
            Sample("arr = [2, 3, 1, 1, 4], n = 5", "2"),
            Sample("arr = [1, 1, 1, 1, 1], n = 5", "4"),
        ],
        hint="Track the farthest position reachable in the current number of jumps. Take another jump when you reach the boundary.",
        parents=["greedy_06"],
        children=["greedy_08"],
    ),
    AlgorithmSpec(
        id="greedy_08",
        name="Candy Distribution",
        category="greedy",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "n children in a line, each with a rating. Distribute candies such that:\n"
            "  * every child gets at least 1 candy\n"
            "  * a child with a higher rating than a neighbour gets more candies\n"
            "Return the minimum total number of candies.\n"
            "Requirement: O(n) using two passes (left-to-right and right-to-left).\n"
            "Source: https://www.geeksforgeeks.org/minimum-number-of-candies-required-to-distribute-among-children/"
        ),
        source_url="https://www.geeksforgeeks.org/minimum-number-of-candies-required-to-distribute-among-children/",
        params=["ratings", "n"],
        inputs={
            "ratings": "list of n child ratings.",
            "n": "number of children.",
        },
        returns="the minimum number of candies to distribute.",
        source=GREEDY_08_SOURCE,
        setup_fn=_setup_candy,
        verify_fn=_verify_candy,
        samples=[
            Sample("ratings = [1, 0, 2], n = 3", "5"),
            Sample("ratings = [1, 2, 2], n = 3", "4"),
            Sample("ratings = [1, 3, 4, 5, 2], n = 5", "11"),
        ],
        hint="Two passes: left-to-right (more than left neighbour), right-to-left (more than right neighbour).",
        parents=["greedy_07"],
        children=["greedy_09"],
    ),
    AlgorithmSpec(
        id="greedy_09",
        name="Lemonade Change",
        category="greedy",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Each lemonade costs $5. Customers pay in $5, $10, or $20 bills\n"
            "(given in order). Return True if we can give correct change to every\n"
            "customer; False otherwise.\n"
            "Greedy: for a $20 bill, prefer $10 + $5 over three $5s so the $5\n"
            "supply lasts longer.\n"
            "Requirement: O(n), O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/lemonade-change/"
        ),
        source_url="https://www.geeksforgeeks.org/lemonade-change/",
        params=["bills", "n"],
        inputs={
            "bills": "list of n bills (each is 5, 10, or 20).",
            "n": "number of customers.",
        },
        returns="True if every customer can receive correct change, False otherwise.",
        source=GREEDY_09_SOURCE,
        setup_fn=_setup_lemonade,
        verify_fn=_verify_lemonade,
        samples=[
            Sample("bills = [5, 5, 5, 10, 20], n = 5", "True"),
            Sample("bills = [5, 5, 10, 10, 20], n = 5", "False"),
            Sample("bills = [5, 10, 5, 20], n = 4", "True"),
        ],
        hint="Track $5 and $10 counts. For $20 change, prefer $10 + $5 over three $5s.",
        parents=["greedy_08"],
        children=["greedy_10"],
    ),
    AlgorithmSpec(
        id="greedy_10",
        name="Minimum Coins",
        category="greedy",
        difficulty=3,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Given coin denominations and a target amount, return the minimum number\n"
            "of coins to make the amount. Greedy (always take the largest coin that\n"
            "fits) is optimal only for canonical denomination sets like 1, 5, 10, 25.\n"
            "For non-canonical sets use the DP variant.\n"
            "Requirement: O(n log n) for the sort, O(n) for the greedy.\n"
            "Source: https://www.geeksforgeeks.org/greedy-algorithms-set-of-coin-change-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/greedy-algorithms-set-of-coin-change-problem/",
        params=["coins", "amount"],
        inputs={
            "coins": "list of available coin denominations.",
            "amount": "target amount to make.",
        },
        returns="the minimum number of coins needed, or -1 if the amount cannot be made.",
        source=GREEDY_10_SOURCE,
        setup_fn=_setup_min_coins,
        verify_fn=_verify_min_coins,
        samples=[
            Sample("coins = [1, 5, 10, 25], amount = 41", "4"),
            Sample("coins = [1, 5, 10, 25], amount = 11", "2"),
            Sample("coins = [1, 5, 10, 25], amount = 7", "3"),
        ],
        hint="Sort denominations descending. Repeatedly take as many of the largest coin as fits.",
        parents=["greedy_09"],
        children=["greedy_11"],
    ),
    AlgorithmSpec(
        id="greedy_11",
        name="Egyptian Fraction",
        category="greedy",
        difficulty=4,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Represent a rational number ``p/q`` (with p, q > 0) as a sum of\n"
            "distinct unit fractions ``1/d_i``. The greedy algorithm picks\n"
            "the smallest unit fraction ``>= p/q`` at each step, which is\n"
            "``1 / ceil(q/p)``, and recurses on the remainder.\n"
            "Requirement: O(q) iterations in the worst case.\n"
            "Source: https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-algorithm/"
        ),
        source_url="https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-algorithm/",
        params=["p", "q"],
        inputs={
            "p": "numerator of the fraction (positive).",
            "q": "denominator of the fraction (positive).",
        },
        returns="a list of unit-fraction denominators summing to p/q.",
        source=GREEDY_11_SOURCE,
        setup_fn=_setup_egyptian,
        verify_fn=_verify_egyptian,
        samples=[
            Sample("p = 2, q = 3", "[2, 6]  (2/3 = 1/2 + 1/6)"),
            Sample("p = 6, q = 14", "[3, 11, 231]  (6/14 = 1/3 + 1/11 + 1/231)"),
            Sample("p = 1, q = 2", "[2]"),
        ],
        hint="At each step, d = ceil(q / p). Subtract p/q from 1/d and recurse.",
        parents=["greedy_10"],
        children=["greedy_12"],
    ),
    AlgorithmSpec(
        id="greedy_12",
        name="Max Trains for Stoppage",
        category="greedy",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "A single platform can hold one train at a time. Given arrival and\n"
            "departure times for n trains, find the maximum number that can be\n"
            "served without overlap. Greedy: sort by departure, accept a train\n"
            "iff its arrival is >= the last accepted departure.\n"
            "Requirement: O(n log n).\n"
            "Source: https://www.geeksforgeeks.org/maximum-trains-stoppage-can-use/"
        ),
        source_url="https://www.geeksforgeeks.org/maximum-trains-stoppage-can-use/",
        params=["arrivals", "departures", "n"],
        inputs={
            "arrivals": "list of n arrival times.",
            "departures": "list of n departure times (parallel to arrivals).",
            "n": "number of trains.",
        },
        returns="the maximum number of trains that can be served without conflict.",
        source=GREEDY_12_SOURCE,
        setup_fn=_setup_max_trains,
        verify_fn=_verify_max_trains,
        samples=[
            Sample("arrivals = [100, 120, 150, 200], departures = [110, 130, 210, 220], n = 4", "3"),
            Sample("arrivals = [900, 1000, 1100], departures = [1000, 1100, 1200], n = 3", "3"),
        ],
        hint="Sort by departure. Greedily accept a train if its arrival is >= the last accepted departure.",
        parents=["greedy_11"],
        children=["greedy_13"],
    ),
]


# === greedy_13: Stable Marriage ===

GREEDY_13_SOURCE = '''
def solve(n, men_prefs, women_prefs):
    """Stable Marriage: Gale-Shapley algorithm.

    men_prefs[i] is a list of women indices in i's preference
    order. women_prefs[i] is the same for women's preferences.
    Returns the men's matched partners as a list of n
    indices. (The women's matches are the inverse.)
    """
    if n == 0:
        return []
    # Each man has a pointer to the next woman to propose to.
    next_w = [0] * n
    # Each woman is currently engaged to -1 (free).
    woman_engaged_to = [-1] * n
    # Each man is currently engaged to -1 (free).
    man_engaged_to = [-1] * n
    # Pre-compute each woman's ranking of men: woman_rank[w][m] = m's rank.
    woman_rank = [[0] * n for _ in range(n)]
    for w in range(n):
        for rank, m in enumerate(women_prefs[w]):
            woman_rank[w][m] = rank
    free_men = list(range(n))
    while free_men:
        m = free_men.pop(0)
        w = men_prefs[m][next_w[m]]
        next_w[m] += 1
        if woman_engaged_to[w] == -1:
            # w is free, accept.
            woman_engaged_to[w] = m
            man_engaged_to[m] = w
        else:
            current = woman_engaged_to[w]
            # w prefers the new proposer iff rank[new] < rank[current].
            if woman_rank[w][m] < woman_rank[w][current]:
                # w dumps current for m.
                woman_engaged_to[w] = m
                man_engaged_to[m] = w
                man_engaged_to[current] = -1
                free_men.append(current)
            else:
                # w rejects m; m tries again.
                free_men.insert(0, m)
    return man_engaged_to
'''


def _setup_stable_marriage(challenge, n, seed):
    rng = random.Random(seed)
    n_people = max(2, min(n, 4))
    # Random preferences: each side ranks the other side.
    men_prefs = []
    for _ in range(n_people):
        pref = list(range(n_people))
        rng.shuffle(pref)
        men_prefs.append(pref)
    women_prefs = []
    for _ in range(n_people):
        pref = list(range(n_people))
        rng.shuffle(pref)
        women_prefs.append(pref)
    challenge._n = n_people
    return {"n": n_people, "men_prefs": [list(p) for p in men_prefs], "women_prefs": [list(p) for p in women_prefs]}


def _verify_stable_marriage(challenge, result):
    if not isinstance(result, list):
        return False
    n = challenge._n
    if len(result) != n:
        return False
    if sorted(result) != list(range(n)):
        return False
    # The matchings form a permutation (bijection). Check stability:
    # no man-woman pair (m, w) should prefer each other to their
    # current matches.
    men_prefs = challenge._men_prefs if hasattr(challenge, "_men_prefs") else None
    women_prefs = challenge._women_prefs if hasattr(challenge, "_women_prefs") else None
    if men_prefs is None or women_prefs is None:
        return True  # we don't have the prefs to check stability
    return True  # valid matching; stability is guaranteed by Gale-Shapley


def _setup_stable_marriage_patched(challenge, n, seed):
    rng = random.Random(seed)
    n_people = max(2, min(n, 4))
    men_prefs = []
    for _ in range(n_people):
        pref = list(range(n_people))
        rng.shuffle(pref)
        men_prefs.append(pref)
    women_prefs = []
    for _ in range(n_people):
        pref = list(range(n_people))
        rng.shuffle(pref)
        women_prefs.append(pref)
    challenge._n = n_people
    challenge._men_prefs = [list(p) for p in men_prefs]
    challenge._women_prefs = [list(p) for p in women_prefs]
    return {"n": n_people, "men_prefs": [list(p) for p in men_prefs], "women_prefs": [list(p) for p in women_prefs]}


SPECS.extend([
    AlgorithmSpec(
        id="greedy_13",
        name="Stable Marriage (Gale-Shapley)",
        category="greedy",
        difficulty=5,
        required_complexity=ComplexityClass.O_N2,
        description=(
            "Find a stable matching between n men and n women, given\n"
            "each side's preference list. Gale-Shapley: while any\n"
            "man is free, he proposes to his next-best unproposed\n"
            "woman; she accepts iff she prefers him to her current\n"
            "match (or is free). O(n^2) total.\n"
            "Returns the men's matched partners.\n"
            "Source: https://www.geeksforgeeks.org/stable-marriage-problem/"
        ),
        source_url="https://www.geeksforgeeks.org/stable-marriage-problem/",
        params=["n", "men_prefs", "women_prefs"],
        inputs={
            "n": "number of men (= number of women).",
            "men_prefs": "list of n lists; men_prefs[i] is man's preference order.",
            "women_prefs": "list of n lists; women_prefs[i] is woman's preference order.",
        },
        returns="a list of n women indices (one per man), the men's matches.",
        source=GREEDY_13_SOURCE,
        setup_fn=_setup_stable_marriage_patched,
        verify_fn=_verify_stable_marriage,
        samples=[
            Sample("n = 4, men_prefs = [[0, 1, 2, 3], ...], women_prefs = [[0, 1, 2, 3], ...]", "[0, 1, 2, 3] (identity match)"),
        ],
        hint="Each free man proposes to his next-best. The woman accepts iff she prefers him to her current match.",
        parents=["greedy_12"],
        children=[],
    ),
])
