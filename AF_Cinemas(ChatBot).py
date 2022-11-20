 #AF Cinemas-ChatBot
import datetime,random,sys,time
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
#Function That will returns actual time
def now():
    now=datetime.datetime.now()
    Now='%H:%M %p'
    return now.strftime(Now)
#Function Of Ticket Issues
def select(choice,movie):
    #problem=0
    match(choice):
            #case '1':problem=print("--------------------------------------------------".rjust(185)),print("Ticket Issues".rjust(209)),print(hr.rjust(185)),Ticket_issues()
        case '1':Ticket_issues(movie)
        #case '2':problem=print("--------------------------------------------------".rjust(185)),print("Payment Issues".rjust(204)),Payment_issues()
        case '2':Payment_issues(movie)
        #case '3':problem=print("--------------------------------------------------".rjust(185)),print("Others".rjust(215)),Others()
        case '3':Others()
        case _:return 1
def Ticket_issues(movie):
    print("Ticket Issues".rjust(209),"\n",now().rjust(142))
    print("--------------------------------------------------".rjust(185))
    time.sleep(3)
    print("1. Unable to Book Ticket\n\
2. Cancellation\n\
3. Change Seats\n\
4. Can't find My Tickets in Order History")
    choice=input(">")
    print("\t\t           ",now(),"\n\
--------------------------------------------------")
    ubt=('tech_issue','unable','noshows','no open','will open')
    cancel=('booked','not booked','code red')
    mdfy=('booked','not booked','code red','HouseFull')
    time.sleep(1)
    if(choice=='1'):
        print("Unable to Book Ticket".rjust(200),"\n",now().rjust(142))
        print("--------------------------------------------------".rjust(185))
        verd=random.choice(ubt)
        time.sleep(2)
        if(verd=='tech_issue'):
             print("There is a small Technical Issue...\nThe issue will be resolved soon...")
        elif(verd=='unable'):
            ch=input("1. KGF Chapter -2\n2. Vikram\n3. Kantara\n4. Karthikeya -2\n\
Please tell us the movie name that you want to book tickets for -")
            print(f"Select your seats\n\
Your Tickets for {movie[int(ch)]} are booked")
        elif(verd=='noshows'):
            print(f'No shows for today')
        elif(verd=='no open'):
            print(f'Bookings Not Yet Started')
        elif(verd=='will open'):
             print(f'Advance Bookings Soon')   
    elif(choice=='2'):
        print("Cancellation".rjust(209),"\n",now().rjust(142))
        print("--------------------------------------------------".rjust(185))
        verd=random.choice(cancel)
        time.sleep(2)
        if(verd=='booked'):
            print(f'Your Tickets for the {movie} \nare been cancelled')
        elif(verd=="not booked"):
            print("Sorry to say this...! your tickets are \nnot yet booked to cancel.")
        elif(verd=='code red'):
            print("Oops...! The time is out for Cancellation")
    elif(choice=='3'):
        print("Change Seats".rjust(209),"\n",now().rjust(142))
        print("--------------------------------------------------".rjust(185))
        verd=random.choice(mdfy)
        time.sleep(2)
        if(verd=="booked"):
            print('Select your seats and we will deduct\nthe previous ticket price from \ncurrent ticket price...')
            print(f'Your Tickets for the {movie} \nare Modified')
        elif(verd=="not booked"):
             print("Sorry to say this...! your tickets are \nnot yet booked to cancel.")
        elif(verd=='code red'):
            print("Oops...! The time is out for Changing Seats")
        elif(verd=='HouseFull'):
            print("We Can't Provide the service of changing Seats\nTickets are been sold for this show...")
    else:
        print("Sorry...Invalid Input")
    print("\t\t           ",now(),"\n\
--------------------------------------------------")
#Function Of Payment Issues    
def Payment_issues(movie):
    def refund(movie):
        print("Refund of Cancelled Booking".rjust(192),"\n",now().rjust(142))
        print("--------------------------------------------------".rjust(185))
        ref=['processed','will']
        verd=random.choice(ref)
        time.sleep(3)
        if(verd=='processed'):
             print("You had recently cancelled the tickets for\nthe movie{movie}. \
immediately, \nwe processed the refund from our end,\n\
it will reflect into your account within the \nnext 2 to 4 days.")
        if(verd=='will'):
             print("we process the refund from our end,\nit will reflect into your account within the \nnext 2 to 4 days")
    def amt_chrg():
        print("Amount has Charged, but i haven't \n".rjust(185),"\
      received any SMS/Email".rjust(171),"\n",now().rjust(142))
        print("--------------------------------------------------".rjust(185))
        time.sleep(3)
        amt='cutted'
        if(amt=='cutted'):
            print("You have nothing to worry about it")
            inp=int(input("Please Enter Your Transaction ID -"))
            lst=['success','failure']
            verd=random.choice(lst)
            print("\t\t           ",now(),"\n\
--------------------------------------------------")
            print("Your payment was succesfull but\n\
for some issues it didn't reflected to\n\
your profile. we will send you the tickets\n to you via SMS/Email") if(verd=='success') else print("Your Payment was \
unsuccessfull.")
    def pay_not_going():
        print("Payment is not going".rjust(203),"\n",now().rjust(142))
        print("--------------------------------------------------".rjust(185))
        time.sleep(3)
        print("AF Cinemas strongly recommend you to \n\
cross-check the details you had entered and \n\
hope you enter OTP in time.")
        print("\t\t           ",now(),"\n\
--------------------------------------------------")
        time.sleep(2)
        print("Even though it didn't work, we suggest\n\
you to try another option or may contact\n\
your personal bank.")
    print("Payment Issues".rjust(203),"\n",now().rjust(142))
    print("--------------------------------------------------".rjust(185))
    time.sleep(3)
    print("1. Refund of Cancelled Booking\n\
2. Amount has Charged, but i haven't \n\
      received any SMS/Email\n\
3. Payment is not going")
    ch=input(">")
    print("\t\t           ",now(),"\n\
--------------------------------------------------")
    #tup=('Refund of Cancelled Booking'," Amount has Charged, but i haven't received any SMS/Email",
        # "Payment is not going")
    time.sleep(1)
    match(ch):
        case '1':refund(movie)
        case '2':amt_chrg()
        case '3':pay_not_going()
        case '_':print("Sorry... INVALID INPUT")
    print("\t\t           ",now(),"\n\
--------------------------------------------------")
#Others
def Others():
    print("Others".rjust(215),"\n",now().rjust(142))
    print("--------------------------------------------------".rjust(185))
    time.sleep(2)
    print("Drop a message about your problem, i will \nhelp you. if i don't have a answer i will \nconnect you to a \
support  assistant (via call)")
    print("\t\t           ",now(),"\n\
--------------------------------------------------")
    text=input(">")
    print(text.rjust(203),"\n",now().rjust(142))
    print("--------------------------------------------------".rjust(185))
    print("Wait a sec...you will get a call from \nour company's support assistant...so \nYour Problem Will be Solved.")
    print("\t\t           ",now(),"\n\
--------------------------------------------------")
#Main Function
problem=0
movies=('KGF Chapter -2','Vikram','Kantara','Karthikeya-2')
movie=random.choice(movies)
tech_ast=['Samu','Rooni','LP','Heer']    
delay_print(" \t\t\t       }- AF CINEMAS -{\n")
delay_print("\n\t\t     ---------- Technical Support Team ----------\n\n\n\n")
time.sleep(1)
wrk_ast=random.choice(tech_ast)
print(f'Hi, this is {wrk_ast}... I am here to help you!\n\
\t\t            ',now())
print("--------------------------------------------------")
n=0
time.sleep(3)
print("May i know What is your problem?")
time.sleep(0.25)
lst=['1. Ticket Issues','2. Payment Issues','3. Others']
print("1. Ticket Issues\n\
2. Payment Issues\n\
3. Others")
choice=input("I want to Know Your Problem please -")
print("\t\t           ",now(),"\n\
--------------------------------------------------")
    #problem="p"
while(1):
    if(n>0):
        print(f'Hi, this is {wrk_ast} again...!\n\
\t\t            ',now())
    problem=select(choice,movie)
    time.sleep(2)
    if(problem==1):
        print("Sorry...INVALID INPUT")
        break
    else:
        #while(1):
        ch=input("Do you need any help from me?\nYes\nNo, i am ok...>")[:2]
        print("\t\t           ",now(),"\n\
--------------------------------------------------")
        time.sleep(1)
        if(ch=='No' or ch=='NO' or ch=='no' or ch=='N' or ch=='n' or ch=='2' ):
            #n=1
            #print("Sorry...! I didn't get you can you tell me once again?")
            #break
            print("No, i am ok...".rjust(209),"\n",now().rjust(142))
            print("--------------------------------------------------".rjust(185))
            break
        elif(ch=='yes'or ch=='Yes' or ch=='1' or ch=='YES' or ch=='Y' or ch=='y'):
            print("Yes".rjust(209),"\n",now().rjust(142))
            print("--------------------------------------------------".rjust(185))
        else:
            print("Sorry...! I didn't get you can you tell me once again?")
            n=1
            '''print("No, i am ok...".rjust(209),"\n",now().rjust(142))
            print("--------------------------------------------------".rjust(185))
            break'''
        for i in lst:
            if(lst.index(i)==int(choice)-1):
                continue
            print(i)
        choice=input(">")
        print("\t\t           ",now(),"\n\
--------------------------------------------------")
time.sleep(0.50)
print(f"Signing Off {wrk_ast}\nTechinal Support Team\nAF Cinemas")
print("\t\t           ",now(),"\n\
--------------------------------------------------")
              


      
