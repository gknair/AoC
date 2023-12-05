def part_one(filename: str) -> int:


    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        
        sum+= 0
   
    return sum
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        
        sum+= 1
   
    return sum

if __name__ == "__main__":
    input_path = "./AoC/day_3/example.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
