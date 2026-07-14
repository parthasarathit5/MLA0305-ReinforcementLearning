states = ["S1", "S2", "S3"]
actions = ["A1", "A2"]

num_states = len(states)
num_actions = len(actions)

transition_probabilities = {
    ("S1", "A1"): {"S2": 0.6, "S3": 0.2},
    ("S1", "A2"): {"S2": 0.4, "S3": 0.8},

    ("S2", "A1"): {"S1": 0.7, "S3": 0.5},
    ("S2", "A2"): {"S1": 0.3, "S3": 0.5},

    ("S3", "A1"): {"S1": 0.9, "S2": 0.4},
    ("S3", "A2"): {"S1": 0.1, "S2": 0.6}
}

rewards = {
    ("S1", "A1", "S2"): 5,
    ("S1", "A2", "S2"): 10,
    ("S1", "A1", "S3"): -1,
    ("S1", "A2", "S3"): -5,

    ("S2", "A1", "S1"): 3,
    ("S2", "A2", "S1"): 7,
    ("S2", "A1", "S3"): 2,
    ("S2", "A2", "S3"): 1,

    ("S3", "A1", "S1"): 4,
    ("S3", "A2", "S1"): 6,
    ("S3", "A1", "S2"): 0,
    ("S3", "A2", "S2"): -2
}

print("Number of States:", num_states)
print("States:", states)

print("\nNumber of Actions:", num_actions)
print("Actions:", actions)

print("\nTransition Probabilities")
for key, value in transition_probabilities.items():
    state, action = key
    print(f"{state}, {action} -> {value}")

print("\nRewards")
for key, value in rewards.items():
    state, action, next_state = key
    print(f"R({state}, {action}, {next_state}) = {value}")