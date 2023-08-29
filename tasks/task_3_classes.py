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
        self._value = value * self.FACTOR

    @property
    def value(self):
        return self._value

    @property
    def value_in_units(self):
        return self._value / self.FACTOR

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def convert_to_base_units(self, other):
        if isinstance(other, LengthUnits):
            return other.value
        if isinstance(other, (int, float)):
            return other
        raise TypeError("Unsupported operand type.")

    def __add__(self, other):
        result = self.__class__(self.value)
        result.value = self.value + self.convert_to_base_units(other)
        return result

    def __iadd__(self, other):
        self._value += other.value
        return self

    def __sub__(self, other):
        result = self.__class__(self.value)
        result.value = self.value - self.convert_to_base_units(other)
        return result

    def __isub__(self, other):
        self._value -= other.value
        return self

    def __mul__(self, other):
        result = self.__class__(self.value)
        result.value = self.value * self.convert_to_base_units(other)
        return result

    def __imul__(self, other):
        self._value *= other.value
        return self

    def __truediv__(self, other):
        result = self.__class__(self.value)
        result.value = self.value / self.convert_to_base_units(other)
        return result

    def __itruediv__(self, other):
        self._value /= other.value
        return self

    def __str__(self):
        return f"{self.value_in_units} {self.UNIT}"

    def __eq__(self, other):
        if isinstance(other, LengthUnits):
            return self.value == other.value
        raise TypeError("Unsupported operand type.")

    def __lt__(self, other):
        if isinstance(other, LengthUnits):
            return self.value < other.value
        raise TypeError("Unsupported operand type.")

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

# Create instances of different length units
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
inch2 = In(20)

# Basic operations between length units
result1 = cm + mm
result2 = m - km
result3 = inch * 2
result4 = yard / 2

# Compound operations between length units
cm += mm       # Incrementing centimeters by millimeters
inch -= feet  # Decrementing inches by feet

# Comparison between length units
comparison1 = m == km    # Comparing meters and kilometers (False)
comparison2 = inch < feet  # Comparing inches and feet (True)

# Printing the values of length units
print(mm)    # Output: 100 мм
print(cm)    # Output: 60 см
print(m)     # Output: 2 м
print(km)    # Output: 0.5 км
print(inch)  # Output: -26 дюймов
print(feet)  # Output: 3 фута
print(yard)  # Output: 1 ярд
print(mile)  # Output: 0.25 мили
print(fen)   # Output: 100 фэнь
print(chi)   # Output: 10 чи
print(inch2) # Output: 20 инчей

print("result1 = cm + mm: ", result1) # 60 см
print("result2 = m - km: ", result2) # -498 m
print("result3 = inch * 2: ", result3) # 20 дюймов
print("result4 = yard / 2: ", result4) # 0.5 ярдов
print("comparison1 = m == km: ", comparison1) # False
print("comparison2 = inch < feet: ", comparison2) # True