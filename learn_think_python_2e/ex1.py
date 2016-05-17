import sys as system

print(system.platform)


def print_lyrics ():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


print_lyrics()


def cat_twice (part1, part2):
    cat = part1 + part2
    print(cat)


line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)


# -----------

def right_justify (s):
    print(' ' * 69 + s)


right_justify('monty')
