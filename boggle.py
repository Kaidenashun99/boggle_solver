def make_grid(width, height):
    #Make an empty boggle grid
    
    return{(row, col): ' ' for row in range(height)
        for col in range(width)
    }