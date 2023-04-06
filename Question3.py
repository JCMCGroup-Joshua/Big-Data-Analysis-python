import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from a CSV file
df = pd.read_csv('Question3DataFull.csv')

# Create a figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Graph 1: Average Time in Hospital by Gender
ax = df.groupby(['gender'])['time_in_hospital'].mean().plot(
    kind='bar', color=['blue', 'pink'], alpha=0.8, ax=axs[0])
ax.set_title('Average Time in Hospital by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Time in Hospital')

for i, v in enumerate(df.groupby(['gender'])['time_in_hospital'].mean()):
    ax.text(i, v+0.2, str(round(v, 2)), horizontalalignment='center')

# Graph 2: Count of Patients by Gender and Age
sns.heatmap(df.groupby(['gender', 'age']).size(
).unstack(), cmap='YlOrRd', ax=axs[1])
axs[1].set_title('Count of Patients by Gender and Age')
axs[1].set_xlabel('Gender')
axs[1].set_ylabel('Age')

# Graph 3: Count of Patients by Gender and Admission Source ID
sns.heatmap(df.groupby(['gender', 'admission_source_id']
                       ).size().unstack(), cmap='YlOrRd', ax=axs[2])
axs[2].set_title('Count of Patients by Gender and Admission Source ID')
axs[2].set_xlabel('Gender')
axs[2].set_ylabel('Admission Source ID')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
