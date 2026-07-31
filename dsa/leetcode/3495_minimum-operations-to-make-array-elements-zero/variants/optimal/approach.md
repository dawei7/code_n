## General

An integer $x>0$ becomes zero after exactly

$$
d(x)=\lfloor\log_4 x\rfloor+1
$$

divisions by four. Think of these as unit tasks attached to that array entry. One operation completes one task from each of two selected entries, so a query with total workload $S$ needs at least $\lceil S/2\rceil$ operations. It also needs at least $\max d(x)$ operations for its deepest individual entry.

For the consecutive interval `[l, r]`, the second lower bound never exceeds the first. If $d(r)=D$, then $d(r-1)\ge D-1`; because `l < r`, both values occur in the interval. Their combined workload is at least $2D-1$, so $\lceil S/2\rceil\ge D$. Pairing entries with remaining work therefore realizes the total-work bound, and the query answer is exactly $\lceil S/2\rceil$.

Compute $S$ without enumerating the interval. All integers in $[4^{k-1},4^k-1]$ have depth $k$. A prefix function sums the overlap of `[1, x]` with each such power-of-four band, multiplied by that band's depth. Then the workload for `[l, r]` is `prefix_steps(r) - prefix_steps(l - 1)`.

## Complexity detail

Let $q$ be the number of queries and $R$ the largest right endpoint. A prefix evaluation visits $O(\log_4 R)$ power-of-four bands, twice per query, for $O(q\log R)$ time and $O(1)$ auxiliary space. Under the stated bound $R\le10^9$, there are at most fifteen bands, so the running time is effectively linear in the input query count.

The benchmark size is $q$. Each tier contains $q$ intervals of width $q$ near $10^8$, keeping all inputs legal while the prefix method still does constant bounded-band work per query. The calibrated slower implementation enumerates all $q$ represented integers in every interval and therefore scales as $\Theta(q^2)$.

## Alternatives and edge cases

- **Enumerate every integer in each interval:** Directly summing `d(x)` is correct but can require up to $10^9$ work for one query.
- **Priority queue simulation:** Repeatedly pairing the two greatest remaining depths mirrors an optimal schedule, but materializing the interval and simulating operations is far more expensive than counting tasks.
- **Use only the maximum depth:** This misses the total workload contributed by the many smaller values.
- **Odd total workload:** One final operation pairs the last positive value with an already-zero entry, which is why the answer rounds upward.
- **Power-of-four boundaries:** The depth increases exactly at `1`, `4`, `16`, and subsequent powers, so prefix bands must use inclusive endpoints carefully.
- **Two-element intervals:** The proof still applies; if the larger value just entered a new band, the other value needs at least one fewer step.
- **Large aggregate answer:** Summing as many as $10^5$ query results requires wide integer arithmetic in fixed-width languages.
