import sympy
from sympy import *
sympy.init_printing()
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))

theta1 = sympy.Symbol('theta1')
alpha1 = sympy.Symbol('alpha1')
d1 = sympy.Symbol('d1')
a1 = sympy.Symbol('a1')

theta2 = sympy.Symbol('theta2')
alpha2 = sympy.Symbol('alpha2')
d2 = sympy.Symbol('d2')
a2 = sympy.Symbol('a2')

theta3 = sympy.Symbol('theta3')
alpha3 = sympy.Symbol('alpha3')
d3 = sympy.Symbol('d3')
a3 = sympy.Symbol('a3')

theta4 = sympy.Symbol('theta4')
alpha4 = sympy.Symbol('alpha4')
d4 = sympy.Symbol('d4')
a4 = sympy.Symbol('a4')

theta5 = sympy.Symbol('theta5')
alpha5 = sympy.Symbol('alpha5')
d5 = sympy.Symbol('d5')
a5 = sympy.Symbol('a5')

theta6 = sympy.Symbol('theta6')
alpha6 = sympy.Symbol('alpha6')
d6 = sympy.Symbol('d6')
a6 = sympy.Symbol('a6')


theta7 = sympy.Symbol('theta7')
alpha7 = sympy.Symbol('alpha7')
d7 = sympy.Symbol('d7')
a7 = sympy.Symbol('a7')

m0_1 = Matrix([[cos(theta1), -sin(theta1)*cos(alpha1), sin(theta1)*sin(alpha1), a1*cos(theta1)], \
               [sin(theta1), cos(theta1)*cos(alpha1), -cos(theta1)*sin(alpha1), a1*sin(theta1)], \
               [0, sin(alpha1), cos(alpha1), d1], [0, 0, 0, 1]])
m1_2 = Matrix([[cos(theta2), -sin(theta2)*cos(alpha2), sin(theta2)*sin(alpha2), a2*cos(theta2)], \
               [sin(theta2), cos(theta2)*cos(alpha2), -cos(theta2)*sin(alpha2), a2*sin(theta2)], \
               [0, sin(alpha2), cos(alpha2), d2], [0, 0, 0, 1]])
m2_3 = Matrix([[cos(theta3), -sin(theta3)*cos(alpha3), sin(theta3)*sin(alpha3), a3*cos(theta3)], \
               [sin(theta3), cos(theta3)*cos(alpha3), -cos(theta3)*sin(alpha3), a3*sin(theta3)], \
               [0, sin(alpha3), cos(alpha3), d3], [0, 0, 0, 1]])
m3_4 = Matrix([[cos(theta4), -sin(theta4)*cos(alpha4), sin(theta4)*sin(alpha4), a4*cos(theta4)], \
               [sin(theta4), cos(theta4)*cos(alpha4), -cos(theta4)*sin(alpha4), a4*sin(theta4)], \
               [0, sin(alpha4), cos(alpha4), d4], [0, 0, 0, 1]])
m4_5 = Matrix([[cos(theta5), -sin(theta5)*cos(alpha5), sin(theta5)*sin(alpha5), a5*cos(theta5)], \
               [sin(theta5), cos(theta5)*cos(alpha5), -cos(theta5)*sin(alpha5), a5*sin(theta5)], \
               [0, sin(alpha5), cos(alpha5), d5], [0, 0, 0, 1]])
m5_6 = Matrix([[cos(theta6), -sin(theta6)*cos(alpha6), sin(theta6)*sin(alpha6), a6*cos(theta6)], \
               [sin(theta6), cos(theta6)*cos(alpha6), -cos(theta6)*sin(alpha6), a6*sin(theta6)], \
               [0, sin(alpha6), cos(alpha6), d6], [0, 0, 0, 1]])
m6_7 = Matrix([[cos(theta7), -sin(theta7)*cos(alpha7), sin(theta7)*sin(alpha7), a7*cos(theta7)], \
               [sin(theta7), cos(theta7)*cos(alpha7), -cos(theta7)*sin(alpha7), a7*sin(theta7)], \
               [0, sin(alpha7), cos(alpha7), d7], [0, 0, 0, 1]])

general_solution = m0_1*m1_2*m2_3*m3_4*m4_5*m5_6*m6_7

home_position = m0_1.subs({d1:165, a1: 0, theta1: 0, alpha1: 0}) *\
m1_2.subs({d2:125, a2: 0, theta2: 0, alpha2: -pi/2}) *\
m2_3.subs({d3:0, a3: 270, theta3: -pi/2, alpha3: 0}) *\
m3_4.subs({d4: 0, a4: 70, theta4: 0, alpha4: -pi/2}) *\
m4_5.subs({d5:302, a5: 0, theta5: 0, alpha5: pi/2}) *\
m5_6.subs({d6:0, a6: 0, theta6: 0, alpha6:-pi/2}) *\
m6_7.subs({d7:72, a7: 0, theta7: 0, alpha7:0})

display(home_position)