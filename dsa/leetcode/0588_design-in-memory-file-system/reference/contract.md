## Function Contract

**LeetCode interface**

Construct one `FileSystem` object and invoke `ls`, `mkdir`, `addContentToFile`, and `readContentFromFile` in sequence. Mutating calls return `null`; query calls return the requested list or string.

**cOde(n) adapter**

- `operations`: a sequence whose entries begin with `"ls"`, `"mkdir"`, `"addContentToFile"`, or `"readContentFromFile"`, followed by that call's arguments.

`solve(operations)` creates a fresh `FileSystem`, applies the entries in order, and returns the results from `ls` and `readContentFromFile` calls. Mutation calls produce no adapter result entry.

For complexity notation, let $P$ be the number of path components traversed, $k$ the number of immediate names returned by a directory listing, $C$ the content length processed by an operation, and $S$ the total stored filesystem state.
