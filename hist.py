import numpy as np
import matplotlib.pyplot as plt


cnt=0
rand_numbers = np.random.randint(1,11,1000)
print(rand_numbers)
for i in rand_numbers:
    if (i >5):
        cnt=cnt+1
print("number of  output coss threshold 5:",cnt)
plt.hist(rand_numbers,bins = (10),edgecolor = "black")
plt.show()