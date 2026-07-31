## Custom Testing

- In LeetCode's custom input, provide the complete list `head` and identify the actual node `node` that will be passed. That node must belong to the list and must not be its last node.
- The judge constructs the list and passes only that node to the function.
- After the function returns, the judge displays the entire resulting list as the output.

The app-local adapter represents the same direct-node contract by passing the suffix that starts at `node`; it does not give the solution access to the preceding link.
