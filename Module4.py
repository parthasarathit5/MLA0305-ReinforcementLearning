states = ["S1", "S2", "S3"]
actions = ["A1", "A2"]

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
    ("S1", "A1", "S3"): -1,
    ("S1", "A2", "S2"): 10,
    ("S1", "A2", "S3"): -5,

    ("S2", "A1", "S1"): 3,
    ("S2", "A1", "S3"): 2,
    ("S2", "A2", "S1"): 7,
    ("S2", "A2", "S3"): 1,

    ("S3", "A1", "S1"): 4,
    ("S3", "A1", "S2"): 0,
    ("S3", "A2", "S1"): 6,
    ("S3", "A2", "S2"): -2
}

print("Expected Reward Calculation\n")

for state in states:
    for action in actions:

        print(f"State = {state}, Action = {action}")

        expected_reward = 0

        for next_state, probability in transition_probabilities[(state, action)].items():

            reward = rewards[(state, action, next_state)]
            value = probability * reward

            print(f"P({next_state}|{state},{action}) × R({state},{action},{next_state})")
            print(f"= {probability} × {reward} = {value}")

            expected_reward += value

        print(f"Expected Reward ({state}, {action}) = {expected_reward}")
        print("-" * 50)