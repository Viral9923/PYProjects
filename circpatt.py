import turtle as t;

colors = ['red','green','orange','blue'];

for i in range(30):
    t.pencolor(colors[i%4]);
    t.circle(5*i);
    t.circle(-5*i);
    t.left(i);
    t.circle(10*i);
    t.circle(-10*i);
    t.right(i);
    
t.done();
    