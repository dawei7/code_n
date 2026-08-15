### 1. Description

Given the `head` of a singly linked list, sort the list using **insertion sort**, and return *the sorted list's head*.

The steps of the **insertion sort** algorithm:

- Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.

- At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.

- It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

![](images/Insertion-sort-example-300px.gif)

### 2. Function Contract

**Inputs**

- `head`: The head of a singly linked list, encoded in app cases as its sequence of integer values.

**Return value**

Return the head of the list after its nodes have been rearranged into non-decreasing order.

### 3. Examples

#### Example 1

![](images/sort1linked-list.jpg)

- **Input:** $head = [4,2,1,3]$
- **Output:** `[1,2,3,4]`

#### Example 2

![](images/sort2linked-list.jpg)

- **Input:** $head = [-1,5,3,4,0]$
- **Output:** `[-1,0,3,4,5]`

### 4. Constraints

- The number of nodes in the list is in the range `[1, 5000]`.

- $-5000 \le \text{Node.val} \le 5000$
