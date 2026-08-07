[TOC]

## Solution

---

### Approach 1: Design using Arrays

#### Intuition  

The most intuitive method is using an array to record the availability of each slot. We build a boolean array `isSlotAvailable` of size `maxNumbers` to indicate whether the slot at index `i` is available. Initially, all values of the array are `true`.

Each slot `i` assigned by `get()` will be marked as `isSlotAvailable[i] = false` to indicate the slot is already occupied. Each slot `i` released by `release()` will be marked as `true` to indicate it's available. 

While performing the `get()` operation, we can iterate on all slots from `0` till `isSlotAvailable.size()` one by one, and search for an unoccupied slot (i.e. `isSlotAvailable[i] == true`), if found, then we mark that slot as occupied (i.e. `isSlotAvailable[i] = false`) and return the slot `i`.    
If no slot is available then in that case we return `-1`.

To check if a slot `number` is occupied or not, we can check if `isSlotAvailable[number]` is `true` (available) or `false` (not available).

To release a slot `number`, we need to set `isSlotAvailable[number] = true`, indicating that the slot is available.

![array_example](images/Slide1.PNG)


#### Algorithm

1. Initialize an array `isSlotAvailable` of size `maxNumbers`, storing `true` at all indices.

2. Implementing the `get()` method:    
    Iterate through our `isSlotAvailable` array and if `isSlotAvailable[i] == true` at any index, mark `isSlotAvailable[i] = false` and return `i`.    
    Otherwise, return `-1`.

3. Implementing the `check(number)` method:    
    Return `isSlotAvailable[number]`.

4. Implementing the `release(number)` method:    
    Mark `isSlotAvailable[number] = true`.
   

#### Implementation


```python
class PhoneDirectory:
    def __init__(self, maxNumbers):
        # List to mark if a slot is available.
        self.is_slot_available = [True] * maxNumbers

    def get(self):
        # Find an empty slot and return the respective index.
        index = next((i for i, available in enumerate(self.is_slot_available) if available), -1)
        if index != -1:
            self.is_slot_available[index] = False
        return index

    def check(self, number):
        # Check if the slot at index 'number' is available.
        return self.is_slot_available[number]

    def release(self, number):
        # Mark the slot at index 'number' as available.
        self.is_slot_available[number] = True
```


#### Complexity Analysis

Let $n$ be the maximum number of slots in the phone directory, i.e. `n = maxNumbers`.

* Time complexity: 
    - In each `get` method call, we iterate over the `isSlotAvailable` array until we reach the end or find the first available slot, one call will take $O(n)$ time on average.
    - In each `check` method call, we only check if the value stored at the respective index in the `isSlotAvailable` array is `true` or not, thus each call will take $O(1)$ time.
    - In each `release` method call, we mark the value at the respective index in the `isSlotAvailable` array as `true`, thus each call will take $O(1)$ time.

* Space complexity: $$O(n)$$
    - We use an auxiliary array `isSlotAvailable` of size $n$, to mark the availability status of $n$ slots.


<br />

---

### Approach 2: Design using Queue / LinkedList

#### Intuition  

In the previous approach, the `get` method is not optimal as to find any available slot we need to iterate over the whole `isSlotAvailable` array. 

Instead, we can use a queue (or, a linked list) `slotsAvalaiableQueue` to keep track of currently available slots, we will push a slot number if it is available, and whenever we require a slot number we will pop from it, both these operations will take constant time.   

Searching if a `number` is present in the queue or not will take linear time, so to avoid searching in the queue to check whether the slot is available or not, we will use the previously used boolean array `isSlotAvailable` where we will mark `isSlotAvailable[number] = true` if `number` is present in the queue. Thus, we can quickly check if the slot `number` is present in the queue (i.e., is available) or not in constant time.

<br />

Initially, all slots are available, thus, `isSlotAvailable` will store `true` at all indices, and `slotsAvailableQueue` will have all numbers in it from `0` till `(maxNumbers - 1)`.

While performing the `get()` operation, we need to return any available slot, so if `slotsAvailableQueue` is not empty, we pop its first element `slot`, mark it as not available (i.e. `isSlotAvailable[number] = false`), and return `slot`.     
Otherwise, if `slotsAvailableQueue` is empty, all slots are already occupied, then we return `-1`.

To check if a slot `number` is occupied or not, we can check if `isSlotAvailable[number]` is `true` (indicating it's available), or `false` (indicating it's not available).

While releasing a slot `number`, if `isSlotAvailable[number]` is already `true` it means it is already available and is present in the queue so there is no need to push it again.   
Otherwise, the `number` was earlier occupied and is now released, so, we will push the `number` in the `slotsAvailableQueue` queue and mark it as available `isSlotAvailable[number] = true`.  


![queue_example](images/Slide2.PNG)




#### Algorithm

1. Initialize an array `isSlotAvailable` of size `maxNumbers` storing `true` at all indices, and a queue `slotsAvalaiableQueue` having all numbers from `0` till `(maxNumbers - 1)` in it.

2. Implementing the `get()` method:    
    If `slotsAvalaiableQueue` is not empty, we pop its first element `slot`, mark `isSlotAvailable[slot] = false`, and return `slot`.     
    Otherwise, return `-1`.

3. Implementing the `check(number)` method:    
    Return `isSlotAvailable[number]`.

4. Implementing the `release(number)` method:    
    If `isSlotAvailable[number] == true`, then return.    
    Otherwise, mark `isSlotAvailable[number] = true` and push `number` in `slotsAvalaiableQueue`.
    

#### Implementation


```python
class PhoneDirectory:
    def __init__(self, max_numbers):
        # Queue to store all available slots.
        self.slots_available_queue = deque(range(max_numbers))

        # List to mark if a slot is available.
        self.is_slot_available = [True] * max_numbers
    
    def get(self):
        # If the queue is empty, it means no slot is available.
        if not self.slots_available_queue:
            return -1

        # Otherwise, get the first available slot from the queue,
        # mark that slot as not available and return the slot.
        slot = self.slots_available_queue.popleft()
        self.is_slot_available[slot] = False
        return slot
    
    def check(self, number):
        # Check if the slot at index 'number' is available or not.
        return self.is_slot_available[number]
    
    def release(self, number):
        # If the slot is already present in the queue, we don't do anything.
        if self.is_slot_available[number]:
            return

        # Otherwise, mark the slot 'number' as available.
        self.slots_available_queue.append(number)
        self.is_slot_available[number] = True
```


#### Complexity Analysis

Let $n$ be the maximum number of slots in the phone directory, i.e. `n = maxNumbers`.

* Time complexity: 
    - In each `get` method call, we pop the first element from `slotsAvailableQueue ` and mark it as not available in `isSlotAvailable`, both of which are constant time operations, thus each call will only take $O(1)$ time.
    - In each `check` method call, we only check if the value stored at the respective index in the `isSlotAvailable` array is `true` or not, thus each call will take $O(1)$ time.
    - In each `release` method call, we mark the value at the respective index in the `isSlotAvailable` array as `true` and push it in `slotsAvailableQueue` both of which are constant time operations, thus each call will take $O(1)$ time.

* Space complexity: $$O(n)$$
    - We use an additional queue `slotsAvailableQueue ` and an array `isSlotAvailable`, both of which have a maximum size of $n$.


<br />

---

### Approach 3: Design using Hash Table

#### Intuition  

We can also use a hash set `slotsAvailable` to store all available slots. In addition, in a hash set, inserting an element, checking if an element is present, and getting the first element are all constant time operations.  

As initially, all slots are available `slotsAvailable` will have all numbers from `0` till `(maxNumbers - 1)` in it.

While performing the `get()` operation, we need to return any available slot, if `slotsAvailable` is not empty then we pop its first element and return it.     
Otherwise, all slots are already occupied, so, we return `-1`.

To check if a slot `number` is occupied or not, we can check if `number` is present in the hash set `slotsAvailable` (indicating it's available), or not (indicating it's not available).

To release a slot `number`, we will push `number` in our `slotsAvailable` hash set.

#### Algorithm

1. Initialize a hash set `slotsAvailable` having numbers from `0` till `(maxNumbers - 1)` in it.

2. Implementing the `get()` method:    
    If `slotsAvailable` is not empty then we pop its first element `slot` and return it.     
    Otherwise, return `-1`.

3. Implementing the `check(number)` method:    
    Return `true` if `number` is present in `slotsAvailable`, otherwise, return `false`.

4. Implementing the `release(number)` method:    
    Push `number` in `slotsAvailable`.
   

#### Implementation


```python
class PhoneDirectory:
    def __init__(self, max_numbers):
        # Hash set to store all available slots.
        self.slots_available = set(range(max_numbers))

    def get(self):
        # If the hash set is empty it means no slot is available.
        if not self.slots_available:
            return -1

        # Otherwise, pop and return the first element from the hash set.
        return self.slots_available.pop()

    def check(self, number):
        # Check if the slot at index 'number' is available or not.
        return number in self.slots_available

    def release(self, number):
        # Mark the slot 'number' as available.
        self.slots_available.add(number)
```


#### Complexity Analysis

Let $n$ be the maximum number of slots in the phone directory, i.e. `n = maxNumbers`.

* Time complexity: 
    - In each `get` method call, we return the first element from the `slotsAvailable` hash set, thus each call will only take $O(1)$ time.
    - In each `check` method call, we check if the value is present in the `slotsAvailable` hash set or not, thus each call will take $O(1)$ time.
    - In each `release` method call, we insert the value in the `slotsAvailable` hash set, thus each call will take $O(1)$ time.

* Space complexity: $$O(n)$$
    - We use an additional hash set `slotsAvailable` of maximum size $n$. 


<br />

---