def digitize(n):
    arr = []
    for char in str(n):
        arr.append(int(char)) 
    arr.reverse()  
    return arr