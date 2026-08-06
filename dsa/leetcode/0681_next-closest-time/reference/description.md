## Description

Given a valid 24-hour clock display in `"HH:MM"` format, form the next chronological display using only digits that appear in the input. A displayed digit may be reused without limit, even when it occurs only once in the original time. Continue forward through midnight when no qualifying display remains later on the same day.

The input is always exactly zero-padded: `"01:34"` and `"12:09"` are valid forms, whereas `"1:34"` and `"12:9"` are not. Return the closest qualifying time in the same five-character format. If the original display is the only constructible time, its next occurrence is one full day later.
