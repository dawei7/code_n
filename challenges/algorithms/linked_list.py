"""Linked List algorithms.

Three classic problems from GFG's linked-list catalog:

  01 Reverse Linked List   - in-place reversal of a singly linked list
  02 Detect Cycle          - Floyd's tortoise and hare
  03 Merge Two Sorted Lists - merge two sorted linked lists into one

Linked lists are passed as parallel lists ``values`` and
``next``, where ``next[i] = j`` means node i's next pointer
is node j, and ``-1`` means null. The setup builds a
deterministic list and stashes the expected result on the
challenge for the verifier to re-derive.
"""


from __future__ import annotations

import random
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


# === linked_list_01: Reverse Linked List ===

LL_01_SOURCE = '''\
"""Optimal solution for linked_list_01: Reverse Linked List.

Iterative in-place reversal. Walk the list with prev, cur,
nxt pointers; on each step, flip cur.next to prev, then
advance. O(n) time, O(1) space. Return the new parallel
``(values, next)`` representation plus the new head.
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return values, next, -1
    new_next = list(next)
    prev = -1
    cur = head
    new_head = -1
    while cur != -1:
        nxt_node = new_next[cur]
        new_next[cur] = prev
        new_head = cur
        prev = cur
        cur = nxt_node
    return list(values), new_next, new_head
'''


def _setup_ll_reverse(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    values = [rng.randint(0, 99) for _ in range(n)]
    nxt = [-1] * n
    for i in range(n - 1):
        nxt[i] = i + 1
    challenge._values = list(values)
    challenge._nxt = list(nxt)
    return {"values": list(values), "next": list(nxt), "head": 0, "n": n}


def _verify_ll_reverse(challenge, result: Any) -> bool:
    if not isinstance(result, tuple) or len(result) != 3:
        return False
    values, nxt, new_head = result
    if values != challenge._values:
        return False
    if new_head == -1 and len(values) > 0:
        return False
    # Walk from the new head, expecting to visit every node exactly once.
    cur = new_head
    visited = set()
    while cur != -1:
        if cur in visited:
            return False  # cycle
        visited.add(cur)
        cur = nxt[cur]
    return visited == set(range(len(values)))


# === linked_list_02: Detect Cycle ===

LL_02_SOURCE = '''\
"""Optimal solution for linked_list_02: Detect Cycle.

Floyd's tortoise and hare: walk with slow and fast pointers
that advance 1 and 2 steps at a time respectively. If they
ever meet, there's a cycle; if fast reaches the end, there
isn't. O(n) time, O(1) space.
"""


def solve(next, head, n):
    if n == 0 or head == -1:
        return False
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
        if slow == fast:
            return True
    return False
'''


def _setup_ll_cycle(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n = max(2, min(n, 16))
    nxt = [-1] * n
    for i in range(n - 1):
        nxt[i] = i + 1
    # Roughly half the time, create a cycle.
    if rng.random() < 0.5:
        cycle_to = rng.randint(0, n - 2)
        nxt[n - 1] = cycle_to
        challenge._has_cycle = True
    else:
        challenge._has_cycle = False
    challenge._nxt = list(nxt)
    return {"next": list(nxt), "head": 0, "n": n}


def _verify_ll_cycle(challenge, result: Any) -> bool:
    if not isinstance(result, bool):
        return False
    # Brute force: walk with a visited set.
    nxt = challenge._nxt
    cur = 0
    seen = set()
    while cur != -1 and cur not in seen:
        seen.add(cur)
        cur = nxt[cur]
    has_cycle = cur != -1
    return result == has_cycle


# === linked_list_03: Merge Two Sorted Lists ===

LL_03_SOURCE = '''\
"""Optimal solution for linked_list_03: Merge Two Sorted Lists.

Two-pointer walk. On each step, attach the smaller of the two
heads to the merged tail and advance that head. Append the
remaining tail of the non-empty list. The merged list is just
the sorted sequence in order, with next[i] = i+1 (or -1 for
the last node). Return (merged_values, merged_next).
"""


def solve(values1, next1, head1, values2, next2, head2, n1, n2):
    if n1 == 0:
        merged = list(values2)
    elif n2 == 0:
        merged = list(values1)
    else:
        merged = []
        i, j = head1, head2
        while i != -1 and j != -1:
            if values1[i] <= values2[j]:
                merged.append(values1[i])
                i = next1[i]
            else:
                merged.append(values2[j])
                j = next2[j]
        while i != -1:
            merged.append(values1[i])
            i = next1[i]
        while j != -1:
            merged.append(values2[j])
            j = next2[j]
    # Build the next pointers: simple 0 -> 1 -> 2 -> ... -> -1.
    n = len(merged)
    merged_nxt = [k + 1 for k in range(n - 1)] + [-1]
    return merged, merged_nxt
'''


def _setup_ll_merge(challenge, n: int, seed: Optional[int]) -> dict[str, Any]:
    rng = random.Random(seed)
    n1 = max(1, min(n // 2 + 1, 8))
    n2 = max(1, min(n - n1 + 1, 8))
    n1 = max(1, n // 2)
    n2 = max(1, n - n1)
    n1 = min(n1, 8)
    n2 = min(n2, 8)
    values1 = sorted(rng.randint(0, 99) for _ in range(n1))
    values2 = sorted(rng.randint(0, 99) for _ in range(n2))
    nxt1 = [-1] * n1
    for i in range(n1 - 1):
        nxt1[i] = i + 1
    nxt2 = [-1] * n2
    for i in range(n2 - 1):
        nxt2[i] = i + 1
    challenge._values1 = list(values1)
    challenge._nxt1 = list(nxt1)
    challenge._values2 = list(values2)
    challenge._nxt2 = list(nxt2)
    return {
        "values1": list(values1),
        "next1": list(nxt1),
        "head1": 0,
        "values2": list(values2),
        "next2": list(nxt2),
        "head2": 0,
        "n1": n1,
        "n2": n2,
    }


def _verify_ll_merge(challenge, result: Any) -> bool:
    if not isinstance(result, tuple) or len(result) != 2:
        return False
    values, nxt = result
    # The merged list should be a permutation of the union, sorted,
    # and the walk should visit every node exactly once.
    expected = sorted(challenge._values1 + challenge._values2)
    if values != expected:
        return False
    cur = 0
    seen = set()
    while cur != -1:
        if cur in seen:
            return False  # cycle
        seen.add(cur)
        cur = nxt[cur]
    return seen == set(range(len(values)))


# === Spec list ====================================================


SPECS: list[AlgorithmSpec] = [
    AlgorithmSpec(
        id="linked_list_01",
        name="Reverse Linked List",
        category="linked_list",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Reverse a singly linked list in place. The list is given as\n"
            "parallel ``values`` and ``next`` arrays (``next[i] = j`` means\n"
            "node i's next pointer is j; ``-1`` is null). Return\n"
            "(new_values, new_next, new_head) - the new pointers and\n"
            "the index of the new head (the original tail).\n"
            "Requirement: O(n) time, O(1) extra space.\n"
            "Source: https://www.geeksforgeeks.org/reverse-a-linked-list/"
        ),
        source_url="https://www.geeksforgeeks.org/reverse-a-linked-list/",
        params=["values", "next", "head", "n"],
        inputs={
            "values": "list of n values.",
            "next": "list of n next-pointers (parallel to values).",
            "head": "head node index (always 0 in the setup).",
            "n": "length of the list.",
        },
        returns="(new_values, new_next, new_head) such that the list is reversed.",
        source=LL_01_SOURCE,
        setup_fn=_setup_ll_reverse,
        verify_fn=_verify_ll_reverse,
        samples=[
            Sample("values = [1, 2, 3, 4], next = [1, 2, 3, -1], head = 0, n = 4", "(values, next=[-1,0,1,2], new_head=3)"),
            Sample("values = [7], next = [-1], head = 0, n = 1", "(values, next=[-1], new_head=0)"),
        ],
        hint="Iterate with prev, cur, nxt pointers. Flip cur.next to prev, then advance.",
        parents=["heap_04"],
        children=["linked_list_02"],
    ),
    AlgorithmSpec(
        id="linked_list_02",
        name="Detect Cycle in Linked List",
        category="linked_list",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return True iff the linked list has a cycle. Floyd's tortoise\n"
            "and hare: walk with slow (1 step) and fast (2 steps); they\n"
            "meet iff there's a cycle. The setup generates roughly half\n"
            "the lists with cycles.\n"
            "Source: https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/"
        ),
        source_url="https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/",
        params=["next", "head", "n"],
        inputs={
            "next": "list of n next-pointers.",
            "head": "head node index.",
            "n": "length of the list.",
        },
        returns="True iff the list contains a cycle.",
        source=LL_02_SOURCE,
        setup_fn=_setup_ll_cycle,
        verify_fn=_verify_ll_cycle,
        samples=[
            Sample("next = [1, 2, -1, 0], head = 0, n = 3", "True (1->2->0)"),
            Sample("next = [1, 2, 3, -1], head = 0, n = 4", "False"),
        ],
        hint="Floyd's: slow += 1, fast += 2. If they ever meet, there's a cycle.",
        parents=["linked_list_01"],
        children=["linked_list_03"],
    ),
    AlgorithmSpec(
        id="linked_list_03",
        name="Merge Two Sorted Linked Lists",
        category="linked_list",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Merge two sorted linked lists into a single sorted list.\n"
            "Two-pointer walk: at each step, attach the smaller head and\n"
            "advance that head. Append the remaining tail at the end.\n"
            "Return the merged (values, next) pair. O(n1 + n2) time.\n"
            "Source: https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/"
        ),
        source_url="https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/",
        params=["values1", "next1", "head1", "values2", "next2", "head2", "n1", "n2"],
        inputs={
            "values1": "list of n1 values (sorted ascending).",
            "next1": "list of n1 next-pointers (parallel to values1).",
            "head1": "head of list 1.",
            "values2": "list of n2 values (sorted ascending).",
            "next2": "list of n2 next-pointers (parallel to values2).",
            "head2": "head of list 2.",
            "n1": "length of list 1.",
            "n2": "length of list 2.",
        },
        returns="(merged_values, merged_next) - the merged sorted list.",
        source=LL_03_SOURCE,
        setup_fn=_setup_ll_merge,
        verify_fn=_verify_ll_merge,
        samples=[
            Sample("list1 = [1, 3, 5], list2 = [2, 4, 6]", "[1, 2, 3, 4, 5, 6]"),
            Sample("list1 = [1, 2], list2 = []", "[1, 2]"),
        ],
        hint="At each step, take the smaller of the two heads; append the rest at the end.",
        parents=["linked_list_02"],
        children=["linked_list_04"],
    ),
]


# === linked_list_04: Find Middle of Linked List ===

LL_04_SOURCE = '''\
"""Optimal solution for linked_list_04: Find Middle of Linked List.

Slow and fast pointers: slow moves 1 step, fast moves 2. When
fast hits the end, slow is at the middle. Return (new_values,
new_next, new_head) with the list unchanged structurally
(only the head is set to the middle index).
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return list(values), list(next), -1
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
    return list(values), list(next), slow
'''


def _setup_ll_middle(challenge, n, seed):
    rng = random.Random(seed)
    n = max(1, min(n, 16))
    values = [rng.randint(0, 99) for _ in range(n)]
    nxt = [-1] * n
    for i in range(n - 1):
        nxt[i] = i + 1
    challenge._values = list(values)
    challenge._nxt = list(nxt)
    return {"values": list(values), "next": list(nxt), "head": 0, "n": n}


def _verify_ll_middle(challenge, result):
    if not isinstance(result, tuple) or len(result) != 3:
        return False
    values, nxt, mid = result
    if values != challenge._values:
        return False
    if nxt != challenge._nxt:
        return False
    if mid == -1 and len(values) > 0:
        return False
    # Walk the list to find the length and the (n//2)-th index.
    seen = []
    cur = 0
    seen_set = set()
    while cur != -1:
        if cur in seen_set:
            return False
        seen_set.add(cur)
        seen.append(cur)
        cur = nxt[cur]
    n = len(seen)
    # For odd n, the middle is the (n//2)-th 0-indexed element.
    # For even n, slow/fast leaves slow at the (n//2)-th (0-indexed),
    # which is the FIRST of the two middle elements.
    expected_mid_idx = n // 2
    return mid == seen[expected_mid_idx]


# === linked_list_05: Reverse in Groups of K ===

LL_05_SOURCE = '''\
"""Optimal solution for linked_list_05: Reverse in Groups of K.

Walk the list in chunks of k; reverse each chunk. The trick is
to thread the previous chunk's tail to the current chunk's
new head. Return (new_values, new_next, new_head) - the new
pointers and the index of the new head.
"""


def solve(values, next, head, k, n):
    if n == 0 or head == -1 or k <= 1:
        return list(values), list(next), head
    new_next = list(next)
    prev_tail_new = -1
    cur = head
    new_head = -1
    while cur != -1:
        # Walk k nodes from cur.
        chunk = []
        c = cur
        for _ in range(k):
            if c == -1:
                break
            chunk.append(c)
            c = new_next[c]
        # If chunk is shorter than k, leave it as is.
        if len(chunk) < k:
            if prev_tail_new != -1:
                new_next[prev_tail_new] = chunk[0]
            break
        # Reverse the chunk; the first reversed node is the tail,
        # the last reversed node is the new head of the chunk.
        for i in range(len(chunk) - 1, 0, -1):
            new_next[chunk[i]] = chunk[i - 1]
        new_next[chunk[0]] = c  # tail points to the next chunk's first
        if prev_tail_new != -1:
            new_next[prev_tail_new] = chunk[-1]
        else:
            new_head = chunk[-1]
        prev_tail_new = chunk[0]
        cur = c
    if new_head == -1:
        new_head = head
    return list(values), new_next, new_head
'''


def _setup_ll_reverse_k(challenge, n, seed):
    rng = random.Random(seed)
    n = max(2, min(n, 16))
    k = max(1, min(3, n // 2))
    values = [rng.randint(0, 99) for _ in range(n)]
    nxt = [-1] * n
    for i in range(n - 1):
        nxt[i] = i + 1
    challenge._values = list(values)
    challenge._nxt = list(nxt)
    challenge._k = k
    return {"values": list(values), "next": list(nxt), "head": 0, "k": k, "n": n}


def _verify_ll_reverse_k(challenge, result):
    if not isinstance(result, tuple) or len(result) != 3:
        return False
    values, nxt, new_head = result
    if values != challenge._values:
        return False
    if new_head == -1 and len(values) > 0:
        return False
    # Walk from new_head; expect to visit all nodes in the k-group-reversed order.
    cur = new_head
    visited = set()
    while cur != -1:
        if cur in visited:
            return False
        visited.add(cur)
        cur = nxt[cur]
    if visited != set(range(len(values))):
        return False
    # Re-derive the expected walk: take k at a time and reverse.
    k = challenge._k
    out = []
    for i in range(0, len(values), k):
        chunk = list(range(i, min(i + k, len(values))))
        chunk.reverse()
        out.extend(chunk)
    return visited == set(out) and new_head == out[0] if out else True


SPECS.extend([
    AlgorithmSpec(
        id="linked_list_04",
        name="Find Middle of Linked List",
        category="linked_list",
        difficulty=2,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Return the index of the middle node of a singly linked\n"
            "list. Slow and fast pointers: slow moves 1 step, fast\n"
            "moves 2. When fast hits the end, slow is at the middle.\n"
            "For even length, the middle is the (n/2)-th node.\n"
            "Source: https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/"
        ),
        source_url="https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/",
        params=["values", "next", "head", "n"],
        inputs={
            "values": "list of n values.",
            "next": "list of n next-pointers (parallel to values).",
            "head": "head node index (always 0 in the setup).",
            "n": "length of the list.",
        },
        returns="(new_values, new_next, mid_index) - the middle index.",
        source=LL_04_SOURCE,
        setup_fn=_setup_ll_middle,
        verify_fn=_verify_ll_middle,
        samples=[
            Sample("values = [1, 2, 3, 4, 5], next = [1, 2, 3, 4, -1], head = 0, n = 5", "mid = 2 (value 3)"),
            Sample("values = [1, 2, 3, 4], next = [1, 2, 3, -1], head = 0, n = 4", "mid = 2 (value 3, the second half's first)"),
        ],
        hint="Slow + 1, fast + 2. When fast hits -1, slow is at the middle.",
        parents=["linked_list_03"],
        children=["linked_list_05"],
    ),
    AlgorithmSpec(
        id="linked_list_05",
        name="Reverse in Groups of K",
        category="linked_list",
        difficulty=5,
        required_complexity=ComplexityClass.O_N,
        description=(
            "Reverse the linked list in chunks of k nodes. The first\n"
            "chunk's tail becomes the new list's head; the tail of\n"
            "each chunk points to the next chunk's (reversed) head.\n"
            "If the last chunk has fewer than k nodes, leave it alone.\n"
            "Source: https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/"
        ),
        source_url="https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/",
        params=["values", "next", "head", "k", "n"],
        inputs={
            "values": "list of n values.",
            "next": "list of n next-pointers (parallel to values).",
            "head": "head node index.",
            "k": "group size (1..3 in the setup).",
            "n": "length of the list.",
        },
        returns="(new_values, new_next, new_head) - the k-group-reversed list.",
        source=LL_05_SOURCE,
        setup_fn=_setup_ll_reverse_k,
        verify_fn=_verify_ll_reverse_k,
        samples=[
            Sample("values = [1, 2, 3, 4, 5], next = [1, 2, 3, 4, -1], head = 0, k = 2, n = 5", "list = [2, 1, 4, 3, 5]; new_head = 1"),
        ],
        hint="Walk k at a time. Reverse each chunk. Thread prev tail -> current head. Last partial chunk is left alone.",
        parents=["linked_list_04"],
        children=[],
    ),
])
