## Function Contract

**Inputs**

- `operations`: In cOde(n), a chronological list of `["hit", timestamp]` and `["getHits", timestamp]` calls.

**Return value**

The app adapter returns the result of each `getHits` call, in query order. On LeetCode, construct `HitCounter` and invoke its two methods directly. At time `t`, the counted interval is $(t-300,t]$, so a hit exactly `300` seconds old is excluded.
