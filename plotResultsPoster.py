import matplotlib.pyplot as plt

# Data for each model
data = {
    "Real": [60.04, 39.06],
    "Linear Regression": [51.24, 48.75],
    "Random Forest": [41.04, 57.67],
    "KNN": [38.39, 60.2]
}

# Turnout percentages for each model
turnout_data = {
    "Real": 0.6712*100,
    "Linear Regression": 100,
    "Random Forest": 0.62588*100,
    "KNN": 0.3572*100
}

# Labels for the parties
labels = ["Republicans", "Democrats"]

# Colors for the pie charts
colors = ["red", "blue"]

# ------------------ PLOT 1: Pie Charts ------------------
fig1, axes = plt.subplots(2, 2, figsize=(12, 10))
fig1.suptitle("Predicted Vote Distribution by Model", fontsize=16, y=0.95)

# Flatten axes for easier indexing
axes_flat = axes.flatten()

# Plot the pie charts
for ax, (model, values) in zip(axes_flat, data.items()):
    ax.pie(
        values,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors
    )
    ax.set_title(model)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.93])

# ------------------ PLOT 2: Turnout Bars ------------------
fig2, ax = plt.subplots(figsize=(12, 6))
fig2.suptitle("Voter Turnout by Model", fontsize=16, y=0.95)

# Plot the turnout bars
models = list(turnout_data.keys())
turnout_values = list(turnout_data.values())
non_turnout_values = [100 - turnout for turnout in turnout_values]

# Plot bars for each model
bar_width = 0.4
x = range(len(models))

ax.bar(
    x, turnout_values, width=bar_width, color="green", edgecolor="black"
)
ax.bar(
    x, non_turnout_values, width=bar_width, bottom=turnout_values, color="grey", edgecolor="black"
)

# Add labels and ticks
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.set_ylim(0, 100)
ax.set_ylabel("Percentage (%)")
ax.set_title("Turnout Breakdown")

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.93])

# Show the plots
plt.show()