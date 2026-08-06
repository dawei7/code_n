## Examples

**Example 1**

- Input: `graph = [[1,1,0],[0,1,0],[1,1,1]]`

Ignoring self-relationships, the directed “knows” edges are:

```mermaid
flowchart LR
    accTitle: Example 1 acquaintance graph
    accDescr: Person 0 knows person 1, and person 2 knows both people 0 and 1. Person 1 knows nobody else.
    P0["0"] --> P1["1"]
    P2["2"] --> P0
    P2 --> P1
```

- Output: `1`
- Explanation: The attendees are labeled `0`, `1`, and `2`. Both `0` and `2` know person `1`, while person `1` knows neither of them, so `1` is the celebrity.

**Example 2**

- Input: `graph = [[1,0,1],[1,1,0],[0,1,1]]`

Ignoring self-relationships, the directed edges form a cycle:

```mermaid
flowchart LR
    accTitle: Example 2 acquaintance cycle
    accDescr: Person 0 knows person 2, person 2 knows person 1, and person 1 knows person 0, forming a cycle.
    P0["0"] --> P2["2"] --> P1["1"] --> P0
```

- Output: `-1`
- Explanation: No attendee is a celebrity.
