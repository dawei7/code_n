## Function Contract

**Inputs**

- `operations`: A sequence of constructor and method names. Its first entry is `"RideSharingSystem"`.
- `arguments`: A parallel sequence in which each entry contains the arguments for the operation at the same index.

Let $Q = \lvert\texttt{operations}\rvert = \lvert\texttt{arguments}\rvert$ be the length of the complete operation trace.

The constructor takes no arguments. `addRider` and `cancelRider` each receive one `riderId`; `addDriver` receives one `driverId`; and `matchDriverWithRider` takes no arguments. Arrival order is tracked independently for riders and drivers. A match removes one rider and one driver only when both are available, while an ineffective cancellation or unsuccessful match leaves all valid waiting entries unchanged.

**Return value**

Return one result for every operation. The constructor and methods without a return value contribute `null`. Each matching call contributes `[driverId, riderId]` for the FIFO pair it removes, or `[-1, -1]` if a pair cannot be formed.
