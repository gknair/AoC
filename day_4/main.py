import re
def part_one(filename: str) -> int:

    sum_nos=0
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    line = [everyline(line) for line in lines]

    sum_nos = sum(line)    
    return sum_nos
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    
    line = [everyline(line, part_two=True) for line in lines]

    copy_deck = [1 for i in range(len(line))]
    i=0
    for match in line:
        j=1
        while j<=match:
            copy_deck[i+j]+=1*copy_deck[i] 
            j+=1
        i+=1
    sum_nos=sum(copy_deck)
    return sum_nos

def everyline(line:str, part_two=False) -> int:
    match=0
    sum_nos=0
    
    _, line = line.split(": ")
    winning_numbers, numbers = line.split(" | ")
    
    winning_numbers = [int(ele) for ele in winning_numbers.split()]
    numbers = [int(ele) for ele in numbers.split()]

    
    for number in numbers:
        if number in winning_numbers:
            match+=1

    if match>0 and not part_two:
        sum_nos = 2**(match-1)
    else:
        sum_nos=match
    return sum_nos 

if __name__ == "__main__":
    input_path = "./AoC/day_4/input.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
