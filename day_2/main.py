import re

def part_one(filename: str) -> int:
    cum_sum = 0
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    every_line_sum = [every_line(line) for line in lines ]
    return sum(every_line_sum)
    

def part_two(filename: str) -> int:
    cum_sum = 0
    with open(filename, encoding="utf8") as f:
        lines = [line.strip() for line in f.readlines()]

    # lines = [   'two1nine',
    #         'eightwothree',
    #         'abcone2threexyz',
    #         'xtwone3four',
    #         '4nineeightseven2',
    #         'zoneight234',
    #         '7pqrstsixteen',
    #         ]
    every_line_sum = [every_line(line, part_two=True) for line in lines ]
    with open('output.txt', "w") as f:
        
        for i in every_line_sum:
            f.write(str(i)+"\n")

    

    return sum(every_line_sum)    
    return 0

def every_line(line: str, part_two=False) -> int:
    sum=0
    if part_two:
        word_to_number = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
        # Add more mappings as needed
        }

    # Use a regular expression to  and rfindeplace words with numbers
        
        line_list = re.findall(r'{}'.format("|".join(word_to_number.keys()) + "|[0-9]"), line)

        line_list = [word_to_number[e] if e in word_to_number.keys() else e for e in line_list]

        sum+= 10*int(line_list[0]) + int(line_list[-1])
        return sum

    numbers = [str(i) for i in range(1,10)]
    
    for i in line:
        if i in numbers:
            sum+=int(i)*10
            set=i
            break
    
    for j in line[::-1]:
        if j in numbers:
            sum+=int(j)
            break        
    return sum


if __name__ == "__main__":
    input_path = "./AoC/day_2/input.txt"
    print("---Part One---")
    print(part_one(input_path))
    print("---Part Two---")
    print(part_two(input_path))
