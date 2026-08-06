## Description

An RGB color written as `"#AABBCC"` has the shorthand form `"#ABC"` when each two-digit channel repeats one hexadecimal digit. For example, `"#15c"` expands to `"#1155cc"`.

For colors `"#ABCDEF"` and `"#UVWXYZ"`, interpret `AB`, `CD`, and `EF` as the first color's hexadecimal channel values and `UV`, `WX`, and `YZ` as the second color's. Their similarity is

$$
-\left(\mathrm{AB}-\mathrm{UV}\right)^2-\left(\mathrm{CD}-\mathrm{WX}\right)^2-\left(\mathrm{EF}-\mathrm{YZ}\right)^2.
$$

Given `color` in six-digit form, find a color that can be represented by some three-digit shorthand `"#XYZ"` and maximizes this similarity to `color`.

Return that color in expanded six-digit form. If several colors share the highest possible similarity, any of them is accepted.
