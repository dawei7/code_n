## Description

Assume today is `2019-06-30`. For every date no more than 90 days before today, report how many users logged in for the first time on that date.

A user's qualifying date is the earliest date among all of that user's `login` rows, not merely the earliest login already inside the reporting window. Activities of the other four kinds do not establish a first login. Return only dates with a nonzero count, and return the rows in any order.
