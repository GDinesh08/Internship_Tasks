import sys

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    n = int(input_data[0].strip())
    stamps = set()
    
    for i in range(1, n + 1):
        if i < len(input_data):
            stamps.add(input_data[i].strip())
            
    print(len(stamps))

if __name__ == '__main__':
    main()