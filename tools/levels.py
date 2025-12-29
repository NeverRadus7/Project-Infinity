import random, math

XpToLevel = 2
LevelMultiply = 3

for a in range(1,100):
    AbsLevel = int((a)) * (XpToLevel+a*LevelMultiply)
    print(a, AbsLevel)
