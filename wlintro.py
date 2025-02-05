import time
import os
import random
from wlengine import *

wl.ConsoleSetSize()
#logo = open("data//whitelight_logo.wlf","r", encoding="utf-8")

wl.Skip()
print(LICENSE.read())
for abs in range(5):
    print()
time.sleep(3)

for abs in range(31):
    print()

wl.Icon()
print(f"Engine version: {EngineVersion}".center(ConsoleSizeX))

for abs in range(7):
    print()

print("Зачекайте будь ласка")
time.sleep(3)