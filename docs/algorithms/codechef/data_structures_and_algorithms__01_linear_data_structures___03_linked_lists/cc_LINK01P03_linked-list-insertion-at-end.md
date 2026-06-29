# Linked List - Insertion at end

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK01P03 |
| Difficulty Rating | 932 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Linked Lists |
| Official Link | [LINK01P03](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST01/problems/LINK01P03) |

---

## Problem Statement

Insertion at end is fairly straightforward.

See the following steps:

1. Make a new node with the desired value.
2. Start at the **head** and move to the last node of the linked list.
3. Insert the new node after the last node.

The only edge case is when there is no value in the linked list. In that case, we set the head of the linked list to the new node.

### Task
Complete the function **insertAtEnd** in IDE to insert an element at the end of a linked list.
I have also added a new function **getLastValue** to print the last value of a linked list.

---

## Input Format

First line denotes 'n' the number of elements to be inserted in the list.
Second line consists of n space-separated integers denoting the elements to be added in the list.

---

## Output Format

The value at the end of the list after each insertion.

---

## Constraints

- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
2 32 23 53
```

**Output**

```text
2 32 23 53
```

**Explanation**

Initially we have an empty linked list. After each step:
1) 2
2) 2->32
3) 2->32->23
4) 2->32->23->53

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

const readline = require('readline');

// This is the node class which is instantiated whenever we add a new element to the list
class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// Head pointer is stored to maintain the beginning of the list
class MyLinkedList {
    constructor() {
        this.head = null; // NULL because initially the list is empty
    }

    insertAtEnd(value) {
        const newNode = new Node(value);

        if (this.head === null) {
            // The list is empty, thus we just need to assign head to the only element
            this.head = newNode;
        } else {
            // Iterating towards the end of the list
            let cur = this.head;
            while (cur.next !== null) {
                cur = cur.next;
            }
            // Updating the next pointer of this element
            cur.next = newNode;
        }
    }

    print() {
        let temp = this.head;
        while (temp !== null) {
            process.stdout.write(`${temp.value} `);
            temp = temp.next;
        }
        console.log();
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let inputLines = [];
rl.on('line', (line) => {
    inputLines.push(line.trim());
});

rl.on('close', () => {
    if (inputLines.length < 2) {
        console.error("Invalid input. Please provide the correct number of inputs.");
        return;
    }

    const n = parseInt(inputLines[0], 10); // First line contains n
    const values = inputLines[1].split(' ').map((str) => parseInt(str, 10)); // Second line contains the elements

    const list = new MyLinkedList();

    for (let i = 0; i < n; i++) {
        list.insertAtEnd(values[i]);
    }

    list.print();
});

</details>
