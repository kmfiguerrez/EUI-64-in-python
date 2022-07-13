# I added a comment
class IPv6:
    def __init__(self, user_ipv6_input) -> None:
        self.ipv6_input = user_ipv6_input # A string.
        self.prefix_length = ""
        self.ipv6_input_no_PL = "" # Will be use by abbreviated method.
        

    
    def check_format(self) -> bool:
        """
        Return value: Boolean.

        This method will check user ipv6 input. The checking is broken into parts.
        Each checking must be met in order to proceed otherwise will return false.
        Returns True if user input passes all checkings.
        A segment means a group of four hex digits.
        """

        ipv6_char = [':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']; # Characters used in ipv6.
        colon_count = 0; # To be use in part five, six and eigth checking.
        double_colon_count = 0; # To be use in part six checking.
        non_zeros_quartet_count = 0; # To be use in part eigth checking.   
        ipv6_input_no_PL = self.ipv6_input # In here it is expected that the prefix length is not included. Used in all parts of checking. PL means Prefix Length. 
        
        
        # Part one.
        # If the prefix length is included it will be taken out and set the remaining string to ipv6_input_no_PL to be tested.
        # Then set this.prefix_length.
        # Then proceed to the next checking.        
        if "/" in self.ipv6_input:
            prefix_length_index = self.ipv6_input.index("/")
            self.prefix_length = self.ipv6_input[prefix_length_index:] # Set self.prefix_length.
            self.ipv6_input_no_PL = self.ipv6_input[0:prefix_length_index] # Re-initialized self.ipv6_input_no_PL
            ipv6_input_no_PL = self.ipv6_input[0:prefix_length_index] # Re-initialized the ipv6_input_no_PL
            prefix_number = 0
            
            # Get the number part of the prefix length and test it.
            # Make sure that there's only numbers after the / in the user input.
            if self.prefix_length[1:].isdecimal():
                prefix_number = int(self.prefix_length[1:]) # If it's decimal then assign it.
            else:
                print("Part one: Prefix Length number should be an integer!")
                return False            
            # Check if the prefix length number is in the range 1-128.
            if prefix_number < 1 or prefix_number > 128:
                print("Part one: Prefix Length number should in the range between 1-128.")
                return False
        else:
            self.ipv6_input_no_PL = self.ipv6_input # Re-initialized self.ipv6_input_no_PL
        
        # Part two.
        # User input cannot be empty.
        if len(ipv6_input_no_PL) == 0:
            print("Part two: User input cannot be empty")
            return False

        
        # Part three.
        # A single colon cannot be at the beginning nor at the end of an ipv6 address.
        if ipv6_input_no_PL[0] == ":" or (ipv6_input_no_PL[-1] == ":" and ipv6_input_no_PL[-2:] != "::"):
            print("Part three: A single colon cannot be at the beginning nor at the end.")
            return False
        
        
        # Part four.
        # Check if each character in user input is valid based on our list ipv6_char.        
        for char in ipv6_input_no_PL:
            if char not in ipv6_char:
                print("Part four: Inputted invalid charater!") 
                return False

        
        # Part five.
        # There should only be two colons(::) that are consecutive in an ipv6 address.   
        # You can't have like this ::: or more in an ipv6 address.     
        for char in ipv6_input_no_PL:
            if char == ":":
                colon_count += 1
                if colon_count > 2:
                    print("Part five: There should only be two consecutive colons.")
                    return False
            else:
                colon_count = 0
        
        
        # Part six.
        # There should only be one double colon.
        for char in ipv6_input_no_PL:
            if char == ":":
                colon_count += 1
                if colon_count == 2:
                    double_colon_count +=1
                    if double_colon_count >= 2:
                        print("Part six: There should only be one double colon.")
                        return False
            else:
                colon_count = 0
                
        # Part seven.
        # A valid ipv6 address should only have a max of four hex digits in each group.    
        for segment in ipv6_input_no_PL.split(":"):
            if len(segment) > 4:
                print("Part seven: Each segment should only have a max of four hex digits")
                return False

        
        # Part eigth.
        # If double colon doesn't exist then a valid ipv6 address has an eight groups of segment and should only have a max of 7 colons.        
        if "::" not in ipv6_input_no_PL:
            for char in ipv6_input_no_PL:
                if char == ":":
                    colon_count += 1
            if colon_count != 7:
                print("Part eigth: Invalid Format!")
                return False        
        # Double colon can only be used if there's two or more consecutive of segments of all zeros.
        # i.e. xxxx:xxxx::xxxx:xxxx:xxxx:xxxx:xxxx. Group of x can't be more than six if :: is present
        # because :: means two ore more consecutive of segments of all zeros. i.e. 0000:0000.         
        elif "::" in ipv6_input_no_PL:
            for segment in ipv6_input_no_PL.split(":"):
                if len(segment) != 0:   # if we split on :: we will get empty strings.
                    non_zeros_quartet_count += 1
            if non_zeros_quartet_count > 6:
                print("Part eigth: :: can only be used if there's two or more consecutive of segments of all zeros")
                return False

        # Finally return true if it passes all checkings.
        # print("Valid input!")
        return True


    def abbreviated(self, is_abbreviated=True) -> list:
        """
        Return value: list

        This function will complete the address if  the user input is abbreviated.
        Then this function returns the abbreviated version of ipv6 by default.
        if is_abbreviated is false then it will return the Unabbreviated version.        
        A segment means a group of four hex digits.
        """

        ipv6_unbrv = [] # Unabbreviated ipv6 in an array.
        ipv6_abrv = []  # Abbreviated ipv6 in an array.
        zeros_to_add = 0 # To be use in part two checking.
        is_adding = True # To be use in part two checking.
        segment_to_add = 0 # To be use in part two checking.
        index_of_non_zero_char = 0 # To be use in part three.
        new_ipv6_abrv = [] # To be use in part three and will be returned by default

        # Part one.
        # Check first if ipv6 is a valid format.
        if self.check_format() == False:
            return # Exit immediately and will not proceed further.

        # Part two.
        # This if/elseif/else part is to complete user input if it's abbreviated.
        # First thing if double colon exists(abbreviated) at the end.
        if self.ipv6_input_no_PL[-2:] == "::":
            for segment in self.ipv6_input_no_PL.split(":"):
                # Split with two consecutive colons would result to empty string.
                # So we skip it.
                if len(segment) == 0:
                    break
                # Complete each quartet by preceeding 0.
                elif len(segment) != 4:
                    zeros_to_add = 4 - len(segment)
                    ipv6_unbrv.append("0"*zeros_to_add + segment)
                    ipv6_abrv.append(segment) # Just add the segment(abbreviated) for abbreviated version.
                    continue
                ipv6_unbrv.append(segment) # Just add the quartet because the user input might have a mix abbrv and unbrrv.
                ipv6_abrv.append(segment)  # Just add the quartet because the user input might have a mix abbrv and unbrrv.
            # Then add zeros of four until there are eight sets of quartets to complete the address.
            # Will complete both abbreviate and Unabbreviated.
            while is_adding:
                if len(ipv6_unbrv) != 8: # We could use the ipv6_abrv.
                    ipv6_unbrv.append("0000")
                    ipv6_abrv.append("0")
                # Exit out of while loop if there's an 8 sets already.
                else:
                    break
        # Then if double colon exists somewhere not at the end. 
        elif "::" in self.ipv6_input_no_PL:
            for segment in self.ipv6_input_no_PL.split(":"):
                # Find the index of the empty string where we'll insert quartet of zeros.
                if len(segment) == 0:
                    segment_to_add = 9 - len(self.ipv6_input_no_PL.split(":")) # Subtracted from 9 not 8 because empty string is included.
                    # Insert "0000" until we get an 8 segments.
                    while segment_to_add != 0:
                        ipv6_unbrv.append("0000")
                        ipv6_abrv.append("0") # Add 0 for the unabrreviated version.
                        segment_to_add -= 1 # Decrement by one as we add segment of zeros.
                    continue
                # Complete each quartet by preceeding 0.
                elif len(segment) != 4:
                    zeros_to_add = 4 - len(segment)
                    ipv6_unbrv.append("0"*zeros_to_add + segment)
                    ipv6_abrv.append(segment) # Just add the segment(abbreviated) for abbreviated version.
                    continue
                ipv6_unbrv.append(segment) # Just add the quartet because the user input might have a mix abbrv and unbrrv.
                ipv6_abrv.append(segment)  # Just add the quartet because the user input might have a mix abbrv and unbrrv.
        # if the user input is a compelete address just return it. i.e xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx
        else:
            return self.ipv6_input_no_PL.split(":") # Return it in a list.

        # Part three.
        # This part is to abbreviate the ipv6_abrv completely because the user might have inputted something like: 100:03::.
        # The 03 part in the input address will bypass the if/elif/else block.        
        for segment in ipv6_abrv:
            new_segment = "" # First time initialization.
            for char in segment:
                if char == "0" and len(segment) != 1:
                    continue # Will not add to the new_segment.
                # This part will not omit trailing zeros.
                elif char != "0":
                    index_of_non_zero_char = segment.index(char)
                    new_segment = segment[index_of_non_zero_char:] # Will slice from non-zero char up to last char.
                    break
                new_segment += char # Just add if the quartet is a single 0.
            new_ipv6_abrv.append(new_segment)
        
        # Part four.
        # Check if to return Unabbreviated version.
        # If is_abbreviated is false return Unabbreviated version. 
        if not is_abbreviated:
            return ipv6_unbrv

        # Finally return the new_ipv6_abrv.
        return new_ipv6_abrv # Default. Example: ["1", "2", "3", "4", "5", "6", "7", "8"]


    def get_prefix_value(self, is_abbreviated=True) -> str:
        """
        Return value: str

        This function will return the the abbreviated prefix value by default.
        If the argument is false then it will return the unabbreviated version.
        This function relies on the output of the abbreviated function.
        """

        prefix_value_Array = []
        prefix_value_string = ""
        column_to_add = 3; # Use in part one.

        # Part one.
        # Construct the prefix value in colon notation.
        # In eui-64 the prefix value is always the first half of an ipv6.
        prefix_value_Array = self.abbreviated(is_abbreviated)[:4] # self.abbreviated() returns an array and we get the half of it. 
        for segment in prefix_value_Array:
            prefix_value_string += segment
            if column_to_add != 0:
                prefix_value_string += ":"
                column_to_add -= 1

        # Finally return the prefix value string version.   
        return prefix_value_string.upper() # Example: "1:2:3:4"     




                        
