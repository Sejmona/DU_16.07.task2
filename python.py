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
    
class Torpedoborec(Ship):
    def __init__(self, name, length, displacement, speed):
        super().__init__(name, length, displacement)
        self.speed = speed
    
    def get_info(self):
        return f"Torpédoborec Name: {self.name}, Length: {self.length} meters, Displacement: {self.displacement} tons, Speed: {self.speed} knots"
class Kriznik(Ship):
    def __init__(self, name, length, displacement, armor):
        super().__init__(name, length, displacement)
        self.armor = armor
    
    def get_info(self):
        return f"Křižník Name: {self.name}, Length: {self.length} meters, Displacement: {self.displacement} tons, Armor: {self.armor} cm"

    
    # Test the classes
fregata = Fregata("Frigate A", 130, 3000, "Missiles")
torpedoborec = Torpedoborec("Destroyer B", 160, 5000, 30)
kriznik = Kriznik("Cruiser C", 200, 10000, 20)
print(fregata.get_info())
print(torpedoborec.get_info())
print(kriznik.get_info())
