import turtle as t;

t.setup(800,800);

t.penup();
t.goto(-400,250);
t.pendown();
t.bgcolor('white');

t.color('cyan');
t.begin_fill();
t.forward(600);
t.right(90);
t.forward(130);
t.right(90);
t.forward(600);
t.end_fill();

t.left(90);

t.color('yellow');
t.begin_fill();
t.forward(130);
t.left(90);
t.forward(600);
t.left(90);
t.forward(130);
t.end_fill();


t.left(180);
t.penup();
t.forward(130);
t.pendown()

t.color('cyan');
t.begin_fill();
t.forward(130);
t.right(90);
t.forward(600);
t.right(90);
t.forward(130);
t.end_fill();


t.penup()
t.goto(-400,-150);
t.pendown();

t.color('black');
t.begin_fill();
t.forward(400);
t.left(55);
t.back(390);
t.end_fill();

t.penup();
t.goto(-400,-400);
t.pendown();

t.color('black');
t.write("BAHAMAS",font=('Times New Roman',60));

t.showturtle();
t.done();
