import re
from typing import Iterable, Tuple

def exec_mul(s: str) -> int:
    stripped = s[4:-1]
    a,b = tuple(map(int, stripped.split(",")))
    return a*b


def find_safe_ranges_2(s: str) -> Iterable[Tuple[int]]:
    dos = re.compile(r"do\(\)")
    donts = re.compile(r"don't\(\)")
    do_locs = [match.span()[0] for match in dos.finditer(s)]
    dont_locs = [match.span()[0] for match in donts.finditer(s)]
    print(do_locs, dont_locs)

    d = {v:"do" for v in do_locs}
    d.update({v:"dont" for v in dont_locs})
    # print(d)
    # print(do_locs, dont_locs)
    dd = {k:v for k,v in sorted(d.items(), key=lambda item: item[0])} # keys are locs
    dd.update({len(s)-1:"dont"})
    # print(dd)

    # ["do", "dont", "dont", "do", "do", "dont", "do", "dont"]
    # go from each do to the next dont
    prev = "do" # do() always at the start
    do = 0
    vs = []
    for k,v in dd.items():
        if v == "dont":
            if prev == "do":
                prev = v  # only change do to dont if the previous was a do
                vs.append((do, k))  # only add a stop if the previous was a start
        else: # v is "do"
            if prev == "dont":
                prev = v  # only change dont to do if the previous was a dont
                do = k
    return vs
        

if __name__ == "__main__":
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    mem = open("03.txt", "r").read()
    ranges = find_safe_ranges_2(mem)
    muls = [pattern.findall(mem, pos=a, endpos=b) for (a,b) in ranges]
    m = []
    for i in muls:
        m.extend(i)
    print(sum(exec_mul(mul) for mul in m))