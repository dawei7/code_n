[TOC]

## Solution

---

### Approach: Topological Sorting 

#### Intuition   

> If you are not familiar with topological sorting, please refer to our explore cards [Topological Sorting Explore Card](https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/). We will focus on the usage in this article and not the underlying principles or implementation details.

Topological sorting is an algorithm used to arrange a set of nodes with directed edges in a linear order, such that for every directed edge `(u, v)`, node `u` appears before node `v` in the ordering. 

![img](images/1.png)

The key idea behind topological sorting is to identify nodes that have no incoming edges (indegree = 0), indicating they have no dependencies on other nodes. These nodes are placed at the beginning of the ordering. Subsequently, we iteratively process the remaining nodes, eliminating their incoming edges and adding them to the order. This process continues until all nodes are placed in the final order.


![img](images/2.png)

However, if the number of visited nodes is less than the total number of nodes, it indicates the presence of a cycle in the graph.

![img](images/2_2.png)

<br>

In this problem, we are dealing with a more complex variation of the topological sorting algorithm. The directed edges are described by `beforeItems`, but we have an additional requirement. Specifically, we need to consider the condition that nodes within the same group must be next to each other. For instance, in the following scenario, there are several nodes belonging to different groups, making it impossible to find a valid arrangement.


![img](images/3.png)

Since the problem statement specifies that nodes within the same group must be grouped together, during the sorting process, if one of the nodes belongs to a particular group `i`, it implies that we also have dependencies with all the nodes within the group `i`.


![img](images/4.png)

Therefore, when performing topological sorting, it is crucial to gather all nodes belonging to the same group and ensure their relative order based on their dependencies. A rough example demonstrating this concept is depicted in the diagram below.

![img](images/5.png)

Consequently, the objective is to achieve two levels of sorting: 

- sorting the groups based on the group dependencies, 
- sorting the items within each group according to the item dependencies. 

As a preliminary step, it is important to consider items that do not belong to any group (`group[i] = -1`) as separate groups, each consisting of only a single item.

![img](images/6.png)

<br>

Firstly, we perform a topological sort on the items. The topological sort ensures that items are processed in an order that respects their dependencies, regardless of the groups they belong to.

It's important to note that this sorted order may **not** always be correct for items that belong to different groups, as depicted by items with red marks, since this topological sort only considers the dependencies of items. For instance, in the picture below, the items belonging to the green group are not interconnected, but we can infer that their order, if connected within the green group, should be `I, II, III`.

![img](images/ig.png)

Afterward, we take into account the dependencies between groups. Whenever we encounter two nodes from different groups, it signifies a precedence relationship between the respective groups. As a result, we sort these groups accordingly, establishing the relationship that determines the order in which they should be processed.

![img](images/sg.png)

Finally, let's combine both the sorted groups and sorted items. Note that if the topological sort on either the groups or items detects a cycle, then the task is impossible. This ensures that groups are processed in an order that respects their dependencies, and within each group, the items are processed in an order that respects their dependencies.


![img](images/combine.png)

<br>

To be more specific, when sorting all the items (without group dependencies), we iterate through them and assign each item to its corresponding group. By doing so, at the end of the iteration, the items within each group will be properly ordered based on their dependencies within that particular group.

![img](images/cb2.png)

After the iteration, we successfully collect all items in each group with correct order. We then refer to the previously established sorted order of the groups and arrange the items within each group accordingly.

![img](images/cb3.png)

Finally, the groups are sorted based on the group dependencies, and items within each group are also sorted based on the their individual dependencies. 


<br>

#### Algorithm

1) Initialize `group_id` as `m`. Iterate over each item `i`, if it does not belong to any group, assign it a unique group id `group_id`, and increment `group_id` by 1.

2) Construct two adjacency maps `item_graph` and `group_graph` for all items and groups, respectively. Build two in degree list `item_indegree` and `group_indegree` for all items and groups, respectively.

3) Traverse through `beforeItems`, add every pair of items dependency `(prev, curr)` as a dependency to `item_graph`, and increment the indegree of `curr` by 1. If two items belong to different groups `group[prev]` and `group[curr]`, add the group dependency to `group_graph`, and increment the indegree of `group[curr]` by 1.


4) Perform a topological sorting of items according to `item_graph` and `item_indegree`. If there is a cycle, the task is impossible.


5) Perform a topological sorting of groups based on `group_graph` and `group_indegree`. If there is a cycle, the task is impossible.


6) Create an empty list `answer` to store the final order and a hash map `ordered_groups` to store the sorted items within each group.

7) Iterate over the sorted items, and for each item `i`, add it to `ordered_groups` while preserving its original order within the group: `ordered_groups[group[i]].append(i)`.

8) Traverse through the sorted groups, and for each group `group_index`, add all its items `order_groups[group_index]` to `answer` while maintaining their original order.


#### Implementation


```python
class Solution:
    def sortItems(self, n, m, group, beforeItems):
        # If an item belongs to zero group, assign it a unique group id.
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        # Sort all item regardless of group dependencies.
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        
        # Sort all groups regardless of item dependencies.
        group_graph = [[] for _ in range(group_id)]
        group_indegree = [0] * group_id      
        
        for curr in range(n):
            for prev in beforeItems[curr]:
                # Each (prev -> curr) represents an edge in the item graph.
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                
                # If they belong to different groups, add an edge in the group graph.
                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1      
        
        # Tologlogical sort nodes in graph, return [] if a cycle exists.
        def topologicalSort(graph, indegree):
            visited = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for neib in graph[cur]:
                    indegree[neib] -= 1
                    if indegree[neib] == 0:
                        stack.append(neib)
            return visited if len(visited) == len(graph) else []

        item_order = topologicalSort(item_graph, item_indegree)
        group_order = topologicalSort(group_graph, group_indegree)
        
        if not item_order or not group_order: 
            return []
        
        # Items are sorted regardless of groups, we need to 
        # differentiate them by the groups they belong to.
        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)
        
        # Concatenate sorted items in all sorted groups.
        # [group 1, group 2, ... ] -> [(item 1, item 2, ...), (item 1, item 2, ...), ...]
        answer = []
        for group_index in group_order:
            answer += ordered_groups[group_index]
        return answer
```



#### Complexity Analysis

* Time complexity: $O(n^2)$

    To topological sort $n$ items:
    - We build an adjacency list that contains all item dependencies. There are at most $O(n^2)$ distinct item dependencies `(prev, curr)` stored in `beforeItem`, which takes $O(n^2)$ time.
    - Next, we repeatedly visit each item with an in degree of zero and decrement the in degree of all items that have this item as a preceding item. In the worst-case scenario, we might visit every vertex in the graph and decrement every outgoing edge once, which takes $O(n^2)$ time.

    The maximum number of groups is $n$, so the time complexity of topological sorting the groups is also $O(n^2)$.


* Space complexity: $O(n)$
    
    - Both adjacency lists take $O(n^2)$ space in the worst-case scenario.
    - Storing the in degree for each item or group requires $O(n)$ space.
    - The stack can contain at most $n$ items or $n$ groups, which takes $O(n)$ space.


<br/>