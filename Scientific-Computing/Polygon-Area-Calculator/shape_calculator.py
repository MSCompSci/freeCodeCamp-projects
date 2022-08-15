class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

  def set_width(self,newWidth):
    self.width = newWidth
  
  def set_height(self,newHeight):
    self.height = newHeight

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2*self.width + 2*self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width**2 + self.height**2)**0.5
    return diagonal

  def get_picture(self):
    picture = ""
    if ((self.height>50) or (self.width>50)):
      return "Too big for picture."
    for x in range(self.height):
      picture += "*"*self.width + "\n"
    return picture
  
  def get_amount_inside(self,shape):
    amount = self.get_area()//shape.get_area()
    return amount

class Square(Rectangle):
  def __init__(self,side):
    Rectangle.width = side
    Rectangle.height = side
    self.side = side

  def __str__(self):
    return "Square(side="+str(self.side)+")"

  def set_side(self,side):
    Rectangle.width = side
    Rectangle.height = side
    self.side = side
    return side

  def set_height(self,height):
    Rectangle.height = height
    self.side = height

  def set_width(self,width):
    Rectangle.width = width
    self.side = width



