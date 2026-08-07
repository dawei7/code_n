[TOC]

## Solution

---

### Approach 1: BFS + DFS

#### Intuition

The problem requires finding the shortest path between two given nodes using step-by-step directions. Shortest path problems are common in graph theory, and several efficient algorithms can be learned to solve them. Let's explore solving the problem with one of these algorithms. 

To apply one of these algorithms, we first must convert the tree to a bidirectional graph. In a binary tree, each node can connect to its children but not directly to its parent. To facilitate all the movement from a node to its parent, we commonly use a `parent` table. This table stores the parent of each node, built by traversing the tree and marking each node's children with their respective parent.

With the ability to traverse the tree in any direction, we first locate the starting node. Once we've identified it, we can then proceed to calculate the shortest path.

To efficiently determine the shortest path, we use a breadth-first search (BFS) to explore nodes at the current depth before moving deeper. For those unfamiliar with BFS, the LeetCode [Explore Card](https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/) provides a helpful introduction.

During the BFS traversal, we use a map `pathTracker` to record the path taken to each node. In `pathTracker`, each key represents a node, while its corresponding value is a pair containing the parent node and the direction from that parent. Upon reaching the destination node, we backtrack using `pathTracker` to trace the path back to the start node. The path string is constructed by appending directions from `pathTracker` and moving to the parent node stored in the tuple.

This process continues until we reach the start node. Since directions are recorded in reverse order during backtracking, we reverse the path string to obtain the correct sequence of directions from the start node to the destination node. Finally, we return this reversed string as the result.

#### Algorithm

Main method `getDirections`:

- Initialize a map `parentMap` to store parent nodes for each node in the tree.
- Find the `startNode` using the `findStartNode` method, which recursively searches the tree for the node with `startValue`.
- Populate `parentMap` using the `populateParentMap` method, which traverses the tree and maps each child node to its parent.
- For the BFS, initialize 
  - A queue containing the `startNode`.
  - A set `visitedNodes` to keep track of visited nodes to avoid cycles.
  - A map `pathTracker` to record the path taken by the BFS.
- While the queue is not empty:
  - Dequeue a TreeNode from the queue.
  - If the current node's value matches `destValue`, we have found our path. Call `backtrackPath` and return the path calculated by it.
- If `parentMap` contains a parent for the current node and it hasn't been visited, enqueue the parent node and add an entry to `pathTracker` with the current node as the key and a pair containing the parent node and direction 'U' as the value.
- If the left child exists and hasn't been visited, enqueue the left child and add an entry to `pathTracker` with the current node as the key and a pair containing the left child and direction 'L' as the value.
- If the right child exists and hasn't been visited, enqueue the right child and add an entry to `pathTracker` with the current node as the key and a pair containing the right child and direction 'R' as the value.
- If the destination node is never reached, an empty string is returned.

Helper method `backtrackPath`:

- Define `backtrackPath` with parameters: destination `node` (TreeNode) and `pathTracker` map.
- Initialize an empty string `path`.
- While `node` exists in `pathTracker`:
  - Retrieve the parent node and direction from `pathTracker`.
  - Append the direction to `path`.
  - Set `node` to the parent node.
- Reverse and return `path`.

Helper method `populateParentMap`:

- Define `populateParentMap` with parameters: current `node` (TreeNode) and `parentMap`.
- If `node` is `null`, return.
- If left or right children exist, add them to `parentMap` with `node` as their parent.
- Recurse on left and right children.

Helper method `findStartNode`:

- Define `findStartNode` with parameters: current `node` (TreeNode) and `startValue`.
- If `node` is `null`, return.
- If `node`'s value matches `startValue`, return `node`.
- Recursively search the left subtree. If a node is found, return it.
- Otherwise, search the right subtree and return the result.

#### Implementation


```python
class Solution:
    def getDirections(
        self, root: TreeNode, startValue: int, destValue: int
    ) -> str:
        # Map to store parent nodes
        parent_map = {}

        # Find the start node and populate parent map
        start_node = self._find_start_node(root, startValue)
        self._populate_parent_map(root, parent_map)

        # Perform BFS to find the path
        q = deque([start_node])
        visited_nodes = set()
        # Key: next node, Value: <current node, direction>
        path_tracker = {}
        visited_nodes.add(start_node)

        while q:
            current_element = q.popleft()

            # If destination is reached, return the path
            if current_element.val == destValue:
                return self._backtrack_path(current_element, path_tracker)

            # Check and add parent node
            if current_element.val in parent_map:
                parent_node = parent_map[current_element.val]
                if parent_node not in visited_nodes:
                    q.append(parent_node)
                    path_tracker[parent_node] = (current_element, "U")
                    visited_nodes.add(parent_node)

            # Check and add left child
            if (
                current_element.left
                and current_element.left not in visited_nodes
            ):
                q.append(current_element.left)
                path_tracker[current_element.left] = (current_element, "L")
                visited_nodes.add(current_element.left)

            # Check and add right child
            if (
                current_element.right
                and current_element.right not in visited_nodes
            ):
                q.append(current_element.right)
                path_tracker[current_element.right] = (current_element, "R")
                visited_nodes.add(current_element.right)

        # This line should never be reached if the tree is valid
        return ""

    def _backtrack_path(self, node, path_tracker):
        path = []
        # Construct the path
        while node in path_tracker:
            # Add the directions in reverse order and move on to the previous node
            path.append(path_tracker[node][1])
            node = path_tracker[node][0]
        path.reverse()
        return "".join(path)

    def _populate_parent_map(self, node, parent_map):
        if not node:
            return

        # Add children to the map and recurse further
        if node.left:
            parent_map[node.left.val] = node
            self._populate_parent_map(node.left, parent_map)

        if node.right:
            parent_map[node.right.val] = node
            self._populate_parent_map(node.right, parent_map)

    def _find_start_node(self, node, start_value):
        if not node:
            return None

        if node.val == start_value:
            return node

        left_result = self._find_start_node(node.left, start_value)

        # If left subtree returns a node, it must be StartNode. Return it
        # Otherwise, return whatever is returned by right subtree.
        if left_result:
            return left_result
        return self._find_start_node(node.right, start_value)
```


#### Complexity Analysis

Let $n$ be the number of nodes in the tree.

- Time complexity: $O(n)$

    The `findStartNode` method traverses the tree once to find the start node, which has a worst case time complexity of $O(n)$ (skewed tree). 

    The `populateParentMap` method visits each node once to populate the map. It has a time complexity of $O(n)$.

    In the worst case, the BFS to find the path might visit all nodes of the tree. Inside the BFS loop, the operations on the set and map are $O(1)$ on average. Thus, the time complexity of the BFS remains $O(n)$.

    The `backtrackPath` method can take at most $O(n)$ time to traverse over the entire length of the resultant path, which can be of length $n$ in the worst case.

    The time complexity of the entire algorithm is sum of these individual complexities, which is $O(n)$.

- Space complexity: $O(n)$

    The `parentMap` stores the parent information for each node, taking $O(n)$ space.

    The `backtrackPath` method stores the length of the final path, which can have a maximum length of $n$.

    The recursive call stacks in the `findStartNode` and `populateParentMap` methods can have a worst case space complexity of $O(n)$ (e.g. a skewed tree).

    The queue for the BFS can contain up to $n/2$ nodes in the worst case (for a complete binary tree). So, it has a space complexity of $O(n/2)$, which simplifies to $O(n)$. The `visitedNodes` set and `pathTracker` map used in the BFS uses another $O(n)$ space each.

    Thus, the overall space complexity of the algorithm is $6 \cdot O(n)$, which simplifies to $O(n)$.

---

### Approach 2: LCA + DFS

#### Intuition

A more optimal method exists to solve a tree problem that doesn't involve converting it to a bidirectional graph. Let's try to solve it as a tree this time.

If we trace paths from the root to the two nodes, we see that these paths share a common segment until a certain point, after which they diverge. This last intersection is the Lowest Common Ancestor (LCA). Since it is the last shared point, any path connecting the two nodes must pass through this LCA. We won't discuss the methods to find the LCA in a binary tree in this article, as it is a separate and popular problem. Here we will be focusing on the application of it. If you are unfamiliar with LCA, check out [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/).

Check out how the LCA is a part of the common paths for the start and destination nodes in this image:

![LCA Image](images/image1.png)

The path between the start node and the destination node can be divided into two parts: the path from the start node to the LCA and the path from the LCA to the destination node. The path from the start node to the LCA consists only of the direction 'U' since all moves are from a child node to a parent node.

To find these paths, we use depth-first search starting from the LCA and moving towards the target nodes. Initially, we explore the left subtree appending 'L' to the path. Upon finding the target node, we return immediately. If not found, we backtrack by replacing 'L' with 'R' to explore the right subtree. If the target node isn't found in either subtree, we backtrack to the parent node. This recursive process continues until the target node is located.

Check out this slideshow to better understand how to find the path for a node:



![Slide 1](images/slideshow_slideshow_slide1.png)

![Slide 2](images/slideshow_slideshow_slide2.png)

![Slide 3](images/slideshow_slideshow_slide3.png)

![Slide 4](images/slideshow_slideshow_slide4.png)

![Slide 5](images/slideshow_slideshow_slide5.png)

![Slide 6](images/slideshow_slideshow_slide6.png)

![Slide 7](images/slideshow_slideshow_slide7.png)

![Slide 8](images/slideshow_slideshow_slide8.png)

![Slide 9](images/slideshow_slideshow_slide9.png)



Now that we have the directions to both the start and destination nodes from the LCA, we can piece together the full path. We transform the path from the LCA to the start node by replacing all directions with "U" and prepend it to the path to the destination node. The resulting sequence gives the step-by-step directions from the start node to the end node in the binary tree

#### Algorithm

Main method `getDirections`:

- Find the `lowestCommonAncestor` of `startValue` and `destValue` using the `findLowestCommonAncestor` method.
- Initialize `pathToStart` and `pathToDest` to store paths from the LCA to the start and destination nodes, respectively.
- Call `findPath` to determine these paths.
- Initialize `directions` to store the final result.
- Add "U" for each step in `pathToStart`.
- Append `pathToDest` to `directions`.
- Return `directions`, which contains the step-by-step directions from the start node to the destination node.

Helper method `findLowestCommonAncestor`:

- Define `findLowestCommonAncestor` with parameters: `node`, `value1`, and `value2`.
- If `node` is null, return `null`.
- If `node`'s value matches `value1` or `value2`, return `node`.
- Recursively search for the LCA in the left and right subtrees, storing results in `leftLCA` and `rightLCA`.
- If `leftLCA` is null, return `rightLCA`.
- If `rightLCA` is null, return `leftLCA`.
- If both `leftLCA` and `rightLCA` contain nodes, the current node is the lowest common ancestor. Return `node`.

Helper method `findPath`:

- Define `findPath` with parameters: `node`, `targetValue`, and `path`.
- If `node` is null, return `false`.
- If `node`'s value matches `targetValue`, return `true`.
- Append "L" to `path` and search the left subtree. If the target node is found, return `true`.
- If not found, remove the last character from `path`.
- Append "R" to `path` and search the right subtree. If the target node is found, return `true`.
- If not found, remove the last character from `path`.
- Return `false` if the target node is not found in either subtree.

#### Implementation


```python
class Solution:
    def getDirections(
        self, root: TreeNode, startValue: int, destValue: int
    ) -> str:
        # Find the Lowest Common Ancestor (LCA) of start and destination nodes
        lowest_common_ancestor = self._find_lowest_common_ancestor(
            root, startValue, destValue
        )

        path_to_start = []
        path_to_dest = []

        # Find paths from LCA to start and destination nodes
        self._find_path(lowest_common_ancestor, startValue, path_to_start)
        self._find_path(lowest_common_ancestor, destValue, path_to_dest)

        directions = []

        # Add "U" for each step to go up from start to LCA
        directions.extend("U" * len(path_to_start))

        # Append the path from LCA to destination
        directions.extend(path_to_dest)

        return "".join(directions)

    def _find_lowest_common_ancestor(
        self, node: TreeNode, value1: int, value2: int
    ) -> TreeNode:
        if node is None:
            return None

        if node.val == value1 or node.val == value2:
            return node

        left_lca = self._find_lowest_common_ancestor(node.left, value1, value2)
        right_lca = self._find_lowest_common_ancestor(
            node.right, value1, value2
        )

        if left_lca is None:
            return right_lca
        elif right_lca is None:
            return left_lca
        else:
            return node  # Both values found, this is the LCA

    def _find_path(
        self, node: TreeNode, target_value: int, path: List[str]
    ) -> bool:
        if node is None:
            return False

        if node.val == target_value:
            return True

        # Try left subtree
        path.append("L")
        if self._find_path(node.left, target_value, path):
            return True
        path.pop()  # Remove last character

        # Try right subtree
        path.append("R")
        if self._find_path(node.right, target_value, path):
            return True
        path.pop()  # Remove last character

        return False
```


#### Complexity Analysis

Let $n$ be the total number of nodes in the tree.

* Time complexity: $O(n)$

    The `findLowestCommonAncestor` method is called once and traverses the tree to find the LCA, which takes $O(n)$ time in the worst case. 
    
    The `findPath` method is called twice, once for the path from the LCA to `startValue` and once for the path to `destValue`. Each call can traverse up to the height of the tree, which is $n$ in the worst case (e.g., a skewed tree), making the total time complexity for both calls $O(n) + O(n) = O(n)$.

    Adding "U" for all upward movements and constructing the final path also takes $O(n)$ time. Therefore, the total time complexity of the entire algorithm is $3 \cdot O(n)$, which simplifies to $O(n)$.

* Space complexity: $O(n)$

    The recursive call stacks for `findLowestCommonAncestor` and `findPath` can each have a space complexity of $O(n)$ in the worst case. The variables `pathToStart`, `pathToDest`, and `directions` can store a path of length up to the height of the tree, which is $O(n)$ in the worst case.

    Combining all elements, the algorithm has a space complexity of $O(n)$.

---

### Approach 3: LCA + DFS (Optimized)

#### Intuition

Instead of focusing on finding the LCA and identifying paths from the LCA to both nodes, we can directly find the full paths from the root to each node and then trim off their common part ourselves. This approach eliminates the need to explicitly find the LCA, resulting in significantly shorter and simpler code.

We'll use the `findPath` method from our previous approach to determine the paths from the root to both the start and end nodes. After obtaining these paths, we identify and remove their common initial segment. Then, we adjust the remaining portion of the start node's path by replacing each step with "U" to indicate upward movement. Finally, we concatenate this adjusted path with the unique part of the end node's path, giving us the step-by-step directions from the start node to the end node.

#### Algorithm

Main method `getDirections`:

- Initialize `startPath` and `destPath` to store paths from the root to the start node and the destination node, respectively.
- Determine `startPath` and `destPath` using `findPath`. 
- Initialize `directions` to store the resultant directions.
- Compare `startPath` and `endPath` to find the length of common path. Store it in `commonPathLength`.
- Iterate through the difference between the length of `startPath` and `commonPathLength`. For each step, add "U" to `directions`.
- From `destPath`, add the directions from index `commonPathLength` to the end of the string to `directions`.
- Return `directions`.

Helper method `findPath`:

- Define `findPath` with parameters: `node`, `targetValue`, and `path`.
- If `node` is `null`, return `false`.
- If `node.val == targetValue`, return `true`.
- Add "L" to `path` and search the left subtree recursively. If the target node is found, return `true`.
- If not found, remove the last character from `path`.
- Add "R" to `path` and search the right subtree recursively. If the target node is found, return `true`.
- If not found, remove the last character from `path`.
- Return `false` if the target node was not found in either subtrees.

#### Implementation


```python
class Solution:
    def getDirections(
        self, root: TreeNode, startValue: int, destValue: int
    ) -> str:
        start_path = []
        dest_path = []

        # Find paths from root to start and destination nodes
        self._find_path(root, startValue, start_path)
        self._find_path(root, destValue, dest_path)

        directions = []
        common_path_length = 0

        # Find the length of the common path
        while (
            common_path_length < len(start_path)
            and common_path_length < len(dest_path)
            and start_path[common_path_length] == dest_path[common_path_length]
        ):
            common_path_length += 1

        # Add "U" for each step to go up from start to common ancestor
        directions.extend("U" * (len(start_path) - common_path_length))

        # Add directions from common ancestor to destination
        directions.extend(dest_path[common_path_length:])

        return "".join(directions)

    def _find_path(self, node: TreeNode, target: int, path: List[str]) -> bool:
        if node is None:
            return False

        if node.val == target:
            return True

        # Try left subtree
        path.append("L")
        if self._find_path(node.left, target, path):
            return True
        path.pop()  # Remove last character

        # Try right subtree
        path.append("R")
        if self._find_path(node.right, target, path):
            return True
        path.pop()  # Remove last character

        return False
```


#### Complexity Analysis

Let $n$ be the number of nodes in the tree.

* Time complexity: $O(n)$

    The `findPath` method is called twice, once for the start node and once for the destination node. Each call may traverse the entire tree in the worst case (skewed tree), making the time complexity $2 \cdot O(n)$, which simplifies to $O(n)$.

    To construct the final result, we iterate over the entire lengths of `startPath` and `destPath`, each of which could have a complexity of $O(n)$ in the worst case. 

    Thus, the overall time complexity of the algorithm is $O(n) + O(n)$, simplifying to $O(n)$. 

* Space complexity: $O(n)$

    The recursive call stack of the `findPath` method can have a space complexity of $O(n)$ in the worst case. The variables `startPath`, `destPath`, and `directions` can each have a length equal to the height of the tree, which is $n$ in the worst case (skewed tree). 

    Thus, the total space complexity of the algorithm is $4 \cdot O(n)$, or $O(n)$.

---