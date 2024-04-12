This is an interpreter for the esoteric language Detour (https://esolangs.org/wiki/Detour). Requires Python to use.
It reads code from a file called "detour.txt" in the same folder as Python.
Indentations are represented with two spaces per indent level.
In order for the code to parse properly, there needs to be a newline at the end of the file. (If you get the error pointer_dict[int(cells[0])] = int(cells[1]) IndexError: list index out of range, and your code is written correctly, that's probably what you did wrong.)
