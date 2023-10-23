from __future__ import annotations
from dice import Dice, RiggedDice

from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich import print
from rich.panel import Panel

""" layout["lower"].split_row(
    Layout(name="left"),
    Layout(name="right"),
) """
""" print(layout) """


print("\n")


class Character:
    _label = "Character"

    def __init__(
        self, name: str, max_health: int, attack: int, defense: int, dice: Dice
    ):
        self._name = name
        self._max_health = max_health
        self._health = self._max_health
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice

    def welcomeCharacter(self):
        return f"[purple]{type(self)._label} {self._name}[/purple] is starting the fight with [blue]{self._health}/{self._max_health}hp[/blue] ([red]{self._attack_value}atk[/red] / [green]{self._defense_value}def[/green])"

    def __str__(self):
        return self.welcomeCharacter()

    # def __repr__(self) -> str:
    #     return self.__str__()

    def get_name(self):
        return self._name

    def get_defense_value(self):
        return self._defense_value

    def is_alive(self):
        return self._health > 0
        # return bool(self._health)

    def regenerate(self):
        self._health = self._max_health

    def show_healthbar(self):
        missing_hp = self._max_health - self._health
        print(
            f"[{'●' * self._health}{' ' * missing_hp}] {self._health}/{self._max_health}hp"
        )

    def decrease_health(self, amount):
        if self._health - amount < 0:
            amount = self._health
        self._health = self._health - amount
        self.show_healthbar()

    def compute_damages(self, target: Character, roll: int) -> int:
        return self._attack_value + roll

    def attack(self, target: Character):
        if self.is_alive():
            roll = self._dice.roll()
            damages = self.compute_damages(target, roll)
            print(
                f"⚔️ {type(self)._label}  {self._name} [red]attack[/red] {target.get_name()} with {damages} damages ! (attack: {self._attack_value} + roll: {roll})"
            )
            target.defense(self, damages)

    def compute_defense(self, damages, roll):
        return damages - self._defense_value - roll

    def defense(self, attacker: Character, damages: int):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll)
        print(
            f"🛡️ {type(self)._label} {self._name} [green]defend[/green] against {attacker.get_name()} for {damages} damages and take {wounds} wounds ! (damages: {damages} - defense: {self._defense_value} - roll: {roll})"
        )
        self.decrease_health(wounds)


class Warrior(Character):
    _label = "Warrior"

    def compute_damages(self, target, roll):
        print(f"🪓 Axe in face ! (bonus: +3)")
        return super().compute_damages(target, roll) + 3


class Mage(Character):
    _label = "Mage"

    def compute_defense(self, damages, roll):
        print(f"🔮 Magic armor ! (bonus: -3)")
        return super().compute_defense(damages, roll) - 3


class Thief(Character):
    _label = "Thief"

    def compute_damages(self, target: Character, roll: int) -> int:
        print(f"🤶 Sneacky sneacky... ! (bonus: +{target.get_defense_value()})")
        return super().compute_damages(target, roll) + target.get_defense_value()


if __name__ == "__main__":
    char_1: Warrior = Warrior("James", 20, 8, 3, Dice(6))
    char_2: Thief = Thief("Dina", 20, 8, 3, Dice(6))

    print(char_1)
    print(char_2)
    
    layout = Layout()

    layout.split_column(
        Layout(Panel("The combat starts!", title="Welcome")),
        Layout(name="lower"),
        Layout(name="footer"),
)

    layout["lower"].split_row(
        Layout(Panel(char_1.welcomeCharacter(), title="Character 1")),
        Layout(Panel(char_2.welcomeCharacter(), title="Character 2")),
)
    
    

    print(layout)
    
    

    while char_1.is_alive() and char_2.is_alive():
        char_1.attack(char_2)
        char_2.attack(char_1)
