import numpy as np

states = ["S1", "S2", "S3"]

P_A1 = np.array([
    [0.0, 0.6, 0.2],
    [0.7, 0.0, 0.5],
    [0.9, 0.4, 0.0]
])

P_A2 = np.array([
    [0.0, 0.4, 0.8],
    [0.3, 0.0, 0.5],
    [0.1, 0.6, 0.0]
])

print("States:", states)

print("\nTransition Probability Matrix for Action A1")
print(P_A1)

print("\nTransition Probability Matrix for Action A2")
print(P_A2)