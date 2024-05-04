shellcode = b""

encoded = bytearray()

for byte in shellcode:
    encoded.append(byte ^ 0xAA)

for byte in encoded:
    print(f"0x{byte:02x},", end="")
print()
print(len(encoded))
