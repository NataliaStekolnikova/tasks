# Задание 3.
# Классы. Наследование, волшебные методы.
# '''
# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения, например "1 км", "2.35 мили" и т.д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число, то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую, желательно с использованием __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит для этого.

class LengthUnits:
    base_unit = "м"

    def __init__(self, value):
        self.value = value

    def to_base_units(self):
        raise NotImplementedError

    def from_base_units(self, value):
        raise NotImplementedError

    def __str__(self):
        return f"{self.value} {self.base_unit}"

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
        if isinstance(other, LengthUnits):
            result = self.to_base_units() + other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() + other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

    def __iadd__(self, other):
        if isinstance(other, LengthUnits):
            result = self.to_base_units() + other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() + other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

    def __sub__(self, other):
        if isinstance(other, LengthUnits):
            result = self.to_base_units() - other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() - other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

    def __isub__(self, other):
        if isinstance(other, LengthUnits):
            result = self.to_base_units() - other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() - other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

    def __mul__(self, other):
        if isinstance(other, LengthUnits):
            result = self.to_base_units() * other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() * other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

    def __imul__(self, other):
        if isinstance(other, LengthUnits):
            result = self.to_base_units() * other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() * other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

    def __truediv__(self, other):
        if isinstance(other, LengthUnits):
            result = self.to_base_units() / other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() / other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

    def __itruediv__(self, other):
        if isinstance(other, LengthUnits):
            result = self.to_base_units() / other.to_base_units()
        elif isinstance(other, (int, float)):
            result = self.to_base_units() / other
        else:
            raise TypeError("Unsupported operand type.")
        return self.from_base_units(result)

class Millimeters(LengthUnits):
    base_unit = "мм"

    def to_base_units(self):
        return self.value / 1000

    def from_base_units(self, value):
        return Millimeters(value * 1000)

class Centimeters(LengthUnits):
    base_unit = "см"

    def to_base_units(self):
        return self.value / 100

    def from_base_units(self, value):
        return Centimeters(value * 100)

class Meters(LengthUnits):
    base_unit = "м"

    def to_base_units(self):
        return self.value

    def from_base_units(self, value):
        return Meters(value)

class Kilometers(LengthUnits):
    base_unit = "км"

    def to_base_units(self):
        return self.value * 1000

    def from_base_units(self, value):
        return Kilometers(value / 1000)

class Inches(LengthUnits):
    base_unit = "дюйм"

    def to_base_units(self):
        return self.value * 0.0254

    def from_base_units(self, value):
        return Inches(value / 0.0254)

class Feets(LengthUnits):
    base_unit = "фут"

    def to_base_units(self):
        return self.value * 0.3048

    def from_base_units(self, value):
        return Feets(value / 0.3048)

class Yards(LengthUnits):
    base_unit = "ярд"

    def to_base_units(self):
        return self.value * 0.9144

    def from_base_units(self, value):
        return Yards(value / 0.9144)

class Miles(LengthUnits):
    base_unit = "миля"

    def to_base_units(self):
        return self.value * 1609.34

    def from_base_units(self, value):
        return Miles(value / 1609.34)

class Fen(LengthUnits):
    base_unit = "фэнь" # Table of Chinese length units effective in 1930 https://en.wikipedia.org/wiki/Chinese_units_of_measurement

    def to_base_units(self):
        return self.value * (3 / 1000 + 1 / 3000)

    def from_base_units(self, value):
        return In(value / (3 / 1000 + 1 / 3000))

class Chi(LengthUnits):
    base_unit = "чи" # Table of Chinese length units effective in 1930 https://en.wikipedia.org/wiki/Chinese_units_of_measurement

    def to_base_units(self):
        return self.value * (33 / 10 + 1 / 30)

    def from_base_units(self, value):
        return In(value / (33 / 10 + 1 / 30))

class In(LengthUnits):
    base_unit = "инь" # Table of Chinese length units effective in 1930 https://en.wikipedia.org/wiki/Chinese_units_of_measurement

    def to_base_units(self):
        return self.value * (33 + 1/3)

    def from_base_units(self, value):
        return In(value / (33 + 1/3))

# Examples:
mm = Millimeters(100)
cm = Centimeters(50)
m = Meters(2)
km = Kilometers(0.5)
inch = Inches(10)
feet = Feets(3)
yard = Yards(1)
mile = Miles(0.25)
fen = Fen(100)
chi = Chi(10)
lin = In(20)
print(cm + mm)  # Adding Centimeters(50) and Millimeters(100)
print(cm + 1)   # Adding Centimeters(50) and 1 meter
print(m - km)   # Subtracting Meters(2) and Kilometers(0.5)
print(inch * 2) # Multiplying Inches(10) by 2
inch *= 2
print(inch)
print(yard / 2) # Dividing Yards(1) by 2
yard /= 2
print(yard)
cm += mm    # Incrementing Centimeters(50) by Millimeters(100)
print(cm)
inch -= feet    # Decrementing Inches(10) by Feets(3)
print(inch)
print(fen.to_base_units())  # Converting fen to base units (meters)
print(chi.from_base_units(3))   # Converting base units (3 meters) to chi
print(m == km)  # Comparing meters and kilometers (False)
print(inch < feet)  # Comparing inches and feet (True)
