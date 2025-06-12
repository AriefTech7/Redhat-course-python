import sys

sys.argv.pop(0)
sys.argv.sort()

for elem in sys.argv:
    print(elem)