val = 0xCAFE
last_four = val & 0xF
count_on_bits = bin(last_four).count("1")

if count_on_bits >= 3:
    print("At least three of last four bits are ON")
else:
    print("Less than three bits are ON")
reversed_val = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)
print("Reversed byte order:", hex(reversed_val))
rotated_val = ((val << 4) & 0xFFFF) | (val >> 12)
print("Rotated 4 bits:", hex(rotated_val))