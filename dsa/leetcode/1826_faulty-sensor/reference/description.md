## Description

Two sensors were intended to record the same sequence. One sensor failed: at some position it omitted the correct reading, every later correct reading shifted one position left in that sensor's array, and an unrelated value was placed in its final position so both recorded arrays still have equal length. Before the omission, the recordings agree.

Given `sensor1` and `sensor2`, determine which sensor's sequence exhibits that shift. Return `1` when only sensor 1 can be faulty, `2` when only sensor 2 can be faulty, or `-1` when the evidence cannot distinguish the two explanations. The arbitrary final value may accidentally preserve ambiguity.
