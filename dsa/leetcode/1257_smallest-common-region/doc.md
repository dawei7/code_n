# Smallest Common Region

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1257 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Tree, Depth-First Search, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-common-region/) |

## Problem Description

### Goal

Regions form a containment hierarchy. Each list in `regions` starts with a parent region, followed by regions it directly contains. Containment is transitive: if one region contains a second and the second contains a third, then the first also contains the third.

Given two distinct region names, return the smallest region that contains both of them. A region contains itself for this purpose, so one query region may be the answer when it contains the other. The input describes a valid rooted hierarchy, both query names occur in it, and a common containing region is guaranteed.

### Function Contract

**Inputs**

- `regions`: hierarchy lists in which `regions[i][0]` directly contains every later name in that list.
- `region1`: the first region name.
- `region2`: the second, distinct region name.
- Let $R=\sum_{g\in\texttt{regions}}\lvert g\rvert$ be the total number of region-name occurrences in the hierarchy lists.

**Return value**

- Return the lowest region in the hierarchy that contains both `region1` and `region2`.

### Examples

**Example 1**

- Input: `regions = [["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]]`, `region1 = "Quebec"`, `region2 = "New York"`
- Output: `"North America"`

**Example 2**

- Input: the same hierarchy, `region1 = "Canada"`, `region2 = "South America"`
- Output: `"Earth"`

**Example 3**

- Input: the same hierarchy, `region1 = "North America"`, `region2 = "Quebec"`
- Output: `"North America"`

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

The hierarchy is a rooted tree whose edges point from a containing region to each directly contained region. Convert the list representation into a `parent` map by recording the first entry of each list as the parent of every later entry.

**Mark one complete ancestor chain**

Starting at `region1`, repeatedly follow the parent map and insert every visited region into a set, including `region1` itself and the root. This set contains exactly the regions that contain the first query.

**Find the lowest shared ancestor**

Starting at `region2`, walk upward until the current region belongs to the first chain's set. Every earlier region on this upward walk is lower but does not contain `region1`. Therefore, the first match is precisely the smallest region containing both queries. Including the query regions themselves naturally handles the case where one contains the other.

The guarantee that a common region exists means the second walk must reach a match no later than the root.

#### Complexity detail

Building the parent map examines the $R$ region-name occurrences once. Both ancestor walks traverse at most the number of distinct regions, which is $O(R)$, so total time is $O(R)$. The parent map and ancestor set use $O(R)$ space.

#### Alternatives and edge cases

- **Scan lists for every parent:** It avoids a map but may rescan all hierarchy lists at every level and take $O(R^2)$ time on a deep tree.
- **Recursive subtree search:** Finding paths from the root to both regions and comparing them is correct, but requires building child adjacency and managing two paths.
- **One region contains the other:** Because each chain begins at the region itself, the ancestor region is returned directly.
- **Different root branches:** Their smallest common region may be the root.
- **Direct siblings:** Their recorded parent is the answer after one upward step.
- **Names containing spaces:** Treat complete strings as opaque keys; no parsing of region names is needed.

</details>
