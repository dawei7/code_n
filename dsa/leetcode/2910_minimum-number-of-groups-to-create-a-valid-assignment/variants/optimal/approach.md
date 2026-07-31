## General

**All box sizes reduce to two adjacent choices.** Let $x$ be the size of the smallest box. The global balance rule means every box must contain either $x$ or $x+1$ balls. No $x$ larger than the minimum value frequency can work, because at least one label must fill a nonempty homogeneous box from only that many balls.

**Test one frequency arithmetically.** Suppose a value occurs $f$ times. To use as few boxes as possible for a fixed $x$, first take

$$
g=\left\lceil\frac{f}{x+1}\right\rceil.
$$

These $g$ boxes have total capacity at least $f$ when each has size $x+1$. They can represent the frequency using sizes $x$ and $x+1$ exactly when their minimum total content is not already too large, that is, when $gx\le f$. If this inequality holds, begin with $g$ boxes of size $x$ and distribute the remaining $f-gx\le g$ balls one per box.

**Choose the largest feasible smaller size.** Count every distinct value, then try $x$ from the minimum frequency downward. For each candidate, apply the feasibility test to every frequency and sum its minimum group counts. The first candidate that works is the largest feasible $x$. Since $\lceil f/(x+1)\rceil$ never increases as $x$ grows, this largest feasible size produces the minimum possible total number of boxes.

Every returned count has a constructive assignment by the distribution argument above, so it is valid. Conversely, any valid assignment has some smallest size $x$ and must pass the same inequality for every frequency. The descending search therefore considers its size and cannot return more boxes than an optimal assignment.

## Complexity detail

Let $n=\lvert\texttt{balls}\rvert$, let $u$ be the number of distinct values, and let $m$ be the minimum frequency. Counting takes $O(n)$ time. The descending search examines at most $m$ sizes and checks $u$ frequencies per size. Because every one of the $u$ frequencies is at least $m$, $um\le n$; the search is therefore also $O(n)$. The frequency table uses $O(u)$ space.

## Alternatives and edge cases

- **Recount raw balls for every candidate size:** Rebuilding frequencies inside the size loop repeats work and can take superlinear time; count once before testing candidates.
- **Construct every box explicitly:** Materializing candidate partitions is unnecessary. The inequality $gx\le f$ completely characterizes feasibility for one frequency.
- **All values distinct:** Every frequency is one, so each ball must occupy its own size-one box.
- **All values equal:** A single box containing every ball is valid and optimal.
- **A singleton frequency:** The smallest box must have size one, restricting every other box to size one or two.
- **Nonconsecutive labels:** Only value equality and frequency matter; the numeric distance between labels has no effect.
- **Guaranteed fallback:** Size $x=1$ is always feasible, so a valid assignment always exists.
