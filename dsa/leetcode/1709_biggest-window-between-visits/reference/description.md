## Description

The `UserVisits` table records the dates on which users visited a website during 2020. A user's visit window is the number of days from one visit to that user's next visit. The final visit has no later table row, so its window ends on the fixed reporting date `2021-01-01`.

Produce one row per user containing the greatest of these windows. Dates must be compared independently within each user: visits by other users do not end a window, and input row order does not imply chronological order. Result rows may appear in any order.
