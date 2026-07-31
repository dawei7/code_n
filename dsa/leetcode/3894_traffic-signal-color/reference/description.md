## Description

You are given an integer `timer` that records how many seconds remain on a traffic signal. The signal's current state is determined by these rules:

- when `timer == 0`, the state is `"Green"`;
- when `timer == 30`, the state is `"Orange"`;
- when $30 < \texttt{timer} \le 90$, the state is `"Red"`.

Return the string for the applicable state. If `timer` satisfies none of those rules, return `"Invalid"`.
