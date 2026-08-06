## Function Contract

**Inputs**

- `logs`: friendship events `[timestamp_i, x_i, y_i]`; the input order need not be chronological.
- `n`: the number of people, labeled consecutively from `0` to `n - 1`.

At each timestamp, the event adds an undirected friendship between its two distinct people. Existing friendships persist. After any chronological prefix of the events, acquaintance groups are the connected components formed by all friendships in that prefix.

**Return value**

Return the earliest event timestamp whose chronological prefix leaves exactly one acquaintance group containing all `n` people. Return `-1` if more than one group remains after every event.
