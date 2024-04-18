from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    #TODO
    # Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum=0
    for i in even_int_list:
        sum+=i**2
    return sum

def main():
    int_list = [1,2,3,4,5,6,7,8,9,10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print("Output: "+output)
    if __name__ == "__main__":
        main()
