import sys

for line in sys.stdin:
  line = line.strip("\n\r")
  amount = int(line)
  discount_price = amount - (amount*0.1)
  print(str(discount_price))
