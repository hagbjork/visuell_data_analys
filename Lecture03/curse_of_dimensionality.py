import numpy as np
import matplotlib.pyplot as plt

dim = 10000

nr_of_dimensions = np.arange(dim)



#Avstånd från [0,0,0..0] till [1,1,1,..1] = sqrt(1+1+1...+1) -> tillväxthastighet svarar mot roten ur summan.
#Detta gör att mer information i classifiers som använder distansmått (t.ex. kNN) inte nödvändigtvis gynnas
#av att inkludera all information!

#Gör en lista med värden där varje värde är avståndet till nollpunkten för [1, 1, 1.. 1]-vektorer
norm_list = [np.linalg.norm(np.ones(vector)) for vector in range(dim)]
print(norm_list[:10])

plt.plot(nr_of_dimensions, norm_list)
plt.ylabel("Number of dimensions")
plt.xlabel("Distance from origin")
plt.title("Distance to origin for n-dimensional [1,1,..1] vectors")

plt.show()

