import itertools
import re
import math
import copy
from collections import defaultdict

# # Part A

class TileConfiguration:
    def __init__(self, flip_x, flip_y, rotate_count, tile_id, north_side, south_side, west_side, east_side):
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.rotate_count = rotate_count # counter-clockwise
        self.tile_id = tile_id
        self.north_side = north_side
        self.south_side = south_side
        self.west_side = west_side
        self.east_side = east_side 

        if flip_y:
            self.west_side, self.east_side = self.east_side, self.west_side
            self.north_side = self.north_side[::-1]
            self.south_side = self.south_side[::-1]
        
        if flip_x:
            self.north_side, self.south_side = self.south_side, self.north_side
            self.east_side = self.east_side[::-1]
            self.west_side = self.west_side[::-1]
        
        for i in range(rotate_count):
            self.north_side, self.east_side, self.south_side, self.west_side = self.east_side, self.south_side, self.west_side, self.north_side

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Tile: {self.tile_id}. Flip X: {self.flip_x}, Flip Y: {self.flip_y}, Rotations: {self.rotate_count}, North: {self.north_side} South: {self.south_side} East: {self.east_side} West: {self.west_side}"

with open('input.txt', 'r') as f:
  input = [line.strip() for line in f]

tiles = []

for i in range(0, len(input), 12):
    tile_num = int(input[i][5:-1])
    tiles.append((tile_num, input[i+1:i+11]))

edge_dict = defaultdict(list)

for tile_num, tile in tiles:
    north_side = tile[0]
    south_side = tile[9]
    west_side = "".join([x[0] for x in tile])
    east_side = "".join([x[9] for x in tile])

    for flip_x, flip_y in itertools.product([True, False], repeat=2):
        for i in range(3):
            config = TileConfiguration(flip_x, flip_y, i, tile_num, north_side, south_side, west_side, east_side)
            edge_dict[(north_side, "north")].append(config)
            edge_dict[(south_side, "south")].append(config)
            edge_dict[(west_side, "west")].append(config)
            edge_dict[(east_side, "east")].append(config)
    

def diagonal_iter():
    for i in range((12)*2 - 1, -1, -1):
        for y in range(12-1, -1, -1):
            x = i - y
            if x >= 0 and x < 12:
                yield (y, x)

diagonals = list(diagonal_iter())

def find_tiles(config):
    used_tile_ids = set(config.tile_id)
    options_not_taken = [[False for x in range(12)] for y in range(12)]
    tile_grid = [[False for x in range(12)] for y in range(12)]
    diagonal_index = 1
    while diagonal_index < len(diagonals):
        x, y = diagonals[diagonal_index]
        diagonal_index += 1
        if x == 0 and y == 0:
            continue
        if x == 12 or x == 0:
            # find available sides
            available = [tile for tile in edge_dict[(tile_grid[x][y-1].north_side, "south")] if tile.tile_id not in used_tile_ids]
            # fail
            if len(available) == 0:
                diagonal_index -= 1
                while True:
                    oldx, oldy = diagonals[diagonal_index - 1]
                    wrong_pick, other_opts = options_not_taken[oldx][oldy]
                    used_tile_ids.remove(wrong_pick)
                    if len(other_opts) > 0:
                        new_pick = other_opts.pop()
                        used_tile_ids.add(new_pick.tile_id)
                        tile_grid[oldx][oldy] = new_pick
                        options_not_taken[oldx, oldy] = (new_pick.tile_id, other_opts)
                        break
                    else:
                        diagonal_index -= 1

            else:
                pick_tile = available[0]
                tile_grid[x][y] = pick_tile
                options_not_taken[x][y] = (pick_tile.tile_id, available[1:])
                used_tile_ids.add(pick_tile.tile_id)
        elif y == 12 or y == 0:
            # find available sides
            available = [tile for tile in edge_dict[(tile_grid[x-1][y].west_side, "east")] if tile.tile_id not in used_tile_ids]
            # fail
            if len(available) == 0:
                # TODO
                pass
            else:
                pick_tile = available[0]
                tile_grid[x][y] = pick_tile
                options_not_taken[x][y] = (pick_tile.tile_id, available[1:])
                used_tile_ids.add(pick_tile.tile_id)
        else:
            # find available sides
            available_east = set([tile for tile in edge_dict[(tile_grid[x-1][y].west_side, "east")] if tile.tile_id not in used_tile_ids])
            available_north = [tile for tile in edge_dict[(tile_grid[x][y-1].north_side, "south")] if tile.tile_id not in used_tile_ids]
            available = [tile for tile in available_north if tile in available_east]
            # fail
            if len(available) == 0:
                # TODO
                pass
            else:
                pick_tile = available[0]
                tile_grid[x][y] = pick_tile
                options_not_taken[x][y] = (pick_tile.tile_id, available[1:])
                used_tile_ids.add(pick_tile.tile_id)

    print(config)

starting_tile = edge_dict.values().__iter__().__next__()[0]
# find_tiles(starting_tile, set())

