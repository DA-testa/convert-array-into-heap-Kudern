# python3


def sift_down(data, i, swaps):
    n = len(data)
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


def main():
  
    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))
  
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
  
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
  
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
