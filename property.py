class Jedi:
    def __init__(self, lightsaber_color="green"):
        self._lightsaber_color = lightsaber_color

    @property
    def lightsaber_color(self):
        return self._lightsaber_color
    
    @lightsaber_color.setter
    def lightsaber_color(self, color):
        valid_colors = ["green", "blue", "purple", "red", "yellow"]
        if color.lower() in valid_colors:
            self._lightsaber_color = color.lower()
        else:
            print(f"Invalid Lightsaber Color (Defaulting to Green)")

    @lightsaber_color.deleter
    def lightsaber_color(self):
        print("Deleting lightsaber color.")
        del self._lightsaber_color

# Example
luke = Jedi()
print(luke.get_lightsaber_color())

luke.set_lightsaber_color("blue")
print(luke.get_lightsaber_color())

luke.delete_lightsaber_color()