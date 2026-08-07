[TOC]

## Solution
---

Lets first look at how the linked list looks like
<center>
<img src="images/138_Copy_List_Random_1.png" width="500"/>
</center>

In the above diagram, for a given node the `next` pointer points to the next node in the linked list. The `next` pointer is something standard for a linked list and this is what ***links*** the nodes together. What is interesting about the diagram and this problem is the `random` pointer which, as the name suggests can point to any node in the linked list or can be a null.

### Approach 1: Recursive

**Intuition**

The basic idea behind the recursive solution is to consider the linked list like a graph. Every node of the Linked List has 2 pointers (edges in a graph). Since, random pointers add the randomness to the structure we might visit the same node again leading to cycles.

<center>
<img src="images/138_Copy_List_Random_2.png" width="500"/>
</center>

In the diagram above we can see the random pointer points back to the previously seen node hence leading to a cycle. We need to take care of these cycles in the implementation.

All we do in this approach is to just traverse the graph and clone it. Cloning essentially means creating a new node for every unseen node you encounter. The traversal part will happen recursively in a depth first manner. Note that we have to keep track of nodes already processed because, as pointed out earlier, we can have cycles because of the random pointers.

**Algorithm**

1. Start traversing the graph from `head` node.

    Lets see the linked structure as a graph. Below is the graph representation of the above linked list example.
    <center>
    <img src="images/138_Copy_List_Random_7.png" width="500"/>
    </center>

    In the above example `head` is where we begin our graph traversal.

2. If we already have a cloned copy of the current node in the visited dictionary, we use the cloned node reference.  
3. If we don't have a cloned copy in the visited dictionary, we create a new node and add it to the visited dictionary.
`visited_dictionary[current_node] = cloned_node_for_current_node.`
4. We then make two recursive calls, one using the `random` pointer and the other using `next` pointer. The diagram from step 1, shows `random` and `next` pointers in red and blue color respectively. Essentially we are making recursive calls for the children of the current node. In this implementation, the children are the nodes pointed by the `random` and the `next` pointers.
<pre>
cloned_node_for_current_node.next = copyRandomList(current_node.next);
cloned_node_for_current_node.random = copyRandomList(current_node.random);
</pre>

<br>


```python
class Solution:
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
```


**Complexity Analysis**

* Time Complexity: $$O(N)$$ where N is the number of nodes in the linked list.
* Space Complexity: $$O(N)$$. If we look closely, we have the recursion stack and we also have the space complexity to keep track of nodes already cloned i.e. using the visited dictionary. But asymptotically, the complexity is $$O(N)$$.

---

### Approach 2: Iterative with $$O(N)$$ Space

**Intuition**

The iterative solution to this problem does not model it as a graph, instead simply treats it as a LinkedList.
When we are iterating over the list, we can create new nodes via the random pointer or the next pointer whichever points to a node that doesn't exist in our old --> new dictionary.

**Algorithm**

1. Traverse the linked list starting at `head` of the linked list.
    <center>
    <img src="images/138_Copy_List_Random_3.png" width="600"/>
    </center>

    In the above diagram we create a new cloned `head` node. The cloned node is shown using dashed lines. In the implementation we would even store the reference of this newly created node in a visited dictionary.

2. Random Pointer
    * If the `random` pointer of the current node $$i$$ points to the a node $$j$$ and a clone of $$j$$ already exists in the visited dictionary, we will simply use the cloned node reference from the visited dictionary.
    * If the `random` pointer of the current node $$i$$ points to the a node $$j$$ which has not been created yet, we create a new node corresponding to $$j$$ and add it to the visited dictionary.

    <center>
    <img src="images/138_Copy_List_Random_4.png" width="600"/>
    </center>

    In the above diagram the `random` pointer of node $$A$$ points to a node $$C$$. Node $$C$$ which was not visited yet as we can see from the previous diagram. Hence we create a new cloned $$C'$$ node corresponding to node $$C$$ and add it to visited dictionary.

3. Next Pointer
    * If the `next` pointer of the current node $$i$$ points to the a node $$j$$ and a clone of $$j$$ already exists in the visited dictionary, we will simply use the cloned node reference from the visited dictionary.
    * If the `next` pointer of the current node $$i$$ points to the a node $$j$$ which has not been created yet, we create a new node corresponding to $$j$$ and add it to the visited dictionary.

    <center>
    <img src="images/138_Copy_List_Random_5.png" width="600"/>
    </center>

    In the above diagram the `next` pointer of node $$A$$ points to a node $$B$$. Node $$B$$ which was not visited yet as we can see from the previous diagram. Hence we create a new cloned $$B'$$ node corresponding to node $$B$$ and add it to visited dictionary.

4. We repeat steps 2 and 3 until we reach the end of the linked list.

    <center>
    <img src="images/138_Copy_List_Random_6.png" width="600"/>
    </center>

    In the above diagram, the `random` pointer of node $$B$$ points to an already visited node $$A$$. Hence in step 2, we don't create a new copy for the clone. Instead we point `random` pointer of cloned node $$B'$$ to already existing cloned node $$A'$$.

    Also, the `next` pointer of node $$B$$ points to an already visited node $$C$$. Hence in step 3, we don't create a new copy for the clone. Instead we point `next` pointer of cloned node $$B'$$ to already existing cloned node $$C'$$.


```python
class Solution:
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        if not head:
            return head

        old_node = head
        # Creating the new head node.
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]
```


**Complexity Analysis**

* Time Complexity : $$O(N)$$ because we make one pass over the original linked list.
* Space Complexity : $$O(N)$$ as we have a dictionary containing mapping from old list nodes to new list nodes. Since there are $$N$$ nodes, we have $$O(N)$$ space complexity.

---

### Approach 3: Iterative with $$O(1)$$ Space

**Intuition**

Instead of a separate dictionary to keep the old node --> new node mapping, we can tweak the original linked list and keep every cloned node next to its original node. This interleaving of old and new nodes allows us to solve this problem without any extra space. Lets look at how the algorithm works.

**Algorithm**

1. Traverse the original list and clone the nodes as you go and place the cloned copy next to its original node. This new linked list is essentially a interweaving of original and cloned nodes.

    <center>
    <img src="images/138_Copy_List_Random_8_1.png" width="800"/>
    </center>
    <center>
    <img src="images/138_Copy_List_Random_8_2.png" width="800"/>
    </center>

    As you can see we just use the value of original node to create the cloned copy. The `next` pointer is used to create the weaving. Note that this operation ends up modifying the original linked list.
    <pre>
    cloned_node.next = original_node.next
    original_node.next = cloned_node
    </pre>

2. Iterate the list having both the new and old nodes intertwined with each other and use the original nodes' random pointers to assign references to random pointers for cloned nodes. For eg. If `B` has a random pointer to `A`, this means `B'` has a random pointer to `A'`.

    <center>
    <img src="images/138_Copy_List_Random_9_1.png" width="800"/>
    </center>

3. Now that the `random` pointers are assigned to the correct node, the `next` pointers need to be correctly assigned to unweave the current linked list and get back the original list and the cloned list.

    <center>
    <img src="images/138_Copy_List_Random_10.png" width="800"/>
    </center>



```python
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head  # A->B->C
        ptr_new_list = head.next  # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = (
                ptr_new_list.next.next if ptr_new_list.next else None
            )
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
```


**Complexity Analysis**

* Time Complexity : $$O(N)$$
* Space Complexity : $$O(1)$$