import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/sample_data.csv')
plt.plot(df['x'], df['y'], marker='o')
plt.title('Sample Line Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
