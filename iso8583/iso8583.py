from open_iso import OpenIso8583




class Iso8583:

    bit_config = [
        {"bit":0, "type": 'n', "size": 4, "action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":1, "type": 'b', "size": 32, "bitmap": 32, "action": OpenIso8583.set_bitmap },
        {"bit":2, "type": 'LL', "size": 19,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":3, "type": 'n', "size": 6,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":4, "type": 'n', "size": 12,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":5, "type": 'n', "size": 0,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":6, "type": 'n', "size": 0,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":7, "type": 'n', "size": 10,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":11, "type": 'n', "size": 6,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":12, "type": 'n', "size": 6,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":13, "type": 'n', "size": 4,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":14, "type": 'n', "size": 4,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":18, "type": 'n', "size": 4,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":25, "type": 'n', "size": 2,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":32, "type": 'LL', "size": 11,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":35, "type": 'LL', "size": 37,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":37, "type": 'a', "size": 12,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":38, "type": 'a', "size": 6,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":39, "type": 'a', "size": 2,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":41, "type": 'a', "size": 8,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":42, "type": 'a', "size": 15,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":43, "type": 'a', "size": 40,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":44, "type": 'LL', "size": 25,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":45, "type": 'LL', "size": 76,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":49, "type": 'n', "size": 3,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":52, "type": 'n', "size": 8,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":53, "type": 'n', "size": 48,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":54, "type": 'LLL', "size": 80,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":59, "type": 'LLL', "size": 64,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":60, "type": 'LLL', "size":999, "bit_map": 8,"action": OpenIso8583.set_bitmap},
        {"bit":61, "type": 'LLL', "size":999, "bit_map": 8,"action": OpenIso8583.set_bitmap},
        {"bit":62, "type": 'LLL', "size":999, "bit_map": 8,"action": OpenIso8583.set_bitmap},
        {"bit":63, "type": 'LLL', "size":999, "bit_map": 8,"action": OpenIso8583.set_bitmap},
        {"bit":70, "type": 'n', "size":3,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":90, "type": 'n', "size":42,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":95, "type": 'a', "size":42,"action": OpenIso8583.set_bit_from_raw_iso},
        {"bit":123, "type": 'LLL', "size":15,"action": OpenIso8583.set_bit_from_raw_iso},
    ]

    raw_iso = ""
    bit_map = []
    active_bits = [0, 1]

    def get_field_bit_map(self, bit):
        bit_map_field = None
        if self.is_field_bitmap(bit):

            active_fields = self.active_bits_in_bitmap(bit)
        pass

    def add_bit_to_bitmap(self, bit, value):
        self.bit_map.append({'bit':bit, 'value':value},)

    def is_field_bitmap(self, bit):
        bit_map_field = None
        for field in self.bits_config:
            if field['bit'] == bit and field['bit_map']:
                bit_map_field = field
        return bit_map_field is not None

    # def set_bit_from_iso_string(self, bit, iso_string):
    #     self.bit_map[self.bits_config[bit].get('bit')] = iso_string[:self.bits_config[bit].get('size')]
    #     return iso_string[:self.bits_config[bit].get('size')]
    #
    # def get_bit_map(self):
    #     bit = 1
    #     return self.get_bit_on_raw_iso(bit)

    def set_active_bits(self, bit_map):

        self.bits_config[1]['size'] = 32 if bin(int(bit_map[0], 16))[2:].zfill(4)[0] == '1' else 16
        bit_map_in_bits = self._convert_bitmap_to_bit_string(bit_map[:self.bits_config[1]['size']])

        self.active_bits += self.active_bits_in_bitmap(bit_map_in_bits, 2)

    def active_bits_in_bitmap(self, bit_map_in_bits, bit_start=0):
        active_bits = []
        for bit in bit_map_in_bits[1:]:
            if bit == '1':
                active_bits.append(bit_start)
            bit_start += 1
        return active_bits

    def _convert_bitmap_to_bit_string(self, bit_map):
        bit_map_in_bits = ''
        for nibble in bit_map:
            bit_map_in_bits += bin(int(nibble, 16))[2:].zfill(4)
        return bit_map_in_bits

    def get_and_set_bit_from_raw_iso(self, bit, iso):
        position = [0,0]
        bit_config = self.get_bit_config(bit)

        if bit_config.get('type') in ['LL','LLL']:
            size = iso[:2] if bit_config.get('type') == 'LL' else iso[:3]
            position[0] = len(size)
            position[1] = len(size) + int(size)*2
        elif bit_config.get('type') == 'a':
            position[1] = bit_config.get('size')*2
        else:
            position[1] = bit_config.get('size')


        bit_value = iso[position[0]:position[1]]

        self.bit_map.append({'bit':bit, 'value':bit_value})
        return iso[position[1]:]

    def get_bit_config(self, bit):
        bit_config = None
        for bit_to_set in self.bits_config:
            if bit_to_set.get('bit') == bit:
                bit_config = bit_to_set
                break
        return bit_config

    def get_message_type(self):
        pass

    def open_iso(self, raw_iso):
        self.raw_iso = iso = raw_iso
        self.add_bit_to_bitmap(0, iso[:self.get_bit_config(0)['size']])
        iso = iso[self.get_bit_config(0)['size']:]
        self.set_active_bits(iso)
        self.bit_map[1]['value'] = iso[:self.get_bit_config(1)['size']]
        iso = iso[self.get_bit_config(1)['size']:]

        for bit in self.active_bits[2:]:
            if self.is_field_bitmap(bit):
                field_bitmap = self.get_field_bit_map(bit)
            else:
                iso = self.get_and_set_bit_from_raw_iso(bit, iso)
