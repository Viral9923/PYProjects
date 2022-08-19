import turtle as t;

t.hideturtle();

t.bgcolor('black');

for x in range(8):
  t.color('red');
  t.begin_fill();
  t.forward(100);
  t.right(45);
  t.end_fill();
  
t.penup();  
t.goto(5,-130);
t.pendown();  
t.write('STOP',font=('Times New Roman',32));
  
  
t.done();
  