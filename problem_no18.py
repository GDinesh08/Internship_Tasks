if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command = input().split()
        method = command[0]
        arguments = command[1:]
        
        if method == "print":
            print(my_list)
        else:
            getattr(my_list, method)(*(map(int, arguments)))
