## Description

The rectangular matrix `units` describes $m$ devices, each containing exactly $n$ units. Entry `units[i][j]` is a capacity, and a device's rating is the minimum capacity among the units it currently holds.

An operation selects a device that has never previously acted as a source, removes exactly one of its current units, and adds that unit to a different device. The chosen source is then permanently marked, while destination devices may receive units any number of times. Performing no operation is allowed.

After any legal sequence of transfers, add the ratings of all devices. Return the greatest total that can be achieved.
