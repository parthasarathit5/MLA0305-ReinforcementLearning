import pandas as pd

summary_data = [
    ["S1", "A1", 2.8],
    ["S1", "A2", 0.0],
    ["S2", "A1", 3.1],
    ["S2", "A2", 2.6],
    ["S3", "A1", 3.6],
    ["S3", "A2", -0.6]
]

summary_table = pd.DataFrame(
    summary_data,
    columns=["Current State", "Action", "Expected Reward"]
)

print("Output Summary Table\n")
print(summary_table)