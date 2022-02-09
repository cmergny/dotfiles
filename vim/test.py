import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 30)  
y = x+3

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
