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
    sum_nos = sum(parts) 
    return sum_nos
    
def part_two(filename: str) -> int:
    
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]
    
    sum_nos = 0
    y=0
    special_char =[]
    neighbor_specials = []
    parts = []
    for line in lines:
        x=0
        for ch in line:
            if ch in "*":
                special_char.append((x,y))    
            x+=1
        y+=1
    y=0
    for line in lines:
       for match in re.finditer(r"\b([0-9]+)", line):
           
           start=match.start()
           end=match.end()
           part_add= False
           neighbor_special = ''
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
                    neighbor_special =neigbor
               start+=1
           if part_add:
            parts.append(int(match.group()))
            neighbor_specials.append({neighbor_special:int(match.group())})
       y+=1       
    
    
    for special in special_char:
        x=1
        gear_ratio=0
        for gear in neighbor_specials:
            if list(gear.keys())[0]==special:
                x*=gear[special]
                gear_ratio+=1
        if gear_ratio>1:
            sum_nos+=x
    return sum_nos

if __name__ == "__main__":
    input_path = "./AoC/day_3/input.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
