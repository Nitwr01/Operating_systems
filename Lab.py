page_table = {
    0: {"frame": 2, "valid": True},
    1: {"frame": 0, "valid": True},
    2: {"frame": 3, "valid": True},
    3: {"frame": None, "valid": False}
}

page_size = 1024

while True:
    user_input = input("Enter virtual address (enter 'q' to quit): ").strip()
    
    if user_input.lower() == 'q':
        print("Exiting program...")
        break
        
    try:
        address = int(user_input)
    except ValueError:
        print("Error: Please enter a number or 'q'.")
        continue
        
    if address < 0:
        print("Error: Negative addresses are not allowed.")
        continue
    elif address > 4095:
        print("Error: Address must be between 0 and 4095.")
        continue
        
    vpn = address // page_size
    offset = address % page_size
    
    print(f"VPN: {vpn}, Offset: {offset}")
    
    page_info = page_table.get(vpn)
    
    if page_info and page_info["valid"]:
        frame = page_info["frame"]
        physical_address = (frame * page_size) + offset
        print(f"Physical frame: {frame}")
        print(f"Physical address: {physical_address}")
    else:
        print("PAGE FAULT")
    
    print("-" * 30)