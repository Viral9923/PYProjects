import turtle as t;

t.setup(800,500);

t.penup();
t.goto(-400,250);
t.pendown();
t.bgcolor('black');


t.color('red');
t.begin_fill();
t.right(90);
t.forward(600);
t.left(90);
t.forward(167);
t.right(90);
t.back(600);
t.end_fill();

t.left(90);

t.color('white');
t.begin_fill();
t.right(90);
t.forward(600);
t.left(90);
t.forward(400);
t.right(90);
t.back(600);
t.end_fill();

t.left(90);

t.color('red');
t.begin_fill();
t.right(90);
t.forward(600);
t.left(90);
t.forward(167);
t.right(90);
t.back(600);
t.end_fill();

t.done();