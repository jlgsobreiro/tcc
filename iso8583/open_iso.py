def _convert_bitmap_to_bit_string(bit_map):
    bit_map_in_bits = ''
    for nibble in bit_map:
        bit_map_in_bits += bin(int(nibble, 16))[2:].zfill(4)
    return bit_map_in_bits

def _active_bits_in_bitmap(bit_map_in_bits, bit_start=0):
    active_bits = []
    for bit in bit_map_in_bits[1:]:
        if bit == '1':
            active_bits.append(bit_start)
        bit_start += 1
    return active_bits

class OpenIso8583:
    def set_bitmap(self, bit_size, iso):
        if bit_size >= 16:
            bit_size = 32 if bin(int(iso[0], 16))[2:].zfill(4)[0] == '1' else 16

        return _convert_bitmap_to_bit_string(iso[:bit_size])


    def set_bit_from_raw_iso(self, bit_size, bit_type, iso):
        position = [0, 0]

        if bit_type in ['LL', 'LLL']:
            size = iso[:2] if bit_type == 'LL' else iso[:3]
            position[0] = len(size)
            position[1] = len(size) + int(size) * 2
        elif bit_type == 'a':
            position[1] = bit_size * 2
        else:
            position[1] = bit_size

        bit_value = iso[position[0]:position[1]]

        return bit_value
