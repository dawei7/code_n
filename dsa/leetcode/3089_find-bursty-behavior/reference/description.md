## Description

The `Posts` table records when users publish posts. Identify users whose February 2024 activity contains a burst: within some period of seven consecutive calendar days, the user's post count is at least twice that user's average weekly post count across the month.

Only posts dated from February 1 through February 28, 2024 are part of the calculation. For the average, treat those 28 days as exactly four weeks. For each qualifying user, report the largest seven-day post count found anywhere in that interval together with the monthly total divided by four.

Return the result in ascending order of `user_id`.
