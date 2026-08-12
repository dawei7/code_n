import math


def solve(
    h0: float = 100.0, v0: float = 20.0, g: float = 9.81, decimals: int = 4
) -> str:
    """Find the volume of the region through which firecracker fragments move before reaching the ground.
    
    Time Complexity: O(1) via Paraboloid of Revolution Kinematic Envelope Integration
    Space Complexity: O(1)
    """
    H = h0 + (v0**2) / (2.0 * g)
    V = (math.pi * (v0**2) * (H**2)) / g
    return f"{V:.{decimals}f}"
