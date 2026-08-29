## General

**The supplied node is a location, not necessarily the head.** A normal linked-list conversion begins from the head and follows `next` pointers. Here the caller may provide any node in the doubly linked list, including the tail or a middle node. Starting the output immediately from that node would omit every value before it. The `prev` links are what allow the algorithm to recover the true beginning.

The source has two simple phases. First, while `node.prev` exists, it replaces `node` with `node.prev`. Each step moves exactly one position toward the head. In a valid finite doubly linked list, this process stops at the unique node whose `prev` pointer is `None`. At that moment `node` is the head regardless of which original node was supplied.

Second, the source initializes `ans` and walks forward while `node` is not `None`. On every node, it appends `node.val` and advances through `node.next`. This is precisely the list's natural order from head to tail, so the returned Python list contains all values in order.

**Why two directions do not duplicate nodes in the answer.** The backward phase does not append anything. Its only purpose is navigation. Once it reaches the head, the forward phase performs the complete collection exactly once. The originally supplied node will be visited during the forward pass along with all other nodes, but it is appended only in that pass.

For example, suppose the list is `1 <-> 2 <-> 3 <-> 4` and the given node contains `3`. The first loop visits `2` and then `1`, stopping because `1.prev` is absent. The second loop appends `1`, `2`, `3`, and `4`. Starting at the head would make the backward loop run zero times; starting at the tail would make it traverse the entire prefix before the same forward collection.

**Why the collected order is correct.** Let the nodes be $v_1,v_2,\ldots,v_n$ from head to tail, and suppose the supplied node is $v_k$. Repeated `prev` moves produce $v_{k-1},v_{k-2},\ldots,v_1$, so the first loop always ends at $v_1$. The second loop follows the defining links $v_1.next=v_2$, $v_2.next=v_3$, and so on. It appends values in the order $v_1.val,v_2.val,\ldots,v_n.val$ and stops only after advancing beyond $v_n$. This establishes both completeness and ordering.

The uniqueness of `Node.val` is not needed by the algorithm. It never searches for a value or uses values to detect visited nodes; it follows structure alone. Even if values repeated, the same traversal would reproduce them in their list positions. The uniqueness guarantee merely simplifies the problem's representation.

**Understand the source's contract assumptions.** The annotation writes `node: "Optional[Node]"`, but the problem promises a nonempty list and an arbitrary node from that list. Therefore the runtime value is not `None`. The source immediately evaluates `node.prev` and would raise an attribute error if passed `None`; that is acceptable under the stated input contract, although a general-purpose library function might defend against it.

The definition of `Node` is shown in a comment because the platform supplies it. The solution is responsible only for traversal. It does not create, detach, or modify nodes. Assigning `node = node.prev` or `node = node.next` changes the local reference, not the linked list's pointers. Consequently, the original data structure remains intact after conversion.

**Why no visited set is used.** A valid doubly linked list is finite, has consistent neighbor links, and contains no cycle. Following `prev` reaches the head, and following `next` reaches `None`. A visited set would add memory without contributing to the promised case. If the structure were malformed or cyclic, both the contract and this proof would fail, and the loops could run forever.

## Complexity detail

Let $n$ be the number of nodes and let the supplied node be at position $k$ from the head, using one-based indexing. The backward phase makes $k-1$ moves. The forward phase visits all $n$ nodes. Total time is $O(k+n)=O(n)$. Although some prefix nodes are traversed once backward and once forward, a constant factor of two does not change the linear bound.

The result list stores all $n$ integer values, so total output space is $O(n)$, matching the manifest. Excluding required output storage, the algorithm uses only the local `node` reference and `ans` reference, so its auxiliary working space is $O(1)$. It uses no recursion and therefore no call-stack growth.

## Alternatives and edge cases

- **Start walking forward from the supplied node:** This works only when the node happens to be the head. For a middle or tail node it omits the earlier portion of the list.
- **Collect backward values and then reverse them:** One could append values while walking toward the head, reverse that prefix, and then continue forward from the original node. It is more complicated and needs careful handling to avoid appending the original node twice.
- **Recursive traversal:** Recursion can find the head or emit nodes, but it adds $O(n)$ call-stack space and risks recursion-depth limits without improving the result.
- **Visited set:** It could protect a general graph-like structure from cycles, but a valid doubly linked list does not need it. It would add $O(n)$ auxiliary space.
- **Given node is the head:** `node.prev` is already absent, so the first loop performs no work and the forward pass returns the whole list.
- **Given node is the tail:** The first loop walks all the way to the head, after which the normal forward pass still emits every value exactly once.
- **Single-node list:** Both `prev` and `next` are `None`. The first loop is skipped, the value is appended once, and the returned array has length one.
- **Repeated values:** The stated input says values are unique, but the traversal does not rely on that property and would preserve duplicates correctly.
- **A `None` argument:** The quoted annotation permits it syntactically, but the source would fail on `node.prev`. The problem guarantee supplies an actual node, so no empty-list case is required.
- **Broken reciprocal pointers:** If `prev` and `next` do not describe one consistent finite list, the method can omit nodes, repeat nodes, or loop forever. Such structures are outside the contract.
- **Input mutation:** Reassigning the local variable `node` does not alter any `prev` or `next` field, so the linked list is unchanged.
- **Output-memory accounting:** The conversion inherently needs $O(n)$ space for the returned array. The working traversal itself is constant-space, a distinction useful when comparing implementations.
