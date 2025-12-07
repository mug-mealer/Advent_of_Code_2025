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
    for i in range(2,len(t_grid)):
        for j in range(0,len(t_grid[i])):
            if(t_grid[i][j] == '^' and t_grid[i-1][j] == '|'):
                print('Splitting!!')
                t_grid[i][j-1] = '|'
                t_grid[i][j+1] = '|'
                split_ct = split_ct + 1
            elif(t_grid[i-1][j] == '|'):
                t_grid[i][j] = '|'
                
    print('Total number of splits is ' + str(split_ct))
    #print(t_grid)
        
if __name__ == "__main__":
    main()