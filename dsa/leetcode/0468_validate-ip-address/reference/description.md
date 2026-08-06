## Description

Given a string `queryIP`, return `"IPv4"` if it is a valid IPv4 address, `"IPv6"` if it is a valid IPv6 address, or `"Neither"` if it satisfies neither grammar.

A valid IPv4 address has the form `"x1.x2.x3.x4"`. Each field is a decimal value from `0` through `255` and cannot contain a leading zero. For instance, `"192.168.1.1"` and `"192.168.1.0"` are valid, whereas `"192.168.01.1"`, `"192.168.1.00"`, and `"192.168@1.1"` are not.

A valid IPv6 address has the form `"x1:x2:x3:x4:x5:x6:x7:x8"`. Every field contains one to four hexadecimal characters chosen from digits, lowercase `a` through `f`, and uppercase `A` through `F`. Leading zeroes within a field are allowed.

Accordingly, `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` and `"2001:db8:85a3:0:0:8A2E:0370:7334"` are valid IPv6 addresses. The strings `"2001:0db8:85a3::8A2E:037j:7334"` and `"02001:0db8:85a3:0000:0000:8a2e:0370:7334"` are invalid because they contain an empty or non-hexadecimal field and an overlong field, respectively.
