## Description

The `Cinema` table records seats by `seat_id` and indicates whether each seat is available. A value of `1` in `free` means the seat is available, while `0` means it is occupied.

Find every longest sequence of available seats whose IDs are consecutive integers. For each maximum-length sequence, report its first seat ID, last seat ID, and number of seats. If several sequences share the maximum length, include all of them. Order the result by `first_seat_id` in ascending order.
