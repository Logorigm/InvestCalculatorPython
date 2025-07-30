period = 45
start_summ = 200000
Summ = start_summ
every_up = 150000
precent = 15
for i in range(0, period):
    Summ *= (1 + precent / 100)
    Summ += every_up * 12
    Summ *= 0.92
print(Summ)