## Description

An equal count substring is a nonempty contiguous part of a lowercase English string in which every distinct letter that appears has the same prescribed frequency `count`. Letters absent from that substring impose no requirement.

Given `s` and the positive integer `count`, return the number of index ranges that form equal count substrings. Count ranges separately even when they contain identical text, and reject any range where at least one present letter occurs either fewer or more than `count` times.
