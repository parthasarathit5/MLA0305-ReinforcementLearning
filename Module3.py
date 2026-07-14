import pandas as pd

reward_data = [
    ["S1", "A1", "S2", 5],
    ["S1", "A2", "S2", 10],
    ["S1", "A1", "S3", -1],
    ["S1", "A2", "S3", -5],
    ["S2", "A1", "S1", 3],
    ["S2", "A2", "S1", 7],
    ["S2", "A1", "S3", 2],
    ["S2", "A2", "S3", 1],
    ["S3", "A1", "S1", 4],
    ["S3", "A2", "S1", 6],
    ["S3", "A1", "S2", 0],
    ["S3", "A2", "S2", -2]
]

print("{:<15} {:<10} {:<12} {:<8}".format(
    "Current State", "Action", "Next State", "Reward"))
print("-" * 50)

for row in reward_data:
    print("{:<15} {:<10} {:<12} {:<8}".format(*row))