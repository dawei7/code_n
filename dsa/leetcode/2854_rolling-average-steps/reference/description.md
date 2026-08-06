## Description

The `Steps` table records how many steps each user took on particular calendar dates. For every user and date, consider the three-day period ending on that date: the date itself and the two immediately preceding calendar dates.

Report a rolling average only when the table contains a row for that user on all three consecutive dates. Average those three `steps_count` values and round the result to two decimal places. Dates whose three-day calendar window is incomplete must not appear, even if the user has three earlier observations separated by gaps.

Return `user_id`, the ending `steps_date`, and the computed `rolling_average`, ordered by `user_id` and then `steps_date`, both in ascending order.
