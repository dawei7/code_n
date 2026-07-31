## Examples

**Example 1**

- Input: `["RideSharingSystem", "addRider", "addDriver", "addRider", "matchDriverWithRider", "addDriver", "cancelRider", "matchDriverWithRider", "matchDriverWithRider"]`
- Arguments: `[[], [3], [2], [1], [], [5], [3], [], []]`
- Output: `[null, null, null, null, [2, 3], null, null, [5, 1], [-1, -1]]`
- Explanation: The complete operation trace is:
  - `RideSharingSystem rideSharingSystem = new RideSharingSystem();` initializes the system.
  - `rideSharingSystem.addRider(3);` places rider `3` in the rider queue.
  - `rideSharingSystem.addDriver(2);` places driver `2` in the driver queue.
  - `rideSharingSystem.addRider(1);` places rider `1` behind rider `3`.
  - `rideSharingSystem.matchDriverWithRider();` returns `[2, 3]`, removing the earliest driver and rider.
  - `rideSharingSystem.addDriver(5);` makes driver `5` available.
  - `rideSharingSystem.cancelRider(3);` has no effect because rider `3` has already been matched.
  - `rideSharingSystem.matchDriverWithRider();` returns `[5, 1]`.
  - `rideSharingSystem.matchDriverWithRider();` returns `[-1, -1]` because no pair remains available.

**Example 2**

- Input: `["RideSharingSystem", "addRider", "addDriver", "addDriver", "matchDriverWithRider", "addRider", "cancelRider", "matchDriverWithRider"]`
- Arguments: `[[], [8], [8], [6], [], [2], [2], []]`
- Output: `[null, null, null, null, [8, 8], null, null, [-1, -1]]`
- Explanation: The complete operation trace is:
  - `RideSharingSystem rideSharingSystem = new RideSharingSystem();` initializes the system.
  - `rideSharingSystem.addRider(8);` places rider `8` in the rider queue.
  - `rideSharingSystem.addDriver(8);` makes driver `8` the first available driver.
  - `rideSharingSystem.addDriver(6);` places driver `6` behind driver `8`.
  - `rideSharingSystem.matchDriverWithRider();` returns `[8, 8]` and removes that pair.
  - `rideSharingSystem.addRider(2);` places rider `2` in the rider queue.
  - `rideSharingSystem.cancelRider(2);` removes rider `2` from consideration.
  - `rideSharingSystem.matchDriverWithRider();` returns `[-1, -1]` because driver `6` has no waiting rider.
