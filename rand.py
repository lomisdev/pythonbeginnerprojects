import random

members = ['Daniel', 'Martin', 'James', 'Johns', 'Bornface', 'Evans']
pick_count = {name: 0 for name in members}  # Initialize count for each name

# Simulate 1000 random picks
for i in range(1000):
    leader = random.choice(members)
    pick_count[leader] += 1

# Display results
for name, count in pick_count.items():
    print(f"{name}: chosen {count} times")