import matplotlib.pyplot as plt
import numpy as np

# DATA
categories = [
    'Ministry of Defence', 
    'Ministry of Education', 
    'Ministry of Science and Technology and Environment', 
    'Ministry of Women, Children and Social Welfare',
    'Ministry of Physical Infrastructure and Transport'
]
values = [
    2.14813,
    2.40093,
    2.27879,
    1.93086,
    2.28043,
]

# Colors For each Category
colors = [
    'orange', 
    'lightblue', 
    'lightgreen', 
    'pink', 
    'salmon'
    ]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the figure size to better fit the labels

# Create the bar chart with different colors
bars = ax.bar(categories, values, color=colors, edgecolor='black')

# Set axis limits and labels
ax.set_ylim(0, 4)
ax.set_yticks(np.arange(0, 5, 1))  
ax.set_ylabel('Scores')
ax.set_title('E-preparedness score of five ministries of Nepal in 2015')

# Add a legend
for i, category in enumerate(categories):
    ax.bar(0, 0, color=colors[i], label=category)  # Invisible bars for legend
ax.legend(title="Ministries", loc="upper right", bbox_to_anchor=(1,1))

# Remove x-axis labels
ax.set_xticklabels([])

# Value annotations on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
    
# Score-based scale on the right side
scale_labels = ["Poor", "Average", "Good", "Very Good"]
for i, label in enumerate(scale_labels, start=1):
    ax.text(5.1, i - 0.1, f"{i}: {label}", fontsize=10, va='center', ha='left', color='black')

# Add horizontal grid lines for clarity
ax.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)


# Save the plot as an image
plt.tight_layout()
plt.savefig('charts/e-preparedness_of_ministries_2015.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
