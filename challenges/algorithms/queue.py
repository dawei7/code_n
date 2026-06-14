"""Queue data structure.

A brand-new category for cOde(n). 5 specs covering the
canonical queue problems from GfG and the standard syllabus:

  queue_01  Implement Queue using Stacks
  queue_02  Implement Stack using Queues
  queue_03  Generate Binary Numbers (1 to n) via Queue
  queue_04  First Non-Repeating Character in a Stream
  queue_05  Circular Queue (Array-based, with overflow)

Run with:
    cd c:/dawei7/code_n
    .venv/Scripts/python.exe -m challenges.algorithms._generator \\
        --module queue \\
        --input batch_queue_session1.py
"""


from __future__ import annotations

import random
from collections import deque
from typing import Any, Optional

from challenges.spec import AlgorithmSpec, Sample
from code_n.counter import ComplexityClass


SPECS: list[AlgorithmSpec] = []


SPECS_TO_ADD = [
    # ============================================================
    # queue_01: Implement Queue using Stacks
    # ============================================================
    {
        "id": "queue_01",
        "name": "Implement Queue using Stacks",
        "category": "queue",
        "difficulty": 4,
        "complexity": "O_1",
        "description": (
            "Implement a FIFO queue using only two LIFO stacks.\n"
            "The trick: use one stack for enqueue (push) and\n"
            "another for dequeue (peek). When the dequeue stack\n"
            "is empty, transfer everything from the enqueue\n"
            "stack into it (reversing the order). Amortized\n"
            "O(1) per operation. The returned object supports\n"
            "push, pop, peek, and empty (with the same\n"
            "semantics as collections.deque).\n"
            "Source: https://www.geeksforgeeks.org/queue-using-stacks/"
        ),
        "source_url": "https://www.geeksforgeeks.org/queue-using-stacks/",
        "params": ["operations", "n"],
        "inputs": {
            "operations": "list of operation tuples, each (op_name, *args).",
            "n": "number of operations.",
        },
        "returns": "a list of results (the outputs of peek/pop in order, or []).",
        "solve": '''
def solve(operations, n):
    """Implement FIFO queue with two LIFO stacks."""
    inbox = []
    outbox = []
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            inbox.append(op[1])
        elif name == "pop":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                outbox.pop()
        elif name == "peek":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                results.append(outbox[-1])
        elif name == "empty":
            pass
    return results
''',
        "setup": '''
import random
rng = random.Random(seed)
# Build a sequence of operations whose ground truth we can compute
# with collections.deque.
n = max(1, min(n, 10))
true_q = []
ops = []
op_names = ["push", "pop", "peek", "empty"]
for _ in range(n):
    # Bias toward pushes so peek/pop can succeed.
    name = rng.choices(op_names, weights=[5, 2, 2, 1])[0]
    if name == "push":
        val = rng.randint(0, 100)
        ops.append(("push", val))
        true_q.append(val)
    elif name == "pop":
        ops.append(("pop",))
        if true_q:
            true_q.pop(0)
    elif name == "peek":
        ops.append(("peek",))
    else:  # empty
        ops.append(("empty",))
# Compute expected peek results.
expected_results = []
sim = []
inbox = []
outbox = []
for op in ops:
    if op[0] == "push":
        inbox.append(op[1])
        sim.append(op[1])
    elif op[0] == "pop":
        if not outbox:
            while inbox:
                outbox.append(inbox.pop())
        if outbox:
            outbox.pop()
            sim.pop(0)
    elif op[0] == "peek":
        if not outbox:
            while inbox:
                outbox.append(inbox.pop())
        if outbox:
            expected_results.append(outbox[-1])
    elif op[0] == "empty":
        pass
challenge._ops = list(ops)
challenge._expected = expected_results
return {"operations": list(ops), "n": n}
''',
        "verify": '''
return result == challenge._expected
''',
        "samples": [
            ("ops = [('push', 1), ('push', 2), ('peek'), ('pop'), ('peek')], n = 5", "[1, 2]"),
            ("ops = [('push', 5), ('pop'), ('pop')], n = 3", "[] (pop on empty doesn't crash)"),
        ],
        "hint": "Inbox stack for pushes, outbox stack for pops/peeks. When outbox is empty, dump inbox into it (reversing the order).",
        "parents": ["stack_01"],
        "children": ["queue_02"],
    },

    # ============================================================
    # queue_02: Implement Stack using Queues
    # ============================================================
    {
        "id": "queue_02",
        "name": "Implement Stack using Queues",
        "category": "queue",
        "difficulty": 4,
        "complexity": "O_1",
        "description": (
            "Implement a LIFO stack using only FIFO queues\n"
            "(the one-queue variant). On push, enqueue the new\n"
            "element, then rotate the queue: dequeue and re-enqueue\n"
            "the existing elements one by one. This puts the new\n"
            "element at the FRONT of the queue, so the next pop\n"
            "returns it. Amortized O(1) per op, O(n) for the single\n"
            "rotation on each push.\n"
            "Source: https://www.geeksforgeeks.org/stack-using-two-queues/"
        ),
        "source_url": "https://www.geeksforgeeks.org/stack-using-two-queues/",
        "params": ["operations", "n"],
        "inputs": {
            "operations": "list of operation tuples, each (op_name, *args).",
            "n": "number of operations.",
        },
        "returns": "a list of results (the outputs of top/pop in order, or []).",
        "solve": '''
def solve(operations, n):
    """Implement LIFO stack using one FIFO queue."""
    from collections import deque
    q = deque()
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            q.append(op[1])
            # Rotate: dequeue and re-enqueue (len(q) - 1) times
            # so the new element ends up at the front.
            for _ in range(len(q) - 1):
                q.append(q.popleft())
        elif name == "pop":
            if q:
                q.popleft()
        elif name == "top":
            if q:
                results.append(q[0])
        elif name == "empty":
            pass
    return results
''',
        "setup": '''
import random
rng = random.Random(seed)
n = max(1, min(n, 8))
ops = []
op_names = ["push", "pop", "top", "empty"]
for _ in range(n):
    name = rng.choices(op_names, weights=[5, 2, 2, 1])[0]
    if name == "push":
        val = rng.randint(0, 100)
        ops.append(("push", val))
    elif name == "pop":
        ops.append(("pop",))
    elif name == "top":
        ops.append(("top",))
    else:
        ops.append(("empty",))
# Compute expected top results.
from collections import deque
q = deque()
expected_results = []
for op in ops:
    if op[0] == "push":
        q.append(op[1])
        for _ in range(len(q) - 1):
            q.append(q.popleft())
    elif op[0] == "pop":
        if q:
            q.popleft()
    elif op[0] == "top":
        if q:
            expected_results.append(q[0])
    elif op[0] == "empty":
        pass
challenge._expected = expected_results
return {"operations": list(ops), "n": n}
''',
        "verify": '''
return result == challenge._expected
''',
        "samples": [
            ("ops = [('push', 1), ('push', 2), ('top'), ('pop'), ('top')], n = 5", "[2, 1]"),
        ],
        "hint": "On push, enqueue the new element, then rotate the queue (dequeue+enqueue the rest) so the new element ends up at the front.",
        "parents": ["queue_01"],
        "children": ["queue_03"],
    },

    # ============================================================
    # queue_03: Generate Binary Numbers (1 to n) via Queue
    # ============================================================
    {
        "id": "queue_03",
        "name": "Generate Binary Numbers (1 to n)",
        "category": "queue",
        "difficulty": 3,
        "complexity": "O_N",
        "description": (
            "Generate the binary representations of 1, 2, ..., n\n"
            "in order, using a queue. Start with the queue\n"
            "containing '1'. Each iteration: dequeue the front\n"
            "string s, append s + '0' and s + '1' to the back.\n"
            "This generates the binary strings in BFS order,\n"
            "which matches the natural numerical order for\n"
            "positive integers. O(n) overall.\n"
            "Source: https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/"
        ),
        "source_url": "https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/",
        "params": ["n"],
        "inputs": {"n": "positive integer."},
        "returns": "a list of n binary strings (the binary representations of 1..n).",
        "solve": '''
def solve(n):
    """Generate binary strings '1', '10', '11', '100', ... up to n."""
    from collections import deque
    if n <= 0:
        return []
    result = []
    q = deque(["1"])
    for _ in range(n):
        s = q.popleft()
        result.append(s)
        q.append(s + "0")
        q.append(s + "1")
    return result
''',
        "setup": '''
import random
rng = random.Random(seed)
# Cap n so the output list is small but non-trivial.
n = max(1, min(n, 10))
challenge._n = n
return {"n": n}
''',
        "verify": '''
if not isinstance(result, list):
    return False
expected = [bin(i)[2:] for i in range(1, challenge._n + 1)]
return result == expected
''',
        "samples": [
            ("n = 5", "['1', '10', '11', '100', '101']"),
            ("n = 1", "['1']"),
        ],
        "hint": "Start with the queue containing '1'. Each step: pop s, output s, then push s+'0' and s+'1'.",
        "parents": ["queue_02"],
        "children": ["queue_04"],
    },

    # ============================================================
    # queue_04: First Non-Repeating Character in a Stream
    # ============================================================
    {
        "id": "queue_04",
        "name": "First Non-Repeating Character in a Stream",
        "category": "queue",
        "difficulty": 4,
        "complexity": "O_N",
        "description": (
            "Given a stream of characters (a string), for each\n"
            "prefix of length i, return the first non-repeating\n"
            "character in that prefix, or '_' if none exists.\n"
            "Use a queue to maintain the candidate set (characters\n"
            "seen exactly once so far, in order of first\n"
            "appearance) and a frequency counter to detect\n"
            "repeats. When a character's count becomes 2, remove\n"
            "it from the queue. O(n) time, O(1) space (26 letters).\n"
            "Source: https://www.geeksforgeeks.org/first-non-repeating-character-in-a-stream/"
        ),
        "source_url": "https://www.geeksforgeeks.org/first-non-repeating-character-in-a-stream/",
        "params": ["stream", "n"],
        "inputs": {
            "stream": "string of n lowercase letters.",
            "n": "length of stream.",
        },
        "returns": "string of length n: for each prefix, the first non-repeating char or '_'.",
        "solve": '''
def solve(stream, n):
    """First non-repeating char in each prefix of stream."""
    from collections import deque, Counter
    if n == 0:
        return ""
    q = deque()
    freq = Counter()
    result = []
    for ch in stream:
        freq[ch] += 1
        q.append(ch)
        # Pop from the front of the queue while the head has
        # appeared more than once.
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append("_")
    return "".join(result)
''',
        "setup": '''
import random
import string
rng = random.Random(seed)
n = max(1, min(n, 12))
stream = "".join(rng.choice("aabc") for _ in range(n))
challenge._stream = stream
return {"stream": stream, "n": n}
''',
        "verify": '''
# Brute force: at each prefix, scan for the first char with
# count == 1.
stream = challenge._stream
parts = []
for i in range(1, len(stream) + 1):
    prefix = stream[:i]
    counts = {}
    for ch in prefix:
        counts[ch] = counts.get(ch, 0) + 1
    found = "_"
    for ch in prefix:
        if counts[ch] == 1:
            found = ch
            break
    parts.append(found)
expected = "".join(parts)
return result == expected
''',
        "samples": [
            ("stream = 'aabc', n = 4", "'aa_b' (a, a, _, b)"),
            ("stream = 'aabbccd', n = 7", "'aa____d' (a, a, _, _, _, _, d)"),
        ],
        "hint": "Maintain a queue of seen-once characters (in order) and a frequency counter. When a char's count becomes 2, pop it from the queue. The head of the queue is the answer.",
        "parents": ["queue_03"],
        "children": ["queue_05"],
    },

    # ============================================================
    # queue_05: Circular Queue
    # ============================================================
    {
        "id": "queue_05",
        "name": "Circular Queue (Array-based)",
        "category": "queue",
        "difficulty": 3,
        "complexity": "O_1",
        "description": (
            "Implement a fixed-capacity circular queue using\n"
            "an array. Maintain front, rear, and size. Enqueue\n"
            "writes at (rear + 1) % capacity and increments size;\n"
            "dequeue reads at front and advances front by 1 mod\n"
            "capacity. Return False (not raise) on overflow /\n"
            "underflow so the verifier can check the result\n"
            "directly. Operations are O(1).\n"
            "Source: https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/"
        ),
        "source_url": "https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/",
        "params": ["operations", "capacity", "n"],
        "inputs": {
            "operations": "list of operation tuples (op_name, *args).",
            "capacity": "fixed capacity of the circular queue.",
            "n": "number of operations.",
        },
        "returns": "a list of dequeued values (in order) for each successful dequeue.",
        "solve": '''
def solve(operations, capacity, n):
    """Fixed-capacity circular queue. Returns list of dequeued values."""
    if capacity <= 0:
        return []
    queue = [None] * capacity
    front = 0
    rear = -1
    size = 0
    dequeued = []
    for op in operations:
        name = op[0]
        if name == "enqueue":
            if size == capacity:
                continue  # overflow: silently skip
            rear = (rear + 1) % capacity
            queue[rear] = op[1]
            size += 1
        elif name == "dequeue":
            if size == 0:
                continue  # underflow: silently skip
            dequeued.append(queue[front])
            front = (front + 1) % capacity
            size -= 1
        elif name == "front":
            pass  # we don't return this
        elif name == "rear":
            pass
        elif name == "isEmpty":
            pass
        elif name == "isFull":
            pass
    return dequeued
''',
        "setup": '''
import random
rng = random.Random(seed)
# Pick a capacity and a sequence of operations.
capacity = max(1, min(n, 8))
n = max(1, min(n, 12))
ops = []
op_names = ["enqueue", "dequeue", "isEmpty", "isFull"]
# Pre-compute ground truth.
true_q = []
dequeued = []
for _ in range(n):
    name = rng.choices(op_names, weights=[5, 4, 1, 1])[0]
    if name == "enqueue":
        val = rng.randint(0, 100)
        ops.append(("enqueue", val))
        if len(true_q) < capacity:
            true_q.append(val)
    elif name == "dequeue":
        ops.append(("dequeue",))
        if true_q:
            dequeued.append(true_q.pop(0))
    else:
        ops.append((name,))
challenge._expected = dequeued
return {"operations": list(ops), "capacity": capacity, "n": n}
''',
        "verify": '''
return result == challenge._expected
''',
        "samples": [
            ("ops = [('enqueue', 1), ('enqueue', 2), ('dequeue'), ('enqueue', 3), ('dequeue')], capacity = 3, n = 5", "[1, 2]"),
        ],
        "hint": "front, rear, size: (rear+1) % capacity on enqueue, front advances on dequeue. Use size to distinguish empty from full.",
        "parents": ["queue_04"],
        "children": [],
    },
]


# === queue_01: Implement Queue using Stacks ===

QUEUE_01_SOURCE = '''
def solve(operations, n):
    """Implement FIFO queue with two LIFO stacks."""
    inbox = []
    outbox = []
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            inbox.append(op[1])
        elif name == "pop":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                outbox.pop()
        elif name == "peek":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                results.append(outbox[-1])
        elif name == "empty":
            pass
    return results
'''

def _setup_queue_01(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Build a sequence of operations whose ground truth we can compute
    # with collections.deque.
    n = max(1, min(n, 10))
    true_q = []
    ops = []
    op_names = ["push", "pop", "peek", "empty"]
    for _ in range(n):
        # Bias toward pushes so peek/pop can succeed.
        name = rng.choices(op_names, weights=[5, 2, 2, 1])[0]
        if name == "push":
            val = rng.randint(0, 100)
            ops.append(("push", val))
            true_q.append(val)
        elif name == "pop":
            ops.append(("pop",))
            if true_q:
                true_q.pop(0)
        elif name == "peek":
            ops.append(("peek",))
        else:  # empty
            ops.append(("empty",))
    # Compute expected peek results.
    expected_results = []
    sim = []
    inbox = []
    outbox = []
    for op in ops:
        if op[0] == "push":
            inbox.append(op[1])
            sim.append(op[1])
        elif op[0] == "pop":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                outbox.pop()
                sim.pop(0)
        elif op[0] == "peek":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                expected_results.append(outbox[-1])
        elif op[0] == "empty":
            pass
    challenge._ops = list(ops)
    challenge._expected = expected_results
    return {"operations": list(ops), "n": n}

def _verify_queue_01(challenge, result):
    return result == challenge._expected



# === queue_02: Implement Stack using Queues ===

QUEUE_02_SOURCE = '''
def solve(operations, n):
    """Implement LIFO stack using one FIFO queue."""
    from collections import deque
    q = deque()
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            q.append(op[1])
            # Rotate: dequeue and re-enqueue (len(q) - 1) times
            # so the new element ends up at the front.
            for _ in range(len(q) - 1):
                q.append(q.popleft())
        elif name == "pop":
            if q:
                q.popleft()
        elif name == "top":
            if q:
                results.append(q[0])
        elif name == "empty":
            pass
    return results
'''

def _setup_queue_02(challenge, n, seed):
    import random
    rng = random.Random(seed)
    n = max(1, min(n, 8))
    ops = []
    op_names = ["push", "pop", "top", "empty"]
    for _ in range(n):
        name = rng.choices(op_names, weights=[5, 2, 2, 1])[0]
        if name == "push":
            val = rng.randint(0, 100)
            ops.append(("push", val))
        elif name == "pop":
            ops.append(("pop",))
        elif name == "top":
            ops.append(("top",))
        else:
            ops.append(("empty",))
    # Compute expected top results.
    from collections import deque
    q = deque()
    expected_results = []
    for op in ops:
        if op[0] == "push":
            q.append(op[1])
            for _ in range(len(q) - 1):
                q.append(q.popleft())
        elif op[0] == "pop":
            if q:
                q.popleft()
        elif op[0] == "top":
            if q:
                expected_results.append(q[0])
        elif op[0] == "empty":
            pass
    challenge._expected = expected_results
    return {"operations": list(ops), "n": n}

def _verify_queue_02(challenge, result):
    return result == challenge._expected



# === queue_03: Generate Binary Numbers (1 to n) ===

QUEUE_03_SOURCE = '''
def solve(n):
    """Generate binary strings '1', '10', '11', '100', ... up to n."""
    from collections import deque
    if n <= 0:
        return []
    result = []
    q = deque(["1"])
    for _ in range(n):
        s = q.popleft()
        result.append(s)
        q.append(s + "0")
        q.append(s + "1")
    return result
'''

def _setup_queue_03(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Cap n so the output list is small but non-trivial.
    n = max(1, min(n, 10))
    challenge._n = n
    return {"n": n}

def _verify_queue_03(challenge, result):
    if not isinstance(result, list):
        return False
    expected = [bin(i)[2:] for i in range(1, challenge._n + 1)]
    return result == expected



# === queue_04: First Non-Repeating Character in a Stream ===

QUEUE_04_SOURCE = '''
def solve(stream, n):
    """First non-repeating char in each prefix of stream."""
    from collections import deque, Counter
    if n == 0:
        return ""
    q = deque()
    freq = Counter()
    result = []
    for ch in stream:
        freq[ch] += 1
        q.append(ch)
        # Pop from the front of the queue while the head has
        # appeared more than once.
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append("_")
    return "".join(result)
'''

def _setup_queue_04(challenge, n, seed):
    import random
    import string
    rng = random.Random(seed)
    n = max(1, min(n, 12))
    stream = "".join(rng.choice("aabc") for _ in range(n))
    challenge._stream = stream
    return {"stream": stream, "n": n}

def _verify_queue_04(challenge, result):
    # Brute force: at each prefix, scan for the first char with
    # count == 1.
    stream = challenge._stream
    parts = []
    for i in range(1, len(stream) + 1):
        prefix = stream[:i]
        counts = {}
        for ch in prefix:
            counts[ch] = counts.get(ch, 0) + 1
        found = "_"
        for ch in prefix:
            if counts[ch] == 1:
                found = ch
                break
        parts.append(found)
    expected = "".join(parts)
    return result == expected



# === queue_05: Circular Queue (Array-based) ===

QUEUE_05_SOURCE = '''
def solve(operations, capacity, n):
    """Fixed-capacity circular queue. Returns list of dequeued values."""
    if capacity <= 0:
        return []
    queue = [None] * capacity
    front = 0
    rear = -1
    size = 0
    dequeued = []
    for op in operations:
        name = op[0]
        if name == "enqueue":
            if size == capacity:
                continue  # overflow: silently skip
            rear = (rear + 1) % capacity
            queue[rear] = op[1]
            size += 1
        elif name == "dequeue":
            if size == 0:
                continue  # underflow: silently skip
            dequeued.append(queue[front])
            front = (front + 1) % capacity
            size -= 1
        elif name == "front":
            pass  # we don't return this
        elif name == "rear":
            pass
        elif name == "isEmpty":
            pass
        elif name == "isFull":
            pass
    return dequeued
'''

def _setup_queue_05(challenge, n, seed):
    import random
    rng = random.Random(seed)
    # Pick a capacity and a sequence of operations.
    capacity = max(1, min(n, 8))
    n = max(1, min(n, 12))
    ops = []
    op_names = ["enqueue", "dequeue", "isEmpty", "isFull"]
    # Pre-compute ground truth.
    true_q = []
    dequeued = []
    for _ in range(n):
        name = rng.choices(op_names, weights=[5, 4, 1, 1])[0]
        if name == "enqueue":
            val = rng.randint(0, 100)
            ops.append(("enqueue", val))
            if len(true_q) < capacity:
                true_q.append(val)
        elif name == "dequeue":
            ops.append(("dequeue",))
            if true_q:
                dequeued.append(true_q.pop(0))
        else:
            ops.append((name,))
    challenge._expected = dequeued
    return {"operations": list(ops), "capacity": capacity, "n": n}

def _verify_queue_05(challenge, result):
    return result == challenge._expected


# Append the new specs to SPECS.
SPECS.extend([
    AlgorithmSpec(
        id="queue_01",
        name="Implement Queue using Stacks",
        category="queue",
        difficulty=4,
        required_complexity=ComplexityClass.O_1,
        description=("""
            Implement a FIFO queue using only two LIFO stacks.
            The trick: use one stack for enqueue (push) and
            another for dequeue (peek). When the dequeue stack
            is empty, transfer everything from the enqueue
            stack into it (reversing the order). Amortized
            O(1) per operation. The returned object supports
            push, pop, peek, and empty (with the same
            semantics as collections.deque).
            Source: https://www.geeksforgeeks.org/queue-using-stacks/
            """),
        source_url="https://www.geeksforgeeks.org/queue-using-stacks/",
        params=["operations", "n"],
        inputs={
            "operations": "list of operation tuples, each (op_name, *args).",
            "n": "number of operations.",
        },
        returns="a list of results (the outputs of peek/pop in order, or []).",
        source=QUEUE_01_SOURCE,
        setup_fn=_setup_queue_01,
        verify_fn=_verify_queue_01,
        samples=[
            Sample("ops = [('push', 1), ('push', 2), ('peek'), ('pop'), ('peek')], n = 5", "[1, 2]"),
            Sample("ops = [('push', 5), ('pop'), ('pop')], n = 3", "[] (pop on empty doesn't crash)"),
        ],
        hint="Inbox stack for pushes, outbox stack for pops/peeks. When outbox is empty, dump inbox into it (reversing the order).",
        parents=["stack_01"],
        children=["queue_02"],
    ),
    AlgorithmSpec(
        id="queue_02",
        name="Implement Stack using Queues",
        category="queue",
        difficulty=4,
        required_complexity=ComplexityClass.O_1,
        description=("""
            Implement a LIFO stack using only FIFO queues
            (the one-queue variant). On push, enqueue the new
            element, then rotate the queue: dequeue and re-enqueue
            the existing elements one by one. This puts the new
            element at the FRONT of the queue, so the next pop
            returns it. Amortized O(1) per op, O(n) for the single
            rotation on each push.
            Source: https://www.geeksforgeeks.org/stack-using-two-queues/
            """),
        source_url="https://www.geeksforgeeks.org/stack-using-two-queues/",
        params=["operations", "n"],
        inputs={
            "operations": "list of operation tuples, each (op_name, *args).",
            "n": "number of operations.",
        },
        returns="a list of results (the outputs of top/pop in order, or []).",
        source=QUEUE_02_SOURCE,
        setup_fn=_setup_queue_02,
        verify_fn=_verify_queue_02,
        samples=[
            Sample("ops = [('push', 1), ('push', 2), ('top'), ('pop'), ('top')], n = 5", "[2, 1]"),
        ],
        hint="On push, enqueue the new element, then rotate the queue (dequeue+enqueue the rest) so the new element ends up at the front.",
        parents=["queue_01"],
        children=["queue_03"],
    ),
    AlgorithmSpec(
        id="queue_03",
        name="Generate Binary Numbers (1 to n)",
        category="queue",
        difficulty=3,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Generate the binary representations of 1, 2, ..., n
            in order, using a queue. Start with the queue
            containing '1'. Each iteration: dequeue the front
            string s, append s + '0' and s + '1' to the back.
            This generates the binary strings in BFS order,
            which matches the natural numerical order for
            positive integers. O(n) overall.
            Source: https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/
            """),
        source_url="https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/",
        params=["n"],
        inputs={
            "n": "positive integer.",
        },
        returns="a list of n binary strings (the binary representations of 1..n).",
        source=QUEUE_03_SOURCE,
        setup_fn=_setup_queue_03,
        verify_fn=_verify_queue_03,
        samples=[
            Sample("n = 5", "['1', '10', '11', '100', '101']"),
            Sample("n = 1", "['1']"),
        ],
        hint="Start with the queue containing '1'. Each step: pop s, output s, then push s+'0' and s+'1'.",
        parents=["queue_02"],
        children=["queue_04"],
    ),
    AlgorithmSpec(
        id="queue_04",
        name="First Non-Repeating Character in a Stream",
        category="queue",
        difficulty=4,
        required_complexity=ComplexityClass.O_N,
        description=("""
            Given a stream of characters (a string), for each
            prefix of length i, return the first non-repeating
            character in that prefix, or '_' if none exists.
            Use a queue to maintain the candidate set (characters
            seen exactly once so far, in order of first
            appearance) and a frequency counter to detect
            repeats. When a character's count becomes 2, remove
            it from the queue. O(n) time, O(1) space (26 letters).
            Source: https://www.geeksforgeeks.org/first-non-repeating-character-in-a-stream/
            """),
        source_url="https://www.geeksforgeeks.org/first-non-repeating-character-in-a-stream/",
        params=["stream", "n"],
        inputs={
            "stream": "string of n lowercase letters.",
            "n": "length of stream.",
        },
        returns="string of length n: for each prefix, the first non-repeating char or '_'.",
        source=QUEUE_04_SOURCE,
        setup_fn=_setup_queue_04,
        verify_fn=_verify_queue_04,
        samples=[
            Sample("stream = 'aabc', n = 4", "'aa_b' (a, a, _, b)"),
            Sample("stream = 'aabbccd', n = 7", "'aa____d' (a, a, _, _, _, _, d)"),
        ],
        hint="Maintain a queue of seen-once characters (in order) and a frequency counter. When a char's count becomes 2, pop it from the queue. The head of the queue is the answer.",
        parents=["queue_03"],
        children=["queue_05"],
    ),
    AlgorithmSpec(
        id="queue_05",
        name="Circular Queue (Array-based)",
        category="queue",
        difficulty=3,
        required_complexity=ComplexityClass.O_1,
        description=("""
            Implement a fixed-capacity circular queue using
            an array. Maintain front, rear, and size. Enqueue
            writes at (rear + 1) % capacity and increments size;
            dequeue reads at front and advances front by 1 mod
            capacity. Return False (not raise) on overflow /
            underflow so the verifier can check the result
            directly. Operations are O(1).
            Source: https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
            """),
        source_url="https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/",
        params=["operations", "capacity", "n"],
        inputs={
            "operations": "list of operation tuples (op_name, *args).",
            "capacity": "fixed capacity of the circular queue.",
            "n": "number of operations.",
        },
        returns="a list of dequeued values (in order) for each successful dequeue.",
        source=QUEUE_05_SOURCE,
        setup_fn=_setup_queue_05,
        verify_fn=_verify_queue_05,
        samples=[
            Sample("ops = [('enqueue', 1), ('enqueue', 2), ('dequeue'), ('enqueue', 3), ('dequeue')], capacity = 3, n = 5", "[1, 2]"),
        ],
        hint="front, rear, size: (rear+1) % capacity on enqueue, front advances on dequeue. Use size to distinguish empty from full.",
        parents=["queue_04"],
        children=[],
    ),
])
