#Table of numbers squares and cubes 

start = int(input("Enter a number: "));

end = int(input("Enter a num: "));

for i in range(start, end+1):
  square = i**2;
  cube = i**3;
  print(i, '\t', square, '\t', cube);