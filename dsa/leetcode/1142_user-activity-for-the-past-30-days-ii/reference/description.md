## Description

For the 30-day period ending on `2019-07-27`, inclusive, determine how many distinct sessions belong to each user who was active during that period. A session qualifies when at least one of its activities falls inside the period, regardless of the activity's enum value.

Return the average of those per-user session counts, rounded to two decimal places. Users without a qualifying activity do not contribute to the average, and repeated events from the same session do not create additional sessions.
