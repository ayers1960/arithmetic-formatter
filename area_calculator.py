class Rectangle:
  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

  def set_width(self, width):
    self.width = width;

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2*self.width + 2*self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)** 0.5

  def get_picture(self):
    pass

  def get_amount_inside(self):
    pass



class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side,side)

  def set_side(self,side):
    self.set_width(side)
    self.set_height(side)
