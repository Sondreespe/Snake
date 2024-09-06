from uib_inf100_graphics.event_app import run_app
from snake_view import draw_board
import random


def app_started(app):
    # Modellen.
    # Denne funksjonen kalles én gang ved programmets oppstart.
    # Her skal vi __opprette__ variabler i som behøves i app.
    app.direction = "east"
    app.debug_mode = False
    app.board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
    app.snake_size = 1
    app.head_pos = (4,0)
    app.state = "active"
    app.start = True
    app.result = False




def timer_fired(app):
    # En kontroller.
    # Denne funksjonen kalles ca 10 ganger per sekund som standard.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    if app.debug_mode == False and app.state =='active' and app.start== False:
        move_snake(app)
    app.timer_delay = 300

def key_pressed(app, event):
    # En kontroller.
    # Denne funksjonen kalles hver gang brukeren trykker på tastaturet.
    # Funksjonen kan __endre på__ eksisterende variabler i app.
    
    #bytter til motsatt verdi av app.debug_mode når det trykkes på "d"
    if event.key == "d":
        if app.debug_mode == True:
            app.debug_mode = False
        else:
            app.debug_mode = True

    if event.key =="Space":
        app.start = False

    #kobler retning opp mot teksten
    if app.state == "active":
        if event.key == "Up":
            app.direction ="north"
        elif event.key =="Down":
            app.direction ="south"
        elif event.key =="Left":
             app.direction ="west"
        elif event.key == "Right":
            app.direction = "east"
            
        elif app.debug_mode == True:
            if event.key =="p":
                move_snake(app)
    



def redraw_all(app, canvas):
    # Visningen.
    # Denne funksjonen tegner vinduet. Funksjonen kalles hver gang
    # modellen har endret seg, eller vinduet har forandret størrelse.
    # Funksjonen kan __lese__ variabler fra app, men har ikke lov til
    # å endre på dem.

    #sjekker verdiene til result,start,state og debug og viser siden i henngold til hva som gjelder.
    if app.result == False:
        if app.start == False:
            if app.state =="active":
                if app.debug_mode == True:
                    #genrerer debug siden
                    canvas.create_text(app.width/2, 10 , text="app.head_pos = "  f'{app.head_pos}' 
                    + ",app.direction = "  f'{app.direction}'   ", app.snake_size = " f'{app.snake_size}'', app.state= ' f'{app.state}' ,font="Arial 10")
                    draw_board(canvas,app.width - (app.width-25),app.height-(app.height-25), app.width -25, app.height-25, app.board,app.debug_mode)

                else:#genererer spill siden
                    draw_board(canvas,app.width - (app.width-25),app.height-(app.height-25), app.width -25, app.height-25, app.board,app.debug_mode)

            else:#genererer gameover siden
                canvas.create_rectangle(0,0,app.width,app.height, fill="Beige")
                canvas.create_text(app.width/2, app.height/2, text="GAMEOVER", fill="Black", font="Arial 40")
                canvas.create_text(app.width/2, app.height/2 + 50, text="Din score ble: " + f'{app.snake_size}', fill="Black", font="Arial 30 ")
        
        else: #Genererer start siden
            canvas.create_rectangle(0,0,app.width,app.height, fill="Beige")
            canvas.create_text(app.width/2, 100, text="Velkommen til spillet mitt", fill="Black", font="Arial 40")
            canvas.create_text(app.width/2, 140, text="Ved å bruke pil-tastene skal du få slangen til å spise de røde eplene.", fill="Black", font="Arial 20")
            canvas.create_text(app.width/2, 170, text="Du taper ved å kræsje enten i deg selv eller i veggene rundt deg.", fill="Black", font="Arial 20")
            canvas.create_text(app.width/2, 370, text="Trykk på space-baren, (mellomrom-tasten) for å starte.", fill="Black", font="Arial 20")
            canvas.create_text(app.width/2, 400, text="Trykk på D-tasten for å gå inn i debug mode, bruk P-tasten til å bevege deg", fill="Black", font="Arial 20")
            

    else:#genererer seier siden
        canvas.create_rectangle(0,0,app.width,app.height, fill="Beige")
        canvas.create_text(app.width/2, 200, text="Gralla! Du greide spillet", fill="Black", font="Arial 40")
        canvas.create_text(app.width/2, 250, text=f'{'Med en score på: '}' f'{app.snake_size}', fill="Black", font="Arial 20")




#funksjon som trekker fra 1 hos alle positive verdier
def subtract_one_from_all_positives(grid):

    for i in range(len(grid)):
        for a in range(len(grid[i])):
            if grid[i][a] > 0:
                grid[i][a] -=1
               

    return(grid)


#funksjon som bestemmer neste pos til hodet, returnerer så hodet
def get_next_head_position(head_pos,direction):
    if direction == "east":
        row, col = head_pos
        col+= 1
        head_pos = (row,col)
    elif direction =="west":
        row,col = head_pos
        col -= 1
        head_pos =(row,col)
    elif direction =="north":
        row,col = head_pos
        row -= 1
        head_pos = (row,col)
    elif direction =="south":
        row,col = head_pos
        row +=1
        head_pos = (row,col)

    return(head_pos)

#funksjon som lager et random eple
def add_apple_at_random_location(grid):
    a = grid
    while True :
        n_row = int(0)
        n_col = int(0)
        for i in range(len(grid)):
            n_row +=1
        for x in range(len(grid[0])):
            n_col +=1
        random_row = random.choice(range(n_row))
        random_col = random.choice(range(n_col))
       

        if a[random_row][random_col] == 0:
            a[random_row][random_col] = -1
            break
    return(a)

#funksjon som sjekker om trekket er lovlig
def is_legal_move(pos,board):
    row,col = pos
    if row < 0 or row ==len(board) :
        return(False)
    elif col < 0 or col == len(board[0]):
        return(False)
    elif board[row][col] > 0:
        return(False)
    
    else:
        return True

def maks_score(board):
    max_row = 0
    max_col = 0
    for i in range(len(board)):
        max_row += 1
    for a in range(len(board[0])):
        max_col += 1
    n_cells = max_col*max_row
    return(n_cells)



   
#funskjon som oppdaterer hvor neste hode er når du trykker 'space', bytter verdi i den cellen og trekker fra en fra alle positive celler
def move_snake(app):
    row,col = get_next_head_position(app.head_pos,app.direction)
  
    app.head_pos = (row,col)
    if is_legal_move(app.head_pos,app.board) == False:
        app.state = "gameover"
        return
    else:
        if app.board[row][col] == -1:
            app.snake_size += 1
            app.board = add_apple_at_random_location(app.board)
        
        else:
            subtract_one_from_all_positives(app.board)

    app.board[row][col] = app.snake_size

    if app.snake_size == maks_score(app.board):
        app.result = True
   




run_app(width=700, height=600, title="Snake")