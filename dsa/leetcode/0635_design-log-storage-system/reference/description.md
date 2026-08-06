## Description

A log consists of a unique integer ID and a timestamp. Every timestamp is written as `Year:Month:Day:Hour:Minute:Second`; for example, `2017:01:01:23:59:59`. Each field is a zero-padded decimal number, so all timestamps have the same fixed-width layout.

Implement a `LogSystem` that begins empty. A `put` operation stores one ID and timestamp pair so that later queries can inspect it.

A `retrieve` operation receives two timestamps and a granularity. Return the IDs whose timestamps lie in the inclusive range from `start` through `end` when both boundaries and stored timestamps are considered only through that granularity. The supported granularities are `Year`, `Month`, `Day`, `Hour`, `Minute`, and `Second`; fields less precise than the selected granularity do not affect membership in the range.
