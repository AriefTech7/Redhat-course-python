#!/usr/bin/env python3
cnt = 0
total = 0
while cnt <= 100:
    cnt += 1
    if cnt % 4 == 0:
        continue         # skip even multiples of 4
    if cnt * cnt > 400:
        break            # will happen at cnt = 21
    total += cnt

print("Total is:", total, "    Count is:", cnt)


count = 0

while count < 10:
    count += 1
    if count % 2 == 0:  # Check if the count is even
        continue         # Skip the rest of the loop for even counts
    print(count)        # This will only print odd counts
