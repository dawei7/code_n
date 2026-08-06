## Examples

**Example 1**

- **Input:** `n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]`
- **Output:** `6`
- **Explanation:** Any two sides of this three-city cycle connect all cities. Selecting the connections of costs `1` and `5` gives the least possible sum, $1 + 5 = 6$.

The source diagram is reproduced independently below. Edge labels record both the cost and whether the minimum selection uses that connection.

```mermaid
---
config:
  flowchart:
    nodeSpacing: 40
    rankSpacing: 45
---
graph LR
    accTitle: Minimum-cost connections among three cities
    accDescr: Cities 1, 2, and 3 form a triangle. The cost-5 edge from 1 to 2 and cost-1 edge from 2 to 3 are chosen; the cost-6 edge from 1 to 3 is omitted.
    C1((1)) ---|cost 5; chosen| C2((2))
    C1 ---|cost 6; omitted| C3((3))
    C2 ---|cost 1; chosen| C3
```

**Example 2**

- **Input:** `n = 4, connections = [[1,2,3],[3,4,4]]`
- **Output:** `-1`
- **Explanation:** Using every available connection still leaves the pair `{1, 2}` disconnected from the pair `{3, 4}`, so all four cities cannot be connected.

The source diagram is reproduced independently as the two disconnected components:

```mermaid
---
config:
  flowchart:
    nodeSpacing: 45
    rankSpacing: 45
---
graph LR
    accTitle: Two disconnected pairs of cities
    accDescr: City 1 connects to city 2 at cost 3, and city 3 connects to city 4 at cost 4. No connection joins the two pairs.
    C1((1)) ---|cost 3| C2((2))
    C3((3)) ---|cost 4| C4((4))
```
