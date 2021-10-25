#Эта программа рассчитывает ваши ежемесячные расходы,а также общую сумму за год
apartment = int( input("Оплата жилья тенге в месяц: "))
food = int(input("Продукты питания и другие бытовые нужды тенге в месяц: "))
utilites_per_month = int(input("Газ,электричество,вода,телефон тенге в месяц: "))
transport = int(input("Транспорт тенге в месяц: "))
insurance = int(input("Страхование тенге в месяц: "))
total = apartment+food+utilites_per_month+transport+insurance #сложение всех переменных
print("\nОбщая сумма за месяц: ",total)
print((str("Итого в год: ")),  total*12)


