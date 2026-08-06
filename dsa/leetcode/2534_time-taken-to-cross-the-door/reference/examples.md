## Examples

**Example 1**

- **Input:** `arrival = [0, 1, 1, 2, 4], state = [0, 1, 0, 0, 1]`
- **Output:** `[0, 3, 1, 2, 4]`
- **Explanation:**
  - Second 0: Person 0 enters at t=0.
  - Second 1: Person 1 (exit) and Person 2 (enter) arrive. Entering retains priority from previous second, so Person 2 enters at t=1.
  - Second 2: Person 3 (enter) arrives. Entering retains priority, so Person 3 enters at t=2.
  - Second 3: Person 1 (exit) crosses at t=3.
  - Second 4: Person 4 (exit) arrives and exits at t=4.

**Example 2**

- **Input:** `arrival = [0, 0, 0], state = [1, 0, 1]`
- **Output:** `[0, 2, 1]`
- **Explanation:**
  - Second 0: Persons 0 (exit), 1 (enter), 2 (exit) arrive. Door was unused, so exit has priority. Person 0 has smaller index than Person 2, so Person 0 exits at t=0.
  - Second 1: Previous second was exit, so Person 2 exits at t=1.
  - Second 2: Person 1 enters at t=2.
