text = str(input())
x = text.split()              #разбивает строку на список строк
y = len(text)-text.count(" ") #не считает пробелы
count = 0
for it in x:
    count+=x.count(it)        #считает кол-во разделенных строк
print(y/count )  
    
