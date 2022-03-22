import numpy as np
import matplotlib.pyplot as plt
import math

#Sätter bara en övre gräns
top_value = 5
constant_factor = 2
#Ingen tillväxt baserad på input size: O(1) time complexity. Till exempel index look-up i dictionary:
vals_o1 = [constant_factor for val in range(top_value)]

#Logaritmisk tillväxt: t.ex. binärsökning i sorterad array
valslog = [max(np.log(val), 0) for val in range(top_value)]

#Linjär tillväxt: till exempel stega genom en array eller lista
valsn = [val for val in range(top_value)]

#Linjär * logaritmisk tillväxt: typiskt vanligt för sortering av listor eller arrays
valsnlog = [val*max(np.log(val),0) for val in range(top_value)]

#Kvadratisk tillväxt: t.ex. elementvis multiplikation av nxn matriser
valsn2 = [val**2 for val in range(top_value)]

#Någon form utav hemsk, hemmasnickrad algoritm
valsn3 = [val**3 for val in range(top_value)]

#Brute forcelösning av SHA256
vals2n =[2**val for val in range(top_value)]

#Brute forcelösning av Travelling Salesman Problem
vals_nfac = [math.factorial(val) for val in range(top_value)]

x = np.arange(top_value)
plt.plot(x, vals_o1, label = "O(1): Constant")
plt.plot(x, valslog, label = "O(log(n)): logarithmic growth")
plt.plot(x, valsn, label = "O(n): 1st degree")
plt.plot(x, valsnlog, label = "O(nlog(n)n): 1st degree * log(n)")
plt.plot(x, valsn2, label = "O(n^2): 2nd degree")
plt.plot(x, valsn3, label = "O(n^3): 3rd degree")
plt.plot(x, vals2n, label = "O(2^n): Exponential growth")
plt.plot(x, vals_nfac, label = "O(n!): factorial")
plt.title("Time complexities: O(f(n))")
plt.legend()
plt.show()



