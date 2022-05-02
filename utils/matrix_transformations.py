def mudanca_base(row: int, col: int, sprite_size: int, matriz_muda_base) -> tuple:

    coord_x = (row * matriz_muda_base[0][0] * sprite_size) + (col * matriz_muda_base[1][0] * sprite_size)

    coord_y = (row * matriz_muda_base[0][1] * sprite_size) + (col * matriz_muda_base[1][1] * sprite_size)

    return ((coord_x, coord_y))