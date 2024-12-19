from abc import ABC, abstractmethod
from threading import Lock
from typing import Dict, Tuple


# Base Coffee Classes
class BaseCoffee:
    def __init__(self, name: str, price: float, recipe: Dict[str, int]):
        self.name = name
        self.price = price
        self.recipe = recipe


class Espresso(BaseCoffee):
    def __init__(self):
        super().__init__("Espresso", 2.0, {"coffee": 2, "water": 50})


class Cappuccino(BaseCoffee):
    def __init__(self):
        super().__init__("Cappuccino", 3.5, {"coffee": 2, "water": 50, "milk": 100})


class Latte(BaseCoffee):
    def __init__(self):
        super().__init__("Latte", 4.0, {"coffee": 2, "water": 50, "milk": 150})


# Ingredient and Inventory Classes
class Ingredient:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def reduce(self, amount: int) -> None:
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            raise ValueError(f"Not enough {self.name} in stock.")

    def is_low(self, threshold: int) -> bool:
        return self.quantity < threshold


class Inventory:
    def __init__(self):
        self.ingredients = {
            "coffee": Ingredient("coffee", 100),
            "water": Ingredient("water", 500),
            "milk": Ingredient("milk", 300)
        }
        self.lock = Lock()

    def check_availability(self, recipe: Dict[str, int]) -> bool:
        with self.lock:
            return all(
                self.ingredients[ingredient].quantity >= amount
                for ingredient, amount in recipe.items()
            )

    def update_stock(self, recipe: Dict[str, int]) -> None:
        with self.lock:
            for ingredient, amount in recipe.items():
                self.ingredients[ingredient].reduce(amount)

    def get_low_ingredients(self, threshold: int) -> Dict[str, int]:
        with self.lock:
            return {
                name: ingredient.quantity
                for name, ingredient in self.ingredients.items()
                if ingredient.is_low(threshold)
            }


# Payment Class
class Payment:
    def __init__(self):
        self.current_balance = 0.0

    def process_payment(self, amount: float, price: float) -> Tuple[bool, float]:
        if amount >= price:
            self.current_balance += price
            return True, amount - price
        return False, 0.0


# State Base Class
class State(ABC):
    @abstractmethod
    def handle(self, machine: 'CoffeeMachine', *args):
        pass


# Concrete States
class IdleState(State):
    def handle(self, machine: 'CoffeeMachine', *args):
        print("Machine is idle. Please select a coffee.")
        machine.state = SelectCoffeeState()


class SelectCoffeeState(State):
    def handle(self, machine: 'CoffeeMachine', coffee_name: str):
        try:
            coffee = machine.menu[coffee_name.lower()]
            if not machine.inventory.check_availability(coffee.recipe):
                print(f"Not enough ingredients for {coffee.name}.")
                machine.state = MaintenanceState()
                return
            print(f"Selected {coffee.name}. Please pay ${coffee.price}.")
            machine.selected_coffee = coffee
            machine.state = PaymentProcessingState()
        except KeyError:
            print("Invalid coffee selection. Returning to idle state.")
            machine.state = IdleState()


class PaymentProcessingState(State):
    def handle(self, machine: 'CoffeeMachine', payment: float):
        coffee = machine.selected_coffee
        success, change = machine.payment_processor.process_payment(payment, coffee.price)
        if success:
            print(f"Payment successful. Change: ${change:.2f}")
            machine.state = DispensingState()
        else:
            print(f"Insufficient payment. {coffee.name} costs ${coffee.price}.")
            machine.state = IdleState()


class DispensingState(State):
    def handle(self, machine: 'CoffeeMachine'):
        coffee = machine.selected_coffee
        machine.inventory.update_stock(coffee.recipe)
        print(f"Dispensing {coffee.name}. Enjoy your coffee!")
        machine.state = IdleState()


class MaintenanceState(State):
    def handle(self, machine: 'CoffeeMachine'):
        low_ingredients = machine.inventory.get_low_ingredients(threshold=10)
        if low_ingredients:
            print(f"Low ingredients: {low_ingredients}. Refill needed.")
        else:
            print("Machine is fully stocked. Returning to idle state.")
        machine.state = IdleState()


# CoffeeMachine Class
class CoffeeMachine:
    def __init__(self):
        self.inventory = Inventory()
        self.payment_processor = Payment()
        self.menu = {
            "espresso": Espresso(),
            "cappuccino": Cappuccino(),
            "latte": Latte()
        }
        self.state: State = IdleState()
        self.selected_coffee: BaseCoffee = None

    def request(self, *args):
        self.state.handle(self, *args)


# Simulation
if __name__ == "__main__":
    machine = CoffeeMachine()

    machine.request()  # Idle -> Select Coffee
    machine.request("espresso")  # Select Coffee -> Payment Processing
    machine.request(2.0)  # Payment Processing -> Dispensing
    machine.request()  # Dispensing -> Idle
