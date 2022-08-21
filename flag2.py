import turtle as t;

t.setup(800,500);

t.penup();
t.goto(-400,250);
t.pendown();
t.bgcolor('black');

t.color('orange');
t.begin_fill();
t.forward(600);
t.right(90);
t.forward(167);
t.right(90);
t.forward(600);
t.end_fill();

t.left(90);

t.color('white');
t.begin_fill();
t.forward(167);
t.left(90);
t.forward(600);
t.left(90);
t.forward(167);
t.end_fill();


t.left(180);
t.penup();
t.forward(167);
t.pendown()

t.color('green');
t.begin_fill();
t.forward(167);
t.right(90);
t.forward(600);
t.right(90);
t.forward(167);
t.end_fill();


t.penup();
t.goto(-30,0); #centering in the screen
t.pendown();
t.pensize(10);
t.pencolor("blue");
t.circle(80,None,100);



t.showturtle();
t.done();