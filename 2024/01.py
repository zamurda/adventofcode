from typing import List, Tuple

left, right = [], []
with open("./01.txt", "r") as f:
    for line in f:
        l, r = line.strip().split("  ")
        left.append(int(l)); right.append(int(r))

left.sort(); right.sort()
assert (len(left) == len(right))


def calc_distance(arr1: List, arr2: List) -> int:  # for part 1
    sum_ = 0
    for i, j in zip(arr1, arr2):
        sum_ += abs(i-j)
    return sum_


def calculate_sim(l: int, right: List, idx_start: int) -> Tuple[int, int]:
    largest_visited = right[idx_start]
    if largest_visited > l:
        # case where it is impossible to have
        # any the same as l
        count = 0
        most_recent_id = idx_start
    else:
        # case where you have to start counting
        # (current position in right array is
        # less than current in left)
        count = 0
        j = 0 if idx_start == 0 else -1
        curr = largest_visited
        while curr <= l:
            if j > len(right) - idx_start - 1:
                # if you go out if index then break
                most_recent_id = len(right) - idx_start
                break
            curr = right[idx_start + j]
            if curr == l:
                count += 1
            j += 1  # not sure why this makes it work
        # when the loop breaks we know we have found
        # the next highest in the loop
        most_recent_id = idx_start + j
                
    return count, most_recent_id


def calc_total_similarity(left: List, right: List) -> int:
    # number of times each element of left appears in right
    # both right and left should be sorted
    sims = [0] * len(left)
    most_recent_id = 0
    for i, l in enumerate(left):
        sim = 0
        # for each element in left, start counting in right
        # check if current number in left is lower than that and if so,
        # skip ones in the left
        # until you get something which is >= most recent in right

        if most_recent_id <= len(right) - 1:
            sim, most_recent_id = calculate_sim(l, right, most_recent_id)
            sims[i] = sim * l
        else:
            break
    return sum(sims)


if __name__ == "__main__":
    print("The total distance is: ", calc_distance(left, right))  # part 1
    print("The total similarity score is: ", calc_total_similarity(left, right))  # part 2