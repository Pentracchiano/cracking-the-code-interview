# 8.6 - In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
# constraints:
# (1) Only one disk can be moved at a time.
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks.

Tower = list[int]
Towers = tuple[Tower, Tower, Tower]
Moves = list[str]


def move_disks(n: int, source: Tower, buffer: Tower, destination: Tower, result: Moves, towers: Towers) -> None:
    if n == 0:
        return

    move_disks(n - 1, source, destination, buffer, result, towers)
    move_top(source, destination)
    result.append(snapshot(towers))
    move_disks(n - 1, buffer, source, destination, result, towers)


def move_top(source: Tower, destination: Tower) -> None:
    destination.append(source.pop())


def snapshot(towers: Towers) -> str:
    return str(towers)


def towers_of_hanoi(disks: int) -> Moves:
    towers = Tower(reversed(range(disks))), Tower(), Tower()
    result = [snapshot(towers)]
    move_disks(disks, towers[0], towers[1], towers[2], result, towers)
    return result


def test_towers_of_hanoi():
    disks = 3
    result = towers_of_hanoi(disks)
    print()
    print("Disks: ", disks)
    print("Moves: ", len(result) - 1)
    print(*result, sep='\n')
