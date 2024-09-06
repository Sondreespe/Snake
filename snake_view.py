def draw_board(canvas,x1,y1,x2,y2,board,debug_mode):
    bredde_brett = x2-x1
    høyde_brett = y2-y1 
    rader = len(board)
    kolonne = len(board[0])
    bredde_celle = bredde_brett/kolonne
    høyde_celle  = høyde_brett/rader

    if debug_mode == True:

        for i in range(0,rader):
            cell_y1 = y1 + høyde_celle *i
            cell_y2 = cell_y1 + høyde_celle
            
            for a in range(0, kolonne):
                cell_x1 = x1 + bredde_celle*a
                cell_x2 = cell_x1 + bredde_celle

                celle_kordinater_x = bredde_celle/2 + cell_x1
                celle_kordinater__y = høyde_celle/2 + cell_y1 - 10
                

                if board[i][a] == 0 and i%2 == 0:
                    if a%2 == 0:
                         canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="GreenYellow")
                    else:
                        canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="LawnGreen")
                if board[i][a] == 0 and i%2 != 0:
                    if a%2 != 0:
                        canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="GreenYellow")
                    else:
                         canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="LawnGreen")
                        


                elif board[i][a] > 0:
                    farge_styrke = 255 - (board[i][a] * 10)
                    color = f'#0000{farge_styrke:02x}'
                elif board[i][a] < 0:
                    canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="Red", outline="Black")
            
 

                    
                canvas.create_text(celle_kordinater_x, celle_kordinater__y, text= f'{i , a}' , fill="Black")
                canvas.create_text(celle_kordinater_x,celle_kordinater__y + 20, text= board[i][a], fill="Black")
         



    else:
        for i in range(0,rader):
            cell_y1 = y1 + høyde_celle *i
            cell_y2 = cell_y1 + høyde_celle

            for a in range(0, kolonne):
                cell_x1 = x1 + bredde_celle*a
                cell_x2 = cell_x1 + bredde_celle
               
                if board[i][a] == 0 and i%2 == 0:
                    if a%2 == 0:
                         canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="GreenYellow")
                    else:
                        canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="LawnGreen")
                if board[i][a] == 0 and i%2 != 0:
                    if a%2 != 0:
                        canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="GreenYellow")
                    else:
                         canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="LawnGreen")
                        
                elif board[i][a] > 0:
                    farge_styrke = 255 - (board[i][a] * 10)
                    if farge_styrke < 0:
                        farge_styrke = 0
                    color = f'#0000{farge_styrke:02x}'
                    canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill=color)
                elif board[i][a] < 0:
                    canvas.create_rectangle(cell_x1,cell_y1,cell_x2,cell_y2, fill="Red", outline="Black")
                
            
 


