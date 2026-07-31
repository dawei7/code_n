## Custom Testing

- In LeetCode's custom input, provide the complete list `head` and identify the actual node `node` that will be passed. That node must belong to the list and must not be its last node.
- The judge constructs the list and passes only that node to the function.
- After the function returns, the judge displays the entire resulting list as the output.

In JSON cases, the runner represents that direct-node contract with the suffix beginning at `node`. It reconstructs the linked nodes before calling `solve(node)`, so the solution still receives only the node object and cannot access a preceding link.
