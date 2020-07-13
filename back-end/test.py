def pow(n, m):
    result = 1
    for i in range(m):
        # result+=n
        for j in range(m):
            result+=n
            
    return result
        
if __name__ == "__main__":
    ex = 9
    print(pow(2,3))
