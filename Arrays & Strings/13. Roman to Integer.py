class Solution:
    # Define a method that takes a Roman numeral string (s) and converts it to an integer
    def romanToInt(self, s: str) -> int:
        # Create a dictionary (roman_key) that maps Roman numerals to their respective integer values
        roman_key = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        # Initialize int_value to store the final integer value
        int_value = 0 
        
        # Loop through each character in the string 's', except the last one
        for char in range(len(s) - 1):
            # Get the integer value of the current Roman numeral
            current_value = roman_key[s[char]]

            # If the next numeral exists in range (this check ensures char + 1 is valid)
            if char + 1 < len(s):
                # Get the integer value of the next Roman numeral
                next_numeral_value = roman_key[s[char + 1]]

                # If the current numeral is smaller than the next one, subtract its value
                if current_value < next_numeral_value:
                    int_value -= current_value
                # If the current numeral is greater than or equal to the next one, add its value
                elif current_value >= next_numeral_value:
                    int_value += current_value 

        # Add the value of the last Roman numeral (since it hasn't been processed in the loop)
        int_value += roman_key[s[-1]]

        # Return the final calculated integer value
        return int_value
