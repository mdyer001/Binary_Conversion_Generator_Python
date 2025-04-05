class Conversion:
    def to_binary(self, num):
        """Converts a decimal number to binary"""
        # Using built-in function bin() to convert decimal to binary and removing
        return bin(num)[2:]

    def to_ternary(self, num):
        """Converts a decimal number to ternary"""
        digits = []
        while num > 0:
            # Taking the remainder when divided by 3 and adding it to the list 
            digits.append(num % 3)
            # Dividing by 3 to move to the next digit
            num //= 3
            # Converting the list of digits to a string in reverse order
        return ''.join(map(str, reversed(digits)))

    def to_quaternary(self, num):
        """Converts a decimal number to quaternary"""
        digits = []
        while num > 0:
            # Taking the remainder when divided by 4 and adding it to the list 
            digits.append(num % 4)
            # Dividing by 4 to move to the next digit
            num //= 4
            # Converting the list of digits to a string in reverse 
        return ''.join(map(str, reversed(digits)))

    def to_octal(self, num):
        """Converts a decimal number to octal"""
        return oct(num)[2:]

    def to_decimal(self, num, base):
        """Converts a number from the given base to decimal"""
        if base == 10: # If the number is already in decimal, return it as is.
            return num
        # Initialize the decimal value to 0.
        decimal = 0 
        power = 0
        # Iterate through the digits of the input number from right to left.
        for digit in reversed(str(num)):
            # Add the decimal value of each digit to the total.
            decimal += int(digit) * (base ** power)
            # Increment the power of the base for each digit.
            power += 1
            # Return the decimal value of the input number.
        return decimal

    def to_duodecimal(self, num):
        """Converts a decimal number to duodecimal"""
        digits = []
        while num > 0:
            digits.append(num % 12)
            num //= 12
            # Convert digits to string and join them
        return ''.join(map(str, reversed(digits)))

    def to_hexadecimal(self, num):
        """Converts a decimal number to hexadecimal"""
        # Return hexadecimal string without '0x' prefix
        return hex(num)[2:]

    def to_vigesimal(self, num):
        """Converts a decimal number to vigesimal"""
        digits = []
        while num > 0:
            digits.append(num % 20)
            num //= 20
            # Convert digits to string and join them
        return ''.join(map(str, reversed(digits)))

    def convert(self, num, base_from, base_to):
        """Converts a number from the given base to the given target base"""
        decimal = self.to_decimal(num, base_from)
        if base_to == 2:
            return self.to_binary(decimal)
        elif base_to == 3:
            return self.to_ternary(decimal)
        elif base_to == 4:
            return self.to_quaternary(decimal)
        elif base_to == 8:
            return self.to_octal(decimal)
        elif base_to == 10:
            return str(decimal)
        elif base_to == 12:
            return self.to_duodecimal(decimal)
        elif base_to == 16:
            return self.to_hexadecimal(decimal)
        elif base_to == 20:
            return self.to_vigesimal(decimal)
        else:
            return None # Return None if base_to is not supported


def main():
    converter = Conversion()
    while True:
        num = int(input("Enter your number: "))
        try:
            base_from = int(input("Enter the base of the number: "))
            base_to = int(input("Enter the target base: "))
            if base_from < 2 or base_to < 2 or base_from > 20 or base_to > 20:
                raise ValueError # raise an error if the input bases are not within the supported range
        except ValueError:
            print("Invalid input. Please enter a number in one of the supported numerical systems, and choose a base between 2 and 20.")
            continue # continue with the next iteration of the loop if an error is raised

        result = converter.convert(num, base_from, base_to)
        if result is None:
            print("Invalid target base. Please choose a base between 2 and 20.")
        else:
            print(f"{num} in base {base_from} and converted to base {base_to} is: {result}")

if __name__ == "__main__":
    main()