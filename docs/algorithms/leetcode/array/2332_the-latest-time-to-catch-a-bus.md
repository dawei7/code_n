# The Latest Time to Catch a Bus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2332 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [the-latest-time-to-catch-a-bus](https://leetcode.com/problems/the-latest-time-to-catch-a-bus/) |

## Problem Description & Examples
### Goal
You are given a list of bus departure times, a list of passenger arrival times, and the maximum capacity for each bus. Passengers board buses in the order of their arrival, always choosing the earliest available bus they can catch. Your task is to determine the latest possible time you can arrive at the bus station and still catch any bus, with the constraint that you cannot arrive at the exact same time as any existing passenger.

### Function Contract
**Inputs**

- `buses`: A list of integers representing the departure times of `n` buses. All departure times are unique.
- `passengers`: A list of integers representing the arrival times of `m` passengers. All arrival times are unique.
- `capacity`: An integer representing the maximum number of passengers each bus can hold.

**Return value**

- An integer representing the latest possible time you can arrive at the bus station to catch a bus, adhering to all rules.

### Examples
**Example 1**

- Input: `buses = [10,20]`, `passengers = [2,17,18,19]`, `capacity = 2`
- Output: `16`
- Explanation:
  - Bus 1 (departs 10): Passenger 2 boards. (1 spot taken)
  - Bus 2 (departs 20): Passengers 17, 18 board. (2 spots taken, bus full)
  - The last passenger to board the last bus arrived at 18. Since the bus is full, you must arrive before 18. The latest time before 18 is 17. However, 17 is an existing passenger's arrival time. So, you try 16. 16 is not an existing passenger's arrival time. If you arrive at 16, you can catch Bus 2.

**Example 2**

- Input: `buses = [20,30,10]`, `passengers = [19,13,26,4,25,11,21]`, `capacity = 2`
- Output: `20`
- Explanation:
  - Sorted buses: `[10,20,30]`
  - Sorted passengers: `[4,11,13,19,21,25,26]`
  - Bus 1 (departs 10): Passenger 4 boards. (1 spot taken)
  - Bus 2 (departs 20): Passengers 11, 13 board. (2 spots taken, bus full)
  - Bus 3 (departs 30): Passengers 19, 21 board. (2 spots taken, bus full)
  - The last passenger to board the last bus arrived at 21. Since the bus is full, you must arrive before 21. The latest time before 21 is 20. 20 is not an existing passenger's arrival time. If you arrive at 20, you can catch Bus 3.

**Example 3**

- Input: `buses = [10]`, `passengers = [10]`, `capacity = 1`
- Output: `9`
- Explanation:
  - Bus 1 (departs 10): Passenger 10 boards. (1 spot taken, bus full)
  - The last passenger to board the last bus arrived at 10. Since the bus is full, you must arrive before 10. The latest time before 10 is 9. 9 is not an existing passenger's arrival time. If you arrive at 9, you can catch Bus 1.

---

## Underlying Base Algorithm(s)
The problem can be solved using a combination of **Sorting** and a **Two-Pointers** approach, along with a **Hash Set** for efficient lookups.

1.  **Sorting**: Both the `buses` departure times and `passengers` arrival times are sorted in ascending order. This ensures that passengers board the earliest available bus they can catch, and buses are processed chronologically.
2.  **Two Pointers**: A pointer (`p_idx`) is used to iterate through the sorted `passengers` array. For each bus, this pointer advances to assign passengers to the current bus based on their arrival time and the bus's capacity and departure time.
3.  **Hash Set (Set)**: A set (`occupied_times`) is used to store all existing passenger arrival times. This allows for `O(1)` average-time complexity when checking if a candidate arrival time for "you" is already taken by another passenger, which is a crucial constraint.

The core idea is to simulate the boarding process for all existing passengers. To find the *latest* time "you" can arrive, we focus on the *last* bus. If the last bus is not full, "you" can arrive at its departure time (or earlier if that time is occupied). If the last bus is full, "you" must arrive just before the last passenger who boarded it (or earlier if that time is occupied). We then decrement this candidate time until a non-occupied time is found.

## Complexity Analysis
- **Time Complexity**: `O(N log N + M log M + M)`.
    - Sorting `buses` takes `O(N log N)` time, where `N` is the number of buses.
    - Sorting `passengers` takes `O(M log M)` time, where `M` is the number of passengers.
    - Creating the `occupied_times` set takes `O(M)` time on average.
    - The main loop iterates `N` times (once for each bus). Inside this loop:
        - The inner `while` loop for assigning passengers to buses advances the `p_idx` pointer. Across all `N` buses, `p_idx` traverses the `passengers` array at most once, contributing `O(M)` total time.
        - The `while candidate_time in occupied_times` loop, which decrements `candidate_time`, runs at most `M` times in total across all buses in the worst case (e.g., if all passenger times are consecutive and need to be skipped). Each `set` lookup is `O(1)` on average.
    - Therefore, the total time complexity is dominated by the sorting steps and the linear scan with set lookups.
- **Space Complexity**: `O(M)`.
    - The `occupied_times` set stores up to `M` passenger arrival times.
    - The sorting algorithms might use `O(log N)` or `O(N)` auxiliary space depending on the implementation (Python's Timsort uses `O(N)` in the worst case).
    - Overall, the space complexity is dominated by the `occupied_times` set.
