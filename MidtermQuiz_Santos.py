class TempConversion:
    def __init__(self):
        pass

    def to_celsius(temp, source_scale):
        if source_scale == 'f':
            return (temp - 32) * 5 / 9
        elif source_scale == 'k':
            return temp - 273.15
        else:
            return temp

    def to_fahrenheit(temp, source_scale):
        if source_scale == 'c':
            return temp * 9 / 5 + 32
        elif source_scale == 'k':
            return (temp - 273.15) * 9 / 5 + 32
        else:
            return temp

    def to_kelvin(temp, source_scale):
        if source_scale == 'c':
            return temp + 273.15
        elif source_scale == 'f':
            return (temp - 32) * 5 / 9 + 273.15
        else:  
            return temp

temp = float(input("Enter a temperature to convert: "))
conversion = TempConversion()

print(str(TempConversion.to_celsius(temp, 'f')) + " Celsius")
print(str(TempConversion.to_celsius(temp, 'k')) + " Celsius")
print(str(TempConversion.to_fahrenheit(temp, 'c')) + " Fahrenheit")
print(str(TempConversion.to_fahrenheit(temp, 'k')) + " Fahrenheit")
print(str(TempConversion.to_kelvin(temp, 'c')) + " Kelvin")
print(str(TempConversion.to_kelvin(temp, 'f')) + " Kelvin")