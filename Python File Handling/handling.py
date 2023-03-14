'''with open ("student.txt", 'w') as file:
    for i in range(3):
        name=input("Enter 1st Name:- ")
        age=input("Enter Ages:- ")
        course=input("Enter current course:- ")
        batch=input("Enter current batch:- ")
        file.write(name+","+age+","+course+","+batch)
'''


with open ("product.txt", 'w') as file:
    for i in range(5):
     while True:
      pname=input("Enter product nmae:- ")
      quantity=int(input("Enter quantity:- "))
      price=float(input("Enter price:- "))
      file.write("pname+","+quantity+","+price")
choice = input("Do you want to enter more records? (y/n): ")
if choice.lower() == "n":
 with open("product.txt", "r") as file:
    invoice = "Product Name\tQuantity\tPrice\tTotal\n"
    for line in file:
        data = line.strip().split(",")
        total = int(data[1]) * float(data[2])
        invoice += f"{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{total}\n"
    print(invoice)
    with open("invoice.txt", "w") as invoice_file:
        invoice_file.write(invoice)

        

                 


















