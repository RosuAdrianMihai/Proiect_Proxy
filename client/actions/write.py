def write_to_file():
    print("""
        Write the text line by line. When you want to stop writing, write 'stop' on a new line.
    """)

    lines = []

    while len(lines) == 0 or lines[-1] != "stop":
        line = input(f"Line {len(lines) + 1}: ")
        lines.append(line)

    return "\n".join(lines[:-1])