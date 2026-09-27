# Guided Example: Rearrange String k Distance Apart

We trace the step-by-step max-heap greedy scheduling (`(-count, char)`), cooldown sliding deque maintenance (`len(q) >= k`), distance-$k$ separation enforcement, and impossibility detection (`len(ans) < len(s)`) on representative string instances:

- **Input:** $s = \text{"aabbcc"}, \quad k = 3$
- **Required output:** $\text{"abcabc"}$
  - Initial frequency counts: `'a': 2, 'b': 2, 'c': 2`
  - Max-heap: `[(-2, 'a'), (-2, 'b'), (-2, 'c')]`
  - Step 1: Pop `'a'` $\implies ans = [\text{'a'}]$, cooldown queue: `[(-1, 'a')]`
  - Step 2: Pop `'b'` $\implies ans = [\text{'a'}, \text{'b'}]$, cooldown queue: `[(-1, 'a'), (-1, 'b')]`
  - Step 3: Pop `'c'` $\implies ans = [\text{'a'}, \text{'b'}, \text{'c'}]$, queue reaches size $3 \ge k \implies$ release `'a'` back to heap!
  - Step 4: Pop `'a'` $\implies ans = [\text{'a'}, \text{'b'}, \text{'c'}, \text{'a'}]$, release `'b'`
  - Step 5: Pop `'b'` $\implies ans = [\text{'a'}, \text{'b'}, \text{'c'}, \text{'a'}, \text{'b'}]$, release `'c'`
  - Step 6: Pop `'c'` $\implies ans = [\text{'a'}, \text{'b'}, \text{'c'}, \text{'a'}, \text{'b'}, \text{'c'}]$
  - All 6 characters scheduled $\implies \text{"abcabc"}$
- **Infeasible Instance:** $s = \text{"aaabc"}, k = 3 \implies \text{""}$ (Heap empties prematurely while 'a' is stuck in cooldown)
- **Zero Distance Limit:** $k = 0 \implies$ string returned unchanged

This instance demonstrates greedy priority-queue scheduling with cooldown window constraints, mathematically proves why prioritizing higher-frequency characters prevents unavoidable starvation, and achieves $O(N \log |\Sigma|)$ time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"aabbcc"}$ ($N = 6$) and an integer $k = 3$:
Rearrange the characters of $s$ such that the same characters are separated by **at least distance $k$** from each other:
$$
\text{index}(c_2) - \text{index}(c_1) \ge k \quad \text{for any identical characters } c_1 = c_2
$$
If no valid rearrangement exists, return the empty string `""`:

```text
Target Separation: k = 3 (At least 2 other characters between identical letters)

Valid Placement:
Index:   0   1   2   3   4   5
Char:   'a' 'b' 'c' 'a' 'b' 'c'
Distance between 'a's: 3 - 0 = 3 >= 3 (Valid!)
Distance between 'b's: 4 - 1 = 3 >= 3 (Valid!)
Distance between 'c's: 5 - 2 = 3 >= 3 (Valid!)

Output: "abcabc"
```

---

## 2. Conceptual Foundation & Invariants

### 1. Greedy Choice Invariant
Characters with higher remaining frequencies exert the greatest future placement constraints.
At every step, always greedily schedule the **eligible** character with the **maximum remaining frequency**.

### 2. The Two-Stage Architecture
1. **Max-Heap (`pq`):**
   Stores currently eligible characters as tuples `(-remaining_count, char)`.
   Using negative counts simulates a max-heap via Python's standard min-heap `heapq`.
2. **Cooldown Queue (`q`):**
   Stores recently placed characters and their decremented counts.
   A character placed at current step enters `q` and cannot re-enter `pq` until at least $k$ steps have elapsed:
   $$
   \text{When } \text{len}(q) \ge k: \quad e = q.\text{popleft}(), \quad \text{if } e[0] < 0: heappush(pq, e)
   $$

### 3. Termination & Validity Check
If the heap becomes empty while characters still have positive counts in `q`:
$$
\text{len}(ans) < \text{len}(s) \implies \text{Return } \text{""}
$$
Otherwise, return `"".join(ans)`.

> **Invariant.** No character can be selected if fewer than $k$ positions have elapsed since its last placement.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aabbcc"}$ with $k = 3$:
Initial counts: `{'a': 2, 'b': 2, 'c': 2}`.
`pq = [(-2, 'a'), (-2, 'b'), (-2, 'c')]`, `q = deque()`, `ans = []`.

---

### Step 1: Position 0
- Pop max-frequency element: `(-2, 'a')`.
- Append to result: $ans = [\mathbf{\text{'a'}}]$.
- Enqueue to cooldown: $q.\text{append}((-1, \text{'a'})) \implies q = [(-1, \text{'a'})]$.
- Condition $\text{len}(q) \ge 3$ is False ($1 < 3$).

---

### Step 2: Position 1
- Pop max-frequency element: `(-2, 'b')`.
- Append to result: $ans = [\text{'a'}, \mathbf{\text{'b'}}]$.
- Enqueue to cooldown: $q.\text{append}((-1, \text{'b'})) \implies q = [(-1, \text{'a'}), (-1, \text{'b'})]$.
- Condition $\text{len}(q) \ge 3$ is False ($2 < 3$).

---

### Step 3: Position 2 — First Cooldown Release!
- Pop max-frequency element: `(-2, 'c')`.
- Append to result: $ans = [\text{'a'}, \text{'b'}, \mathbf{\text{'c'}}]$.
- Enqueue to cooldown: $q.\text{append}((-1, \text{'c'}))$.
- Cooldown queue: $q = [(-1, \text{'a'}), (-1, \text{'b'}), (-1, \text{'c'})]$, $\text{len}(q) = 3 \ge 3$!
- **Release expired character:**
  - $e = q.\text{popleft}() = (-1, \text{'a'})$.
  - Since remaining count $-1 \ne 0$, push back to heap: $heappush(pq, (-1, \text{'a'}))$.
- Heap now has: `[(-1, 'a')]`.

---

### Step 4: Position 3
- Pop max-frequency element: `(-1, 'a')`.
- Append to result: $ans = [\text{'a'}, \text{'b'}, \text{'c'}, \mathbf{\text{'a'}}]$.
- Enqueue to cooldown: $q.\text{append}((0, \text{'a'}))$.
- Queue: $[(-1, \text{'b'}), (-1, \text{'c'}), (0, \text{'a'})]$, $\text{len}(q) = 3 \ge 3$.
- Release expired character:
  - $e = q.\text{popleft}() = (-1, \text{'b'})$.
  - Push back to heap: $heappush(pq, (-1, \text{'b'}))$.
- Heap now has: `[(-1, 'b')]`.

---

### Step 5: Position 4
- Pop max-frequency element: `(-1, 'b')`.
- Append to result: $ans = [\text{'a'}, \text{'b'}, \text{'c'}, \text{'a'}, \mathbf{\text{'b'}}]$.
- Enqueue: $q.\text{append}((0, \text{'b'}))$.
- Release expired character:
  - $e = q.\text{popleft}() = (-1, \text{'c'})$.
  - Push back to heap: $heappush(pq, (-1, \text{'c'}))$.

---

### Step 6: Position 5
- Pop max-frequency element: `(-1, 'c')`.
- Append to result: $ans = [\text{'a'}, \text{'b'}, \text{'c'}, \text{'a'}, \text{'b'}, \mathbf{\text{'c'}}]$.
- Enqueue: $q.\text{append}((0, \text{'c'}))$.
- Release expired character:
  - $e = q.\text{popleft}() = (0, \text{'a'})$.
  - Remaining count is $0 \implies$ discarded!
- Loop ends as `pq` is empty.

---

### Step 7: Verification
Length of `ans` is $6 == \text{len}(s)$.
Return valid rearranged string:
$$
\mathbf{\text{"abcabc"}}
$$

---

## 4. Complete Execution Trace

```text
s = "aabbcc", k = 3
pq = [(-2,'a'), (-2,'b'), (-2,'c')]

Pos 0: pop 'a' -> ans=['a'], q=[(-1,'a')]
Pos 1: pop 'b' -> ans=['a','b'], q=[(-1,'a'),(-1,'b')]
Pos 2: pop 'c' -> ans=['a','b','c'], q=[(-1,'a'),(-1,'b'),(-1,'c')]
       len(q)>=3 -> popleft (-1,'a') -> push to pq: [(-1,'a')]
Pos 3: pop 'a' -> ans=['a','b','c','a'], q=[(-1,'b'),(-1,'c'),(0,'a')]
       len(q)>=3 -> popleft (-1,'b') -> push to pq: [(-1,'b')]
Pos 4: pop 'b' -> ans=['a','b','c','a','b'], q=[(-1,'c'),(0,'a'),(0,'b')]
       len(q)>=3 -> popleft (-1,'c') -> push to pq: [(-1,'c')]
Pos 5: pop 'c' -> ans=['a','b','c','a','b','c'], q=[(0,'a'),(0,'b'),(0,'c')]
       len(q)>=3 -> popleft (0,'a') (count 0, discarded)

Final String: "abcabc"
```

| Output Index | Selected Character | Remainder Stored | Cooldown Queue State Before Release | Released from Cooldown | Re-added to Heap? | String Emitted So Far |
|:---:|:---:|:---:|:---|:---:|:---:|:---|
| 0 | `'a'` | $-1$ | `[(-1, 'a')]` | None | No | `"a"` |
| 1 | `'b'` | $-1$ | `[(-1, 'a'), (-1, 'b')]` | None | No | `"ab"` |
| **2** | **'c'** | **$-1$** | **`[(-1, 'a'), (-1, 'b'), (-1, 'c')]`** | **`(-1, 'a')`** | **Yes (`'a'`)** | **`"abc"`** |
| 3 | `'a'` | $0$ | `[(-1, 'b'), (-1, 'c'), (0, 'a')]` | `(-1, 'b')` | Yes (`'b'`) | `"abca"` |
| 4 | `'b'` | $0$ | `[(-1, 'c'), (0, 'a'), (0, 'b')]` | `(-1, 'c')` | Yes (`'c'`) | `"abcab"` |
| 5 | `'c'` | $0$ | `[(0, 'a'), (0, 'b'), (0, 'c')]` | `(0, 'a')` | No (Exhausted) | **`"abcabc"`** |

---

## 5. Algorithmic Correctness

**Soundness.** A character is pushed back into `pq` only after $\text{len}(q) \ge k$, which implies that at least $k - 1$ intervening characters have been placed since its last use. Thus, any two occurrences of the same character are separated by an index difference of at least $k$.

**Completeness.** Prioritizing characters with the maximum remaining counts minimizes the risk of deadlock. If a valid arrangement exists, this greedy strategy successfully places all $N$ characters without prematurely exhausting separator letters.

---

## 6. Traps This Instance Exposes

- **Enqueuing Exhausted Characters:** Characters with remaining count 0 must still be pushed into `q` to maintain the chronological timeline of $k$ elapsed slots. Only after leaving `q` are they filtered out by `if e[0]:`.
- **Heap Starvation on Infeasible Inputs:** For inputs like `"aaabc"` with $k = 3$, `a` cannot be placed without violating distance $k$. The heap becomes empty before `ans` reaches length $N$. Returning `""` when `len(ans) < len(s)` prevents partial invalid output.
- **$k = 0$ Edge Case:** When $k \le 1$, identical characters can be adjacent. The condition `len(q) >= k` releases the character immediately.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log |\Sigma|)$, where $N = \text{len}(s)$ and $|\Sigma|$ is the alphabet size ($|\Sigma| \le 26$). Each of the $N$ steps involves at most one `heappop` and one `heappush`, taking $O(\log 26) = O(1)$ time. Overall runtime is strictly $O(N)$.
- **Auxiliary Space Complexity:** $O(|\Sigma| + k) = O(1)$ bounded auxiliary memory to store heap and cooldown queue, plus $O(N)$ for output list `ans`.
