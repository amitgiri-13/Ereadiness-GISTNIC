import matplotlib.pyplot as plt
import csv

def get_columns_from_csv(file_path):
    column1 = []
    column2 = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            if len(row) >= 2:
                column1.append(int(row[0]))  # Ensure years are integers
                column2.append(row[1])
    return column1, column2

# File path
data = "/home/amit/Repositories/College/CaseStudy/Ereadiness-GISTNIC/Finding/InNepal/ict_history_nepal - Sheet1.csv"
years, events = get_columns_from_csv(data)

# Plot setup
fig, ax = plt.subplots(figsize=(20, 10))  # Increased figure size

# Plotting the timeline
for i, (year, event) in enumerate(zip(years, events)):
    ax.plot(0, year, 'o', markersize=10, color='skyblue')  # Plot points
    ax.text(0.2, year, event, va='top', fontsize=10, wrap=True)  # Add event text to the right of the points

# Customizing the axes
ax.set_ylim(min(years) - 1, max(years) + 1)  # Adjust the y-axis limits dynamically
ax.set_xlim(-0.5, 1.5)  # Expand x-axis to fit text
ax.set_yticks(years)  # Show only event years on the y-axis
ax.set_yticklabels(years, fontsize=10)  # Format year labels
ax.set_xticks([])  # Remove x-axis ticks for a clean look

# Add title
ax.set_title("ICT History of Nepal (1972-2015)", fontsize=14)

# Hide unnecessary spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Adjust layout to prevent overlap
plt.subplots_adjust(left=0.2, right=0.8, top=0.95, bottom=0.05)

# Save the plot
plt.savefig("charts/ict_nepal_timeline.png", dpi=300, bbox_inches='tight')
plt.show()
