import random

l_shape = [
    [
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    ],
    
    [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    ]

]

n_shape = [
    [
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],     
    ],

    [
    [0, 0, 1, 1],
    [1, 1, 1, 0]         
    ]

]

t_shape = [
    [
    [1, 1, 1],
    [0, 1, 0]    
    ],

    [
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 0]    
    ],
]



#this is what needs to be done:
#random shape and it's position must be returned to the game
#when the player presses Z, they need to return the name of the shape they are using, and what position it is in (based on 1 or 0)
#give them back the rotated shape

shapes = {
    "t_shape": t_shape,
    "n_shape": n_shape,
    "l_shape": l_shape
}

def shapeOptions(rotate):
    # rand_choice = random.choice(list(shapes.keys()))
    # rand_num = random.randrange(0, 1)

    # return rand_choice[rand_num]

    dec = random.choice(list(shapes.items()))
    return dec