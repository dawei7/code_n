## Description

Build a video-sharing service whose videos are digit strings: the character at index $i$ is the content at minute $i$. The service stores each video's view, like, and dislike counts and supports uploads, removals, watching an inclusive minute range, reactions, and statistic queries.

An upload receives the smallest nonnegative `videoId` that is not currently in use. Removing a video makes its identifier available again. Watching an existing video adds one view and returns the requested substring, stopping at the video's last minute when `endMinute` extends farther. Operations targeting a missing identifier must return the specified sentinel or have no effect.

Implement `VideoSharingPlatform` so every operation obeys these state, identifier-reuse, range, and missing-video rules across the complete call sequence.
