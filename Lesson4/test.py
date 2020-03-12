# coding: utf-8
days = [d for d in range(1, 32)]

wdays6 = [wd for (i, wd) in enumerate(days,1) if i % 7 != 0]  # Удаляем каждый 7-й день
# Удаляем каждый 6 день в оставшихся после первого удаления:
wdays5 = [wd for (i, wd) in enumerate(wdays6, 1) if i % 6 != 0]

print(wdays5)

days = [d+1 for d in range(31) if d%7<5]
print(days)