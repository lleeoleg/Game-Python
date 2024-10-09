from game.character import Character
from game.player_actions import PlayerActions

class Player(Character, PlayerActions):
    def __init__(self, name, hp, attack):
        super().__init__(name, hp, attack)
        PlayerActions.__init__(self, self)

    def attack_target(self, target, attack_type):
        if attack_type == "strong":
            self.strong_attack(target)
        elif attack_type == "heal":
            self.heal()
        elif attack_type == "defend":
            self.defend()
        elif attack_type == "power_attack":
            self.power_attack(target)
        else:
            self.normal_attack(target)
