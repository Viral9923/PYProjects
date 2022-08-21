#This program is to show the gender of 
# baby in mothers womb 

sperm = int(input("Enter sperm count: "));

if(sperm>=60):
    print("Congrats...Pregnant.");
    
    print("Determine gender of baby.");
    color= input("Pick a color from bucket:");
    
    if(color=='blue'):
        print("Yay..its a BOY");
    elif(color=='pink'):
        print("wow..its a GIRL");

else:
    print("SORRY... Not Pregnant..");
    

