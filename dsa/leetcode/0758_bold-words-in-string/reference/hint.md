## Hint

First determine which source positions should be bold and record that result in a Boolean mask. Then insert tags only at group boundaries. Position `i` starts a bold group exactly when `mask[i]` is true and either `i == 0` or `mask[i - 1]` is false; identify the end of a group with the corresponding condition on the following position.
