## Description

Assume today is `2019-07-05`. For the preceding day, report how many distinct posts were reported for each report reason.

Only rows whose `action` is `report` and whose `action_date` is yesterday, `2019-07-04`, contribute. Several users—or duplicate rows—may report the same post for one reason, but that post contributes only once to that reason's count. Return the result in any order.
