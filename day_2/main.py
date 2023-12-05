import operator
from functools import reduce


def part_one(filename: str) -> int:

    constraints = {"red": 12,
                   "green": 13,
                   "blue": 14,
                   }

    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        
        game_id, game_sets = line.split(": ")
        game_id = game_id.replace("Game ", "")
        game_sets= game_sets.replace("; ",",")
        game_sets= game_sets.replace(", ",",").split(",")
        exclude = 0
        for sets in game_sets:
            number, color = sets.split(" ")
            if int(number) > constraints[color]:
                exclude = 1
        if exclude!=1:
            sum+= int(game_id)
   
    return sum
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        
        game_id, game_sets = line.split(": ")
        game_id = game_id.replace("Game ", "")
        game_sets= game_sets.replace("; ",",")
        game_sets= game_sets.replace(", ",",").split(",")
        
        base = {"red":0, "blue":0, "green":0}
        for sets in game_sets:
            number, color = sets.split(" ")
            if int(number) > base[color]:
                base[color] = int(number)
        
        values = list(base.values())
        sum+= reduce(operator.mul,values)
   
    return sum

if __name__ == "__main__":
    input_path = "./AoC/day_2/input.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
