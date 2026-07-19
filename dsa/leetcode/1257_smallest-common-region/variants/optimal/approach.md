## General
The hierarchy is a rooted tree whose edges point from a containing region to each directly contained region. Convert the list representation into a `parent` map by recording the first entry of each list as the parent of every later entry.

**Mark one complete ancestor chain**

Starting at `region1`, repeatedly follow the parent map and insert every visited region into a set, including `region1` itself and the root. This set contains exactly the regions that contain the first query.

**Find the lowest shared ancestor**

Starting at `region2`, walk upward until the current region belongs to the first chain's set. Every earlier region on this upward walk is lower but does not contain `region1`. Therefore, the first match is precisely the smallest region containing both queries. Including the query regions themselves naturally handles the case where one contains the other.

The guarantee that a common region exists means the second walk must reach a match no later than the root.

## Complexity detail
Building the parent map examines the $R$ region-name occurrences once. Both ancestor walks traverse at most the number of distinct regions, which is $O(R)$, so total time is $O(R)$. The parent map and ancestor set use $O(R)$ space.

## Alternatives and edge cases
- **Scan lists for every parent:** It avoids a map but may rescan all hierarchy lists at every level and take $O(R^2)$ time on a deep tree.
- **Recursive subtree search:** Finding paths from the root to both regions and comparing them is correct, but requires building child adjacency and managing two paths.
- **One region contains the other:** Because each chain begins at the region itself, the ancestor region is returned directly.
- **Different root branches:** Their smallest common region may be the root.
- **Direct siblings:** Their recorded parent is the answer after one upward step.
- **Names containing spaces:** Treat complete strings as opaque keys; no parsing of region names is needed.
