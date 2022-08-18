import turtle as t;

start_x = -200;
start_y = 0;
num_lines = 36;
angle = 170;
line_len = 400;

t.hideturtle();
t.penup();
t.goto(start_x,start_y);
t.pendown();
t.bgcolor('black');
color = ['orange','white','blue','green'];

for x in range(num_lines):
   t.pencolor(color[x%4]);
   t.forward(line_len);
   t.left(angle);