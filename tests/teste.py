import unittest
from datetime import datetime

import IsoRequest
import iso8583

payment_json = {
    "request_type": "payment",
    "local_date": "2023-07-01T12:00:00",
    "request_info": {
        "payment_method": "credit",
        "amount": 100,
        "card_data": {
            "holder_name": "Fulano de Tal",
            "card_number": "0123456789101112",
            "cvv2": "Fulano de Tal",
            "expire_date": "0828",
            "payment_mode": "chip",
            "installments": 1
        },
        "establishment": {
            "address": "Rua XPTO",
            "address_number": "123",
            "business_name": "Loja XPTO",
            "business_id": "123",
            "descriptor": "XPTO",
            "pos_id": "001"
        }
    }
}

void_json = {
    "request_type": "payment",
    "local_date": "2023-07-01T12:00:00",
    "request_info": {
        "payment_method": "credit",
        "amount": 100,
        "card_data": {
            "holder_name": "Fulano de Tal",
            "card_number": "0123456789101112",
            "cvv2": "Fulano de Tal",
            "expire_date": "0828",
            "payment_mode": "chip",
            "installments": 1
        },
        "establishment": {
            "address": "Rua XPTO",
            "address_number": "123",
            "business_name": "Loja XPTO",
            "business_id": "123",
            "descriptor": "XPTO",
            "pos_id": "001"
        }
    }
}

class TestIso8583(unittest.TestCase):
    def test_read_payment_json(self):
        payment = iso8583.Iso8583()
        payment.make_payment_request_iso(payment_json)
        local_date = datetime.strptime(payment_json.get("local_date"), "%Y-%m-%dT%H:%M:%S")
        expected_raw_iso = "0200d91c0000002000080000000000000010000000000000000100070112000000000112000007010000012312345671003123000000000000200"

        self.assertEqual(payment.raw_iso, expected_raw_iso)
        self.assertEqual(payment.get_bit_config_value(3), "000000")
        self.assertEqual(payment.get_bit_config_value(4), payment_json.get("request_info").get("amount"))
        self.assertEqual(payment.get_bit_config_value(7), str(local_date.strftime("%m%d%H%M%S")))
        self.assertEqual(payment.get_bit_config_value(11), "000001")
        self.assertEqual(payment.get_bit_config_value(12), str(local_date.strftime("%H%M%S")))
        self.assertEqual(payment.get_bit_config_value(13), str(local_date.strftime("%m%d")))
        self.assertEqual(payment.get_bit_config_value(42), "1231234567")
        self.assertEqual(payment.get_bit_config_value(60), "1003123")
        self.assertEqual(payment.get_bit_config_value(123), "0200")


if __name__ == '__main__':
    unittest.main()
