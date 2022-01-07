x = str(input())
y = str(input())
count = 0
for item in x:
    if y in x:
        count+=y.count(item)
print(int(count/len(x)*100))    



