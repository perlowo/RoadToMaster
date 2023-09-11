def interpret(command: str) -> str:
    result = []
    i = 0

    while i < len(command):
        if command[i] == 'G':
            result.append('G')
            i += 1
        elif command[i:i+2] == '()':
            result.append('o')
            i += 2
        elif command[i:i+4] == '(al)':
            result.append('al')
            i += 4
        else:
            # Handle unexpected characters
            i += 1

    return ''.join(result)

# Example usage:
command1 = "G()(al)"
print(interpret(command1))  # Output: "Goal"

command2 = "G()()()()(al)"
print(interpret(command2))  # Output: "Gooooal"

command3 = "(al)G(al)()()G"
print(interpret(command3))  # Output: "alGalooG"