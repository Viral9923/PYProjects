# Flag of country MICRONESIA

import turtle as t;

t.setup(800,800);

t.penup();
t.goto(-200,200);
t.pendown();
t.bgcolor('black');


t.color('cyan');
t.begin_fill();
t.right(90);
t.forward(300);
t.left(90);
t.forward(500);
t.right(90);
t.back(300);
t.end_fill();

t.penup()
t.goto(50,120);
t.pendown();

t.color('white');
t.hideturtle();
t.begin_fill();
for i in range(5):
    t.forward(30);
    t.right(144);
t.end_fill();

t.penup()
t.goto(50,10);
t.pendown();

t.color('white');
t.hideturtle();
t.begin_fill();
for i in range(5):
    t.forward(30);
    t.right(144);
t.end_fill();

t.penup()
t.goto(-20,60);
t.pendown();

t.color('white');
t.hideturtle();
t.begin_fill();
for i in range(5):
    t.forward(30);
    t.right(144);
t.end_fill();

t.penup()
t.goto(120,60);
t.pendown();

t.color('white');
t.hideturtle();
t.begin_fill();
for i in range(5):
    t.forward(30);
    t.right(144);
t.end_fill();

t.penup();
t.goto(-200,200);
t.pendown();
t.color('red');
t.write("MICRONESIA", font=('Times New Roman', 60));


t.done();