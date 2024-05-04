import subprocess

def convert_to_shellcode(asm_file):
    shellcode = ""
    try:
        output = subprocess.check_output(["objdump", "-d", asm_file])
        lines = output.decode().splitlines()
        for line in lines:
            # Check if the line contains assembly instruction
            if ":" in line:
                parts = line.split("\t")
                if len(parts) > 1:
                    opcodes = parts[1]
                    opcodes = opcodes.strip().split()
                    shellcode += "\\x" + "\\x".join(opcodes)
                else:
                    print("Unexpected line format:", line)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    return shellcode

asm_file = "bc.o"
shellcode = convert_to_shellcode(asm_file)
print(shellcode)
