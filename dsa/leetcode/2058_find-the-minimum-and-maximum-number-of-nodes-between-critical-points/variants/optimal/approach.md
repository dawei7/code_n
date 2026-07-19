## General
**Recognizing critical nodes with three pointers**

Traverse using `previous`, `current`, and `next_node`. The current node is critical when its value is strictly above both neighbors or strictly below both. Starting with the second node and stopping before the tail automatically excludes the endpoints; equal neighboring values satisfy neither strict comparison.

**Keeping only the positions that determine the answers**

Record the first critical position, the immediately previous critical position, and the current minimum gap. When a new critical point appears, its distance from the previous one is a candidate minimum. The maximum distance is always between the first and last critical points because those are the extreme positions.

Consecutive critical points yield every candidate for the minimum: inserting an intermediate critical point can only split a wider gap into no-larger adjacent gaps. The most widely separated pair must use the earliest and latest positions. Thus the retained state is sufficient for both requested extrema.

## Complexity detail
The traversal visits every node once and performs constant work per node, giving $O(n)$ time. It stores a fixed number of pointers, indices, and distances, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Store all critical positions:** A second pass over the position array makes the distance calculations simple but uses $O(n)$ extra space.
- **Compare every critical pair:** This directly finds both extrema but can take $O(n^2)$ time when values alternate.
- The head and tail are never critical, even if their values exceed their sole neighbors.
- Comparisons are strict; a plateau cannot contain a local maximum or minimum.
- Exactly two critical points produce equal minimum and maximum distances.
