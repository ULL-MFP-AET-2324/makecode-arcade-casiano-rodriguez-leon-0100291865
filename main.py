heroe = sprites.create(img("""
        . . . . . . . . . . . . . . 
            . . . . . f f f f . . . . . 
            . . . f f 5 5 5 5 f f . . . 
            . . f 5 5 5 5 5 5 5 5 f . . 
            . f 5 5 5 5 5 5 5 5 5 5 f . 
            c b 5 5 5 d b b d 5 5 5 b c 
            f 5 5 5 b 4 4 4 4 b 5 5 5 f 
            f 5 5 c c 4 4 4 4 c c 5 5 f 
            f b b f b f 4 4 f b f b b f 
            f b b e 1 f d d f 1 e b b f 
            c f b 4 4 d d d d d f b f c 
            . c d d d 4 9 9 9 6 c e c . 
            . c 4 d d 4 9 9 9 9 c 4 e . 
            . . c e e b b b 3 b b c e . 
            . . c c 3 b 3 b 3 3 c c . . 
            . . . . c c c b b c . . . .
    """),
    SpriteKind.player)
controller.move_sprite(heroe)