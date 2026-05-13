"""
============================================================
Q1. Hero Quest
============================================================
A hero goes on an adventure, starting at Full Health.
He fights monsters and loses health randomly each round.

Requirements:
- Start with 100 health
- Print starting message
- Lose between 1 to 15 health each round (random)
- Use a while-loop
- Continue until health <= 0
- Print total number of battles fought

============================================================
"""

# ============================================================
# Step 1: Import required module
# ============================================================

import random

# ============================================================
# Step 2: Initialize variables
# ============================================================

health = 100
battles = 0
# ============================================================
# Step 3: Print starting message
# ============================================================

print("Hero starts on his adventure with Health: 100")

# ============================================================
# Step 4: Create while-loop for battles
# ============================================================
# - Randomly reduce health between 1 and 15
# - Increase battle counter
# - Print updated health
# ============================================================

while health >= 0:
    battles = battles + 1
    health = health - random.randint(1,15)
    print(f"After fighting monsters, his Health is now: {health}")
# ============================================================
# Step 5: Print final result
# ============================================================
# Print in this format:
# He fought xxx battles, and died
# ============================================================
print(f"He fought {battles} battles, and died")