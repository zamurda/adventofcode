
def check(arr) -> bool:
    # for part 1
    lb, ub = 1, 3
    if len(arr) <= 1:
        return True
    tone  = 1 if arr[1] - arr[0] > 0 else 0
    for i in range(1,len(arr)):
        if abs(arr[i] - arr[i-1]) < lb or abs(arr[i] - arr[i-1]) > ub: # if gap is out of bounds
            return False
        tmp = 1 if arr[i] - arr[i-1] > 0 else 0
        if i > 1:
            if tmp != tone: return False
        tone = tmp
    return True


def check_with_removal(arr) -> bool:
    # for part 2
    return any(check(arr[:i]+arr[i+1:]) for i in range(len(arr)))


global count
global ineligible
reps = []
with open("./02.txt", "r", newline="\n") as f:
    count = 0
    ineligible = []
    for i,line in enumerate(f):
        line = list(map(int, line.strip().split(" ")))
        reps.append(line)
        # print(line)
        if check_with_removal(line):
            # print(i)
            count += 1
            # print(count)
        else:
            ineligible.append(line)
print("Total eligible reports are :", count)
