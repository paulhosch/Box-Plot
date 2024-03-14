
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Setup Matplotlib to use Arial font and uniform font sizes
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 12  

# Path to the preprocessed data file and save path for the figure
data_file_path = '/Users/paulhosch/Library/CloudStorage/OneDrive-Persönlich/Uni/IWW/BoxPlot/preprocessed_dataMax.csv'
save_path = '/Users/paulhosch/Library/CloudStorage/OneDrive-Persönlich/Uni/IWW/BoxPlot/figures/figure_.svg'  

# Load the preprocessed data
data = pd.read_csv(data_file_path)

# Prepare data for plotting: Remove missing values from each column
data_for_plotting = [data[col].dropna().values for col in data.columns]

# Initialize figure with specified dimensions
plt.figure(figsize=(6, 4))  # 6x4 inches figure size

# Generate box plot with aesthetic customizations
plt.boxplot(data_for_plotting,
            notch=False,  # Disables notch on box for cleaner appearance
            vert=True,  # Vertical box orientation
            patch_artist=True,  # Enables box color filling
            widths=0.6,  # Custom width for each box
            showmeans=False,  # Do not show mean markers for a cleaner look
            showcaps=True,  # Display caps at ends of whiskers
            showbox=True,  # Ensure boxes are visible
            showfliers=False,  # Hide outliers for focus on main data
            boxprops=dict(facecolor='lightgrey', color='black', linewidth=1),  # Box appearance customization
            whiskerprops=dict(color='black', linewidth=1.5),  # Whisker appearance customization
            capprops=dict(color='black', linewidth=1.5),  # Cap appearance customization
            medianprops=dict(color='black', linewidth=1),  # Median line customization
            )

# Plot title, axis labels, and ticks customization
plt.title('Distribution of Flow Velocity', fontweight='bold')  # Bold title
plt.xticks(ticks=np.arange(1, len(data.columns) + 1), labels=data.columns, rotation=45)
plt.ylabel('m/s')

# Configure solid gridlines for better readability
plt.grid(True, linestyle='-', linewidth=0.5, color='grey', axis='y', alpha=0.7)

# Remove top and right spines for a cleaner look
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust subplot parameters to prevent overlap
plt.tight_layout()

# Save the figure in SVG format at the specified path
plt.savefig(save_path, format='svg')

# Display the plot
plt.show()
