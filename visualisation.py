import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the tips dataset
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
tips.head()

plt.figure(figsize=(10, 6))
sns.histplot(tips['total_bill'], kde=True)
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='total_bill', y='tip', data=tips, hue='time', style='time')
plt.title('Total Bill vs. Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.legend(title='Time of Day')
plt.show()

