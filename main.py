import random
#random libary to randomly move food and snake at start

#grid
app.setMaxShapeCount(1000000)
def drawGrid(x,y):
    Rect(x,y,25,25,fill='forestGreen', border='black')

def grid():
    for row in range(16):
        row *= 25
        for colluem in range(16):
            colluem *= 25
            drawGrid(row,colluem)
grid()

Rect(0,0,400,50)
score=Label(0,105,25,fill='red',size=30)
Label('Score: ',50,25,fill='red',size=30)

# the border where if snake hits it you lose
wall = Rect(0,50,400,400,fill=None, border='red')

#define our start values
start_x = random.choice(range(50, 350, 25))
start_y = random.choice(range(150, 350, 25))

apple_start_x = random.choice(range(50, 350, 25))
apple_start_y = random.choice(range(50, 350, 25))
align_appleX = apple_start_x + 12.5
align_appleY = apple_start_y + 12.5
apple=Group(
            Circle(align_appleX, align_appleY , 12.5, fill='red'),
            Oval(align_appleX + 7,align_appleY - 6,11,6, fill='tomato',rotateAngle=40),
            Rect(align_appleX - 5.25, align_appleY - 15.5 ,6.25, 6.25, fill='brown' )
            )

#our snake 
app.stepsPerSecond=5
snake=Group(
    Rect(start_x ,start_y ,25,25,fill='red')
    )
app.head = snake.children[0]
snake.children[0].direction = "up"
def move_snake():
    adjust_snake()
    update_snake()
   #define out hit logic
    if snake.children[0].left < 0  or snake.children[0].right > 400 or snake.children[0].top < 50 or snake.children[0].bottom > 400:
        end_game()
        
def end_game():
    Rect(0,0,400,400)
    Label('Game Over!', 220, 50, size = 50, fill = 'red')
    snake.children[0].centerX = 200
    snake.children[0].centerY = 200

#define logic for keypresses
def onKeyPress(key):
    if key == 'up' and snake.children[0].direction != 'down':
        snake.children[0].direction = 'up'
    elif key == 'down' and snake.children[0].direction != 'up':
        snake.children[0].direction = 'down'
    elif key == 'left' and snake.children[0].direction != 'right':
        snake.children[0].direction = 'left'
    elif key == 'right' and snake.children[0].direction != 'left':
        snake.children[0].direction = 'right'


app.last_speed= -1
def update_snake():
        #when apple is hit add +1 to score
    if(snake.children[0].hits(apple.centerX,apple.centerY)==True):
        score.value+=1
        apple.centerX = random.choice(range(50, 350, 25)) + 12.5
        apple.centerY = random.choice(range(50, 350, 25)) + 12.5
        add_piece()
    if score.value >= 10:
        score.centerX = 110
    for i in range(app.last_speed + 1, score.value // 10 + 1):
        app.stepsPerSecond += .5
        if score.value >= 50:
            break
    app.last_speed = score.value // 10

#initlize it once to not reset
app.level = 0
def add_piece():
   #adds a new piece to the group when an apple is hit and adjusts the position
   # add a thing to cycle the colour
    app.color = ['red', 'orange', 'yellow', 'lightGreen', 'blue', 'indigo', 'violet']
    app.level =app.level + 1 
    app.level = app.level % 7 

    piece = Group(
        Rect(app.head.left , app.head.top , app.head.width, app.head.height, fill = app.color[app.level])
    )
    snake.add(piece)
    if snake.children[0].direction == "up":
        piece.centerY += 25
    elif snake.children[0].direction == "down":
        piece.centerY -= 25
    elif snake.children[0].direction == 'left':
        piece.centerX += 25
    elif snake.children[0].direction == 'right':
        piece.centerX -=25
    
#movement for each piece in the snake and calls end game if snake head hits body 
def adjust_snake():
    head = snake.children[0]
    previous_position = (head.left, head.top)
    if snake.children[0].direction == "up":
        head.centerY -= 25
    elif snake.children[0].direction == "down":
        head.centerY += 25
    elif snake.children[0].direction == 'left':
        head.centerX -= 25
    elif snake.children[0].direction == 'right':
        head.centerX +=25
    for piece in snake.children[1:]:
        current_position = (piece.left, piece.top)
        piece.left, piece.top = previous_position
        previous_position = current_position
        if apple.hits(piece.centerX,piece.centerY) and score.value <= 51:
            apple.centerX =  random.choice(range(50, 350, 25)) + 12.5
            apple.centerY =  random.choice(range(50, 350, 25)) + 12.5
        if head.hits(piece.centerX, piece.centerY):
            end_game()
def onStep():    
    move_snake()
