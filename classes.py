class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
           
    def moves(self):
        print("moves along..")
        
    def get_make_model(self):
        print(f"i am a {self.make} {self.model}")
        
    
my_car = Vehicle("tesla", "model3")

# print(my_car.make)
# print(my_car.model)

my_car.get_make_model()
my_car.moves()

you_car =Vehicle("cadiallac","esclade")
you_car.get_make_model()
you_car.moves()

class Airplain(Vehicle):
    def __init__(self, make, model):
        self.make =make
        self.model = model
    def moves(self):
        print("flies along")
        
class Truck(Vehicle):
    def moves(self):
        print("rumbles along..")

class golfcart(Vehicle):
    pass

cessna =Airplain("cessna","skyhawak")        
mack =Truck("mack","pinnacle")        
golfwagon =golfcart("yamaha","GC100")        

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()


