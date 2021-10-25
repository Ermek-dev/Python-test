#This program is calculating your month,year costs
apartment = int(input("Houson payment dollars per month: "))
food = int(input("Food and other household needs dollars per month: "))
utilites_per_month = int(input("Gas,electricity,water,phone dollars per month: "))
transport = int(input("Transport dollars per month: "))
insurance = int(input("Insurance dollars per month: "))
total = apartment+food+utilites_per_month+transport+insurance  #
print("\nTotal amount per month: ",total,"dollars")
print((str("Total per year: ")),total*12,"dollars")
