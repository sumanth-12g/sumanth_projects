vehicle = []
days = []
price = []
total = 0
Gst_amount = 0
Total_amount = 0
def final_bill():
    print()
    print("------------------------  GAURISH RENTAL SHOP  -------------------------")
    print()
    print("Maruti mandir road, 2nd Cross, Vijaynagar, Bangalore-577409, KARNATAKA.")
    print()
    print("\tORDERED VEHICLE\t\t\tNUMBER OF DAYS\t\t\tPRICE_AMOUNT")
    print("\t____________________________________________________________\t")
    print()
    i = 0
    while(i<len(vehicle and days and price)):
        v = vehicle[i]
        d = days[i]
        p = price[i]
        print("\t",v,end="\t\t\t\t")
        print(d,end="\t\t\t\t\t\t")
        print(p)
        i = i + 1
    cal()
def cal():
    Gst_amount = total * (12 / 112)
    Total_amount = Gst_amount + total
    print()
    print("GST AMOUNT:\t\t\t\t\t\t\t\t\t\t ", Gst_amount)
    print("----------------------------------------------------------------------")
    print("TOTAL AMOUNT:\t\t\t\t\t\t\t\t\t ", Total_amount)
    print()
    print("\t\t\t\t<<<<<<<<<<\tTHANK YOU\t>>>>>>>>>>\t\t\t")
def two_wheeler():
    print()
    print("1.Bike")
    print("2.scooter")
    a = int(input("please enter your choice : "))
    if(a==1):
        print()
        print("1.Royal_enfield")
        print("2.KTM DUKE")
        print("3.PULSER NS")
        print("4.Yamaha MT")
        s = int(input("please choose the vehicle for rent : "))
        if(s==1):
            vehicle.append("Royal_enfield")
            print("1.Royal_enfield\t\t\t\tper day = 1000 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 1000 * d
            price.append(cost)
        if(s==2):
            vehicle.append("KTM DUKE")
            print("2.KTM DUKE\t\t\t\tper day = 2000 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 2000 * d
            price.append(cost)
        if(s==3):
            vehicle.append("PULSER NS")
            print("3.PULSER NS\t\t\t\tper day = 800 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 800 * d
            price.append(cost)
        if (s == 4):
            vehicle.append("YAMAHA MT")
            print("4.YAMAHA MT\t\t\t\tper day = 900 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 900 * d
            price.append(cost)
    if(a==2):
        print()
        print("1.Honda active")
        print("2.Jupiter")
        print("3.Honda dio")
        print("4.Ntorq")
        s = int(input("please choose the vehicle for rent : "))
        if(s==1):
            vehicle.append("Honda active")
            print("1.Honda active\t\t\t\tper day = 500 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 500 * d
            price.append(cost)
        if(s==2):
            vehicle.append("Jupiter")
            print("2.Jupiter\t\t\t\tper day = 450 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 450 * d
            price.append(cost)
        if(s==3):
            vehicle.append("Honda dio")
            print("3.Honda dio\t\t\t\tper day = 600 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 600 * d
            price.append(cost)
        if(s==4):
            vehicle.append("Ntoq")
            print("4.Ntorq\t\t\t\tper day = 650 RS")
            d = int(input("How many days would you like to : "))
            days.append(d)
            cost = 650 * d
            price.append(cost)
def four_wheeler():
    print()
    print("1.Maruti swift desire")
    print("2.Mahindra thar")
    print("3.Renault duster")
    print("4.Hyundai creta")
    s = int(input("please choose the vehicle for rent : "))
    if(s==1):
        vehicle.append("Maruti swift desire")
        print("1.Maruti swift desire\t\t\t\tper day = 3000 RS")
        d = int(input("How many days would you like to : "))
        days.append(d)
        cost = 3000 * d
        price.append(cost)
    if(s==2):
        vehicle.append("Mahindra thar")
        print("2.Mahindra thar\t\t\t\tper day = 4000 RS")
        d = int(input("How many days would you like to : "))
        days.append(d)
        cost = 4000 * d
        price.append(cost)
    if(s==3):
        vehicle.append("Renault duster")
        print("3.Renault duster\t\t\t\tper day = 3500 RS")
        d = int(input("How many days would you like to : "))
        days.append(d)
        cost = 3500 * d
        price.append(cost)
    if(s==4):
        vehicle.append("4.Hyundai creta")
        print("4.Hyundai creta\t\t\t\tper day = 4500 RS")
        d = int(input("How many days would you like to : "))
        days.append(d)
        cost = 4500 * d
        price.append(cost)

print()
print("---------------------------------------WELCOME TO GAURISH RENTAL SHOP-------------------------------------")
print()
print("\t\t\t\t\tMaruti mandir road, 2nd Cross, Vijaynagar, Bangalore-577409, KARNATAKA.")
print()
a = input("enter your name : ")
b = int(input("enter your phone number : "))
c = int(input("enter your age : "))
d = int(input("enter your adar number : "))
e = int(input("enter your driving license number : "))
print()
print("What type of vehicle you are looking for?")
print()
f = int(input("1.Two_wheeler\t\t\t\t\t2.Four_wheeler  "))
if(f==1):
    two_wheeler()
    for i in price:
        total = total + i
        print()
        print("have a safe ride with using helmet, please collect your bill")
    final_bill()
elif(f==2):
    four_wheeler()
    for i in price:
        total = total + i
        print()
        print("have a safe ride with using helmet, please collect your bill")
    final_bill()
