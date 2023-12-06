def part_one(filename: str) -> int:


    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    MaxX = len(lines[0])
    MaxY = len(lines)
    sum = 0
    x=0
    special_char =[]
    for line in lines:
        y=0
        for ch in line:
            if ch in "123456789.":
                pass
            else:
                special_char.append((x,y))    
            y+=1
        x+=1
        
        sum+= 0
    print(special_char)
    return sum
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        
        sum+= 1
   
    return sum

if __name__ == "__main__":
    input_path = "/Users/uraval/Documents/GitHub/AoC/day_3/example.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
