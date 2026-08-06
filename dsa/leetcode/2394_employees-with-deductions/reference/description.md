## Description

The `Employees` table gives every employee's monthly work requirement in
whole hours. The `Logs` table records zero or more work sessions for an
employee, using the session's starting and ending timestamps. Every timestamp
is in October 2022, although a session that begins before midnight may end on
the following day.

Compute each session's duration in minutes and round that session upward
independently whenever any seconds remain. Add the rounded session durations
for each employee. Report the identifiers of employees whose total is less
than their required number of hours; this must include an employee with no
logged sessions. The result rows may be returned in any order.
