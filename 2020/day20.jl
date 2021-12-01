using ResumableFunctions

@enum Direction begin
    NORTH
    EAST
    SOUTH
    WEST
end 

const SideType = Tuple{Vararg{Bool, 10}}

struct TileConfig
    flip_x::Bool
    flip_y::Bool
    rotate_count::Int
    tile_id::Int
    north_side::SideType
    south_side::SideType
    west_side::SideType
    east_side::SideType
end

const EdgeDictType = Dict{Tuple{Direction, SideType}, Array{TileConfig}}

function makeTile(id::Int, tile::Array{String})::TileConfig
    north_side = Tuple([char == '#' for char=tile[1]])
    south_side = Tuple([char == '#' for char=tile[end]])
    west_side = Tuple([line[1] == '#' for line=tile])
    east_side = Tuple([line[end] == '#' for line=tile])
    TileConfig(false, false, 0, id, north_side, south_side, west_side, east_side)
end

function transformTile(config::TileConfig, flip_x, flip_y, rotate_count)::TileConfig
    id, north, south, west, east = config.tile_id, config.north_side, config.south_side, config.west_side, config.east_side

    if flip_y
        west, east = east, west
        north = reverse(north)
        south = reverse(south)
    end

    if flip_x
        north, south = south, north
        west = reverse(west)
        east = reverse(east)
    end

    for i = 1:rotate_count
        north, east, south, west = east, reverse(south), west, reverse(north)
    end

    TileConfig(flip_x, flip_y, rotate_count, id, north, south, west, east)
end

function addOrAppend!(dict::EdgeDictType, key, value)
    if haskey(edge_dict, key)
        push!(edge_dict[key], value)
    else
        edge_dict[key] = [value]
    end
    return nothing
end

file = open("input.txt", "r")
lines = readlines(file)
close(file)

tiles = NamedTuple{(:id, :tile), Tuple{Int, Array{String}}}[]

for i in range(1, length(lines) - 1, step=12)
    push!(tiles, (id=parse(Int, lines[i][5:end-1]), tile=lines[i+1:i+10]))
end


edge_dict = EdgeDictType()
all_config = TileConfig[]

for (id, tile) in tiles
    tile = makeTile(id, tile)
    for (flip_x, flip_y) in Iterators.product((true, false), (true, false))
        for r = 0:2
            tile = transformTile(tile, flip_x, flip_y, r)
            push!(all_config, tile)
            addOrAppend!(edge_dict, (NORTH, tile.north_side), tile)
            addOrAppend!(edge_dict, (SOUTH, tile.south_side), tile)
            addOrAppend!(edge_dict, (WEST, tile.west_side), tile)
            addOrAppend!(edge_dict, (EAST, tile.east_side), tile)
        end
    end
end

@show length(edge_dict)

@resumable function diagonal_iter(n::Int)::Tuple{Int, Int}
    for i in range(n*2 - 1, 0, step=-1)
        for x in range(n-1, 0, step=-1)
            y = i - x
            if y >= 0 && y < n
                @yield (x + 1, y + 1)
            end
        end
    end
end

function find_tiles(start_config::TileConfig, edge_dict::EdgeDictType, diagonals::Array{Tuple{Int, Int}})
    used_tile_ids = Set{Int}([start_config.tile_id])
    options_not_taken = Tuple{Int, Array{TileConfig}}[]
    tile_grid = Array{Union{TileConfig, Nothing}}(nothing, 12, 12)
    tile_grid[12, 12] = start_config
    diagonal_index = 2
    while diagonal_index <= length(diagonals)
        x, y = diagonals[diagonal_index]
        if y == 12 || (y == 1 && x != 12 && x != 1)
            available = [tile for tile = get(edge_dict, (EAST, tile_grid[x+1, y].west_side), []) if !(tile.tile_id in used_tile_ids)]
        elseif x == 12 || (x == 1 && y != 12 && y != 1)
            available = [tile for tile = get(edge_dict, (NORTH, tile_grid[x, y+1].south_side), []) if !(tile.tile_id in used_tile_ids)]
        else
            available_east = Set{TileConfig}(tile for tile = get(edge_dict, (EAST, tile_grid[x+1, y].west_side), []) if !(tile.tile_id in used_tile_ids))
            available = [tile for tile = get(edge_dict, (NORTH, tile_grid[x, y+1].south_side), []) if tile in available_east && !(tile.tile_id in used_tile_ids)]
        end
        # backtrack
        if length(available) == 0
            while true
                if diagonal_index <= 2
                    return nothing
                end
                oldx, oldy = diagonals[diagonal_index - 1]
                wrong_pick, other_opts = pop!(options_not_taken)
                delete!(used_tile_ids, wrong_pick)
                tile_grid[oldx, oldy] = nothing
                if length(other_opts) > 0
                    new_pick = pop!(other_opts)
                    push!(used_tile_ids, new_pick.tile_id)
                    tile_grid[oldx, oldy] = new_pick
                    push!(options_not_taken, (new_pick.tile_id, other_opts))
                else
                    diagonal_index -= 1
                end
            end
        else
            pick_tile = pop!(available)
            tile_grid[x, y] = pick_tile
            push!(options_not_taken, (pick_tile.tile_id, available))
            push!(used_tile_ids, pick_tile.tile_id)
            diagonal_index += 1
        end
    end
    tile_grid
end

diagonals = collect(diagonal_iter(12))

for (i, tile_config) in enumerate(all_config)
    tile_grid = find_tiles(tile_config, edge_dict, diagonals)
    if tile_grid !== nothing
        print(tile_grid[1,1].tile_id * tile_grid[12,1].tile_id * tile_grid[1,12].tile_id * tile_grid[12,12].tile_id)
        exit(0)
    end
end
