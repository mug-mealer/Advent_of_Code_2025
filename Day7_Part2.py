import sys

def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.readlines()
    
    S_ind = lines_raw[0].find('S')
    t_grid = []
    for line in lines_raw:
        t_grid.append(list(line.strip()))
        
    #print(t_grid[2])
    t_grid[1][S_ind] = '|'
    split_ct = 0

    timelines = [[0 for _ in range(len(t_grid[0]))] for _ in range(len(t_grid))]

    timelines[1][S_ind] = 1
    
    #print(timelines)

    for i in range(2, len(t_grid)):
        for j in range(0, len(t_grid[i])):
            if (t_grid[i][j] == '^' and t_grid[i-1][j] == '|'):
                #print('Splitting!!')
                t_grid[i][j-1] = '|'
                t_grid[i][j+1] = '|'
                split_ct = split_ct + 1
                
                timelines[i][j-1] = timelines[i][j-1] + timelines[i-1][j]
                timelines[i][j+1] = timelines[i][j+1] + timelines[i-1][j]
            elif (t_grid[i-1][j] == '|'):
                t_grid[i][j] = '|'
                timelines[i][j] = timelines[i][j] + timelines[i-1][j]
                
    total_timelines = sum(timelines[len(t_grid)-1])

    print('Total number of splits is ' + str(split_ct))
    print('Total number of timelines is ' + str(total_timelines))
    
        
if __name__ == "__main__":
    main()
