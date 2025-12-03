import sys

def find_max(batt_list,max_index,j):
    highest = batt_list[max_index+1]
    h_index = max_index+1
    i = h_index
    
    while(i<(len(batt_list) - j)):
        if batt_list[i] > highest:
            highest = batt_list[i]
            h_index = i
        i = i + 1
    
    return highest,h_index
    
def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    total_jolt = 0
    
    
    for line in lines:
        line_str = line.strip()
        print(line_str)
        line_int = [int(digit) for digit in line_str]
        mi = -1
        j = 11
        max_batt = []
        while(j>=0):
            print(line_int[int(mi+1):int(len(line_int)-j)])
            #mb, mi = find_max(line_int[int(mi+1):int(len(line_int)-j)])
            mb, mi = find_max(line_int,mi,j)
            print(mb)
            print(mi)
            max_batt.append(mb)
            j = j - 1
        
        joltage_str = ''
        for digit in max_batt:
            joltage_str = joltage_str + str(digit)
        
        total_jolt = total_jolt + int(joltage_str)
        
        
        print('Joltage is ' + joltage_str)
    
    print('Total sum of joltage is ' + str(total_jolt))
    
if __name__ == "__main__":
    main()
            