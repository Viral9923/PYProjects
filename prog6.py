#advanced time converter

again = 'y';
 
while again=='y':
    
    time = int(input("Enter number of seconds: "));
    hours = time // 3600;
    minutes = (time // 60) % 60;
    seconds = time % 60;
    
    print("The time is: ", hours, minutes, seconds, sep=':');
    again = input("Do you want to do again?(Y/N)");