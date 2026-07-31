## Examples

**Example 1**

- Input: `tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]`
- Output: `["JFK","MUC","LHR","SFO","SJC"]`

```text
JFK -> MUC -> LHR -> SFO -> SJC
```

**Example 2**

- Input: `tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]`
- Output: `["JFK","ATL","JFK","SFO","ATL","SFO"]`
- Explanation: `["JFK","SFO","ATL","JFK","ATL","SFO"]` is another reconstruction that uses every ticket, but it comes later in lexical order.

```text
Chosen:      JFK -> ATL -> JFK -> SFO -> ATL -> SFO
Other route: JFK -> SFO -> ATL -> JFK -> ATL -> SFO
```
