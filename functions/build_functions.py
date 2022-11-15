
class Part:
    def __init__(self, part):
        self.part = part

    def Color(part, color):
        return color

    def BrickColor(part, color):
        return color

    def Transparency(part, num):
        if num > 1:
            return "[ERROR] You cannot exceede the number of 1."
        elif num < 0:
            return "[ERROR] You cannot specify the value lower than the number of 0."
        else:
            return num
        
    def Material(part, newmaterial):
        materials = [
            "Asphalt",
            "Basalt",
            "Brick",
            "Brass",
            "Cobblestone",
            "Concrete",
            "Corroded Metal",
            "Cracked Lava",
            "Diamond Plate",
            "Fabric",
            "Foil",
            "Forcefield",
            "Glacier",
            "Glass",
            "Granite",
            "Grass",
            "Ground",
            "Ice",
            "Leafy Grass",
            "Limestone",
            "Marble",
            "Metal",
            "Mud",
            "Neon",
            "Pavement",
            "Pebble",
            "Plastic",
            "Rock",
            "Salt",
            "Sand",
            "Sandstone",
            "Slate",
            "Smooth Plastic",
            "Snow",
            "Wood",
            "Wood Planks"
        ]
        if newmaterial in materials:
            return newmaterial
        else:
            return "[ERROR] Material passed is not correct. Check for typos."
    
    def Cancollide(part, statement:bool=None):
        if statement == None:
            return True
        else:
            return statement

    def CanQuery(part, statement:bool=None):
        if statement == None:
            return True
        else:
            return statement

    def CanTouch(part, statement:bool=None):
        if statement == None:
            return True
        else:
            return statement

    def CastShadow(part, statement:bool=None):
        if statement == None:
            return True
        else:
            return statement

    def Anchoured(part, statement:bool=None):
        if statement == None:
            return False
        else:
            return statement

    def Position(part, x, y, z):
        return x, y, z
