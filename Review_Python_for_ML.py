import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]

# 1
plt.plot(x, y)
plt.show()

# 2
plt.figure(figsize = (5, 5))
plt.plot(x, y, color='blue')
plt.title("Line Chart")
plt.legend(["Line 1"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 3
plt.bar(x, y, color='green')
plt.title("Bar Chart")
plt.legend(["Line 1"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 4
plt.scatter(x, y, color = "red")
plt.title("Scatter Plot")
plt.legend(["Line 1"])
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# 5
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots( figsize=(5, 2.7) )
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Simple Plot")
ax.legend()
plt.show()

# 6 
x = np.linspace(0, 2, 100)
fig, axs = plt.subplots(2, 1, figsize=(4, 4))
axs[0].plot(x, x, label='linear')
axs[0].plot(x, x**2, label='quadratic')
axs[0].set_title('Line Plot')
axs[0].set_xlabel('x label')
axs[0].set_ylabel('y label')
axs[0].legend()
x = [1,5,6,3,2,7]
y = [2,3, 7, 8,1,2]
axs[1].scatter(x, y, label='scatter')
axs[1].set_title('Scatter Plot')
axs[1].set_xlabel('x label')
axs[1].set_ylabel('y label')
axs[1].legend()
plt.tight_layout()
plt.show()

# 7
df = pd.read_csv("sales_data_100.csv")
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Month'] = df['OrderDate'].dt.strftime('%B')
month_order = ['January', 'February', 'March']
df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)
summary = df.pivot_table(index='Month', columns='Category', values='Quantity', aggfunc='sum', fill_value=0,
    observed=False)
summary.plot(kind='bar', figsize=(14, 6))
plt.ylabel("Quantity")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()



