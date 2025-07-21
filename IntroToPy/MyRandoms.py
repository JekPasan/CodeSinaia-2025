import matplotlib.pyplot as plt
from random import randint

vals = {}
vals_list = []

class Val():
    def __init__(self, val: int, freq: int = 0, positions: list = []):
        self.val = val
        self.freq = freq
        self.positions = positions
    
    def increment(self, pos: int):
        self.freq += 1
        self.positions.append(pos)

count = int(input("Enter the number of random values to generate: "))
min_val = int(input("Enter the minimum value: "))
max_val = int(input("Enter the maximum value: "))
it = 0
file = open("randoms.txt", "w")

while it < count:
    i = randint(min_val, max_val)
    vals_list.append(i)
    if i not in vals:
        vals[i] = Val(i, 1, [it])
    else:
        vals[i].increment(it)
    it += 1

for key in vals.keys():
    file.write(f"{vals[key].val}: {vals[key].positions}\n")
file.close()

# aflam numarul de valori unice
print(f"Number of unique values: {len(vals)}")

# aflam minimul si maximul
print(f"Minimum value: {min(vals.keys())}")
print(f"Maximum value: {max(vals.keys())}")

# aflam valoarea mediana
sorted_vals = sorted(vals.keys())
if len(sorted_vals) % 2 == 1:
    median = sorted_vals[len(sorted_vals) // 2]
print (median)

# aflam valoarea medie
sum = 0
cnt = 0
for key in vals.keys():
    cnt += vals[key].freq
    sum += vals[key].val * vals[key].freq
medie = sum/cnt if cnt > 0 else 0
print(medie)

# aflam deviatia standard
sum = 0
for key in vals.keys():
    sum += vals[key].freq * (vals[key].val - medie) ** 2
deviation = (sum / cnt) ** 0.5 if cnt > 0 else 0

# generam un grafic cu bare
fig, ax = plt.subplots()
ax.bar(vals.keys(), [vals[key].freq for key in vals.keys()], color='orange')
plt.show()

# generam un grafic plot
print(vals_list)
plt.plot(vals_list, marker='o', linestyle='-', color='blue')
plt.show()