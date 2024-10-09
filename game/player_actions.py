import random
from game.character import Character
from typing import Type

class PlayerActions:
    def __init__(self, player):
        self.player = player
        self.defending = False

    def normal_attack(self, target: Type[Character]) -> None:
        damage = Character.calculate_damage(self.player.attack)
        print(f"{self.player.name} атакует {target.name}!")
        target.take_damage(damage)

    def strong_attack(self, target: Type[Character]) -> None:
        if random.random() > 0.5:  # 50% шанс промаха
            damage = Character.calculate_damage(self.player.attack, 2)
            print(f"{self.player.name} использует сильную атаку на {target.name}!")
        else:
            damage = 0
            print(f"{self.player.name} промахивается сильной атакой!")
        target.take_damage(damage)

    def power_attack(self, target: Type[Character]) -> None:
        if random.random() > 0.3:  # 70% шанс попасть
            damage = Character.calculate_damage(self.player.attack, 3)
            print(f"{self.player.name} использует усиленную атаку на {target.name}!")
        else:
            damage = 0
            print(f"{self.player.name} промахивается усиленной атакой!")
        target.take_damage(damage)

    def heal(self) -> None:
        heal_amount = 20
        if self.player.hp + heal_amount > self.player.max_hp:
            heal_amount = self.player.max_hp - self.player.hp
        self.player.hp += heal_amount
        print(f"{self.player.name} лечит себя на {heal_amount} HP и теперь у него {self.player.hp} HP.")

    def defend(self) -> None:
        self.defending = True
        print(f"{self.player.name} готовится к защите и уменьшает получаемый урон вдвое!")

    def take_damage(self, damage: int) -> None:
        if self.defending:
            damage //= 2
            self.defending = False
        self.player.take_damage(damage)