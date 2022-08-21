#Lottery game 
import random;


again='y';

while again=='y':
  a = int(input("Enter a number: "));

  b = random.randint(1,20);
  if(a==b):
      print("Yay..You won..");
  else:
      print("Try Again");
      
      again = input("Do you want to continue?(y/n)");

 