from os import get_terminal_size
import numpy as np
import math


def first():
    data = open("20/jj.txt", "r").read().split("\n\n")

    tiles = {lines[0][-5:-1]: (np.array([list(line) for line in lines[1:]])
                               == '#').astype(int) for lines in map(str.splitlines, data)}

    def get_borders(tile):
        return [
            tuple(tile[0, :]),
            tuple(tile[:, -1]),
            tuple(tile[-1, :]),
            tuple(tile[:, 0]),
            tuple(tile[0, ::-1]),
            tuple(tile[::-1, -1]),
            tuple(tile[-1, ::-1]),
            tuple(tile[::-1, 0]),
        ]

    corner_tiles = {}

    for id, tile in tiles.items():
        border_face = 0
        for border in get_borders(tile)[:4]:
            matches = 0
            for i, t in tiles.items():
                if i == id:
                    continue
                if border in get_borders(t):
                    matches += 1
            if matches == 0:
                border_face += 1
        if border_face == 2:
            corner_tiles[id] = tile

    print(math.prod(map(int, corner_tiles.keys())))


def second():
    data = open("20/jj.txt", "r").read().split("\n\n")

    tiles = {lines[0][-5:-1]: (np.array([list(line) for line in lines[1:]])
                               == '#').astype(int) for lines in map(str.splitlines, data)}

    def get_borders(tile):
        return [
            tuple(tile[0, :]),
            tuple(tile[:, -1]),
            tuple(tile[-1, :]),
            tuple(tile[:, 0]),
            tuple(tile[0, ::-1]),
            tuple(tile[::-1, -1]),
            tuple(tile[-1, ::-1]),
            tuple(tile[::-1, 0]),
        ]

    def get_matches(id, border):
        matches = 0
        for i, t in tiles.items():
            if i == id:
                continue
            if border in get_borders(t):
                matches += 1
        return matches

    corner_tiles = {}
    outer_tiles = {}
    inner_tiles = {}

    for id, tile in tiles.items():
        border_face = 0
        for border in get_borders(tile)[:4]:
            if get_matches(id, border) == 0:
                border_face += 1
        if border_face == 2:
            corner_tiles[id] = tile
        elif border_face == 1:
            outer_tiles[id] = tile
        else:
            inner_tiles[id] = tile

    tile_layout = np.array((12, 12), int)

    # build first line o' 12
    tile_layout[0, 0] = list(corner_tiles.keys())[0]
    # TODO: check which directions are border facing, rotate/flip so its facing left/up for easier understanding
    for j in range(1, 11):
        tile = list(outer_tiles.keys())[0]
        # TODO: check the border facing side is the same as for the starting tile (left)
        tile_layout[0, j] = tile
    tile_layout[0, 11] = list(corner_tiles.keys())[1]
    # TODO: find the matching corner tile, it has to match one border face (left) and the advancing direction (down)

    # build lines 2 to 11
    for i in range(1, 11):
        tile = list(outer_tiles.keys())[0]
        # TODO: check the border facing side inverts the advancing direction (top)
        tile_layout[i, 0] = tile
        for j in range(1, 11):
            tile = list(inner_tiles.keys())[0]
            # TODO: find an inner tile that matches the left border and the top border
            tile_layout[i, j] = tile
        tile = list(outer_tiles.keys())[0]
        # TODO: check the border facing side matches the advancing direction (top)
        tile_layout[i, 11] = tile

    # build last line o' 12
    tile_layout[11, 0] = list(corner_tiles.keys())[0]
    # TODO: find the corner tile that matches the left border, and has a top + right border face
    for j in range(1, 11):
        tile = list(outer_tiles.keys())[0]
        # TODO: check the border facing side is the opposite of the starting tile (right)
        # it also has to match the left border
        tile_layout[0, j] = tile
    tile_layout[0, 11] = list(corner_tiles.keys())[1]
    # TODO: find the last corner tile, it has to match the left border and have a bottom + right border face


if __name__ == "__main__":
    # first()
    second()
