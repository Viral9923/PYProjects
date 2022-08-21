import turtle as t;

start_x = -100;
start_y = 0;

t.hideturtle();
t.penup();
t.goto(start_x,start_y);
t.pendown();
t.bgcolor('black');

color = ['red','green','yellow','cyan','purple'];

for x in range(36):
    t.pencolor(color[x%5]);
    t.forward(100);
    t.right(45);
    x = t.xcor();
    y = t.ycor()-10;
    
    
t.done();