def ip_port_to_hex(ip_address, port):
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Convert each octet to hexadecimal and pad with zeros if necessary
    hex_octets = [hex(int(octet))[2:].zfill(2) for octet in octets]
    
    # Reverse the order of octets and concatenate them with '0x' prefix
    hex_ip = ''.join(hex_octets[::-1])
    
    # Convert port number to hexadecimal and pad with zeros if necessary
    hex_port = hex(port)[2:].zfill(4)
    
    # Reverse the order of port bytes and concatenate them with '0x' prefix
    hex_port = hex_port[2:] + hex_port[:2]
    
    # Combine IP and port hexadecimal representations
    hex_ip_port = '0x' + hex_port + hex_ip
    
    return hex_ip, hex_port

# Example usage
ip_address = input("Enter IP address (format: x.x.x.x): ")
port = int(input("Enter port number: "))
hex_ip, hex_port = ip_port_to_hex(ip_address, port)
print("Hexadecimal representation - IP:", hex_ip)
print("Hexadecimal representation - Port:", hex_port)
