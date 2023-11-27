from abc import ABC, abstractmethod


# Абстрактные классы для компонентов машины
class Wheel(ABC):
    @abstractmethod
    def get_wheel_type(self):
        pass


class Suspension(ABC):
    @abstractmethod
    def get_suspension_type(self):
        pass


class Engine(ABC):
    @abstractmethod
    def get_engine_type(self):
        pass


# Конкретные классы для компонентов машины
class RegularWheel(Wheel):
    def get_wheel_type(self):
        return "Обычные колеса"


class SportsWheel(Wheel):
    def get_wheel_type(self):
        return "Спортивные колеса"


class RegularSuspension(Suspension):
    def get_suspension_type(self):
        return "Обычная подвеска"


class SportsSuspension(Suspension):
    def get_suspension_type(self):
        return "Спортивная подвеска"


class RegularEngine(Engine):
    def get_engine_type(self):
        return "Обычный двигатель"


class TurboEngine(Engine):
    def get_engine_type(self):
        return "Турбо двигатель"


# Абстрактная фабрика для создания компонентов машины
class CarComponentFactory(ABC):
    @abstractmethod
    def create_wheel(self):
        pass

    @abstractmethod
    def create_suspension(self):
        pass

    @abstractmethod
    def create_engine(self):
        pass


# Конкретные фабрики для создания компонентов машины
class RegularCarComponentFactory(CarComponentFactory):
    def create_wheel(self):
        return RegularWheel()

    def create_suspension(self):
        return RegularSuspension()

    def create_engine(self):
        return RegularEngine()


class SportsCarComponentFactory(CarComponentFactory):
    def create_wheel(self):
        return SportsWheel()

    def create_suspension(self):
        return SportsSuspension()

    def create_engine(self):
        return TurboEngine()


# Класс машины, который использует созданные компоненты
class Car:
    def __init__(self, factory):
        self.wheel = factory.create_wheel()
        self.suspension = factory.create_suspension()
        self.engine = factory.create_engine()

    def get_description(self):
        return f"Машина имеет {self.wheel.get_wheel_type()}, {self.engine.get_engine_type()} и " \
               f"{self.suspension.get_suspension_type()} "
