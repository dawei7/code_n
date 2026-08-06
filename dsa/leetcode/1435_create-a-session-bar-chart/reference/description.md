## Description

Summarize application visits as a four-row session-duration bar chart. Although `duration` is stored in seconds, the bins are defined in minutes: from 0 inclusive to 5 exclusive, from 5 inclusive to 10 exclusive, from 10 inclusive to 15 exclusive, and 15 minutes or more.

For each interval, report its exact output label and the number of `Sessions` rows it contains. The required labels are `[0-5>`, `[5-10>`, `[10-15>`, and `15 or more`. Every label must appear even when its count is zero. Result rows may be returned in any order.
