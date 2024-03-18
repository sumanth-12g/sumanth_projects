price = []
quantity = []
item = []
total = 0
Gst_amount = 0
Total_amount = 0
Date = []
def final_bill():
    print("________________  HOTEL SHIVA GANGA  ______________________")
    print( )
    print("                                             Date:         ")
    print("                                             Place: Bangalore")
    print("-------------------------------------------------------------")
    print("ORDERED FOODS           :           QUANTITY")
    print()

    i = 0
    while (i < len(item and quantity)):
        s = item[i]
        q = quantity[i]
        print(s,end="\t\t\t\t\t\t\t\t\t")
        print(q)
        i = i + 1

    print("_____________________________________________________________")
    calculation()
    print()
    print("    ---------THANK YOU VISIT AGAIN----------")

def calculation():
    Gst_amount = total * 18/118
    Total_amount = Gst_amount + total
    print("Gst Amount              =           {}".format(Gst_amount))
    print()
    print("TOTAL AMOUNT            =           {}".format(Total_amount))


def mrg():
     print("1.Idli")
     print("2.Dosa")
     print("3.Rice bath")
     a = int(input("Enter the food you want to order"))
     if(a==1):
         print("1.Idli           =            30 RS")
         item.append("Idli")
         qua = int(input("Enter the quantity you want to order"))
         quantity.append(qua)
         bill = 30 * qua
         price.append(bill)
     elif(a==2):
         print("2.Dosa            =             40 RS")
         item.append("Dosa")
         qua = int(input("Enter the quantity you want to order"))
         quantity.append(qua)
         bill = 40 * qua
         price.append(bill)
     elif(a==3):
         print("3.Rice bath       =             30 RS")
         item.append("Rice bath")
         qua = int(input("Enter the quantity you want to order"))
         quantity.append(qua)
         bill = 30 * qua
         price.append(bill)

def after():
    print("1.south indian meal")
    print("2.north indian meal")
    a = int(input("Enter the food you want to order"))
    if(a==1):
        print("1.south indian meal    =              60 RS")
        item.append("south indian meal")
        qua = int(input("Enter the quantity you want to order"))
        quantity.append(qua)
        bill = 60 * qua
        price.append(bill)
    elif(a==2):
        print("2.north indian meal        =             80 RS")
        item.append("north indian meal")
        qua = int(input("Enter the quantity you want to order"))
        quantity.append(qua)
        bill = 80 * qua
        price.append(bill)

def eve():
    print("1.Gobi manchurian")
    print("2.Cold coffee")
    print("3.Milk shake")
    a = int(input("Enter the food you want to order>> :  "))
    if(a==1):
        print("1.Gobi manchurian          =             70 RS")
        item.append("Gobi manchurian")
        qua = int(input("Enter the quantity you want to order"))
        quantity.append(qua)
        bill = 70 * qua
        price.append(bill)
    elif(a==2):
        print("2.Cold coffee             =             30 RS")
        item.append("Cold coffee")
        qua = int(input("Enter the quantity you want to order"))
        quantity.append(qua)
        bill = 30 * qua
        price.append(bill)
    elif(a==3):
        print("3.Milk shake            =             40 RS")
        item.append("Milk shake")
        qua = int(input("Enter the quantity you want to order"))
        quantity.append(qua)
        bill = 40 * qua
        price.append(bill)

print()
print("***********************************   WELCOME TO HOTEL SHIVA GANGA   ************************************")
print()
print("\t\t\t\t\t\t\t1.Morning Timings    :   [6:00AM to 12:00PM]")
print("\t\t\t\t\t\t\t2.Afternoon Timings  :   [12:00PM to 5:00PM]")
print("\t\t\t\t\t\t\t3.Evening Timings    :   [5:00PM to 10:00PM]")
print()
i = int(input("please choose the timings to check the foods available right now>> "))
if(i==1):
    mrg()
    print("1.Next order                         2.Bill")
    x = int(input())
    while(x==1):
        mrg()
        print("1.Next order                           2.Bill")
        x = int(input())
    for i in price:
        total = total + i
    final_bill()


if(i==2):
    after()
    print("1.Next order                         2.Bill")
    x = int(input())
    while(x==1):
        after()
        print("1.Next order                           2.Bill")
        x = int(input())
    for i in price:
        total = total + i
    final_bill()

if(i==3):
    eve()
    print("1.Next order                         2.Bill")
    x = int(input())
    while(x==1):
        eve()
        print("1.Next order                           2.Bill")
        x = int(input())
    for i in price:
        total = total + i
    final_bill()




