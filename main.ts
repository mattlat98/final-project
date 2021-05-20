controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(blue_player_ball, 0, 50)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(blue_player_ball, 50, 0)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(blue_player_ball, 50, 0)
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    blue_player_ball.destroy(effects.confetti, 500)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    controller.moveSprite(blue_player_ball, 0, 50)
})
let blue_player_ball: Sprite = null
blue_player_ball = sprites.create(img`
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
    `, SpriteKind.Player)
blue_player_ball.setPosition(130, 90)
let red_enemy_ball = sprites.create(img`
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
    `, SpriteKind.Enemy)
red_enemy_ball.setPosition(65, 25)
scene.setBackgroundColor(5)
tiles.setTilemap(tilemap`level1`)
scene.cameraFollowSprite(blue_player_ball)
red_enemy_ball.follow(blue_player_ball, 25)
game.onUpdateInterval(500, function () {
    if (blue_player_ball.x <= 0) {
        blue_player_ball.setVelocity(50, 50)
    }
    if (blue_player_ball.y <= 0) {
        blue_player_ball.setVelocity(50, 50)
    }
})
