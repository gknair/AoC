import re
def part_one(filename: str) -> int:

    sum_nos=0
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    line = [everyline(line) for line in lines]

    return sum_nos
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    
    sum_nos=0
    return sum_nos

def everyline(line:str) -> int:
    sum_nos=0

    
    _, line = line.split(": ")
    winning_numbers, numbers = line.split(" | ")
    
    winning_numbers = winning_numbers.replace(" ",",")
    print(winning_numbers, "|", numbers)
    return sum_nos

if __name__ == "__main__":
    input_path = "./AoC/day_4/example.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
