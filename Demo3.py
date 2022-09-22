book = {"ds":20,"java":80,"c++":40,"js":300}

name = input("Enter book name: ")
quant = int(input("Enter quantity: "))

for i in(book):
    if i == name:
        book[i] += quant
print(book)


# other logic
book = {"ds":20,"java":80,"c++":40,"js":300}

name = input("Enter book name: ")
quant = int(input("Enter quantity: "))

if name in book:
    book[name]+=quant
else:
    print("Book doesn't exist")
print(book)
