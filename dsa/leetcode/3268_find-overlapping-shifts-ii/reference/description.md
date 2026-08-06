## Description

The `EmployeeShifts` table records employees' shift start and end datetimes. The pair `(employee_id, start_time)` uniquely identifies a shift. Two shifts for the same employee are eligible to overlap only when their start datetimes fall on the same date, and their time intervals intersect for positive duration. Merely touching at one endpoint is not an overlap.

For every employee, report the greatest number of eligible shifts active simultaneously at any instant. Also report the total overlap duration in minutes, summing the intersection duration of every overlapping shift pair. When three shifts share an interval, that interval contributes once for each of the three pairs.

Include employees who never overlap: their maximum is one and their total overlap duration is zero. Order the result by `employee_id` ascending.
