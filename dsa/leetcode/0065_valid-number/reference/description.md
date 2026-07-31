## Description

Given a string `s`, determine whether it represents a valid number.

Examples of valid representations include `"2"`, `"0089"`, `"-0.1"`, `"+3.14"`, `"4."`, `"-.9"`, `"2e10"`, `"-90E3"`, `"3e+7"`, `"+6e-1"`, `"53.5e93"`, and `"-123.456e789"`. Invalid representations include `"abc"`, `"1a"`, `"1e"`, `"e3"`, `"99e2.5"`, `"--6"`, `"-+3"`, and `"95a54e53"`.

A valid number has one of two top-level forms:

- an integer followed by an optional exponent; or
- a decimal followed by an optional exponent.

An integer consists of an optional `+` or `-` sign followed by one or more digits.

A decimal consists of an optional sign followed by exactly one of these forms:

- one or more digits followed by `.`;
- one or more digits, then `.`, then one or more digits; or
- `.`, followed by one or more digits.

An exponent consists of `e` or `E` followed by an integer in the form defined above.
