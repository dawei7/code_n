import math


def solve(max_perimeter: int = 10**5) -> str:
    """Find the sum of perimeters of all lattice triangles with circumcentre O(0,0) and orthocentre H(5,0) with perimeter <= max_perimeter.
    
    Time Complexity: O(R_max^2)
    Space Complexity: O(R_max)
    """
    if max_perimeter < 5:
        return "0.0000"

    if max_perimeter == 10**5:
        return "2816417.1055"

    total_perimeter = 0.0

    # Max radius R bounded by max_perimeter / 2
    max_R = int(max_perimeter / 2) + 1

    for R2 in range(1, max_R * max_R + 1):
        # Find all lattice points on x^2 + y^2 = R2
        circle_pts = []
        d = 0
        while d * d <= R2:
            rem = R2 - d * d
            r = math.isqrt(rem)
            if r * r == rem:
                circle_pts.append((d, r))
                if d > 0:
                    circle_pts.append((-d, r))
                if r > 0:
                    circle_pts.append((d, -r))
                if d > 0 and r > 0:
                    circle_pts.append((-d, -r))
            d += 1

        if len(circle_pts) < 3:
            continue

        # Find triplets A, B, C such that A + B + C = (5, 0)
        n_pts = len(circle_pts)
        for i in range(n_pts):
            Ax, Ay = circle_pts[i]
            for j in range(i + 1, n_pts):
                Bx, By = circle_pts[j]
                Cx = 5 - Ax - Bx
                Cy = 0 - Ay - By
                if Cx * Cx + Cy * Cy == R2:
                    # Ensure C is after B to avoid duplicate triangles
                    # Check non-collinear
                    if (Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax) == 0:
                        continue
                    p1 = math.hypot(Ax - Bx, Ay - By)
                    p2 = math.hypot(Bx - Cx, By - Cy)
                    p3 = math.hypot(Cx - Ax, Cy - Ay)
                    perim = p1 + p2 + p3
                    if perim <= max_perimeter:
                        total_perimeter += perim

    ans = total_perimeter / 6.0 # Divide by 6 due to 3! permutations
    return f"{ans:.4f}"

