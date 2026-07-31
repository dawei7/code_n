## General

Parse `start` and `end` as UTC midnight timestamps. Keep the end timestamp fixed and store one mutable `currentTime`, initially equal to the start timestamp. While `currentTime` does not exceed the end, convert it back to an ISO string, keep the first ten characters `YYYY-MM-DD`, and yield that value. After the generator resumes, add `step` whole days in milliseconds to prepare the next candidate.

**Why UTC epoch-day arithmetic preserves calendar steps**

An ISO date-only string is parsed at UTC midnight. Every UTC calendar day in this domain is exactly `24 * 60 * 60 * 1000` milliseconds, so adding `step` times that constant moves from the current date to the date exactly `step` days later. Local daylight-saving changes cannot shorten or lengthen the interval because no local-time operation is involved.

At iteration $i$, the stored timestamp represents `start` plus $i \cdot \textit{step}$ days. The generator yields it precisely when it is at most `end`. Advancing preserves that relation for the next iteration, and the first candidate greater than `end` terminates the loop. Thus every required progression date is yielded once, in order, `end` is included exactly when aligned, and no out-of-range date appears.

Because this is a generator, it computes a date only when the consumer requests the next value. It retains only the current and end timestamps rather than constructing the full range in advance.

## Complexity detail

Let $k = \lfloor d / \textit{step} \rfloor + 1$ be the number of yielded dates. Each generator resumption performs constant timestamp arithmetic and formatting, so consuming the entire range takes $O(k)$ time. The generator retains a constant number of scalar values and therefore uses $O(1)$ auxiliary space, excluding the strings already yielded to its consumer.

## Alternatives and edge cases

- **Mutable `Date` with local setters:** Repeatedly calling `setDate(getDate() + step)` is concise, but local daylight-saving transitions can make day-length arithmetic harder to reason about; UTC timestamps avoid that dependency.
- **Eager result array:** Building all dates first also takes $O(k)$ time but requires $O(k)$ storage and defeats the lazy generator contract.
- **Restarting from `start` for every output:** Recomputing the $i$th date through $i$ one-day updates is correct but takes $O(k^2)$ work over the full range.
- **Equal endpoints:** Yield the single start date before the first increment, regardless of `step`.
- **Unaligned endpoint:** Stop after the last progression date below `end`; do not force `end` into the output.
- **Leap days and month boundaries:** Epoch-day increments and ISO formatting naturally cross varying month lengths and February 29.
- **Inclusive aligned endpoint:** Use `currentTime <= endTime`, not a strict comparison.
- **Large step:** If the first increment passes `end`, iteration contains only `start`.
