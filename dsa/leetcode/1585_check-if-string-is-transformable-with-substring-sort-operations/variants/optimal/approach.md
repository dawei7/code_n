## General

**What an ascending substring sort can and cannot move**

Sorting a substring into ascending order can move a smaller digit left across larger digits. For instance, sorting `"53"` changes it to `"35"`, so digit three crosses digit five. In contrast, a larger digit cannot move left across a smaller digit by ascending sorts: if the smaller digit and larger digit occur in the same sorted substring, ascending order keeps the smaller one first.

This creates the central blocking rule. To take an occurrence of digit `x` from the source and make it the next output character, no still-unused digit smaller than `x` may occur before that source occurrence. Such a smaller digit cannot be crossed by `x` and must appear earlier in every reachable output.

Larger preceding digits do not block `x`. The digit `x` can move left across them by sorting suitable substrings, equivalently by a sequence of adjacent swaps of inverted pairs.

**Remembering every occurrence position**

The solution builds `pos`, a dictionary from each digit to a deque of its indices in `s`. While scanning `s` from left to right, it converts character `c` to integer `int(c)` and appends index `i`.

Therefore, each deque is in increasing source-index order. Its front is the earliest occurrence of that digit that has not yet been assigned to the target prefix.

Keeping occurrence positions rather than only digit frequencies is necessary. Equal digit counts can show that `s` and `t` are anagrams, but counts alone cannot reveal the blocking order. For example, target order may request a larger digit before a smaller source digit that it is unable to cross.

Using deques makes removing an accepted earliest occurrence efficient: `popleft()` takes constant time, while deleting index zero from a Python list would shift all later positions.

**Matching the target from left to right**

The second loop considers each target character `c` in order and converts it to digit `x`. The next target position must use some unused occurrence of `x` from `s`.

The first failure condition is `not pos[x]`. If the deque is empty, every source occurrence of `x` has already been used, or `s` never contained enough copies. The target therefore cannot be formed.

When occurrences exist, the only sensible candidate is `pos[x][0]`, the earliest unused `x`. Choosing a later equal occurrence cannot help: the earlier equal digit would remain before it, and sorting cannot reverse two equal values into a distinguishable advantage. The earliest occurrence also minimizes the number of possible blockers before the chosen digit.

The second failure test examines all digits `i` in `range(x)`, meaning zero through `x - 1`:

`pos[i] and pos[i][0] < pos[x][0]`.

For each smaller digit, only its earliest unused occurrence matters. If that earliest occurrence is not before the chosen `x`, no later occurrence of the same smaller digit can be before it either. If any smaller deque has a front index below the candidate `x` index, that smaller digit is an unavoidable blocker and the method returns `False`.

If no smaller digit blocks `x`, the target character is feasible. `pos[x].popleft()` consumes that source occurrence, conceptually fixing it at the next target position. The loop then repeats for the following target character.

**Why larger digits may be ignored in the blocker check**

Suppose an unused digit `y > x` lies before the selected occurrence of `x`. The adjacent pair `yx` is in descending order. Sorting that two-character substring turns it into `xy`, moving `x` one position left. Repeating this operation lets `x` cross any sequence of larger unused digits.

This adjacent-swap view is sufficient even though the problem allows arbitrary non-empty substrings: a two-character substring is a valid substring. Therefore, every conceptual leftward move used by the greedy construction is an allowed operation.

Equal digits also do not need to be checked as blockers. Swapping equal values changes nothing, and selecting the earliest unused occurrence of `x` preserves their natural order.

**Why a smaller preceding digit makes transformation impossible**

Consider a smaller unused digit `i < x` that originally lies before the chosen `x`. To put `x` at the current target position while leaving `i` for later, their relative order would have to reverse.

An ascending sort cannot reverse that ordered pair. If an operation contains both, it places `i` before `x` because `i < x`. If an operation contains only one of them, it cannot directly swap their relative positions. Across any sequence of operations, the larger `x` cannot cross left over the smaller `i`. Thus the blocker test rejects only a genuinely impossible request.

For the simple impossible transformation `s = "12345"` and `t = "12435"`, target digits one and two consume normally. When target asks for four, the earliest unused three lies before the earliest four and is smaller. Four cannot cross three through ascending sorting, so the method returns false.

**Why passing all checks is sufficient**

Assume the algorithm accepts a target digit `x`. Every unused source digit before the selected occurrence is at least `x`; smaller ones were ruled out. Equal `x` occurrences cannot precede the selected one because the selected occurrence is the deque front. Hence every truly preceding unused digit is larger.

The selected `x` can be moved left across those larger digits by repeatedly sorting adjacent inverted pairs. This places `x` immediately after the already fixed target prefix without disturbing that prefix. Consuming the deque front records this constructive step.

By induction, after processing the first $k$ target characters, there is a sequence of legal sorts that fixes exactly that prefix while the deques describe the remaining source occurrences. If all target characters are processed, every required prefix step is feasible and the whole target is reachable. The equal string lengths ensure all source occurrences are accounted for; an unavailable digit would already have triggered the empty-deque condition.

**A successful pattern**

For `s = "84532"` and a target beginning with three, the earliest three has larger digits eight, four, and five before it, while no unused zero, one, or two lies before it. Three can move left across those larger digits. Later, smaller requested digits are checked against whatever occurrences remain. This explains transformation in terms of legal crossings rather than simulating the editorial’s chosen large-substring operations.

## Complexity detail

Let $N$ be the common length of `s` and `t`.

Building the position deques processes $N$ source characters once, taking $O(N)$ time. For every one of the $N$ target characters, the code checks at most ten digit values—specifically at most `x` smaller digits, and digits range only from zero to nine. Ten is a fixed constant independent of $N$. Deque-front access and `popleft()` are $O(1)$, so the target scan is $O(10N)=O(N)$.

The total time complexity is $O(N)$. All source indices are stored exactly once across the deques, giving $O(N)$ auxiliary space. The dictionary has at most ten meaningful digit keys, which is constant-sized apart from the stored positions.

Python’s `defaultdict` may create empty deques when missing digits are accessed during checks, but there are only ten possible digits, so this does not change the asymptotic space bound.

## Alternatives and edge cases

- **Simulate arbitrary substring sorts:** Searching operation sequences has an enormous state space and hides the simple invariant about which digits can cross. Position queues decide reachability without constructing the operations.
- **Compare only digit frequencies:** Matching frequencies is necessary but not sufficient. Relative blocking by smaller digits can make two anagram strings non-transformable.
- **Repeatedly find characters with `str.index`:** Searching the source for every target position can become quadratic and still needs careful tracking of consumed occurrences. Deques provide ordered unused indices directly.
- **Balanced trees of positions:** Ordered sets can retrieve and delete earliest occurrences in $O(\log N)$ time, but per-digit deques are enough because occurrences are always consumed from left to right.
- **Missing target digit:** An empty deque immediately proves that `t` requests more copies of a digit than `s` supplies.
- **Duplicate digits:** The earliest unused occurrence is always selected. This preserves equal-digit order and cannot be worse than choosing a later copy.
- **Digit zero:** `range(0)` is empty, so zero can always cross larger preceding digits when an unused zero exists. No smaller digit can block it.
- **Digit nine:** Every digit zero through eight is checked, because any of them before the selected nine would be an unavoidable blocker.
- **Already equal strings:** Each target character consumes the matching earliest source occurrence, and no smaller unused digit lies before it. The method returns true.
- **Single-character strings:** The sole target digit succeeds exactly when the source contains that digit, which equal length reduces to ordinary equality.
- **Larger preceding digits:** They are intentionally allowed because adjacent ascending sorts can swap `yx` to `xy` whenever `y > x`.
- **Smaller preceding digits:** They are intentionally rejected because ascending sorting preserves their order before `x`.
- **Equal-length guarantee:** The source and target have the same number of positions. If lengths were not guaranteed equal, the method should reject unequal lengths before building queues.
- **Only decimal digits:** Converting with `int(c)` and checking `range(x)` relies on the alphabet being digits zero through nine with their natural numeric order.
