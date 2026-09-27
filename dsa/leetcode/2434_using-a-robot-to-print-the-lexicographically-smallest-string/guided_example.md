# Guided Example: Using a Robot to Print the Lexicographically Smallest String

## 1. The Instance and the Two Allowed Operations

The robot starts with an empty string `t`, the input `s` sits untouched, and a sheet of
paper begins empty. Two operations may be applied until both `s` and `t` are empty:

- **Consume from the left:** remove the first character of `s` and append it to the end of
  `t`.
- **Write to the paper:** remove the *last* character of `t` and append it to the paper.

The paper content is built left to right and is never revised, so the goal is to make that
left-to-right sequence lexicographically smallest. For this lesson we trace

$$
s = \texttt{"cbaabc"},
$$

whose authored answer is `"aabbcc"`. The instance is chosen because the alphabet has only
three letters, so every state fits on one line, and because it exercises all three regimes
of the decisive test: a blocked stack top, an *equal* stack top that is still safe to
write, and a final unrestricted flush.

The subtlety is the LIFO discipline. Characters are pushed on the left and popped on the
right, so a character that has been pushed can only be written after everything pushed on
top of it has been written first. The input `"bca"` makes the consequence concrete: the best
achievable output there is `"acb"`, not the sorted string `"abc"`, because the `b` is buried
under the `c` before the `a` ever arrives.

## 2. The State the Method Maintains

Everything the decision needs is captured by four quantities.

| Running quantity | What it represents in this instance | Value before the scan |
|---|---|---|
| The stack `t` | characters already taken from the front of `s` but not yet written; only its **last** element is reachable | empty |
| Remaining counts | how many copies of each letter still sit in the unread suffix of `s` | `a` → 2, `b` → 2, `c` → 2 |
| The unread minimum `mi` | the smallest letter with a positive remaining count, that is $\min$ over the unread suffix | `a` |
| The written prefix `p` | output already committed to the paper; it can never be changed | empty |

The written prefix is why the method is greedy rather than exhaustive: once a character is
on the paper it is fixed, so the only decision that matters is what the *next* written
character should be.

Two properties make `mi` cheap. It is the minimum of the unread suffix only — characters
already on the stack are excluded, because they cannot be written before the current stack
top. And it is non-decreasing: as characters are consumed, counts fall to zero, so the
smallest remaining letter can only move upward, and one forward pointer over the 26 letters
suffices.

## 3. When Is It Safe to Write from the Stack?

At any step the only character that can be written is the current stack top, call it $\tau$.
The alternatives are to write $\tau$ now, or to postpone it by consuming more of `s` (which
appends above $\tau$ without disturbing it). Postponing can only ever present a character
that is still in the unread suffix. So the comparison is between $\tau$ and the smallest
letter that could possibly be written before $\tau$ if we wait — and that smallest letter is
exactly `mi`.

- If $\tau \le mi$, nothing that can be produced later is smaller than $\tau$. Writing
  $\tau$ now minimises the next character, so pop.
- If $\tau > mi$, some strictly smaller letter is still unread. It must be pushed before it
  can be written, and pushing puts it *above* $\tau$, so $\tau$ cannot be written until that
  smaller letter is. Writing $\tau$ now would place a larger character earlier in the
  output. So do not pop; consume more input.

After every push, the rule is re-applied until it fails. When `s` is exhausted there is no
unread suffix left, so `mi` becomes larger than every remaining stack character and the
whole stack drains onto the paper.

The case $\tau = mi$ is the trap. It looks like a tie that could go either way, but it must
pop: because an equally small character is available later, writing $\tau$ now is not worse
than waiting, and popping keeps the stack shallower. A strict `<` comparison would leave
$\tau$ sitting on the stack unnecessarily and could destroy a later opportunity.

## 4. Full Step-by-Step Trace

The table below follows the scan over `cbaabc`, showing the remaining counts after the
current character is consumed, the value of `mi`, the push, and every pop that follows.

| Step | Character read | Counts `a`,`b`,`c` after reading | `mi` | Push | Pops on this step | Written prefix after | Stack after (bottom → top) |
|---|---|---|---|---|---|---|---|
| 0 | — | 2, 2, 2 | `a` | none | none | `""` | empty |
| 1 | `c` | 2, 2, 1 | `a` | `c` | none, since `c > a` | `""` | `c` |
| 2 | `b` | 2, 1, 1 | `a` | `b` | none, since `b > a` | `""` | `c b` |
| 3 | `a` | 1, 1, 1 | `a` | `a` | `a`, since `a = a` | `"a"` | `c b` |
| 4 | `a` | 0, 1, 1 | `b` | `a` | `a`, then `b`, since `a = b` and `b = b` | `"aab"` | `c` |
| 5 | `b` | 0, 0, 1 | `b` | `b` | `b`, since `b = b` | `"aabb"` | `c` |
| 6 | `c` | 0, 0, 0 | `z` (nothing unread) | `c` | `c`, then `c` | `"aabbcc"` | empty |

The final paper holds `"aabbcc"`, matching the authored answer. Three behaviours appear. At
steps 1 and 2 the top exceeds `mi`, so the robot keeps consuming. At steps 3, 4, and 5 the
top is *equal* to `mi`, exactly the case a strict inequality would mishandle. At step 6
nothing is unread, and the same rule drains the whole stack.

Step 4 repays attention: the last `a` of the input is consumed and written immediately, but
the older `a` pushed at step 3 is still on the stack when it pops, and the equality test is
what permits it. The character written at step 5 is the `b` pushed at step 2, which had
waited under two `a`s.

## 5. State Before and After Each Step

The same trace read as a pure state transition, which makes the monotonic behaviour of `mi`
and the one-way growth of the written prefix explicit.

| Step | Stack before | Stack after | `mi` before | `mi` after | Written prefix before | Written prefix after |
|---|---|---|---|---|---|---|
| 1 | empty | `c` | `a` | `a` | `""` | `""` |
| 2 | `c` | `c b` | `a` | `a` | `""` | `""` |
| 3 | `c b` | `c b` | `a` | `a` | `""` | `"a"` |
| 4 | `c b` | `c` | `a` | `b` | `"a"` | `"aab"` |
| 5 | `c` | `c` | `b` | `b` | `"aab"` | `"aabb"` |
| 6 | `c` | empty | `b` | `z` | `"aabb"` | `"aabbcc"` |

The `mi` column never decreases, confirming that the pointer only advances. The stack is not
monotone — at step 2 it reads `c b` — which is why sorting the input is not a valid strategy.

## 6. Why the Greedy Rule Is Optimal

**Invariant.** Before each step, the written prefix `p` is a prefix of some lexicographically
minimal achievable output, and the pair (stack, unread suffix) still admits a completion that
attains the remainder of that minimal output.

**Sufficiency of a pop.** Suppose the stack top satisfies $\tau \le mi$. Any strategy that
does not write $\tau$ next must write some other character first. A character currently below
$\tau$ in the stack is unreachable, so that other character must come from the unread suffix,
where every letter is at least $mi \ge \tau$. Writing $\tau$ now therefore produces a next
character no larger than the alternative, and the exchange argument applies: if an optimal
output writes something else at this position, swapping in $\tau$ cannot make the output
larger. The invariant is preserved.

**Necessity of waiting.** Suppose $\tau > mi$. Let $\mu$ be a smallest letter still unread,
so $\mu = mi < \tau$. Before $\mu$ can be written it must be pushed, and at that moment it
lies above $\tau$, so $\tau$ is unreadable until $\mu$ (or an equally small letter) has been
written. Any strategy that writes $\tau$ now would place a character strictly larger than
$\mu$ at this output position, while the strategy that waits places $\mu$ there. Since a
strictly smaller character at the earliest differing position makes the whole string
smaller, writing $\tau$ now is strictly suboptimal. Hence the rule is not merely sufficient
but necessary.

**Termination and completeness.** Every character of `s` is consumed once and every pushed
character is written once, so the process ends with an output of length $n$. Once `s` is
exhausted, `mi` becomes `z` and no letter exceeds it, so the whole stack drains and nothing
is stranded.

**Why the state is sufficient.** The next decision needs only the stack top, whether a
smaller letter is still unread, and the remaining counts. The order of characters below the
top is irrelevant until they surface, and the written prefix cannot affect future choices.

## 7. Boundary and Degenerate Instances

| Instance | Structural feature | Behaviour of the rule | Answer |
|---|---|---|---|
| `"a"` | single character | pushed and immediately written, since `a = mi` | `"a"` |
| `"abcdef"` | strictly increasing input | every character written immediately after being read | `"abcdef"` |
| `"dcba"` | strictly decreasing input | no pop is ever safe until `s` is exhausted, then the whole stack drains in reverse | `"abcd"` |
| `"cbaabc"` | repeated letters, equality case `b = mi` | two blocked steps, three equality pops, one full flush | `"aabbcc"` |
| `"vzhofnpo"` | two copies of `o`, a blocked step after three pops | after `h` is written the top is `z` while `mi` is `o`, so the robot waits for the last `o` before flushing | `"fnohopzv"` |
| `"zza"` | the smallest letter arrives last | the entire input is pushed before any write is safe | `"azz"` |
| `"bca"` | a letter buried under a larger one | the `b` cannot precede the `c`, so sorting is impossible; the best output is `"acb"` | `"acb"` |

Two traps live here. The answer is *not* the sorted multiset of the input: `"bca"` disproves
that, since `"abc"` is unreachable. It is not a rotation or a reversal either: for `"cbaabc"`
the output interleaves pops from the middle of the stack with the last consumed character.

## 8. Alternative Methods and Their Costs

| Alternative | Idea | Trade-off |
|---|---|---|
| Sort all input characters | Emit the letters of `s` in non-decreasing order | Illegal in general: only the last element of `t` is writable, so `"bca"` yields `"acb"`, not `"abc"` |
| Exhaustive search over operation sequences | Enumerate every interleaving of the two operations and keep the best output | The number of interleavings grows exponentially with the input length, and almost all of them are dominated by a single local test |
| Precomputed suffix-minimum array | Build an array of $\min(\text{s}[i:])$ for every $i$ and compare the stack top against it | Equivalent decision with $O(n)$ extra memory, versus the $26$-letter count table that the running pointer needs |
| Two-stack or deque formulation | Keep a deque and rotate between ends | Adds structure the problem never uses: only one end of `t` is ever written, so a plain stack is the exact model |

## 9. Complexity Derivation

Let $n = \lvert s \rvert$ and let $\sigma = 26$ be the size of the lowercase alphabet.

**Time.** The initial pass counts the letters of `s` in $O(n)$. During the scan, each
character of `s` is consumed exactly once and pushed exactly once, and each pushed character
is written exactly once, so the total number of stack operations is at most $2n$. The
unread-minimum pointer advances through the alphabet at most $\sigma - 1$ times in total,
because it never moves backward, so its whole contribution over the scan is $O(\sigma)$. The
dominant term is therefore

$$
O(n + \sigma) = O(n).
$$

The bound is tight: every character of `s` must be consumed and every character of the output
must be written, so no method can do better than $\Omega(n)$ in a model where reading and
writing are constant-time.

**Auxiliary space.** The stack holds at most $n$ characters in the worst case, as in the
strictly decreasing input `"dcba"`, and the count table holds $\sigma$ integers. The written
output grows to length $n$ but is the required output rather than auxiliary storage.
Combining the simultaneous maxima gives

$$
O(n + \sigma) = O(n)
$$

auxiliary space. In the best case, a strictly increasing input such as `"abcdef"` keeps the
stack at size $1$ while still producing an output of length $n$, so the worst case is not
reached on every input — but the decreasing case shows the bound is necessary.
