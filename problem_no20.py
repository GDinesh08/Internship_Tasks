import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, m = map(int, data[:2])
    arr = data[2:n+2]
    A = set(data[n+2:n+2+m])
    B = set(data[n+2+m:])
    
    print(sum((i in A) - (i in B) for i in arr))

if __name__ == '__main__':
    main()S