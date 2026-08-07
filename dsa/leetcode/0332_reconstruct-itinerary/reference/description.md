### 1. Description

You are given a list of airline `tickets` where $\text{tickets}[i] = [\text{from}_{i}, \text{to}_{i}]$ represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

- For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

### 2. Function Contract

**Inputs**

- `tickets`: A list of two-airport entries `[departure,arrival]`, each representing one ticket occurrence.

**Return value**

Return the lexically smallest airport sequence that starts at `"JFK"` and uses every ticket exactly once.

### 3. Examples

#### Example 1

![](images/itinerary1-graph.jpg)

- **Input:** $tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]$
- **Output:** `["JFK","MUC","LHR","SFO","SJC"]`
#### Example 2

![](images/itinerary2-graph.jpg)

- **Input:** $tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]$
- **Output:** `["JFK","ATL","JFK","SFO","ATL","SFO"]`
- **Explanation:** Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

### 4. Constraints

- $1 \le \text{tickets.length} \le 300$

- $\text{tickets}[i].length = 2$

- $\text{from}_{i}.length = 3$

- $\text{to}_{i}.length = 3$

- $\text{from}_{i}$ and $\text{to}_{i}$ consist of uppercase English letters.

- $\text{from}_{i} \neq \text{to}_{i}$