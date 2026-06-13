"""Randomized algorithms.

Two classic problems from GFG's randomized-algorithms catalog:

  01 Randomized Quicksort - partition with a random pivot; O(n log n) expected
  02 Reservoir Sampling     - pick k items uniformly from a stream

The setup uses random.Random(seed) for determinism, but the
algorithms themselves use random.randint/random.choice to pick
the random pivot (or skip index). Expected O(n log n) on
average; the tests don't measure the exact operation count.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === randomized_01: Randomized Quicksort ===

RAND_01_SOURCE = '''\
"""Optimal solution for randomized_01: Randomized Quicksort.

Quicksort with a random pivot. Each partition picks a random
index in [lo, hi], swaps it to the end, then Lomuto-partitions.
Expected O(n log n); with adversarial input, expected
O(n log n) - the random pivot breaks the bad case.
"""


def solve(data, n):
    import random
    work = list(data)

    def partition(lo, hi):
        pivot_idx = random.randint(lo, hi)
        work[pivot_idx], work[hi] = work[hi], work[pivot_idx]
        pivot = work[hi]
        i = lo
        for j in range(lo, hi):
            if work[j] <= pivot:
                work[i], work[j] = work[j], work[i]
                i += 1
        work[i], work[hi] = work[hi], work[i]
        return i

    def sort(lo, hi):
        if lo < hi:
            p = partition(lo, hi)
            sort(lo, p - 1)
            sort(p + 1, hi)

    if n > 1:
        sort(0, n - 1)
    return work
'''


def _setup_rand_quicksort(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    data = [rng.randint(0, 99) for _ in range(n)]
    challenge._data = list(data)
    return {"data": list(data), "n": n}


def _verify_rand_quicksort(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    return sorted(result) == sorted(challenge._data) and result == sorted(result)


# === randomized_02: Reservoir Sampling ===

RAND_02_SOURCE = '''\
"""Optimal solution for randomized_02: Reservoir Sampling.

Pick k items uniformly at random from a stream of unknown
length. Standard algorithm: fill the reservoir with the first
k items; for each subsequent item i (i >= k), replace a
random reservoir index with probability k / (i + 1).
"""


def solve(stream, k, n):
    import random
    if k <= 0 or n == 0:
        return []
    reservoir = list(stream[:k])
    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir
'''


def _setup_reservoir(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 20))
    stream = [rng.randint(0, 99) for _ in range(n)]
    k = max(1, min(n // 2, 5))
    challenge._stream = list(stream)
    challenge._k = k
    challenge._seed = seed
    return {"stream": list(stream), "k": k, "n": n}


def _verify_reservoir(challenge, result: Any) -> bool:
    if not isinstance(result, list):
        return False
    if len(result) != min(challenge._k, len(challenge._stream)):
        return False
    # Each element of result must be an element of the stream.
    stream_set = set(challenge._stream)
    for v in result:
        if v not in stream_set:
            return False
    return True


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="randomized_01",
        name="Randomized Quicksort",
        category="randomized",
        difficulty=4,
        required_complexity=ComplexityClass.O_N_LOG_N,
        description=(
            "Quicksort with a random pivot. Each partition picks a\n"
            "random index in [lo, hi] and uses that as the pivot; this\n"
            "breaks the pathological O(n^2) cases of deterministic\n"
            "quicksort on sorted / reverse-sorted / all-equal input.\n"
            "Expected O(n log n) regardless of input order.\n"
            "Source: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/"
        ),
        source_url="https://www.geeksforgeeks.org/quicksort-using-random-pivoting/",
        params=["data", "n"],
        inputs={
            "data": "list of n random integers.",
            "n": "length of data.",
        },
        returns="the sorted list.",
        source=RAND_01_SOURCE,
        setup_fn=_setup_rand_quicksort,
        verify_fn=_verify_rand_quicksort,
        samples=[
            Sample("data = [10, 7, 8, 9, 1, 5], n = 6", "[1, 5, 7, 8, 9, 10]"),
            Sample("data = [1, 2, 3, 4, 5], n = 5", "[1, 2, 3, 4, 5]"),
        ],
        hint="Random pivot. Lomuto partition. Recurse on both halves.",
        parents=["dc_03"],
        children=["randomized_02"],
    ),
    AlgorithmSpec(
        id="randomized_02",
        name="Reservoir Sampling",
        category="randomized",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Pick k items uniformly at random from a stream of unknown\n"
            "length. Fill the reservoir with the first k items; for each\n"
            "subsequent item i, replace a random reservoir slot with\n"
            "probability k / (i + 1). O(n) time, O(k) space.\n"
            "Source: https://www.geeksforgeeks.org/reservoir-sampling/"
        ),
        source_url="https://www.geeksforgeeks.org/reservoir-sampling/",
        params=["stream", "k", "n"],
        inputs={
            "stream": "list of n integers (the stream).",
            "k": "reservoir size (>= 1).",
            "n": "stream length.",
        },
        returns="a list of k items (the reservoir) sampled uniformly from the stream.",
        source=RAND_02_SOURCE,
        setup_fn=_setup_reservoir,
        verify_fn=_verify_reservoir,
        samples=[
            Sample("stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3, n = 10", "k items, each a stream element"),
        ],
        hint="Reservoir = first k. For item i (i >= k), replace reservoir[randint(0, i)] with prob k/(i+1).",
        parents=["randomized_01"],
        children=[],
    ),
]
