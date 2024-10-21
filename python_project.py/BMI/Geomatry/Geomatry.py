area_square=lambda s:s**2
p_square=lambda s:4*s

a_triangle=lambda b,h:b*h/2
p_triangle=lambda a,b,c:a+b+c

p_rectangle=lambda l,w: 2*(l+w)
a_rectangle=lambda l,w:l*w

c_circle=lambda r:2*3.14*r
a_circle=lambda r:r*r*3.14

a_circular_ring =lambda R,r:(R*R-r*r)*3.14

p_parallelogram=lambda a,b:2*(a+b)
a_parallelogram=lambda b,h:b*h

p_trapezoid=lambda a,b1,b2,c:a+b1+b2+c
a_trapezoid=lambda b1,b2,h:h*(b1+b2)/2


