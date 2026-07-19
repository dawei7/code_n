## General
**Each subtree needs two answers, not one**

For every node, compute a pair `(skip, take)`. `skip` is the best value in its subtree when the node itself is not robbed; `take` is the best when it is robbed. A single best value would lose the information a parent needs to enforce adjacency.

If the node is taken, neither child may be taken, so
`take = node.value + left.skip + right.skip`.
If the node is skipped, each child independently chooses its better state, so
`skip = max(left.skip, left.take) + max(right.skip, right.take)`.

An empty child contributes `(0, 0)`. The final answer is the larger state at the root because the root has no parent imposing a choice.

**Grandchildren are included through child skip states**

Taking a node does not mean discarding its entire child subtrees. Requiring a child to be skipped still lets that child's own `skip` state select grandchildren or deeper descendants. This is why the two-state recurrence captures choices such as robbing a root together with all profitable grandchildren.

For `[3,4,5,1,3,null,1]`, taking the root combines it with grandchildren for value eight, while skipping it lets the left subtree contribute four and the right subtree five, producing the optimum nine.

**Postorder makes both child decisions final before the parent**

Use an explicit stack of `(node, expanded)` entries. A first visit schedules the node after its children; the expanded visit reads both child pairs and stores the node pair. This reproduces recursive postorder without risking call-stack overflow on a deep tree.

By induction, each child pair is optimal under its stated take/skip condition. The parent recurrence enumerates the only two possibilities for the parent and, within each, combines independent optimal child choices allowed by that condition. Therefore the stored pair is optimal for the parent subtree, and the root maximum is globally optimal.

## Complexity detail
Every node is pushed a constant number of times and summarized once, giving $O(n)$ time. The explicit stack and state table contain at most $O(n)$ nodes, using $O(n)$ space.

## Alternatives and edge cases
- **Recurse separately on children and grandchildren without memoization:** repeats subtrees and can take exponential time.
- **Always choose the larger of a parent and its children:** ignores profitable combinations deeper in both branches.
- **Memoized recursion:** has the same $O(n)$ bound but may exceed the language recursion limit on a very deep tree.
- An empty tree returns zero. A single node returns its value, and a one-child tree chooses the larger nonadjacent arrangement.
