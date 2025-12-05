import sys

def search_ranges(ranges, ing_id):
    start = 0
    end = len(ranges)-1
    
    while start<=end:
        mid = (start+end)//2
        
        if(ing_id<ranges[mid][0]):
            end = mid - 1
        elif(ing_id<=ranges[mid][1]):
            return ranges[mid]
        else:
            start = mid + 1
    
    return False

def brute_force_ranges(ranges, ing_id):
    for r in ranges:
        if(ing_id>=r[0] and ing_id<=r[1]):
            return r
    
    return False

def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.readlines()
        
    ranges = []
    range_flag = True
    ing_ids = []
    for line in lines_raw:
        if(line.strip() == ''):
            range_flag = False
            continue
        
        if(range_flag):
            range_tuple = (int(line.strip().split('-')[0]),int(line.strip().split('-')[1]))
            ranges.append(range_tuple)
        else:
            ing_ids.append(int(line.strip()))
            
    print(len(sorted(ranges)))
    print(len(ing_ids))
    
    ranges = sorted(ranges)
    
    fresh_ct = 0
    
    for i in ing_ids:
        #found_range = search_ranges(ranges, i)
        found_range = brute_force_ranges(ranges, i)
        if(found_range):
            print(str(i) + ' is found in ' + str(found_range[0]) + '-' + str(found_range[1]))
            fresh_ct = fresh_ct + 1
        
    print('Total fresh count is '+str(fresh_ct))
    
    
if __name__ == "__main__":
    main()