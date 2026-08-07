from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(
        self,
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str],
    ) -> List[str]:
        dependents = defaultdict(list)
        missing = {}

        for recipe, required in zip(recipes, ingredients):
            missing[recipe] = len(required)
            for ingredient in required:
                dependents[ingredient].append(recipe)

        available = deque(supplies)
        possible = []

        while available:
            item = available.popleft()
            for recipe in dependents[item]:
                missing[recipe] -= 1
                if missing[recipe] == 0:
                    possible.append(recipe)
                    available.append(recipe)

        return possible
