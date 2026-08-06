## Description

Begin with an empty screen and a keyboard that provides four operations:

- `A`: print one `A` on the screen.
- `Ctrl-A`: select the entire screen.
- `Ctrl-C`: copy the selection into the buffer.
- `Ctrl-V`: append the buffer contents after everything already printed on the screen.

Given an integer `n`, choose a sequence containing at most `n` keypresses. Return the greatest number of `A` characters that can be printed on the screen within that budget. Selection and copying consume keypresses even though they do not immediately increase the displayed character count.
