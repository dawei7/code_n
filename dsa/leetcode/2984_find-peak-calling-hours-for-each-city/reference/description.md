## Description

The `Calls` table records each call's caller, recipient, timestamp, and city.
Its primary key is the combination `(caller_id, recipient_id, call_time)`, so
every row represents one distinct call.

For each city, group calls by the hour of day in which `call_time` falls and
find the greatest call count. Return every hour attaining that maximum; when a
city has a tie, all of its tied peak hours must appear. The result columns are
`city`, `peak_calling_hour`, and `number_of_calls`. Sort first by
`peak_calling_hour` descending and then by `city` descending.
