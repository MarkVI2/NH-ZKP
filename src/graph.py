import matplotlib.pyplot as plt
import os.path as osp
from statistics import mean


def listCreation(bit_size: int, fPath: str, listName: list):
    file = open(osp.join(fPath, f"{bit_size}bit.txt"), "r").read()
    listName = file.replace(" ", "").split(",")
    fList = list(map(float, listName))
    print(mean(fList))
    powList = [(fList[i]**10) for i in range(0, len(fList))]
    return powList


fPath = "../snapshot/loss/"

x = [i for i in range(0, 1000)]

'''
bit_16 = np.genfromtxt(osp.join(fPath, "16bit.csv"), delimiter=",")
bit_32 = np.genfromtxt(osp.join(fPath, "32bit.csv"), delimiter=",")
bit_48 = np.genfromtxt(osp.join(fPath, "48bit.csv"), delimiter=",")
'''
bit_16, bit_32, bit_48 = [], [], []
bit_16 = listCreation(16, fPath, bit_16)
bit_32 = listCreation(32, fPath, bit_32)
bit_48 = listCreation(48, fPath, bit_48)

plt.plot(x, bit_16, label="16 bit", linestyle="-")
plt.plot(x, bit_32, label="32 bit", linestyle="-.")
plt.plot(x, bit_48, label="48 bit", linestyle=":")

plt.xlabel("Iteration number")
plt.ylabel("$\mathregular{Loss Recorded^{10}}$")

plt.legend()
plt.show()
