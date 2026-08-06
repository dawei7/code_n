## Description

Start with an empty string \`s\`. The arrays \`words\` and \`costs\` have equal length, and choosing index \`i\` appends \`words[i]\` to the end of \`s\` while charging \`costs[i]\`. Any index may be chosen repeatedly, and operations may be performed any number of times.

Find the minimum total cost of a sequence of appends that makes \`s\` exactly equal to \`target\`. Every append must therefore match the next unbuilt portion of the target; extra or different characters cannot be removed. Return \`-1\` when no sequence of available words constructs the complete target.
