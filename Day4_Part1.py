import sys

def main():
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        lines_raw = f.readlines()
    
    lines = []
    for line in lines_raw:
        lines.append(line.strip())
    
    num_rolls = 0
    
    
    for i, line in enumerate(lines):
        for j, roll in enumerate(line):
            #print('The character is :'+lines[i][j])
            m = len(lines)-1
            n = len(line)-1
            if(roll=='@'):
                if((i==0 or i==m) and (j==0 or j==n)):
                    num_rolls = num_rolls + 1
                    print('Suitable for forklift!')
                    print(str(i)+str(j))
                elif(i==0):
                    adj_rolls = ''
                    adj_rolls = adj_rolls + lines[0][j-1]
                    adj_rolls = adj_rolls + lines[0][j+1]
                    adj_rolls = adj_rolls + lines[1][j-1]
                    adj_rolls = adj_rolls + lines[1][j]
                    adj_rolls = adj_rolls + lines[1][j+1]
                    #print(adj_rolls)
                    #print(adj_rolls.count('@'))
                    if(adj_rolls.count('@') < 4):
                        num_rolls = num_rolls + 1
                        print('Suitable for forklift!')
                        print(str(i)+str(j))
                elif(j==0):
                    adj_rolls = ''
                    adj_rolls = adj_rolls + lines[i-1][0]
                    adj_rolls = adj_rolls + lines[i+1][0]
                    adj_rolls = adj_rolls + lines[i-1][1]
                    adj_rolls = adj_rolls + lines[i][1]
                    adj_rolls = adj_rolls + lines[i+1][1]
                    #print(adj_rolls)
                    #print(adj_rolls.count('@'))
                    if(adj_rolls.count('@') < 4):
                        num_rolls = num_rolls + 1
                        print('Suitable for forklift!')
                        print(str(i)+str(j))
                elif(i==m):
                    adj_rolls = ''
                    adj_rolls = adj_rolls + lines[m][j-1]
                    adj_rolls = adj_rolls + lines[m][j+1]
                    adj_rolls = adj_rolls + lines[m-1][j-1]
                    adj_rolls = adj_rolls + lines[m-1][j]
                    adj_rolls = adj_rolls + lines[m-1][j+1]
                    #print(adj_rolls)
                    #print(adj_rolls.count('@'))
                    if(adj_rolls.count('@') < 4):
                        num_rolls = num_rolls + 1
                        print('Suitable for forklift!')
                        print(str(i)+str(j))
                elif(j==n):
                    adj_rolls = ''
                    adj_rolls = adj_rolls + lines[i-1][n]
                    adj_rolls = adj_rolls + lines[i+1][n]
                    adj_rolls = adj_rolls + lines[i-1][n-1]
                    adj_rolls = adj_rolls + lines[i][n-1]
                    adj_rolls = adj_rolls + lines[i+1][n-1]
                    #print(adj_rolls)
                    #print(adj_rolls.count('@'))
                    if(adj_rolls.count('@') < 4):
                        num_rolls = num_rolls + 1
                        print('Suitable for forklift!')
                        print(str(i)+str(j))
                else:
                    adj_rolls = ''
                    adj_rolls = adj_rolls + lines[i-1][j]
                    adj_rolls = adj_rolls + lines[i+1][j]
                    adj_rolls = adj_rolls + lines[i-1][j-1]
                    adj_rolls = adj_rolls + lines[i][j-1]
                    adj_rolls = adj_rolls + lines[i+1][j-1]
                    adj_rolls = adj_rolls + lines[i-1][j+1]
                    adj_rolls = adj_rolls + lines[i+1][j+1]
                    adj_rolls = adj_rolls + lines[i][j+1]
                    if(adj_rolls.count('@') < 4):
                        num_rolls = num_rolls + 1
                        print('Suitable for forklift!')
                        print(str(i)+str(j))
                        
    print('Number of rolls:' + str(num_rolls))
    print('Grid size is '+ str(m+1) + 'x' + str(n+1))
    #print(lines[0][3])
        
        
if __name__ == "__main__":
    main()