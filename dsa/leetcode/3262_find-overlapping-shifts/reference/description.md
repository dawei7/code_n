## Description

The `EmployeeShifts` table records work shifts on one date. Each row contains an employee identifier together with that shift's start and end times, and the pair `(employee_id, start_time)` is unique.

For every employee, count the pairs of that employee's shifts that overlap. When the shifts are ordered by start time, a pair overlaps exactly when the earlier shift ends later than the later shift begins. Equality does not count: one shift ending at the instant another starts is merely adjacent.

Return only employees who have at least one overlapping pair. Name the count `overlapping_shifts` and order the result by `employee_id` in ascending order.
