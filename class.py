import math
# class Complex(object):
#     def __init__(self, real, imaginary):
#         self.r = real
#         self.i= imaginary
#     def __add__(self, no):
#         return Complex(self.r+no.r, self.i+no.i)
        
#     def __sub__(self, no):
#         return Complex(self.r-no.r, self.i-no.i)
    
#     def __mul__(self, no):
#         re_mul = self.r*no.r - self.i*no.i
#         im_mul = self.r*no.i + self.i*no.r
#         return Complex(re_mul,im_mul)
    
#     def __truediv__(self, no):
#         denominator = no.r**2 + no.i**2
#         re_truediv = (self.r*no.r + self.i*no.i)/denominator
#         im_truediv = (self.i*no.r - self.r*no.i)/denominator
#         return Complex(re_truediv,im_truediv)
    
#     def mod(self):
#         return Complex(math.sqrt(self.r**2 + self.i**2), 0)
    
#     def __str__(self):
#         if self.i== 0:
#             result = "%.2f+0.00i" % (self.r)
#         elif self.r== 0:
#             if self.i >= 0:
#                 result = "0.00+%.2fi" % (self.i)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.i))
#         elif self.i > 0:
#             result = "%.2f+%.2fi" % (self.r, self.i)
#         else:
#             result = "%.2f-%.2fi" % (self.r, abs(self.i))
#         return result
# if __name__ == '__main__':
#     c = map(float, input().split())                #2 4
#     d = map(float, input().split())                #5 6
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))
#     #(7.00+10.00i -3.00-2.00i -14.00+32.00i 0.56+0.13i 4.47+0.00i 7.81+0.00i)
    
# # ----------------------------------------------------------------------------------------------------------------------------------

# class Points(object):
#     def __init__(self, x, y, z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def __sub__(self, no):
#         return __class__((self.x-no.x ),(self.y-no.y),(self.z-no.z))
#     def dot(self, no):
#         return  ((self.x*no.x )+(self.y*no.y)+(self.z*no.z))
#     def cross(self, no):
#         x=(self.y*no.z)-(self.z*no.y)
#         y=(self.x*no.z)-(self.z*no.x)
#         z = (self.x*no.y)-(self.y*no.x)
#         return __class__(x,y,z)
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

# if __name__ == '__main__':
#     points = list()
#     for i in range(4):
#         a = list(map(float, input().split()))
#         points.append(a)

#     a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3]) #0 4 5
#                                                                                                 #1 7 6
#                                                                                                 #0 5 9
#                                                                                                 #1 7 2
#     x = (b - a).cross(c - b)
#     y = (c - b).cross(d - c)
#     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

#     print("%.2f" % math.degrees(angle))     #8.19