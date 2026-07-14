from graphviz import Digraph

activity = Digraph("MDP_Activity_Diagram", format="png")

# Top to Bottom Layout
activity.attr(rankdir="TB", bgcolor="white", splines="ortho", nodesep="0.6", ranksep="0.8")

# Default Node Style
activity.attr("node",
              fontname="Arial",
              fontsize="12",
              style="filled",
              color="black")

# -----------------------------
# Nodes
# -----------------------------

activity.node("Start",
              "START",
              shape="circle",
              fillcolor="#90EE90")

activity.node("Init",
              "Initialize\nMDP",
              shape="box",
              fillcolor="#87CEFA")

activity.node("State",
              "Define\nStates\n(S1,S2,S3)",
              shape="box",
              fillcolor="#FFFACD")

activity.node("Action",
              "Define\nActions\n(A1,A2)",
              shape="box",
              fillcolor="#FFFACD")

activity.node("TP",
              "Store Transition\nProbabilities",
              shape="box",
              fillcolor="#D8BFD8")

activity.node("Reward",
              "Store\nReward Matrix",
              shape="box",
              fillcolor="#F4A460")

activity.node("Display",
              "Display States,\nActions,\nMatrices",
              shape="box",
              fillcolor="#AFEEEE")

activity.node("Decision",
              "More\nStates?",
              shape="diamond",
              fillcolor="#FFD700")

activity.node("Current",
              "Select\nCurrent State",
              shape="box",
              fillcolor="#E6E6FA")

activity.node("Choose",
              "Choose\nAction",
              shape="box",
              fillcolor="#E6E6FA")

activity.node("Transition",
              "Apply\nTransition\nProbability",
              shape="box",
              fillcolor="#98FB98")

activity.node("Next",
              "Move to\nNext State",
              shape="box",
              fillcolor="#98FB98")

activity.node("RewardCalc",
              "Receive\nReward",
              shape="box",
              fillcolor="#FFB6C1")

activity.node("Expected",
              "Calculate\nExpected Reward",
              shape="box",
              fillcolor="#87CEEB")

activity.node("Summary",
              "Generate\nSummary Table",
              shape="box",
              fillcolor="#FFA07A")

activity.node("Visual",
              "Visualize\nGrid Environment\n& State Diagram",
              shape="box",
              fillcolor="#ADD8E6")

activity.node("End",
              "END",
              shape="doublecircle",
              fillcolor="#90EE90")

# -----------------------------
# Connections
# -----------------------------

activity.edge("Start", "Init")
activity.edge("Init", "State")
activity.edge("State", "Action")
activity.edge("Action", "TP")
activity.edge("TP", "Reward")
activity.edge("Reward", "Display")
activity.edge("Display", "Decision")

activity.edge("Decision", "Current", label="Yes")
activity.edge("Current", "Choose")
activity.edge("Choose", "Transition")
activity.edge("Transition", "Next")
activity.edge("Next", "RewardCalc")
activity.edge("RewardCalc", "Expected")
activity.edge("Expected", "Decision")

activity.edge("Decision", "Summary", label="No")
activity.edge("Summary", "Visual")
activity.edge("Visual", "End")

# -----------------------------
# Generate Diagram
# -----------------------------

activity.render("MDP_Activity_Diagram", view=True)

print("Activity Diagram Generated Successfully!")