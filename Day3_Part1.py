import sys

def find_max(batt_list):
    highest = batt_list[0]
    h_index = 0
    for index, i in enumerate(batt_list):
        if i>highest:
            highest = i
            h_index = index
    
    return highest,h_index
    
def main():
    path = sys.argv[1]
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except OSError as e:
        print(f"Error opening file: {e}")
        sys.exit(1)
        
    total_jolt = 0
    
    for line in lines:
        line_str = line.strip()
        line_int = [int(digit) for digit in line_str]
        max_batt, max_index = find_max(line_int[:int(len(line_int)-1)])
        second_batt, second_index = find_max(line_int[int(max_index+1):])
        
        joltage = int( str(max_batt) + str(second_batt) )
        total_jolt = total_jolt + joltage
        
        print(line)
        print('Joltage is ' + str(joltage))
    
    print('Total sum of joltage is ' + str(total_jolt))
    
if __name__ == "__main__":
    main()
            