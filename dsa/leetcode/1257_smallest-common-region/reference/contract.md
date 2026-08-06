## Function Contract

### Inputs

- `regions`: Lists describing direct containment. For each list, its first name directly contains every later name in that same list.
- `region1`: The first queried region name.
- `region2`: The second queried region name, distinct from `region1`.

The lists describe one rooted containment hierarchy: a region has at most one direct container, one region contains every other region directly or indirectly, and both queried names belong to the hierarchy.

For the complexity discussion, let

$$
R = \sum_{g \in \texttt{regions}} \lvert g \rvert
$$

be the total number of region-name occurrences across all lists.

### Return value

Return the smallest region that contains both queried regions. Containment includes the region itself.
