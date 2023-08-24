class Rectangle(object):

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width
    return width

  def set_height(self, height):
    self.height = height
    return height

  def get_area(self):
    self.area = self.width * self.height
    return self.area

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**0.5)

  def get_picture(self):
    if self.width < 50 and self.height < 50:
      shape = (self.width * "*" + "\n") * self.height
      return shape
    else:
      return "Too big for picture."

  def get_amount_inside(self, shape):
    if isinstance(
        shape, Rectangle
    ) and shape.width <= self.width and shape.height <= self.height:
      return (self.width // shape.width) * (self.height // shape.height)
    elif isinstance(
        shape,
        Square) and shape.width <= self.width and shape.height <= self.height:
      return (self.width // shape.width) * (self.height // shape.height)
    else:
      return 0


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    self.width = side
    self.height = side
    return side

  def set_width(self, width):
    return self.set_side(width)

  def set_height(self, height):
    return self.set_side(height)