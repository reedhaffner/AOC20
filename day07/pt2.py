import re

with open("input.txt") as file:
    lines = re.findall('(.+) bags? contain (.*)\.', file.read())

bags = {a:
        {n: int(q) for q, n in re.findall(
            '\s*(\d+) (.*?) bags?', b)}
        for a, b in lines
        }
parents = {a: {k for k, v in bags.items() if a in v} for a in bags}


def rcount(bag): return 1 + sum(q*rcount(n)
                                for n, q in bags.get(bag, {}).items())


print(rcount('shiny gold')-1)
