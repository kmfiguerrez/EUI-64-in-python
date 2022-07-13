from ipv6 import IPv6
from mac import Mac

    
is_entering = True
while is_entering:

    ipv6_address = input("Enter an IPv6 Address: ")
    user_ipv6 = IPv6(ipv6_address.strip())
    mac_address = input("Enter an MAC Address: ")
    user_mac = Mac(mac_address.strip())

    # Check user inputs first.
    if user_ipv6.check_format() == False and user_mac.check_format() == False:
        print("Please enter a valid ipv6 address")
        print("Please enter a valid mac address")
        decision = input("Wanna enter again?[Y/N] ")
        if decision != "y":
            is_entering = False
        continue
    elif user_ipv6.check_format() == False:
        print("Please enter a valid ipv6 address")
        decision = input("Wanna enter again?[Y/N] ")
        if decision != "y":
            is_entering = False
        continue
    elif user_mac.check_format() == False:
        print("Please enter a valid mac address")
        decision = input("Wanna enter again?[Y/N] ")
        if decision != "y":
            is_entering = False
        continue

    # If valid.
    print(f"Prefix value: {user_ipv6.get_prefix_value()}")
    print(f"Interface ID: {user_mac.eui_64()}")
    print(f"New IPv6 Address: {user_ipv6.get_prefix_value()}:{user_mac.eui_64()}")

    decision = input("Wanna enter again?[Y/N] ")
    if decision != "y":
        is_entering = False
    
    

    

