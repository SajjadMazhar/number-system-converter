class NumberSystem:

    def __init__(self):
        self.hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        self.reverse_hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        self.initialized = ""
        self.alph = 'ABCDEF'

    def to_hex_from_dec(self, decimal):
        while decimal > 0:
            remainder = decimal % 16
            if remainder <= 9:
                self.initialized = str(remainder) + self.initialized

            elif remainder >= 10 and remainder < 16:
                self.initialized = self.hex_letters[remainder] + self.initialized

            decimal = decimal // 16

        return self.initialized

    def to_dec_from_hex(self, hexadecimal):
        hexadecimal = str(hexadecimal)
        hexadecimal = hexadecimal.upper()
        decimal = 0
        size = len(hexadecimal) - 1
        for char in hexadecimal:
            if char in self.alph:
                decimal = decimal + (self.reverse_hex[char] * (16 ** size))

            else:
                decimal = decimal + (int(char) * (16 ** size))

            size -= 1

        return decimal

    def to_dec_from_bin(self, binary):
        decimal = 0
        binary_length = len(str(binary))
        for i in range(0, binary_length):
            remainder = binary % 10
            binary = binary // 10
            decimal = decimal + remainder * (2 ** i)

        return decimal

    def to_bin_from_dec(self, decimal):
        remainder = decimal % 2
        binary = str(remainder)
        decimal = decimal // 2
        while (decimal > 0):
            remainder = decimal % 2
            binary = str(remainder) + binary
            decimal = decimal // 2

        return binary

    def to_oct_from_dec(self, dec):
        remainder = dec % 8
        octal = str(remainder)
        dec = dec // 8
        while (dec > 0):
            remainder = dec % 8
            octal = str(remainder) + octal
            dec = dec // 8

        return octal

    def to_dec_from_oct(self, octal):
        oct_length = len(str(octal))
        decimal = 0
        for i in range(oct_length):
            remainder = octal % 10
            octal = octal // 10
            decimal = decimal + remainder * (8 ** i)

        return decimal

    def to_hex_from_bin(self, binary):
        dec = numSys.to_dec_from_bin(binary)
        hexa = numSys.to_hex_from_dec(dec)
        return hexa

    def to_bin_from_hex(self, hexadecimal):
        dec = numSys.to_dec_from_hex(hexadecimal)
        binary = numSys.to_bin_from_dec(dec)
        return binary

    def to_oct_from_bin(self, binary):
        dec = numSys.to_dec_from_bin(binary)
        octal = numSys.to_oct_from_dec(dec)
        return octal

    def to_bin_from_oct(self, octal):
        dec = numSys.to_dec_from_oct(octal)
        binary = numSys.to_bin_from_dec(dec)
        return binary

    def to_oct_from_hex(self, hexadecimal):
        dec = numSys.to_dec_from_hex(hexadecimal)
        octal = numSys.to_oct_from_dec(dec)
        return octal

    def to_hex_from_oct(self, octal):
        dec = numSys.to_dec_from_oct(octal)
        hexa = numSys.to_hex_from_dec(dec)
        return hexa

if __name__ == '__main__':

    numSys = NumberSystem()
    print(numSys.to_bin_from_dec(10))
    print(numSys.to_hex_from_dec(84))
    print(numSys.to_hex_from_oct(84))
    print(numSys.to_hex_from_bin(84))