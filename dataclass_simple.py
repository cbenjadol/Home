from dataclasses import dataclass, field

from enum import Enum

class Sex(Enum):
    male = 'MALE'
    female = 'FEMALE'

@dataclass(slots=True)
class Person:
    firstname: str = field(compare=False)
    lastname: str
    # For mutable fields, 
    emails: list[str] = field(compare=False, default_factory=list)

    _name: str = field(init=False, compare=False, repr=False)
    
    def __post_init__(self) -> None:
        self._name = f"{self.firstname} {self.lastname}"

    @property
    def name(self):
        return self.name

def main():
    p1 = Person("Chakravut", "Benjadol", ["benjadol@gmail.com"])
    p2 = Person("Benjamin", "Benjadol", ["bbenjadol@gmail.com"])

    print(f"Testing {p1}")
    print(f"Testing {p2}")
    print(p1 == p2)
    # print(p1.__dict__["_name"])
    print(Sex.male.value)

if __name__ == "__main__":
    main()