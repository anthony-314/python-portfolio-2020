#couldn't convert string to float with the word two

# Geometry Homework
#9/19

#Anthony Peraza
#options

def intro():
    print("""
    tri=1
    square=2
    circle=3
    pSquare=4
    cube=5
    quit = 6""")
# triangle function          
def triangle():
    print("Area of a triangle\n")
    base_tri = input("Base of triangle\n")
    height = input("Height of triangle\n")
    area = 0.5*float(base_tri)*float(height)
    tri_shape = str.format("""
                *
                **
                ***
                ****
                *****
     {0:5}      ******
                *******
                ********
                *********
                **********
                         {1}
    Area of this triangle is: {2}
    """, height, base_tri, area)

    print(tri_shape)
#Area of square
def aSquare():
    print("Area of square")
    print("Area in square feet")
    length = float(input("Length of square\n"))
    heightsq = float(input("Height of square\n"))
    area_of_square = length * heightsq
    square_shape = str.format("""
                 ______
                l      l
                l      l {0}
                l      l
                l______l
                       {1}
    Area of this square is: {2}
    """, heightsq, length, area_of_square)

    print(square_shape)
#cir of circle
def circle():
    radius = input("Radius of circle\n")
    circumferance = 2*3.14*float(radius)
    print(circumferance)
    print("cir. of circle--")
    circ_shape= str.format("""
             , - ~ ~ ~ - ,
         , '              ' ,
       ,                     ,
      ,                       ,
     ,                         ,
     ,          ---------------,{0}
     ,                         ,
      ,                       ,
       ,                     ,
         ,                  ,  
           ' - , _  _  _  ,'
    Circumference of this circle is: {1:.2f}""", radius, circumferance)

    print(circ_shape)
    
  #perimeter of square                      
def perimeter_square():
    print(" Perimeter of square\n")
    length = input("Length of square\n")
    heightsq = input("Height of square\n")
    perimeter_of_square = float(length)*2+float(heightsq)*2
    print(perimeter_of_square)
    square_shape = str.format("""
                 ______
                l      l
                l      l {0}
                l      l
                l______l
                       {1}
    Perimeter of this square is: {2}
    """, heightsq, length, perimeter_of_square)

    print(square_shape)


#volume of cube
def cube ():
    print("volume of cube --")
    side = input("side of cube")
    volume = float(side)*float(side)*float(side)
    volume_square = str.format ("""

               _______________________                         
             /                      /l
           /                      /  l
         /                      /    l
       /                      /      l
     /______________________/        l    
    l                      l         l
    l                      l         l
    l                      l         l    
    l                      l         l
    l                      l         l
    l                      l       /
    l                      l    /
    l                      l  /
    l______________________l/
                            {0}
    Volume of this cube is: {1}
    """, side, volume)

    print(volume_square)
    








def menu():
    while True:
        intro()
        ask=input("What do you want to find. tri,square,circle,pSquare,or cube ")
        if ask == "1":    
            triangle()
        elif ask == "2":
            aSquare()
        elif ask == "3":
            circle()
        elif ask == "4":
            perimeter_square()
        elif ask == "5":
            cube()
        elif ask =="6":
            quit()
        else:
            print("not valid")
            
            
            
        

menu()













