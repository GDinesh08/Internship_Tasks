if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_scores = sorted(list(set(arr)))
    print(sorted_scores[-2])
