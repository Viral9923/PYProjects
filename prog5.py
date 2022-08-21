#Program to print the following from a list 
# i - print even numbers 
# ii - print all numbers divide by 5
# iii - print all numbers divide by 4 and 6


numbers = [    
    105,122,133,137,386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527 ];

print("All even numbers: ")
for x in numbers:
    
    if x%2==0:
        
        print(x , end= ' ');
        
print("All nos by 5:");   
for y in numbers:
   
    if y%5==0:
        
        print(y, end= ' ');
        
print("All duals : ")    
for z in numbers:
   
    if z%4==0 and z%6==0:
        
        print(z, end= ' ');
        