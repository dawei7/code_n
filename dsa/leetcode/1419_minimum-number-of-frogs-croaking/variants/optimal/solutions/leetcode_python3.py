class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        sound = "croak"
        waiting = [0] * 4
        active = 0
        maximum_active = 0

        for character in croakOfFrogs:
            stage = sound.find(character)
            if stage == 0:
                waiting[0] += 1
                active += 1
                maximum_active = max(maximum_active, active)
            elif stage > 0 and waiting[stage - 1] > 0:
                waiting[stage - 1] -= 1
                if stage == 4:
                    active -= 1
                else:
                    waiting[stage] += 1
            else:
                return -1

        return maximum_active if active == 0 else -1
