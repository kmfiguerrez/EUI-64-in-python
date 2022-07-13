
import re

class Mac:
    def __init__(self, user_mac_input) -> None:
        self.mac_input = user_mac_input


    def check_format(self):
        """
        Return value: bool | list

        This function will return the mac address in an array format if the user input is valid.
        Otherwise will return false.
        This function use Regular Expression to check user input.        
        Mac address is a 12 hex digits.
        \d means digit 0 to 9.
        A-F means A to F.
        {2} will match two character from the class [\dA-F].        
        ^ at the beginning and $ at the end in the pattern means that the regex pattern must matched exactly.
        ? matches the previous token between zero and one times.
        re.compile method will return regex(Pattern) object. Regex object has search() method.
        search() method returns match object. Match object has group() method.
        group() method returns the part of the string where there was a match(first occurence) 
        """

        # Part one.
        # In this part we set acceptable mac address format.
        # Four types of mac address format:
        # Hyphen notation: B4-2E-99-F1-48-5A
        # longer pattern: ^[\dA-F]{2}-[\dA-F]{2}-[\dA-F]{2}-[\dA-F]{2}-[\dA-F]{2}-[\dA-F]{2}$
        format1 =  re.compile(r"^([\da-fA-F]{2}-?){6}$")
        # Colon notation: B4:2E:99:F1:48:5A
        # longer pattern: ^[\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2}:[\dA-F]{2}$
        format2 = re.compile(r"^([\da-fA-F]{2}:?){6}$")
        # Colon notation that usually use on networking devices like switches and router: B42E:99F1:485A
        # longer pattern: ^[\dA-F]{4}:[\dA-F]{4}:[\dA-F]{4}$
        format3 = re.compile(r"^([\da-fA-F]{4}:?){3}$")
        # Just hex digits notation: B42E99F1485A
        format4 = re.compile(r"^[\da-fA-F]{12}$")

        formats = [format1, format2, format3, format4] # Will check user input against these formats.
        selected_format_index = -1 #  Will be use to select matched format. Used in part two and four.
        error = 0 # Used in part three.
        mo = None # mo means match object. Used in part two and four.
        mac_address = "" # Will be use to store the mac address that the function will return.

        # Part two.
        # Will check the the user input if it meets any of the format.
        for format in formats:
            selected_format_index += 1
            if format.search(self.mac_input) == None:
                error += 1
            else:
                # If found break the loop immediately.
                # Meaning search method did not return None.
                mo = format.search(self.mac_input)
                break
        
        # Part three.
        # If error equals 4 then it means that the input mac address did not meet any of the format.
        if error == 4:
            print("Invalid format!")
            return False

        # Part four.
        # If there's a match.
        # If the selected format is any of the format1, format2, and format3, it will be parsed into format4 format which is a single string. 
        if selected_format_index == 0:
            # Turned into a list of groups of two hex digit. Then join each group into a single string.
            mac_address = ''.join(mo.group().split('-'))        
        elif selected_format_index == 1:
            # Turned into a list of groups of two hex digit. Then join each group into a single string.
            mac_address = ''.join(mo.group().split(':'))
        elif selected_format_index == 2:
            # Turned into a list of groups of two hex digit. Then join each group into a single string.
            mac_address = ''.join(mo.group().split(':'))
        # If format4 is used which is at index 3, then just used it.
        elif selected_format_index == 3:
            mac_address = mo.group()

        # Finally.
        # This method will the mac_adress in a list format.
        return list(mac_address) 
    

    def eui_64(self) -> str:
        """
        Return value: str

        This function will generate the interface ID(Host part) using the eui-64 method.
        This function relies on the output of check_format method.
        """

        seven_bit_conversion = {'0':'2', '1':'3', '2':'0', '3':'1', '4':'6', '5':'7','6':'4', # This let us avoid working with binaries.
        '7':'5', '8':'A', '9':'B', 'a':'8', 'b':'9', 'c':'E', 'd':'F', 'e':'C', 'f':'D'} 
        mac_address = "" # an array of hex digits. Used in part one, two
        interface_ID = "" # Will be return by the function.
        middle_index = 0 # Use in part two.
        column_to_add = 3; # Use in part four.
        hex_count = 0; # Use in part four.  

        # Part one.
        # Check if user mac address input is valid.
        if self.check_format() == False:
            return False # Will not proceed.
        # If valid then set the output to mac_address.
        mac_address = self.check_format()

        # Part two.
        # Insert FFEE in the middle of the mac address.
        middle_index = int(len(mac_address)/2)
        mac_address.insert(middle_index, "E")
        mac_address.insert(middle_index, "F")
        mac_address.insert(middle_index, "F")
        mac_address.insert(middle_index, "F")

        # Part three.
        # To convert(flip) 7 bit in the first group of the interface ID. 
        for key in seven_bit_conversion: # Iterate over the keys of the dict seven_bit_conversion.
            if mac_address[1] == key:    # The seven bit is located in the second hex digit: mac_address[1].
                mac_address[1] = seven_bit_conversion[key] # Change the second hex digit.
                break    
        
        # Part four.
        # Construct the interface ID. Add : every four hex digits.
        for char in mac_address:
            if hex_count == 4 and column_to_add != 0:
                interface_ID += ":"
                column_to_add -= 1
                hex_count = 0 # Reset every four count.
            interface_ID += char
            hex_count += 1

        # Finally.
        # Return the interface ID.
        return interface_ID.upper()