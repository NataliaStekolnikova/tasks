'''
Задание 3.
Классы. Наследование, волшебные методы.
'''


# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.

class LengthUnits:
    BASE_UNIT = "м"

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def to_base_units(self):
        return self.value * self.FACTOR

    def from_base_units(self, value):
        return self.__class__(value / self.FACTOR)

    def perform_operation(self, other, operator):
        if isinstance(other, LengthUnits):
            other_value = other.to_base_units()
        elif isinstance(other, (int, float)):
            other_value = other
        else:
            raise TypeError("Unsupported operand type.")

        if operator == "*":
            result = self.to_base_units() * other_value
        elif operator == "/":
            result = self.to_base_units() / other_value
        elif operator == "+":
            result = self.to_base_units() + other_value
        elif operator == "-":
            result = self.to_base_units() - other_value
        else:
            raise ValueError("Unsupported operator.")

        return self.from_base_units(result)

    def __str__(self):
        return f"{self.value} {self.UNIT}"

    def __eq__(self, other):
        if isinstance(other, LengthUnits):
            return self.to_base_units() == other.to_base_units()
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, LengthUnits):
            return self.to_base_units() < other.to_base_units()
        else:
            raise TypeError("Unsupported operand type.")

    def __add__(self, other):
        return self.perform_operation(other, "+")

    def __iadd__(self, other):
        return self.perform_operation(other, "+")

    def __sub__(self, other):
        return self.perform_operation(other, "-")

    def __isub__(self, other):
        return self.perform_operation(other, "-")

    def __mul__(self, other):
        return self.perform_operation(other, "*")

    def __imul__(self, other):
        return self.perform_operation(other, "*")

    def __truediv__(self, other):
        return self.perform_operation(other, "/")

    def __itruediv__(self, other):
        return self.perform_operation(other, "/")

class Millimeters(LengthUnits):
    UNIT = "мм"
    FACTOR = 1 / 1000

class Centimeters(LengthUnits):
    UNIT = "см"
    FACTOR = 1 / 100

class Meters(LengthUnits):
    UNIT = "м"
    FACTOR = 1

class Kilometers(LengthUnits):
    UNIT = "км"
    FACTOR = 1000

class Inches(LengthUnits):
    UNIT = "дюйм"
    FACTOR = 0.0254

class Feets(LengthUnits):
    UNIT = "фут"
    FACTOR = 0.3048

class Yards(LengthUnits):
    UNIT = "ярд"
    FACTOR = 0.9144

class Miles(LengthUnits):
    UNIT = "миля"
    FACTOR = 1609.34

class Fen(LengthUnits):
    UNIT = "фэнь"
    FACTOR = 0.00333

class Chi(LengthUnits):
    UNIT = "чи"
    FACTOR = 0.3333

class In(LengthUnits):
    UNIT = "инь"
    FACTOR = 33.3333

# Examples:
mm = Millimeters(100)
cm = Centimeters(50)
m = Meters(2)
km = Kilometers(10)
km2 = Kilometers(Meters(10000))
inch = Inches(10)
feet = Feets(3)
yard = Yards(1)
mile = Miles(0.25)
fen = Fen(100)
chi = Chi(10)
lin = In(20)
print(cm + mm)  # Adding Centimeters(50) and Millimeters(100)
print(cm + 20)  # Adding Centimeters(50) and Millimeters(100)
print(cm + 1)   # Adding Centimeters(50) and 1 meter
print(km)
print(km2)
print(m - km)   # Subtracting Meters(2) and Kilometers(0.5)
print(inch * 2) # Multiplying Inches(10) by 2
print(yard / 2) # Dividing Yards(1) by 2
cm += mm    # Incrementing Centimeters(50) by Millimeters(100)
print(cm)
inch -= feet    # Decrementing Inches(10) by Feets(3)
print(inch)
print(fen.to_base_units())  # Converting fen to base units (meters)
print(chi.from_base_units(3))   # Converting base units (3 meters) to chi
print(m == km)  # Comparing meters and kilometers (False)
print(inch < feet)  # Comparing inches and feet (True)
