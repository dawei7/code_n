## Description

An IP address is the dotted-decimal representation of a 32-bit unsigned integer. Its bits are divided into four groups of eight; each group is written as a decimal number, and periods separate the groups. For example, the binary value `00001111 10001000 11111111 01101011` is written as `"15.136.255.107"`.

A CIDR block describes a set of IP addresses with a base address followed by `/` and a prefix length $k$. It covers precisely the addresses whose first $k$ bits match the first $k$ bits of the base. For example, `"123.45.67.89/20"` has prefix length `20` and covers binary addresses matching `01111011 00101101 0100xxxx xxxxxxxx`, where every `x` may independently be `0` or `1`.

You are given a starting address `ip` and a positive address count `n`. Cover the inclusive interval `[ip, ip + n - 1]` exactly: every address in the interval must be included, and no address outside it may be included. Return a shortest possible list of CIDR blocks. If more than one shortest list exists, any one is acceptable.
