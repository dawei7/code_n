## General
**Store only timestamps that can still be recent.** Maintain a double-ended queue in increasing timestamp order. On `ping(t)`, append `t`, then compute the inclusive lower boundary `t - 3000`.

**Expire requests from the front.** While the oldest timestamp is strictly less than the lower boundary, remove it from the left of the queue. Strict comparison is essential: a request exactly at `t - 3000` is still inside the inclusive interval and must remain. Because timestamps arrive in increasing order, once the oldest request is valid, every later queued timestamp is valid as well.

**Return the active queue size.** After expiration, the queue contains exactly the requests in $[t-3000,t]$, so its length is the required answer. Each timestamp is appended once and removed at most once over the entire operation sequence. This gives constant amortized work per call even if one call removes many old requests.

## Complexity detail
Across $m$ calls, every timestamp enters and leaves the queue at most once, so the total time is $O(m)$. In the worst case all $m$ requests fall within one 3000-millisecond interval and remain stored, requiring $O(m)$ space.

## Alternatives and edge cases
- **Scan all previous timestamps:** Count qualifying requests from the complete history after every ping. It is correct but costs $O(m^2)$ total time.
- **Binary search in retained full history:** Find the first qualifying timestamp in $O(\log m)$ per call, but never discarding obsolete history uses $O(m)$ space and is slower than the queue's amortized bound.
- **Inclusive left boundary:** A timestamp equal to `t - 3000` must be counted; remove only smaller values.
- **Large gap between calls:** One ping may empty the old queue, after which the new request still makes the answer at least one.
- **First request:** With no older timestamps, the result is exactly one.
