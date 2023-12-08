import re
def part_one(filename: str) -> int:


    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    MaxX = len(lines[0])
    MaxY = len(lines)
    sum_nos = 0
    y=0
    special_char =[]
    for line in lines:
        x=0
        for ch in line:
            if ch in "0123456789.":
                pass
            else:
                special_char.append((x,y))    
            x+=1
        y+=1

    parts = []
    y=0    
    for line in lines:
       for match in re.finditer(r"\b([0-9]+)", line):
           
           start=match.start()
           end=match.end()
           part_add= False
           while start<end:
               neighbours = [(start-1,y), 
                             (start,y-1),  
                             (start+1,y), 
                             (start, y+1),
                             (start+1,y+1),
                             (start-1,y-1),
                             (start+1,y-1),
                             (start-1,y+1)
               ]
               for neigbor in neighbours:
                   if neigbor in special_char:
                    part_add=True
               start+=1
           if part_add:
            parts.append(int(match.group())) 
       y+=1       
    print(parts)
    sum_nos = sum(parts) 
    return sum_nos
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        
        sum+= 1
   
    return sum

if __name__ == "__main__":
    input_path = "./AoC/day_3/input.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
