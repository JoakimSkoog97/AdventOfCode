def move_elements(towers, x, y, n):
    """
    Moves the last `n` elements from tower `x` to tower `y`, reversing the order of the elements in the process.

    :param towers: A dictionary representing the towers.
    :param x: The source tower number.
    :param y: The destination tower number.
    :param n: The number of elements to move.
    """
    # Get the last n elements from tower x
    elements = towers[x][-n:]

    # Reverse the order of the elements
    elements = reversed(elements)

    # Remove the elements from tower x
    towers[x] = towers[x][:-n]

    # Add the elements to the end of tower y
    towers[y].extend(elements)


def read_lines_from_file(filename):
    """
    Reads the lines from a file and returns them as a list of strings.

    :param filename: The name of the file to read.
    :return: A list of strings representing the lines from the file.
    """
    # Initialize the list of lines
    lines = []

    # Read the lines from the file
    with open(filename) as f:
        for line in f:
            # Remove the newline character from the line
            line = line.strip("\n")

            # Replace any remaining whitespace with underscores
            line = line.replace(" ", "_")

            # Add the line to the list
            lines.append(line)

    return lines


def create_towers_from_lines(lines):
    """
    Creates a towers dictionary from a list of strings.

    :param lines: A list of strings.
    :return: A towers dictionary.
    """
    # Initialize the towers dictionary
    towers = {}

    # Create the towers from the lines
    for i, line in enumerate(lines):
        # Split the line into elements
        elements = line.strip().split("_")

        # Add each element to the appropriate tower, stripping the brackets and whitespace
        for j, element in enumerate(elements):
            element = element.strip().strip("[]")
            if not element:
                continue

            tower_num = j + 1
            if tower_num not in towers:
                towers[tower_num] = []
            towers[tower_num].append(element)

    return towers


def replace_brackets_with_underscores(lines):
    """
    Replaces all brackets in the lines with underscores.

    :param lines: A list of strings.
    :return: A list of strings with brackets replaced by underscores.
    """
    # Initialize the list of modified lines
    new_lines = []

    # Replace all brackets with underscores in each line
    for line in lines:
        new_line = line.replace("[", "_").replace("]", "_")
        new_lines.append(new_line)

    return new_lines


def remove_underscore_indices(lines):
    """
    Removes any indices that contain only underscores from the lines.

    :param lines: A list of strings.
    :return: A list of strings with underscore-only indices removed.
    """
    # Initialize the list of modified lines
    new_lines = []

    # Transpose the lines to make it easier to work with each index
    transposed_lines = list(map(list, zip(*lines)))

    # Remove any indices that contain only underscores
    for indices in transposed_lines:
        if all(index == "_" for index in indices):
            continue

        new_lines.append("".join(indices))

    # Transpose the modified lines back to the original format
    new_lines = list(map(list, zip(*new_lines)))

    return new_lines


def create_towers_from_lists(lists):
    """
    Creates a towers dictionary from a list of lists.

    :param lists: A list of lists.
    :return: A towers dictionary.
    """
    # Initialize the towers dictionary
    towers = {}

    # Create the towers from the lists
    for i, indices in enumerate(lists):
        # Add each element to the appropriate tower
        for j, element in enumerate(indices):
            if not element:
                continue

            tower_num = j + 1
            if tower_num not in towers:
                towers[tower_num] = []
            towers[tower_num].append(element)

    return towers


def reverse_and_filter(d):
    """
    Reverses and filters the elements in the towers dictionary.

    :param d: The towers dictionary.
    :return: The towers dictionary with reversed and filtered elements.
    """
    for k, v in d.items():
        d[k] = [x for x in reversed(v) if x.isalpha()]
    return d


def get_instructions(filename):
    """
    Reads the instructions from a file and returns them as a list of lists.

    :param filename: The name of the file containing the instructions.
    :return: A list of lists of instructions, where each sublist contains the instructions for a single move.
    """
    # Read the file
    with open(filename, "r") as f:
        lines = f.readlines()

    # Extract the instructions from each line
    instructions = [[int(x) for x in line.strip().split() if x.isdigit()] for line in lines]

    return instructions


def apply_instructions(instructions, towers):
    """
    Applies a list of instructions to the towers.

    :param instructions: A list of lists of instructions, where each sublist contains the instructions for a single move.
    :param towers: The towers dictionary.
    """
    for instr in instructions:
        move_elements(towers, instr[1], instr[2], instr[0])


def get_last_elements(towers):
    """
    Gets the last element from each tower in the towers dictionary.

    :param towers: The towers dictionary.
    :return: A list of the last elements from each tower.
    """
    last_elements = []
    for _, tower in towers.items():
        last_elements.append(tower[-1])
    return last_elements

def concat_strings(strings):
    """
    Concatenates a list of strings.

    :param strings: A list of strings.
    :return: A concatenated string.
    """
    # Use the join method to concatenate the strings
    return ''.join(strings)

def main():
    # Read the instructions from the file
    instructions = get_instructions("instructions.txt")

    # Read the lines from the file
    lines = read_lines_from_file('tower.txt')

    # Replace the brackets with underscores
    lines = replace_brackets_with_underscores(lines)

    # Remove the underscore indices
    lines = remove_underscore_indices(lines)

    # Create the towers dictionary
    towers = create_towers_from_lists(lines)

    # Reverse and filter the towers
    towers = reverse_and_filter(towers)

    # Apply the instructions to the towers
    apply_instructions(instructions, towers)

    # Concatenate the last elements of the towers
    concatenated_string = concat_strings(get_last_elements(towers))

    print(concatenated_string)


if __name__ == "__main__":
    main()

