import datetime


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


def set_bitmap(self, bit_size, iso):
    if bit_size >= 16:
        bit_size = 32 if bin(int(iso[0], 16))[2:].zfill(4)[0] == '1' else 16

    return _convert_bitmap_to_bit_string(iso[:bit_size])


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


class Iso8583:
    bit_config = {
        0: {"type": 'n', "size": 4, "action": set_bit_from_raw_iso},
        1: {"type": 'b', "size": 32, "bitmap": 32, "action": set_bitmap},
        2: {"type": 'LL', "size": 19, "action": set_bit_from_raw_iso},
        3: {"type": 'n', "size": 6, "action": set_bit_from_raw_iso},
        4: {"type": 'n', "size": 12, "action": set_bit_from_raw_iso},
        5: {"type": 'n', "size": 0, "action": set_bit_from_raw_iso},
        6: {"type": 'n', "size": 0, "action": set_bit_from_raw_iso},
        7: {"type": 'n', "size": 10, "action": set_bit_from_raw_iso},
        11: {"type": 'n', "size": 6, "action": set_bit_from_raw_iso},
        12: {"type": 'n', "size": 6, "action": set_bit_from_raw_iso},
        13: {"type": 'n', "size": 4, "action": set_bit_from_raw_iso},
        14: {"type": 'n', "size": 4, "action": set_bit_from_raw_iso},
        18: {"type": 'n', "size": 4, "action": set_bit_from_raw_iso},
        25: {"type": 'n', "size": 2, "action": set_bit_from_raw_iso},
        32: {"type": 'LL', "size": 11, "action": set_bit_from_raw_iso},
        35: {"type": 'LL', "size": 37, "action": set_bit_from_raw_iso},
        37: {"type": 'a', "size": 12, "action": set_bit_from_raw_iso},
        38: {"type": 'a', "size": 6, "action": set_bit_from_raw_iso},
        39: {"type": 'a', "size": 2, "action": set_bit_from_raw_iso},
        41: {"type": 'a', "size": 8, "action": set_bit_from_raw_iso},
        42: {"type": 'a', "size": 15, "action": set_bit_from_raw_iso},
        43: {"type": 'a', "size": 40, "action": set_bit_from_raw_iso},
        44: {"type": 'LL', "size": 25, "action": set_bit_from_raw_iso},
        45: {"type": 'LL', "size": 76, "action": set_bit_from_raw_iso},
        49: {"type": 'n', "size": 3, "action": set_bit_from_raw_iso},
        52: {"type": 'n', "size": 8, "action": set_bit_from_raw_iso},
        53: {"type": 'n', "size": 48, "action": set_bit_from_raw_iso},
        54: {"type": 'LLL', "size": 80, "action": set_bit_from_raw_iso},
        59: {"type": 'LLL', "size": 64, "action": set_bit_from_raw_iso},
        60: {"type": 'LLL', "size": 999, "bit_map": 8, "action": set_bitmap},
        61: {"type": 'LLL', "size": 999, "bit_map": 8, "action": set_bitmap},
        62: {"type": 'LLL', "size": 999, "bit_map": 8, "action": set_bitmap},
        63: {"type": 'LLL', "size": 999, "bit_map": 8, "action": set_bitmap},
        70: {"type": 'n', "size": 3, "action": set_bit_from_raw_iso},
        90: {"type": 'n', "size": 42, "action": set_bit_from_raw_iso},
        95: {"type": 'a', "size": 42, "action": set_bit_from_raw_iso},
        123: {"type": 'LLL', "size": 15, "action": set_bit_from_raw_iso},
    }

    raw_iso = ""
    bit_map = []
    active_bits = [0, 1]

    def get_field_bit_map(self, bit):
        bit_map_field = None
        if self.is_field_bitmap(bit):
            active_fields = self.active_bits_in_bitmap(bit)
        pass

    def add_bit_to_bitmap(self, bit, value):
        self.bit_map.append((bit, value))

    def is_field_bitmap(self, bit):
        return self.bit_config.get(bit).get("bitmap") is not None

    # def set_bit_from_iso_string(self, bit, iso_string):
    #     self.bit_map[self.bits_config[bit].get('bit')] = iso_string[:self.bits_config[bit].get('size')]
    #     return iso_string[:self.bits_config[bit].get('size')]
    #
    # def get_bit_map(self):
    #     bit = 1
    #     return self.get_bit_on_raw_iso(bit)

    def set_active_bits(self, bit_map):

        self.bit_config[1]['size'] = 32 if bin(int(bit_map[0], 16))[2:].zfill(4)[0] == '1' else 16
        bit_map_in_bits = self._convert_bitmap_to_bit_string(bit_map[:self.bit_config[1]['size']])
        print("active bits in bitmap")
        print(self.active_bits_in_bitmap(bit_map_in_bits, 2))
        print("active bits")
        print(self.active_bits)
        self.active_bits += [x for x in self.active_bits_in_bitmap(bit_map_in_bits, 2) if x not in self.active_bits]

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
        position = [0, 0]
        bit_config = self.get_bit_config(bit)

        if bit_config.get('type') in ['LL', 'LLL']:
            size = iso[:2] if bit_config.get('type') == 'LL' else iso[:3]
            position[0] = len(size)
            position[1] = len(size) + int(size) * 2
        elif bit_config.get('type') == 'a':
            position[1] = bit_config.get('size') * 2
        else:
            position[1] = bit_config.get('size')

        bit_value = iso[position[0]:position[1]]

        self.bit_map.append({'bit': bit, 'value': bit_value})
        return iso[position[1]:]

    def get_bit_config(self, bit):
        return self.bit_config.get(bit)

    def get_message_type(self):
        pass

    def open_iso(self, raw_iso):
        self.raw_iso = iso = raw_iso
        opened_iso = Iso8583()
        opened_iso.set_bit(0, raw_iso[:4])
        opened_iso.set_active_bits(raw_iso[4:])  # TODO: Terminar abertura da iso
        print("opened iso")
        print(opened_iso.active_bits)
        #
        # self.add_bit_to_bitmap(0, iso[:self.get_bit_config(0)['size']])
        #
        # iso = iso[self.get_bit_config(0)['size']:]
        # self.set_active_bits(iso)
        # self.bit_map[1]['value'] = iso[:self.get_bit_config(1)['size']]
        # iso = iso[self.get_bit_config(1)['size']:]
        #
        # for bit in self.active_bits[2:]:
        #     if self.is_field_bitmap(bit):
        #         field_bitmap = self.get_field_bit_map(bit)
        #     else:
        #         iso = self.get_and_set_bit_from_raw_iso(bit, iso)

    def generate_nsu(self, date, local_nsu):
        pass

    def set_bit(self, bit, value):
        self.bit_config[bit]['value'] = value
        self.bit_map.append(bit)

    def update_iso(self):
        bit_map = self.bit_map
        bit_map.sort(reverse=True)
        if bit_map[0] > 63:
            self.set_bit(1, "1"+"".zfill(127))
        else:
            self.set_bit(1, "0"+"".zfill(63))
        for bit in bit_map:
            self.bit_config[1]['value'] = self.bit_config[1]['value'][:bit] + "1" + self.bit_config[1]['value'][bit+1:]
        self.bit_config[1]['value'] = hex(int(self.bit_config[1]['value'], 2))[2:]
        types = {"n": lambda x: str(x["value"]).zfill(int(x["size"])),
                 "a": lambda x: str(x["value"]).zfill(int(x["size"])),
                 "LL": lambda x: str(x["value"]),
                 "LLL": lambda x: str(x["value"]),
                 "b": lambda x: str(x["value"])}
        raw_iso = ""
        bits = [self.bit_config[bit] for bit in self.bit_config if self.bit_config[bit].get("value")]
        for bit in bits:
            # print(f"BIT {bit}")
            raw_iso += types[bit.get("type")](bit)
        self.raw_iso = raw_iso
        return self.raw_iso

    def make_payment_request_iso(self, request):
        local_date = datetime.datetime.strptime(request.get("local_date"), "%Y-%m-%dT%H:%M:%S")
        self.set_bit(0, "0200")
        self.set_bit(3, "000000")
        self.set_bit(4, request.get("request_info").get("amount"))
        self.set_bit(7, local_date.strftime("%H%M%S%m%d"))
        self.set_bit(11, "000001")
        self.set_bit(12, local_date.strftime("%H%M%S"))
        self.set_bit(13, local_date.strftime("%m%d"))
        # self.set_bit(14, request.get("card_data").get("expiration_date"))
        # self.set_bit(18, "get merchant code type on bd")
        # self.set_bit(37, local_date.strftime("%Y")[-1]+local_date.strftime("%m%d").zfill(3)+local_date.strftime("%H") + self.get_bit_config(11).get("value"))
        # self.set_bit(41, "0200")
        self.set_bit(42, "1231234567")
        # self.set_bit(43, "0200")
        # self.set_bit(49, "0200")
        # self.set_bit(52, "0200")
        # self.set_bit(54, "0200")
        # self.set_bit(59, "0200")
        bit_60_tlv = self.TLV("LL")
        bit_60_tlv.add_tag("10", "123")
        self.set_bit(60, bit_60_tlv.raw_value)
        # self.set_bit(61, "0200")
        self.set_bit(62, "0200")
        # self.set_bit(63, "0200")
        self.set_bit(123, "0200")
        self.update_iso()
        print(self.open_iso(self.raw_iso))
        return self.raw_iso

    def make_payment_response_iso(self, request_iso):
        local_date = datetime.datetime.strptime(request_iso.get("local_date"), "%Y-%m-%dT%H:%M:%S")
        self.set_bit(0, "0200")
        self.set_bit(3, "000000")
        self.set_bit(4, request_iso.get("request_info").get("amount"))
        self.set_bit(7, local_date.strftime("%H%M%S%m%d"))
        self.set_bit(11, "000001")
        self.set_bit(12, local_date.strftime("%H%M%S"))
        self.set_bit(13, local_date.strftime("%m%d"))
        # self.set_bit(14, request.get("card_data").get("expiration_date"))
        # self.set_bit(18, "get merchant code type on bd")
        # self.set_bit(37, local_date.strftime("%Y")[-1]+local_date.strftime("%m%d").zfill(3)+local_date.strftime("%H") + self.get_bit_config(11).get("value"))
        # self.set_bit(41, "0200")
        self.set_bit(42, "1231234567")
        # self.set_bit(43, "0200")
        # self.set_bit(49, "0200")
        # self.set_bit(52, "0200")
        # self.set_bit(54, "0200")
        # self.set_bit(59, "0200")
        bit_60_tlv = self.TLV("LL")
        bit_60_tlv.add_tag("10", "123")
        self.set_bit(60, bit_60_tlv.raw_value)
        # self.set_bit(61, "0200")
        self.set_bit(62, "0200")
        # self.set_bit(63, "0200")
        self.set_bit(123, "0200")
        self.update_iso()
        return self.raw_iso

    class TLV:
        def __init__(self, tlv_type):
            if tlv_type == "LL":
                self.length = 2
            if tlv_type == "LLL":
                self.length = 3
            self.raw_value = ""

        def add_tag(self, tag=None, value=None):
            if tag:
                self.raw_value += tag + str(len(value)).zfill(self.length) + value
            else:
                self.raw_value += value


class JsonRequest:

    def __init__(self):
        self.base_request = {
            "request_type": "",
            "local_date": datetime.datetime.now(),
            "request_info": {}
        }

    def set_request(self, request: dict):
        if not self.base_request:
            self.base_request = {
                "request_type": "",
                "local_date": datetime.datetime.now(),
                "request_info": {}
            }
        self.set_request_type(request.get("request_type"))
        self.set_card_info(request.get("request_info").get("card_data"))
        self.set_payment_method(request.get("request_info"))
        self.set_number_of_installments(request.get("number_of_installments"))
        self.set_amount(request.get("amount"))
        self.set_establishment_data(request)

    def set_request_type(self, request_type: str):
        request_types = {
            "payment": "0200",
            "void": "0420"
        }
        self.base_request["request_type"] = request_types[request_type]

    def set_card_info(self, data: dict):
        payment_modes = {
            "chip": "01",
            "contacless": "02",
            "magstripe": "03",
            "manually_keyed": "04"
        }
        card_data = {
            "holder_name": data["holder_name"],
            "card_number": data["card_number"],
            "cvv2": data["holder_name"],
            "expire_date": data["expire_date"],
            "payment_mode": payment_modes[data["payment_mode"]],
        }
        self.base_request["request_info"]["card_data"] = card_data

    def set_payment_method(self, method):
        payment_methods = {
            "credit": "01",
            "debit": "02"
        }
        self.base_request["request_info"]["payment_method"] = payment_methods[method]

    def set_number_of_installments(self, numer_of_installments: int = 1):
        if numer_of_installments:
            self.base_request["request_info"]["installments"] = numer_of_installments

    def set_amount(self, amount: int):
        if amount:
            self.base_request["request_info"]["amount"] = amount

    def set_establishment_data(self, data):
        establishment_data = {
            "address": data["address"],
            "address_number": data["address_number"],
            "business_name": data["business_name"],
            "business_id": data["business_id"],
            "descriptor": data["descriptor"],
            "pos_id": data["pos_id"]
        }
        self.base_request["request_info"]["establishment"] = establishment_data

    def set_nsu(self, nsu):
        pass
