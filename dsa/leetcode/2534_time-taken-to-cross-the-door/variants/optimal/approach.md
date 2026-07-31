## General

Maintain one FIFO queue for entering people and one for exiting people. Because arrivals are non-decreasing and people are inserted in index order, each queue's front is always the smallest-index waiting person for that direction.

At the start of a simulated second, enqueue every person whose arrival time is at most the current time. Prefer the direction used in the immediately previous second; if its queue is empty, use the other direction. Initialize the preference to exiting, which represents an unused door. After a person crosses, record the current second, remember that direction, and advance by one.

If both queues are empty before the next arrival, no crossing can occur in the gap. Jump directly to that arrival time and reset the preferred direction to exiting because the door was unused during the preceding second. This reset is essential even when the last actual crossing used a different direction. Each person is enqueued and removed exactly once, and every choice follows the stated direction and index priorities.

## Complexity detail

Let $n$ be the number of people. The arrival pointer advances $n$ times, and each person undergoes one constant-time queue insertion and removal, so the total time is $O(n)$. The two queues and returned answer hold $O(n)$ indices or timestamps, giving $O(n)$ space.

## Alternatives and edge cases

- **One unsorted waiting list:** Searching it for the preferred direction and smallest index every second can cost $O(n^2)$ time.
- **Second-by-second idle simulation:** Walking through empty time gaps is unnecessary; jumping to the next arrival preserves all decisions.
- **Unused previous second:** Any idle gap resets preference to exiting, regardless of the last non-idle direction.
- **Same-second arrivals:** Enqueue all of them before choosing who crosses.
- **Same-direction tie:** FIFO order is index order because the input is aligned and arrivals are non-decreasing.
- **Preferred queue empty:** The other direction crosses even if it lacks nominal priority.
- **Continuous backlog:** With no idle second, the last crossing direction continues to control priority.
