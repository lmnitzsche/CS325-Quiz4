from dataclasses import dataclass

@dataclass
class Jedi:
    name: str
    skill: float
    age: int

    def output_age_and_skill(self):
        print(f"{self.name} is {self.age} years old and has a skill level of {self.skill} out of 10.")

# Example:
luke = Jedi(name="Luke Skywalker", skill=9.0, age=22)
luke.output_age_and_skill()
yoda = luke = Jedi(name="Yoda", skill=9.5, age=899)
yoda.output_age_and_skill
