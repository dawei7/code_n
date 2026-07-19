def solve(n: int, k: int) -> list[int]:
    # Use a set to efficiently track friends who have received the ball.
    # Friends are 1-indexed, so we store their IDs directly.
    received_ball = set()

    # The game starts with friend 1 holding the ball.
    current_friend = 1
    # The round number starts from 1.
    round_num = 1

    # Simulate the game until a friend receives the ball who has already received it.
    while current_friend not in received_ball:
        # Mark the current friend as having received the ball.
        received_ball.add(current_friend)

        # Calculate the number of steps for this round.
        steps = round_num * k

        # Calculate the next friend to receive the ball.
        # We adjust to 0-indexed for modulo arithmetic (current_friend - 1),
        # then convert back to 1-indexed (+ 1).
        current_friend = (current_friend - 1 + steps) % n + 1

        # Increment the round number for the next iteration.
        round_num += 1

    # After the game ends, identify the friends who never received the ball.
    losers = []
    for i in range(1, n + 1):
        if i not in received_ball:
            losers.append(i)

    # The problem requires the output to be sorted in ascending order,
    # which is naturally achieved by iterating from 1 to n.
    return losers
