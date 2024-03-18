print("Welcome to SBI calculator Please insert your card <<<<<<<<<<<")
print()
print("enter value 1 for card initializastion++:")
i=int(input())
amount = 50000
pin = 9999
if(i==1):
    print("Enter the two digits value within 1 to 100 to continue...")
else:
    print("please enter the value 1 after card insertion, Try again____")
    exit()
n=int(input())
if(n>=10 and n<100):
    print("enter your security pin for further processing")
else:
    print("check the digit's what you enterd? Try again...")
    exit()
pin=int(input())
if(pin==9999):
    print()
    print("Please choose any option below displayed on the screen for further processing:")
    print()
    print("1.Withdrwa","2.Change your security pin")
    print("3.Deposit","4.Balance Enquiery")
else:
    print("Sorry wrong pin! pin must contains 4 digits please try again")
    exit()
a=int(input())
if((a==1) or (a==2) or (a==3) or (a==4)):
    print()
else:
    print("Sorrry! please select correct option")
    exit()
if(a==1):
    print("1.savings accuont")
    print("2.current account")
    print("3.debit card")
if(a==2):
    print("Change your security pin [PLESE ENTER YOUR ACCOUNT NUMBER]")
    a=int(input())
    if(a>100000000000 and a<=999999999999):
        print("please enter your mobile number registerd with your account")
        a=int(input())
        if(a>1000000000 and a<=9999999999):
            print("OTP has sent to your mobile number please enter here for next process")
        else:
            print("please enter proper number")
            exit()
        otp=int(input())
        if(otp>=1000 and otp<=9999):
            print("Plese set your new security pin:")
        else:
            print("wrong otp your entered please try again")
            exit()
        s=int(input())
        if(s>=1000 and s<=9999):
            print("your security pin has been changed")
            exit()
        else:
            print("pin must contains 4 digits value,,,")
            exit()

    else:
        print("check your account number")
        exit()
b=int(input())
if(b==1):
    print("cash amount you wish to withdraw")
    print("$")
    c=int(input())
if(int(c)>=100 and int(c)<=50000):
    print("your transaction is being processed! please wait and collect the cash")
    print("select below option to check balance & exit:")
    print()
    print("1.Balance Enquiery")
    print("2.Exit")
else:
    print("sorry! insufficient balance")
a=int(input())
if(a==1):
    print("1.Balance Enquiery")
    print()
    rem = amount - c
    print("Your balance is $", rem)
a=int(input())
if(a==2):
     print("please remove your card")
     print("Thank you for being a valuable customer, Visit again")
     exit()
