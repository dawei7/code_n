## General

Serializing only the node values is not enough to reconstruct an arbitrary binary tree. Two different shapes can contain the same values in the same broad traversal order. The encoding must preserve both pieces of information:

- the value stored at every real node;
- the positions where a left or right child is absent.

The exact source uses a breadth-first traversal with `#` as an explicit null marker. Commas separate tokens. Deserialization reads those tokens in the same breadth-first parent order and assigns exactly two child tokens to each real node.

The local manifest calls this an iterative preorder codec, but `solution.py` actually uses queues and level-order processing. This document follows the executable breadth-first format exactly.

**The serialization format**

For a nonempty tree, each token is one of the following:

- the decimal text of a real node value, such as `7`, `0`, or `-12`;
- `#`, meaning that this particular child position is empty.

The comma delimiter makes adjacent signed or multi-digit values unambiguous. The null marker cannot be confused with an integer because valid node values are serialized through `str(node.val)`, and no integer representation is `#`.

The empty tree has a special representation: the empty string. It never enters the breadth-first loop. A nonempty tree can never serialize to the empty string because it always begins with the root value.

The format does not trim trailing null markers. That choice makes decoding especially direct: every real node always has two following child-position tokens somewhere in the sequence, even when it is a leaf.

**Serializing with a queue**

For a nonempty root, `q = deque([root])` starts a queue with one pending position. The list `ans` collects text tokens. Each loop iteration removes the leftmost queued item with `popleft()`.

If the item is a real node, the algorithm:

1. appends the node's value as text;
2. enqueues its left child reference;
3. enqueues its right child reference.

Either child reference may be `None`, and that is intentional. Empty child positions must reach the queue so that their structural markers are emitted.

If the removed item is `None`, the algorithm appends `#` and enqueues nothing. An absent node has no children of its own, so expanding it further would create an infinite sequence of absent descendants.

Because the queue processes a parent before its children and processes siblings from left to right, the tokens appear in level order. Finally, `",".join(ans)` combines them into one string without ambiguity.

**Why null markers preserve shape**

Consider a root with only a left child and another root with only a right child. If null positions were omitted, both might appear as the same two value tokens. With explicit markers, their encodings differ:

- left child only: `root,left,#,...`;
- right child only: `root,#,right,...`.

The marker occupies the exact child slot that is absent. It is therefore not merely saying that some null exists; its location says whether the missing link was a left child or a right child of a particular parent.

For any nonempty binary tree with $N$ real nodes, there are $2N$ child pointers in total. Exactly $N-1$ of those pointers connect to other real nodes, because a tree with $N$ nodes has $N-1$ edges. The remaining

$$
2N-(N-1)=N+1
$$

child pointers are null. Serialization emits one token for each real node and one token for each null child pointer, for a total of

$$
N+(N+1)=2N+1
$$

tokens. This complete accounting is what lets the decoder consume the stream without guessing where the tree ends.

**Example serialization**

For `root = [1,2,3,null,null,4,5]`, breadth-first processing emits

`1,2,3,#,#,4,5,#,#,#,#`.

The first three tokens are the root and its two children. The next two `#` tokens are the absent children of node 2. Tokens `4` and `5` are the children of node 3. The final four markers are the two absent children of node 4 and the two absent children of node 5.

Keeping those final markers may look redundant to a human reader, but it gives every real node a uniform pair of child tokens and keeps the decoding logic small and deterministic.

**Deserializing the token stream**

If `data` is empty, the source returns `None`, reversing the serializer's empty-tree case.

Otherwise, `data.split(",")` creates the token list `vals`. The first token must be the non-null root value, so the source converts it with `int(vals[0])`, constructs the root, and puts that real node in a queue. The index `i = 1` identifies the next unconsumed token.

The decoder's queue contains real nodes whose child positions still need to be filled. For each queued parent, it consumes exactly two tokens in order:

1. The first token describes the left child. If it is not `#`, create a `TreeNode`, assign it to `node.left`, and enqueue that new real child. Then increment `i`.
2. The second token describes the right child. If it is not `#`, create and attach the right node and enqueue it. Then increment `i` again.

A `#` token causes no node construction and no enqueue, leaving the corresponding child at its default null value. A numeric token creates a real child that will later consume its own two tokens.

This process mirrors serialization. Serialization enqueues left and right child positions for each real parent; deserialization consumes the left and right tokens for each real parent. Serialization enqueues descendants in breadth-first order; deserialization enqueues newly created descendants in that same order.

**A decoding invariant**

At the start of each loop iteration, every token before index `i` has already been assigned, and the front of `q` is the earliest real node whose two child tokens have not yet been consumed. Reading the next two tokens fills exactly those two links. Any real children are appended behind the other parents already waiting at the same or earlier level, preserving breadth-first order.

When the queue becomes empty, every created real node has received both child decisions. Since the input came from `serialize`, there are neither missing child tokens nor unrelated extra structure. The returned root consequently has the same values in the same left/right positions as the original tree.

**Why round-trip reconstruction is exact**

For an empty tree, serialization returns the empty string and deserialization returns `None`.

For a nonempty tree, begin with the root. Its first token recreates the same value. The following two tokens state exactly whether its left and right children exist and, when they do, give their values. Those real children enter the decoder queue in the same order in which the serializer enqueued the original children. Repeating this argument for each queued real node reproduces every edge and every missing edge. Because each move through the queues is deterministic, `deserialize(serialize(root))` reconstructs the original structure and values.

## Complexity detail

Let $N$ be the number of real nodes. A nonempty encoding contains $N$ value tokens and $N+1$ null tokens, so serialization processes $2N+1$ queue items. Each item performs constant structural work. Joining the tokens also visits the serialized characters once. Since node values are bounded between $-1000$ and $1000$, each value token has bounded length, and total serialization time is $O(N)$.

Deserialization splits $O(N)$ tokens and processes every real node exactly once. Each numeric token is converted once, and each non-root node is created and enqueued once. Its time complexity is therefore $O(N)$.

The serialization output itself contains $O(N)$ tokens. `ans` holds those tokens before joining, and the queue can hold $O(N)$ pending positions at the widest level, so serialization uses $O(N)$ auxiliary space including its output construction.

During deserialization, `vals` holds $O(N)$ tokens, the queue can contain $O(N)$ real nodes, and the reconstructed tree contains $O(N)$ nodes. Thus, deserialization also uses $O(N)$ space. The traversal is iterative, so it does not consume a recursion stack proportional to tree height.

## Alternatives and edge cases

- **Recursive preorder with null markers:** Emit root, left subtree, then right subtree, writing a null marker for missing nodes. It is also unambiguous and linear, but a tree with up to $10^4$ nodes can exceed Python's default recursion depth if highly skewed.
- **Breadth-first encoding with trimmed trailing nulls:** Removing redundant final markers makes strings shorter, but the decoder must recognize end-of-input and treat missing trailing positions as null. The exact source instead keeps the uniform two-token-per-node rule.
- **Values without null markers:** Traversal values alone cannot distinguish different arbitrary binary-tree shapes. Null positions or an equivalent structural encoding are required.
- **Using inorder traversal alone:** Even with distinct values, inorder values do not uniquely identify an arbitrary tree without another traversal or structural markers.
- **A binary structural encoding:** Values and shape bits could be packed more compactly, but the comma-separated text format is simpler to inspect and satisfies the unrestricted contract.
- **Empty tree:** `serialize(None)` returns `""`, and `deserialize("")` returns `None`. No root token is accessed.
- **Single node:** A leaf with value 7 serializes as `7,#,#`. The two markers explicitly close its left and right child positions.
- **Only a left child:** The right-child `#` remains essential; otherwise the decoder could mistake the child orientation.
- **Only a right child:** The left-child `#` appears before the right value, preserving the missing left link.
- **Node value zero:** A `TreeNode` object is truthy even when `node.val` is 0, so `if node` tests whether the node reference exists rather than whether its stored value is nonzero.
- **Negative values:** The minus sign is part of the numeric token and does not conflict with commas or `#`. `int` restores the signed value.
- **Repeated values:** Reconstruction does not rely on uniqueness. Queue position and null markers determine structure, so identical values at several nodes are safe.
- **A very skewed tree:** The iterative queues avoid recursive call-stack overflow. The token count remains $2N+1$.
- **A wide tree:** The queue may hold an entire level and therefore can grow to $O(N)$, which is included in the space bound.
- **Malformed external strings:** The decoder assumes data produced by its matching serializer. It does not validate invalid integers, missing child tokens, or extra tokens because the required contract is round-trip compatibility, not parsing arbitrary hostile input.
- **LeetCode's display format:** The problem explicitly permits any internal serialization. This codec's untrimmed `#` format need not match the level-order list shown in test-case displays as long as its own decoder reverses it exactly.
