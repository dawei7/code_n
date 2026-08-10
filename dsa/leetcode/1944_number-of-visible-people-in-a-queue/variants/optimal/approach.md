## General

**Scan from the direction people are looking**

Every person looks to the right. Scanning the queue from right to left means that when processing person $i$, all possible people they might see have already been incorporated into a stack.

The stack stores heights that remain relevant as visible blockers for people farther left. From bottom to top, these heights are strictly decreasing. The top is the nearest surviving candidate.

For current height `heights[i]`, the algorithm repeatedly pops a stack top that is shorter. Each popped person is visible to the current person, so `ans[i]` increases.

After all shorter tops are removed, one of two things is true:

- the stack is empty, so nobody taller remains to block the view;
- the stack top is taller than the current person. That person is also visible, and then blocks every person farther behind it.

Accordingly, the code adds one more when `stk` remains nonempty, then pushes the current height for people farther left.

**Why every popped shorter person is visible**

Consider a shorter height at the stack top. The stack invariant means no already processed person between it and the current position remains as an equal-or-taller obstruction to it. Any people removed earlier were shorter than some nearer survivor and do not invalidate the top's visibility from the new, taller current person.

More intuitively, as the current person looks right, they can see a sequence of record-high silhouettes. Every time the stack pops a shorter height, that height rises above all people between it and the current viewer but remains below the viewer. Therefore everyone between is shorter than both endpoints, satisfying the visibility definition.

Distinct heights remove equality complications: each comparison is strictly shorter or strictly taller.

**Why only one taller person is visible**

Once the shorter visible people have been popped, the remaining top is the first surviving person taller than the current viewer. Everyone between is shorter than the current viewer, so this taller person is visible.

Any person behind that taller top is blocked by it. The blocking person's height is greater than the current viewer, so it is not shorter than the minimum of the two endpoint heights for any farther target. Thus the current viewer can see at most that one taller person beyond all popped shorter people.

This explains the two contributions exactly: all popped shorter heights, plus at most one unpopped taller height.

**How the stack invariant is maintained**

Before pushing the current height, all smaller heights have been removed. If a stack value remains, it is larger. Therefore appending the current height keeps the stack strictly decreasing from bottom to top.

The stack also contains exactly the suffix candidates that can matter to a future viewer. A height popped by the current person is shorter than the current person, which stands closer to every future viewer on the left. That popped height will always be blocked by the current person and can never matter again. Removing it is safe.

**Example of the process**

For suffix heights `[11, 9]`, scanning from the right first pushes 9. Person 11 pops 9 and sees them, then is pushed. When a shorter person such as 5 is processed to the left, 11 is not popped; 5 sees 11 as the one taller blocker. The stack becomes `[11, 5]`. A later height 8 pops 5, sees 5, then sees 11 and stops. This yields exactly the visible sequence 5 followed by 11.

**Why the counts are correct**

Every increment corresponds to a visible person by the arguments above. Conversely, every visible person to the right is either shorter than the viewer and appears among the successive popped silhouettes, or is the first taller blocker left on the stack. Any other person is hidden behind one of these. Therefore `ans[i]` counts all and only visible people for every index.

## Complexity detail

Let $N$ be the number of people.

Each height is pushed once. A height can be popped at most once over the entire scan. Although a while loop is nested inside the for loop, total pop operations are at most $N$, so total time is $O(N)$ by amortized analysis.

The answer array uses $O(N)$ output space. In a decreasing-height arrangement from left to right, scanning from right can make the stack contain all $N$ heights, so auxiliary stack space is $O(N)$.

Every comparison and stack operation is constant time.

## Alternatives and edge cases

- **Check every pair:** For each viewer, scan rightward while tracking intervening maxima. This can take $O(N^2)$ time.
- **Next-greater links:** One can precompute blocking relationships and follow visibility chains, but the monotonic stack computes counts directly in one pass.
- **Strictly increasing heights left to right:** Each person sees every person until the first taller sequence behavior permits; the stack repeatedly pops shorter suffix heights, producing the correct growing counts.
- **Strictly decreasing heights left to right:** Each person sees only the immediate next person, because that nearer person blocks all shorter people behind.
- **Last person:** The stack is empty when processed, so their answer remains zero.
- **Single person:** It is also the last person and correctly sees nobody.
- **One shorter then one taller:** Both can be visible: the shorter is popped and counted, and the taller survivor is counted once.
- **Distinct-height guarantee:** The exact comparisons rely on no equal heights. With duplicates, equality visibility and stack handling would need explicit policy.
- **Amortized loop:** A person may pop many heights in one iteration, but those heights never reenter, keeping the full scan linear.
- **Stack stores heights only:** Indices are unnecessary because the result is assigned to the current index and only height comparisons determine blocking.
