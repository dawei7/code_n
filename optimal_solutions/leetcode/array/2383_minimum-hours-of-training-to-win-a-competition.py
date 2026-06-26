from typing import List

def solve(initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
    total_training_hours = 0
    current_energy = initialEnergy
    current_experience = initialExperience
    
    for e_req, x_req in zip(energy, experience):
        # Check energy requirement
        if current_energy <= e_req:
            needed = e_req - current_energy + 1
            total_training_hours += needed
            current_energy += needed
            
        # Check experience requirement
        if current_experience <= x_req:
            needed = x_req - current_experience + 1
            total_training_hours += needed
            current_experience += needed
            
        # Update stats after winning
        current_energy -= e_req
        current_experience += x_req
        
    return total_training_hours
