import sys

def superset_range(ranges):
    super_ranges = []
    super_ranges.append(ranges[0])
    ranges.pop(0)
    for r in ranges:
        if(r[0]>super_ranges[len(super_ranges)-1][1]):
            super_ranges.append(r)
        elif(r[1]>super_ranges[len(super_ranges)-1][1]):
            super_ranges[len(super_ranges)-1][1] = r[1]
    
    return super_ranges

def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.readlines()
        
    ranges = []
    for line in lines_raw:
        if(line.strip() == ''):
            break

        range_item = [int(line.strip().split('-')[0]),int(line.strip().split('-')[1])]
        ranges.append(range_item)

            
    #print(sorted(ranges))
    
    ranges = sorted(ranges)
    
    fresh_ct = 0
    
    sranges = superset_range(ranges)
    
    for s in sranges:
        slen = s[1] - s[0] + 1
        fresh_ct = fresh_ct + slen
        print(slen)
        
    print(len(sranges))
    print('Total fresh count is '+str(fresh_ct))
    
    
if __name__ == "__main__":
    main()