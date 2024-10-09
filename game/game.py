import random
from game.player import Player
from game.monster import Monster
from config import PLAYER_NAME, PLAYER_HP, PLAYER_ATTACK, MONSTER_HP_RANGE, MONSTER_ATTACK_RANGE, MONSTER_COUNT

class Game:
    def __init__(self, player, monsters):
        self.player = player
        self.monsters = monsters

    @classmethod
    def create_game(cls):
        player = Player("Герой", 100, 20)
        monsters = [
            Monster(f"Чудовище {i+1}", random.randint(50, 150), random.randint(5, 20))
            for i in range(7)
        ]
        return cls(player, monsters)

    def start(self):
        print("Игра начинается!")
        self.battle()

    def process_user_input(self) -> str:
        valid_actions = {'a': 'normal', 's': 'strong', 'h': 'heal', 'd': 'defend', 'p': 'power_attack'}
        while True:
            action = input("Выберите действие: [a]атаковать, [s]сильная атака, [h]лечиться, [d]защищаться, [p]усиленная атака: ").lower()
            if action in valid_actions:
                print()
                return valid_actions[action]
            else:
                print("Некорректный ввод. Попробуйте еще раз.")

    def battle(self):
        while self.player.hp > 0 and any(monster.hp > 0 for monster in self.monsters):
            for monster in self.monsters:
                if monster.hp > 0:
                    action = self.process_user_input()
                    self.player.attack_target(monster, action)

                    if monster.hp > 0:
                        print(f"{monster.name} атакует {self.player.name}!")
                        self.player.take_damage(monster.attack)
                    if self.player.hp <= 0:
                        print("Игра окончена! Игрок был побеждён. Печаль!")
                        return
            print()

        if self.player.hp > 0:
            print("Поздравляем! Все монстры были побеждены. Поехали к принцессе!")
        else:
            print("Игра окончена! Игрок был побеждён. Печаль!")
