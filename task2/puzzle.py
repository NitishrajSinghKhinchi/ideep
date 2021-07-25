def convert(num_rows,string,arr):
    """
    No validation provide on input Please valid
    input enter so this programme right output
    
    """
    rows = [[] for i in range(num_rows)]
    sindex=0
    lst=[]
    for i in range(1,num_rows+1):
        for j in range(1,i+1):
            if (i%3!=0):
                rows[i-1].append(string[sindex])
                if i == j:
                    rows[i-1].reverse()
                sindex +=1
            else:
                rows[i-1].append(string[sindex])
                sindex +=1
            if sindex == len(string):
                sindex = 0
    for l in arr:
        counts = rows[int(l[0])-1].count(l[1])
        lst.append(counts)
    return lst
 
if __name__ == '__main__':
    """No validation provide on input Please valid input enter so this programme right output"""
    print("Please enter correct input")
    num_rows = int(input("Enter number of rows triangle ="))
    string = input("Enter a string =")
    arr=[]
    query = int(input("Enter number for query ="))
    for _ in range(query):
        l1 = input("Enter row number and character with space seprated =").split()
        arr.append(l1)
    counts = convert(num_rows,string,arr)
    for n in counts:
        print(n)


    
    
