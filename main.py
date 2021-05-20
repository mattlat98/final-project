def on_up_pressed():
    controller.move_sprite(blue_player_ball, 0, 50)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_left_pressed():
    controller.move_sprite(blue_player_ball, 50, 0)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    controller.move_sprite(blue_player_ball, 50, 0)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    blue_player_ball.destroy(effects.confetti, 500)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_down_pressed():
    controller.move_sprite(blue_player_ball, 0, 50)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

blue_player_ball: Sprite = None
blue_player_ball = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . f f f f f . . . . . . . 
            . . . f 1 8 8 8 8 f . . . . . . 
            . . f 1 8 8 8 8 8 8 f . . . . . 
            . . f 8 8 8 8 8 8 8 f . . . . . 
            . . f 8 8 8 8 8 8 8 f . . . . . 
            . . f 8 8 8 8 8 8 8 f . . . . . 
            . . f 8 8 8 8 8 8 8 f . . . . . 
            . . . f 8 8 8 8 8 f . . . . . . 
            . . . . f f f f f . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
blue_player_ball.set_position(130, 90)
red_enemy_ball = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . f f f f f . . . . . . . . 
            . . f 1 2 2 2 2 f . . . . . . . 
            . f 1 2 2 2 2 2 2 f . . . . . . 
            . f 2 2 2 2 2 2 2 f . . . . . . 
            . f 2 2 2 2 2 2 2 f . . . . . . 
            . f 2 2 2 2 2 2 2 f . . . . . . 
            . f 2 2 2 2 2 2 2 f . . . . . . 
            . . f 2 2 2 2 2 f . . . . . . . 
            . . . f f f f f . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.enemy)
red_enemy_ball.set_position(65, 25)
scene.set_background_color(5)
tiles.set_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(blue_player_ball)
red_enemy_ball.follow(blue_player_ball, 25)

def on_update_interval():
    if blue_player_ball.x <= 0:
        blue_player_ball.set_velocity(50, 50)
    if blue_player_ball.y <= 0:
        blue_player_ball.set_velocity(50, 50)
game.on_update_interval(500, on_update_interval)
