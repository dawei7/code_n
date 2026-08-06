## Examples

**Example 1**

- Input: `nums = [2,-1,1,2,2]`
- Output: `true`
- **Explanation:** In the movement graph, positive entries jump forward and the negative entry jumps backward. The route `0 -> 2 -> 3 -> 0 -> ...` is a cycle whose entries are all positive, so it is valid.

```mermaid
flowchart LR
    accTitle: Movement graph for the first circular-array example
    accDescr: Positions 0, 2, and 3 form a forward cycle. Position 1 jumps backward to 0, and position 4 jumps forward to 1.
    n0["0 (+2)"] --> n2["2 (+1)"]
    n2 --> n3["3 (+2)"]
    n3 --> n0
    n1["1 (-1)"] --> n0
    n4["4 (+2)"] --> n1
```

**Example 2**

- Input: `nums = [-1,-2,-3,-4,-5,6]`
- Output: `false`
- **Explanation:** Positions `0` through `4` all jump backward to position `5`. Position `5` jumps to itself, so the only cycle has length one and is invalid.

```mermaid
flowchart TD
    accTitle: Movement graph for the second circular-array example
    accDescr: Every backward-jumping position from 0 through 4 points to position 5. Position 5 has a forward self-loop, which is not a valid multi-position cycle.
    n0["0 (-1)"] --> n5["5 (+6)"]
    n1["1 (-2)"] --> n5
    n2["2 (-3)"] --> n5
    n3["3 (-4)"] --> n5
    n4["4 (-5)"] --> n5
    n5 --> n5
```

**Example 3**

- Input: `nums = [1,-1,5,1,4]`
- Output: `true`
- **Explanation:** Positions `0` and `1` repeat as `0 -> 1 -> 0 -> ...`, but their jumps have opposite signs, so that route is invalid. Position `2` has an invalid one-position self-loop. Positions `3` and `4` form `3 -> 4 -> 3 -> ...`, and both jumps are positive, so this is a valid cycle.

```mermaid
flowchart LR
    accTitle: Movement graph for the third circular-array example
    accDescr: Positions 0 and 1 form a mixed-direction two-position loop, position 2 forms an invalid self-loop, and positions 3 and 4 form a valid all-forward two-position cycle.
    n0["0 (+1)"] --> n1["1 (-1)"]
    n1 --> n0
    n2["2 (+5)"] --> n2
    n3["3 (+1)"] --> n4["4 (+4)"]
    n4 --> n3
```
