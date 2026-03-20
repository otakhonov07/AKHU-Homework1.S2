from abc import ABC, abstractmethod 

class Converter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def convert(self, value):
        pass

    def describe(self, value):
        result = self.convert(value)
        return f"{self.name}: {value} -> {result}"


class CelsiusToFahrenheit(Converter):
    def __init__(self):
        super().__init__("CelsiusToFahrenheit")

    def convert(self, value):
        result = round(value * 9/5 + 32, 2)
        return result


class KilometersToMiles(Converter):
    def __init__(self):
        super().__init__("KilometersToMiles")

    def convert(self, value):
        result = round(value * 0.621371, 2)
        return result


class KilogramsToPounds(Converter):
    def __init__(self):
        super().__init__("KilogramsToPounds")

    def convert(self, value):
        result = round(value * 2.20462, 2)
        return result


class CustomConverter:
    def __init__(self, name, factor):
        self.name = name
        self.factor = factor
    
    def convert(self, value):
        result = round(value * self.factor, 2)
        return result
    
    def describe(self, value):
        result = self.convert(value)
        return f"{self.name}: {value} -> {result}"


class ConversionLog:
    def __init__(self):
        self.entries = []

    def log(self, converter_name, original, converted):
        entry = f"{converter_name}: {original} -> {converted}"
        self.entries.append(entry)

    def show(self):
        for entry in self.entries:
            print(entry)


class ConversionStation:
    def __init__(self, name):
        self.name = name
        self.converters = []
        self.log = ConversionLog()

    def add_converter(self, converter):
        self.converters.append(converter)

    def convert_all(self, value):
        print(f"=== {self.name} ===")
        for converter in self.converters:
            converted = converter.convert(value)
            print(converter.describe(value))
            self.log.log(converter.name, value, converted)

    def show_log(self):
        print(f"--- Log for {self.name} ---")
        self.log.show()

station = ConversionStation('Science Lab')
station.add_converter(CelsiusToFahrenheit())
station.add_converter(KilometersToMiles())
station.add_converter(KilogramsToPounds())
station.add_converter(CustomConverter('LitersToGallons', 0.264172))

station.convert_all(100)
print()
station.convert_all(50)
print()
station.show_log()

try:
    c = Converter('test')
except TypeError:
    print('Cannot instantiate abstract class')
