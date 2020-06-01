def test_f(*args):
    print(*args)
    
    
def test_call_back(f, *args):
    f(args)
    
if __name__ == "__main__":
    test_call_back(test_f, 1, 2, 3)