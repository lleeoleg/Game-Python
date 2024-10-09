class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} получил {damage} урона и у него {self.hp} HP.")

    @staticmethod
    def calculate_damage(base_attack: int, multiplier: int = 1) -> int:
        return base_attack * multiplier