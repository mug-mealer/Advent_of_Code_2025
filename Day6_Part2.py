import sys

def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.readlines()
        
    hw_grid = []
    for line in lines_raw:
        hw_grid.append(line.strip('\n'))
        #print(line.strip('\n') + 'End')
    #print(hw_grid)
    #print(hw_grid[1][8])
    
    m = len(hw_grid)
    n = len(hw_grid[m-1])
    total = 0
    prev_op = n
    for i in range(n-1,-1,-1):
        if(hw_grid[m-1][i] == '+'):
            #stmt
            col_total = 0
            for k in range(i,prev_op):
                num_str = ''
                for l in range(0,m-1):
                    num_str = num_str + hw_grid[l][k]
                print(num_str)
                col_total = col_total + int(num_str)
            total = total + col_total
            prev_op = i-1
            print(' ')
        elif(hw_grid[m-1][i] == '*'):
            #stmt
            col_total = 1
            for k in range(i,prev_op):
                num_str = ''
                for l in range(0,m-1):
                    num_str = num_str + hw_grid[l][k]
                print(num_str)
                col_total = col_total * int(num_str)
            total = total + col_total
            prev_op = i-1
            print(' ')

            
    print('Total is ' + str(total))
       
        
        
if __name__ == "__main__":
    main()