class Ship:
    def __init__(self, name, length, displacement):
        self.name = name
        self.length = length
        self.displacement = displacement
    
    def get_info(self):
        return f"Ship Name: {self.name}, Length: {self.length} meters, Displacement: {self.displacement} tons"
    
class Fregata(Ship):
    def __init__(self, name, length, displacement, armament):
        super().__init__(name, length, displacement)
        self.armament = armament
    
    def get_info(self):
        return f"Fregata Name: {self.name}, Length: {self.length} meters, Displacement: {self.displacement} tons, Armament: {self.armament}"
    
    # Test the classes
fregata = Fregata("Frigate A", 130, 3000, "Missiles")
print(fregata.get_info())
