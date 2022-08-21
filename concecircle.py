import turtle as t;

NUM_CIRCLE = 40;
START_RAD = 15;
OFSET = 10;
ANIMAT_SPEED = 0;

t.speed(ANIMAT_SPEED);
t.hideturtle();

rad = START_RAD;

for i in range(NUM_CIRCLE):
    t.pencolor('red');
    t.circle(rad);
    
    x = t.xcor();
    y = t.ycor() - OFSET;
    
    rad = rad+OFSET;
    
    t.penup();
    t.goto(x,y);
    
    t.pendown();
    
    
        
t.showturtle();
t.done();