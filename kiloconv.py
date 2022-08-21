#Ch 5 Program 1 Kilometer Convertor

def main():
    kilo = float(input("Enter distance in kilometers: "));
    kiloconv(kilo);
    
    
def kiloconv(kilo):
    miles = kilo * 0.6214;
    print("the distance is :", miles);
    
main();