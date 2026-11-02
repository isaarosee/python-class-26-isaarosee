# Starting file for PROJECT 1
# Include your course number, student first and last name, and date in the comment header
# CS 31 Isabella Garcia 11/01/26
print("Hello! Welcome to Virtual Cats Now, or VCN, where you can own as many cats as you desire on the web!")
print()
start_overview = input("Would you like to learn more about VCN and all we have to offer? Y/N ")
print()
if start_overview.upper() == "Y":
    print("Puurfect! Allow me to walk you through the infinite wonders of VCN.") #I created this command and the no version at the same time for format, just making sure my code functions properly
    print()
    print("Virtual Cats Now is not just taking care of cats on a webspace, it's the possiblities for growth like never before.")
    print()
    print("Hate how expensive it can be to raise a cat? VCN has a no-cost care plan just for you! Now you can get your kitties all of the treats and toys they desire.")
    print("Not to mention the endless catibbilities! Swim, surf, hike, and bike all with your cats. See how much your cats enjoy those acitvities, they may be picky!")
    print()
    print("Each cat has their own personality and style, just like your cats in home!")
    print() #all of my print code is separated so it looks nicer for output!
    start_vcn = input("Now, are you ready to unleash a new world with VCN? Y/N ") #need in order to start command
    print() #creating for spacing, making sure user interface is friendly
    price = 14.99 #one subscription price but months will become a factor instead
    if start_vcn.upper() == "Y": #checked my notes to see the upper/lower case sensitivity
        print("Cattastic! Let's get started ↓")
        print()
        #variables
        player_name = input("What is your first and last name? ")
        print()
        player_info = input("What is your phone number and email address? ") #getting their input as variables to use for the reciept
        print()
        #how much service costs
        print("VCN is a monthly subscrption! Today and forever it is $14.99 for Virutal Cats Now.")
    
        #amount of items wanted
        items_wanted =int(input("How many months of VCN would you like to buy today? ")) #using int because they must input a number
        
        
        subtotal = (items_wanted * price)
        quantity_price = (items_wanted * price * 1.1) #the 1.1 is used for the 10% tax, of course items wanted and price have been set variables so i could set an equation up
        print()
        print("-YOUR RECEIPT ₍^. .^₎⟆-")
        print(player_name)
        print(player_info)
        print()
        print("TOTAL MONTHS OF VCN:", items_wanted)
        print("PRICE OF VCN: $",price)
        print("TOTAL BEFORE TAX: $",subtotal)
        (print)
        print("10% kitty tax")
        print("TOTAL:") 
        print()
        print("$",quantity_price)
        print("≽^•⩊•^≼")
        print() #wanted to make the receipt cute cat themed!
        print("Thank you so much for purchasing Virtual Cats Now! We look forward to your many months of biscuits and purrs, enjoy!")


    elif start_vcn.upper() == "N":
        print("Join us next time, anything is pawsible!")
    

elif start_overview.upper() == "N":
    print("Need to take a cat nap? No worries, see you later!")
else:
    print("Sorry, invalid input. Type Y or N!") #placed just in case users type yes or no
    #im not sure how to describe/be more clear in code description for comments. is there something specific you're looking for? thank you!