def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),
        [],
        []
    ]

    result = []

    def record():
        result.append(
            f"{rods[0]} {rods[1]} {rods[2]}"
        )

    def move(disks, source, target, auxiliary):
        if disks == 0:
            return

        # Move n-1 disks to auxiliary rod
        move(disks - 1, source, auxiliary, target)

        # Move the largest disk
        disk = rods[source].pop()
        rods[target].append(disk)

        record()

        # Move n-1 disks to target rod
        move(disks - 1, auxiliary, target, source)

    # Starting arrangement
    record()

    # Solve the puzzle
    move(n, 0, 2, 1)

    return "\n".join(result)