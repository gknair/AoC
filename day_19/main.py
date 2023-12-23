import re
from typing import Tuple
def part_one(filename: str) -> int:

    sum_nos=0
    rules, parts = parse(filename)
    rules = everyrule(rules)
    accepted = []
    status = "NA"
    for part in parts:
        while status != "A" or status != "R":
            

    return sum_nos
    
def part_two(filename: str) -> int:
    
    rules, parts = parse(filename)
    

    return 0

def parse(filename: str) -> Tuple:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
        index = lines.index('')
        rules = lines[:index]
        parts = lines[index+1:]
    return rules, parts

def everyrule(lines:list, part_two=False) -> dict:
    workflow = {}
    sum_nos=0
    for line in lines:
        workflow_name = re.finditer(r".*\{", line)
        workflow_name = line[0:workflow_name.__next__().end()-1]
        workflow[workflow_name] = re.findall(r"\{([^}]*)\}", line)
    return workflow 

if __name__ == "__main__":
    input_path = "./AoC/day_19/example.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
