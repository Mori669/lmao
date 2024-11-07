class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Номера автомобиля должны быть представлены в виде строки")

        if len(numbers)!= 6:
            raise IncorrectCarNumbers("Номер VIN автомобиля должен состоять из 6 символов")

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Номер VIN автомобиля должен быть представлен в виде числа")

        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")

        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
