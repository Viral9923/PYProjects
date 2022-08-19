# Progrm to demonstrate Stadium Seating

seat_A = 20;
seat_B = 15;
seat_C = 10;

tic_a = int(input("How many seats of A were sold?"));
tic_b = int(input("How many seats of B were sold?"));
tic_c = int(input("How many seats of C were sold?"));

sal_a = tic_a*seat_A;
sal_b = tic_b*seat_B;
sal_c = tic_c*seat_C;

tot_sal = sal_a + sal_b + sal_c;

print("The total sales of tickets is: ", tot_sal);