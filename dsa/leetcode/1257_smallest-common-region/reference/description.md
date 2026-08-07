## Description

You are given some lists of `regions` where the first region of each list **directly** contains all other regions in that list.

If a region `x` contains a region `y` *directly*, and region `y` contains region `z` *directly*, then region `x` is said to contain region `z` **indirectly**. Note that region `x` also **indirectly** contains all regions **indirectly** containd in `y`.

Naturally, if a region `x` contains (either *directly* or *indirectly*) another region `y`, then `x` is bigger than or equal to `y` in size. Also, by definition, a region `x` contains itself.

Given two regions: `region1` and `region2`, return *the smallest region that contains both of them*.

It is guaranteed the smallest region exists.
### Function Contract

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

### Examples
#### Example 1

- **Input:** ``
**regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
- **Output:** `"North America"`
#### Example 2

- **Input:** $regions = [["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 = "South America"$
- **Output:** `"Earth"`
### Constraints

- $2 \le \text{regions.length} \le 10^{4}$

- $2 \le \text{regions}[i].length \le 20$

- $1 \le \text{regions}[i][j].length, \text{region1.length}, \text{region2.length} \le 20$

- $region1 \neq region2$

- $\text{regions}[i][j]$, `region1`, and `region2` consist of English letters.

- The input is generated such that there exists a region which contains all the other regions, either directly or indirectly.

- A region cannot be directly contained in more than one region.