## Function Contract

`solve(ip: str, n: int) -> list[str]`

**Inputs**

- `ip`: the first IPv4 address in dotted-decimal form.
- `n`: the number of consecutive IPv4 addresses to cover, beginning at `ip`.

**Return value**

Return a minimum-length list of strings in `"base-address/prefix-length"` form whose CIDR ranges together cover exactly the inclusive interval `[ip, ip + n - 1]`. No returned block may cover an address outside that interval. If several minimum-length covers are possible, any of them is valid.
