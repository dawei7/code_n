### 1. Description

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the `FirstUnique` class:

- `FirstUnique(int[] nums)` Initializes the object with the numbers in the queue.

- `int showFirstUnique()` returns the value of **the first unique** integer of the queue, and returns **-1** if there is no such integer.

- `void add(int value)` insert value to the queue.

### 2. Function Contract

The source-native object exposes these operations:

- `FirstUnique(nums)`: initialize the queue with the integers in `nums`, preserving their order;
- `showFirstUnique()`: return the earliest value whose current frequency is exactly one, or `-1` when no such value exists;
- `add(value)`: append `value` to the queue and return nothing.

The app represents one object lifecycle with two aligned arrays:

- `operations`: begins with `"FirstUnique"`; each later entry is `"showFirstUnique"` or `"add"`;
- `arguments`: supplies `[nums]` to the constructor, no arguments to `showFirstUnique`, and `[value]` to `add`.

Let $n = \lvert\texttt{nums}\rvert$ and let $q$ be the number of calls after construction.

**Return value**

Return one result per operation. Construction and `add` produce `null`; each `showFirstUnique` entry produces the requested integer or `-1`.

### 3. Examples

#### Example 1

- **Input:** ``
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
- **Output:** ``
[null,2,null,2,null,3,null,-1]
- **Explanation:** FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

#### Example 2

- **Input:** ``
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
- **Output:** ``
[null,-1,null,null,null,null,null,17]
- **Explanation:** FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17

#### Example 3

- **Input:** ``
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
- **Output:** ``
[null,809,null,-1]
- **Explanation:** FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{8}$

- $1 \le value \le 10^{8}$

- At most `50000` calls will be made to `showFirstUnique` and `add`.
