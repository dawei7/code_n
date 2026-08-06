## Description

An undirected connected graph has `n` cities numbered from zero to $n-1$. Each city has a name given by `names[city]`, and every pair in `roads` connects two cities that may be consecutive in a route.

Construct a route containing exactly as many cities as `targetPath` contains names. Consecutive route entries must be connected by a road; revisiting cities and roads is allowed. The edit distance of the route is the number of positions where the visited city's name differs from the corresponding target name. Return any valid route with minimum possible edit distance.
