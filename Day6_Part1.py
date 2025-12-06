import sys

def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.readlines()
        
    hw_grid = []
    for line in lines_raw:
        hw_grid.append(line.strip().split())
        
    #print(hw_grid)
    
    m = len(hw_grid)
    n = len(hw_grid[0])
    total = 0
    
    for i in range(0,n):
        if(hw_grid[m-1][i] == '+'):
            col_total = 0
            for j in range(0,m-1):
                col_total = col_total + int(hw_grid[j][i])
                #print(hw_grid[j][i])
        else:
            col_total = 1
            for j in range(0,m-1):
                col_total = col_total * int(hw_grid[j][i])
                #print(hw_grid[j][i])
        total = total + col_total
            
    print('Total is ' + str(total))
        
        
        
if __name__ == "__main__":
    main()