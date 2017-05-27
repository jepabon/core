from core.classes.Base import Base
from core.functions.Factory import collisionMovement


class BaseCharacter(Base):
    life = 100
    agility = 10
    strength = 10
    intelligence = 10
    dexterity = 10
    evasion = agility * 0.1
    mana = intelligence * 2

    def __init__(self, position=None, life=None):
        if life:
            self.life = life
        if position:
            super(BaseCharacter, self).__init__(position)

    def movement(self, up=None, down=None, right=None, left=None):
        pos = {}
        pos['y'] = self.position['y']
        pos['x'] = self.position['x']
        pos['width'] = self.size['width']
        pos['height'] = self.size['height']
        if up == True:
            pos['y'] = self.position['y'] - self.speed
            if not collisionMovement(base_one=pos, limit={'x': 400, 'y': 400}):
                self.position['y'] -= self.speed
        elif down == True:
            pos['y'] = self.position['y'] + self.speed
            if not collisionMovement(base_one=pos, limit={'x': 400, 'y': 400}):
                self.position['y'] += self.speed
        if right == True:
            pos['x'] = self.position['x'] + self.speed
            if not collisionMovement(base_one=pos, limit={'x': 400, 'y': 400}):
                self.position['x'] += self.speed
        elif left == True:
            pos['x'] = self.position['x'] - self.speed
            if not collisionMovement(base_one=pos, limit={'x': 400, 'y': 400}):
                self.position['x'] -= self.speed

        return self.position

    def change_life(self, life):
        self.life += life

    def set_attribute(self, agility=None,strength=None, intelligence=None, dexterity=None):
        if agility:
            self.agility = agility
            self.evasion = self.agility * 0.1
        if strength:
            self.strength = strength
        if intelligence:
            self.intelligence = intelligence
            self.mana = self.intelligence * 2
        if dexterity:
            self.dexterity = dexterity

    def get_attribute(self):
        attribute = {
            'life': self.life,
            'agility': self.agility,
            'strength': self.strength,
            'intelligence': self.intelligence,
            'dexterity': self.dexterity,
            'evasion': self.evasion,
            'mana': self.mana
        }

        return attribute
