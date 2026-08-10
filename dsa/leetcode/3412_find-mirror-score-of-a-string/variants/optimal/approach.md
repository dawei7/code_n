## General

**The current index needs the closest available mirror on its left.** The process is fixed: scan from left to right, and whenever index $i$ can pair with an earlier unmarked mirror character, choose the closest such index $j$. Once paired, both positions are marked and can never participate again.

For each letter, the source stores the indices of its currently unmarked occurrences in a list. These lists act as stacks. As the scan proceeds left to right, indices are appended in increasing order. Therefore, the last index in a letter's list is always its closest unmatched occurrence to the current position. A stack provides exactly the required choice without searching backward through the string.

The dictionary `d` is a `defaultdict(list)`. A key is a lowercase letter and its value is the stack of unmatched indices holding that letter. Across all stacks, an index appears if and only if it has been scanned but not marked.

**Compute the mirror character directly.** Lowercase English letters occupy consecutive character codes. The reversed alphabet pairs positions whose zero-based alphabet indices add to $25$. The expression

`chr(ord("a") + ord("z") - ord(x))`

computes that counterpart. For `x = "a"`, it becomes `"z"`; for `x = "b"`, it becomes `"y"`; and applying the transformation twice returns the original letter.

Call this mirror `y`. At index `i`, the source checks `d[y]`.

If the stack is non-empty, its final element is the greatest unmarked index $j<i$ containing `y`. The operation `pop()` removes that index, marking it. The current index is also considered marked and is deliberately not appended to any stack. The score increases by `i - j`.

If the mirror stack is empty, no eligible earlier index exists. The current index remains unmarked, so `i` is appended to `d[x]`. It may later be used when a mirror of `x` appears.

**Why LIFO order gives “closest.”** All indices in a stack were appended as the scan moved forward, so they are strictly increasing. A list's final element is its greatest index. Among indices less than the current $i$, the greatest one has the smallest distance $i-j$, exactly matching the statement's closest-left rule. After it is popped, the next element becomes the closest still-unmarked occurrence for a future character.

For `s = "aczzx"`:

- index $0$ contains `"a"`, has no earlier `"z"`, and is pushed onto `d["a"]`;
- index $1$ contains `"c"`, has no earlier `"x"`, and is pushed;
- index $2$ contains `"z"`, finds index $0$ on the `"a"` stack, pops it, and adds $2$;
- index $3$ contains `"z"` but the `"a"` stack is now empty, so index $3$ is stored as unmatched;
- index $4$ contains `"x"`, pops index $1$ from the `"c"` stack and adds $3$.

The total is $5$. Notice that index $3$ remains unmatched; the algorithm does not pair two equal letters unless they are actual alphabet mirrors, which no lowercase letter is because the alphabet has an even number of letters.

**The dictionary represents exactly the unmarked history.** This invariant can be proved after each scanned index. Initially all stacks are empty and no index has been processed. If no mirror exists, appending the current index records precisely the one new unmarked position. If a mirror exists, popping $j$ removes the earlier position that becomes marked, while not pushing $i$ correctly omits the newly marked current position. Every other stack is unchanged. Thus the invariant continues to hold.

Given the invariant, a non-empty mirror stack contains all and only eligible earlier unmarked mirror positions, and its last element is closest. The source therefore performs exactly the process specified at every index. The accumulated `ans` is the sum of precisely the required distances, proving correctness.

It is also useful to understand why a queue would be wrong. A queue would choose the oldest unmatched mirror, which is farthest rather than closest. The problem does not ask for a globally optimized pairing; it prescribes a deterministic left-to-right greedy process. The stack recreates that process exactly.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Each index is visited once. It is either appended to one list or immediately paired. An appended index can be popped at most once later. Dictionary access, list append, and list pop from the end take expected $O(1)$ time. Mirror computation is constant work. Total expected time is therefore $O(n)$.

At most $n$ unmatched indices can be stored across all stacks, so auxiliary space is $O(n)$. The dictionary has at most $26$ meaningful letter keys, although accessing `d[y]` may create an empty list for a mirror not previously seen. The integer score may grow quadratically in numeric value, but Python stores it safely; this does not change the count of stored indices.

## Alternatives and edge cases

- **Backward scan for every index:** Searching left through the string for the closest unmarked mirror directly can take $O(n^2)$ time and requires a separate marked array.
- **Queue per letter:** Removing the earliest stored index chooses the farthest unmatched mirror, violating the closest-index rule. The per-letter container must be LIFO.
- **One global stack:** The closest unmatched character overall may not be the required mirror. Separate stacks allow direct access to the correct letter class.
- **Fixed array of 26 stacks:** A list indexed by alphabet position works equally well and avoids dictionary key creation. The protected source uses a dictionary for concise character-based access.
- **No possible mirrors:** For a string such as `"abcdef"`, every index is pushed and none is popped, so the score remains zero.
- **Repeated same letter:** Identical letters do not mirror each other. They accumulate on one stack until their opposite letter appears, at which point the most recent is consumed first.
- **Nested pairings:** A later mirror always pops the closest currently unmatched index, regardless of earlier completed pairs. Marked indices were removed and cannot interfere.
- **Current index after a match:** It must not be pushed after pairing. Both positions become marked immediately, so storing `i` would allow an illegal second use.
- **Empty mirror stack:** Access through `defaultdict` yields an empty list, and the source correctly stores the current index instead of attempting a pop.
- **Large score:** Distances can accumulate beyond a small fixed-width integer in related constraints. Python's arbitrary-precision integer makes the addition safe.
- **Lowercase-only contract:** The character-code formula relies on the contiguous lowercase English alphabet and should not be generalized to arbitrary Unicode characters without a different mapping.
