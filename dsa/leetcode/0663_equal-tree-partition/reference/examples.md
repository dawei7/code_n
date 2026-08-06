## Examples

**Example 1**

- Input: `root = [5,10,10,null,null,2,3]`
- Output: `true`

The edge from the root value `5` to its right child value `10` can be removed. The component containing `5` then has values `5` and `10`, while the detached subtree has values `10`, `2`, and `3`; both sums are `15`.

```mermaid
flowchart LR
  accTitle: A valid equal-sum partition for Example 1
  accDescr: The original tree has root 5, left child 10, and right child 10 with children 2 and 3. Removing the edge to the right child produces two trees whose values each sum to 15.
  subgraph Original["Original tree"]
    direction TB
    o5((5)) --- o10l((10))
    o5 -. "remove this edge" .- o10r((10))
    o10r --- o2((2))
    o10r --- o3((3))
  end
  subgraph Components["After the cut"]
    direction LR
    subgraph RootComponent["Sum 15"]
      direction TB
      r5((5)) --- r10((10))
    end
    subgraph DetachedSubtree["Sum 15"]
      direction TB
      d10((10)) --- d2((2))
      d10 --- d3((3))
    end
  end
```

**Example 2**

- Input: `root = [1,2,10,null,null,2,20]`
- Output: `false`
- Explanation: No single edge can be removed to make the sums of the two resulting trees equal.

```mermaid
flowchart TB
  accTitle: Example 2 binary tree
  accDescr: The tree has root 1, left child 2, and right child 10 with children 2 and 20. None of its four edges yields equal component sums when removed.
  n1((1)) --- n2l((2))
  n1 --- n10((10))
  n10 --- n2r((2))
  n10 --- n20((20))
```
