def solve(features: list[str], responses: list[str]) -> list[str]:
    original_index = {feature: index for index, feature in enumerate(features)}
    popularity = {feature: 0 for feature in features}

    for response in responses:
        for word in set(response.split()):
            if word in popularity:
                popularity[word] += 1

    return sorted(
        features,
        key=lambda feature: (-popularity[feature], original_index[feature]),
    )
