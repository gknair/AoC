import re
def part_one(filename: str) -> int:

    sum_nos=0
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]


    return sum_nos
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    
    return 0

def everyline(line:str, part_two=False) -> int:
    match=0
    sum_nos=0
    

    
    return sum_nos 

if __name__ == "__main__":
    input_path = "./AoC/day_5/example.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
