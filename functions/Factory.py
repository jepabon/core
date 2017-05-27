def collision(base_one, base_two):
    return False

def collisionMovement(base_one, limit, base_two=None):
    if base_one['x'] < 0 or base_one['x'] + base_one['width'] < 0:
        return True
    if base_one['y'] < 0 or base_one['y'] + base_one['height'] < 0:
        return True
    if base_one['x'] > limit['x'] or base_one['x'] + base_one['width'] > limit['x']:
        return True
    if base_one['y'] > limit['y'] or base_one['y'] + base_one['height'] > limit['y']:
        return True
    if base_two:
        return collision(base_one,base_two)
    return False
