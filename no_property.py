class Jedi:
    def __init__(self, lightsaber_color="green"):
        self._lightsaber_color = lightsaber_color

    def get_lightsaber_color(self):
        return self._lightsaber_color

    def set_lightsaber_color(self, color):
        valid_colors = ["green", "blue", "purple", "red", "yellow"]
        if color.lower() in valid_colors:
            self._lightsaber_color = color.lower()
        else:
            print(f"Invalid Lightsaber Color (Defaulting to Green)")

    def delete_lightsaber_color(self):
        print("Deleting lightsaber color.")
        del self._lightsaber_color

# Example:
yoda = Jedi()
print(yoda.get_lightsaber_color())

yoda.set_lightsaber_color("blue")
print(yoda.get_lightsaber_color())

yoda.delete_lightsaber_color()

