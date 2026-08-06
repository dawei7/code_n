## Description

The `Playback` table records viewing sessions. Each `session_id` is unique, and every row identifies the customer plus the session's `start_time` and `end_time`. A session includes both endpoints of this interval. Sessions belonging to the same customer never overlap.

The `Ads` table records individual advertisements, including the customer who saw each ad and its `timestamp`. Report every playback session during which its customer saw no ad. An ad affects a session only when both the customer identifiers match and the timestamp lies within that session's inclusive interval. Return the qualifying `session_id` values in any order.
