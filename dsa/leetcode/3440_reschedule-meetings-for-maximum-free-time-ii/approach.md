## General

**Focus on one meeting and the free region around it.** Suppose meeting $i$ is the one meeting we may move. Let

$$
l=
\begin{cases}
0,&i=0,\\
\texttt{endTime}[i-1],&i>0,
\end{cases}
$$

and

$$
r=
\begin{cases}
\texttt{eventTime},&i=n-1,\\
\texttt{startTime}[i+1],&i<n-1.
\end{cases}
$$

The interval from $l$ to $r$ contains the free gap immediately before meeting $i$, the meeting itself, and the free gap immediately after it. Let its duration be

`w = endTime[i] - startTime[i]`.

There are two materially different ways to move this meeting.

**Case 1: the meeting remains inside its surrounding region.** Pack the meeting against the left or right side of $[l,r]$. The two adjacent free gaps merge, but the meeting still occupies $w$ time units inside the region. The resulting continuous free duration is

$$
r-l-w.
$$

This move is always possible because the original meeting already fits between its two neighbors. The source evaluates `r - l - w` for every meeting.

**Case 2: the meeting moves into a separate free gap.** If some non-adjacent free gap has length at least $w$, meeting $i$ can be placed there. Its entire old surrounding region $[l,r]$ then becomes free, giving duration

$$
r-l.
$$

The destination must be non-adjacent to the old meeting. Using either immediately neighboring gap would put the meeting back inside $[l,r]$ and leave only the Case 1 amount free.

Because this version allows relative meeting order to change, a fitting free gap can lie anywhere else in the event. The problem therefore becomes: for each meeting, quickly determine whether a sufficiently large non-adjacent gap exists on its left or right.

**Build maximum free-gap information from both directions.** The source creates `pre` and `suf`.

`pre[0] = startTime[0]` is the free time before the first meeting. For $i\ge1$,

`pre[i] = max(pre[i - 1], startTime[i] - endTime[i - 1])`.

Thus `pre[i]` is the largest free gap among the event-start gap and the between-meeting gaps through the gap immediately before meeting $i$.

For meeting $i$, that immediately preceding gap is adjacent and cannot serve as a separate destination. Therefore, the source tests `pre[i - 1]`, which contains only gaps farther left. The condition is available only when `i > 0`.

Symmetrically, `suf[n - 1]` is the free gap after the last meeting. The reverse loop makes `suf[i]` the largest gap from immediately after meeting $i$ through the event-end gap. For meeting $i$, `suf[i + 1]` excludes its immediately following gap and represents only non-adjacent gaps farther right.

If either excluded-side maximum is at least $w$, the source updates the answer with `r - l`. It uses `elif` for the right test because once a fitting left gap exists, finding a right one cannot improve the same candidate value.

For example, if meeting $i$ has duration $1$, its previous neighbor ends at time $1$, and its next neighbor starts at time $7$, then moving it into a separate one-unit gap makes all of `[1,7]` free. The candidate is $6$, not merely the sum of its two adjacent gaps after retaining the meeting locally.

**Why checking only gap length is sufficient.** A meeting has fixed duration and may be placed anywhere inside a free interval at least that long. The destination gap contains no meeting, remains inside the event, and is non-adjacent to the vacated region by construction. Placing the meeting there cannot create an overlap.

**Why every optimal move is covered.** If the moved meeting stays between its original neighbors, at most the two neighboring free gaps can merge, and Case 1 is optimal for that meeting. If it leaves that region, it must fit in some other original free gap; the prefix or suffix maximum detects such a gap and Case 2 gives the completely vacated region. No third placement type exists.

The algorithm also effectively covers making no move. Every original free gap is adjacent to at least one meeting, and that meeting's Case 1 candidate includes that gap plus another nonnegative adjacent gap. Therefore, `ans` cannot be smaller than the original longest free interval.

## Complexity detail

Let $n$ be the number of meetings. Building `pre` takes $O(n)$ time, building `suf` takes $O(n)$ time, and evaluating all meetings takes $O(n)$ time. Total time is $O(n)$.

The two arrays each hold $n$ gap maxima, so auxiliary space is $O(n)$. All other variables use constant space, matching the manifest.

## Alternatives and edge cases

- **Try every destination gap for every meeting:** This takes $O(n^2)$ time. Prefix and suffix maxima answer the only needed question—whether any fitting non-adjacent gap exists—in constant time per meeting.
- **Use adjacent gaps as relocation destinations:** They are already part of $[l,r]$ and cannot make the full region free; they belong to Case 1.
- **Do not move a meeting:** The maximum remains covered because local packing never produces less free time than either adjacent original gap.
- **First meeting:** Its left boundary is zero, and only non-adjacent gaps on the right can support Case 2.
- **Last meeting:** Its right boundary is `eventTime`, and only non-adjacent gaps on the left can support Case 2.
- **Exactly fitting destination:** A gap of length `w` is sufficient, so the comparison is `>=`.
- **Zero-length gaps:** They remain valid prefix/suffix values but can hold only a zero-duration meeting, which the constraints exclude.
- **Touching meetings:** Their between-gap length is zero and the formulas remain correct.
- **Changed relative order:** Moving to any non-adjacent gap is legal specifically because version II removes the order-preservation restriction.
- **Destination gap loses free time:** That does not invalidate `r-l` as a newly created free interval; the objective is the longest single free interval, not total free time.
