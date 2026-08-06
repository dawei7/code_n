## Description

The `Servers` table records when identified servers start and stop running. Each row contains a server identifier, the time of the event, and a `session_status` value of either `start` or `stop`. For each server, its chronologically corresponding start and stop events delimit running sessions.

Find the total running time accumulated across every session of every server. Convert that combined duration to days and round it down, so only complete 24-hour periods are counted. Return the resulting number as `total_uptime_days`; the result has one row, so row order is immaterial.
