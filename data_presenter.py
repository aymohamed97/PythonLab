open_file = open("CupcakeInvoices.csv")

for row in open_file:
  print(row.rstrip())

open_file = open("CupcakeInvoices.csv")

for line in open_file:
    line= line.rstrip().split(',')
    print(line[2])

open_file = open("CupcakeInvoices.csv")

for line in open_file:
    line= line.rstrip().split(',')
    sum = float(line[3]) * float(line[4])
    print(round(sum, 2))

open_file = open("CupcakeInvoices.csv")

total = 0
for line in open_file:
    line= line.rstrip().split(',')
    sum = float(line[3]) * float(line[4])
    total += sum
print(round(total, 2))