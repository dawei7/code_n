## Function Contract

Construct one `TrafficLight` instance for an intersection whose initial green road is Road A. The judge may invoke its method concurrently:

`carArrived(carId, roadId, direction, turnGreen, crossCar)`

**Inputs**

- `carId`: the unique identifier of the arriving car.
- `roadId`: the road the car is using; `1` identifies Road A and `2` identifies Road B.
- `direction`: the car's direction, where `1` and `2` belong to Road A and `3` and `4` belong to Road B.
- `turnGreen`: a zero-argument judge callback that changes the arriving car's road to green. Invoke it only when that road is currently red.
- `crossCar`: a zero-argument judge callback that makes this arriving car cross. Invoke it once after its road is green.

**Return value**

- `carArrived` returns no value. Across concurrent calls, every car must cross, different roads must never cross simultaneously, redundant green changes are forbidden, and all calls must finish without deadlock.
