## Function Contract

**Inputs**

- `buckets`: The number of buckets, exactly one of which contains poison.
- `minutesToDie`: The number of minutes between a pig consuming poison and dying.
- `minutesToTest`: The total number of minutes available for all testing rounds.

**Return value**

- Return the minimum number of pigs sufficient to identify the poisoned bucket with certainty.

Only complete `minutesToDie` intervals create additional observable death outcomes.
