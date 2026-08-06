## Description

The `Users` table records purchases. A row identifies the user, purchased item, purchase timestamp, and amount. The table can contain duplicate rows; each row still represents a purchase occurrence.

A user is active when one of their purchases is followed by another purchase no more than seven days later. The seven-day boundary is inclusive, so purchases exactly seven days apart qualify, as do two purchases on the same date. Return the identifiers of all active users in any order, with each qualifying user appearing once.
