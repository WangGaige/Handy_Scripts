####################################################
class Car:
    def __init__(self):
        self.engine_started = False

    def is_engine_started(self):
        return self.engine_started

    def start_engine(self):
        self.engine_started = True

my_car = Car()
my_car.engine_started      #=> False  - Calling the attribute
my_car.is_engine_started() #=> False  - Calling the method therefore using ()
my_car.start_engine()      #=> Calling the method, therefore using ()
my_car.engine_started      #=> True   - Calling the attribute

####################################################
class Castle:
  def __init__(self, name, ruler):
    self.name = name
    self.ruler = ruler

  def castle_details(self):
    return f"{self.name} is ruled by {self.ruler_name()}"

  def ruler_name(self):
    return self.ruler.capitalize()

dragonstone = Castle("Dragonstone", "targaryen")
dragonstone.castle_details() # => "Dragonstone is ruled by Targaryen"

####################################################
class Building:
  def __init__(self, name, width, length):
    self.name = name
    self.width = width
    self.length = length

  def floor_area(self):
    return self.width * self.length
  
class Castle(Building):
    def __init__(self, name, width, length):
        super().__init__(name, width, length)
        self.butler = None

    def has_a_butler(self):
        return self.butler is not None

####################################################      
class Castle(Building):
  # A castle always has a garden of 300 sq. m
  def floor_area(self):
    return super().floor_area() + 300  # `super` calls `floor_area` of `Building`
  
  
  

####################################################
class Castle(Building):

  @classmethod
  def categories(self):
    return ['Medieval', 'Norman', 'Ancient']
  
class House:
  @classmethod
  def price_per_square_meter(self, city):
      if city is "Paris":
          return 9000
      elif city is "Brussels":
          return 3000
      else:
        return f"No data for {city}"

print(House.price_per_square_meter("Paris")) # => 9000
  
