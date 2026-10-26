from collections import Counter
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    num_shoes = int(input_data[0])
    shoe_sizes = [int(x) for x in input_data[1:num_shoes + 1]]
    
    inventory = Counter(shoe_sizes)
    
    num_customers = int(input_data[num_shoes + 1])
    
    total_earned = 0
    idx = num_shoes + 2
    
    for _ in range(num_customers):
        size = int(input_data[idx])
        price = int(input_data[idx + 1])
        idx += 2
        
        if inventory[size] > 0:
            total_earned += price
            inventory[size] -= 1
            
    print(total_earned)

if __name__ == '__main__':
    main()
