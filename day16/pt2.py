from math import prod


PACKET_TYPE_LITERAL_VALUE = 4
LENGTH_TYPE_BITS = 0
LENGTH_TYPE_PACKETS = 1
OPERATOR_TYPE_SUM = 0
OPERATOR_TYPE_PROD = 1
OPERATOR_TYPE_MIN = 2
OPERATOR_TYPE_MAX = 3
OPERATOR_TYPE_GT = 5
OPERATOR_TYPE_LT = 6
OPERATOR_TYPE_EQ = 7


class LiteralPacket:
    def __init__(self, version, type_id, number):
        self.version = version
        self.type_id = type_id
        self.number = number

    def get_value(self):
        return self.number

    def get_version_sum(self):
        return self.version


class OperatorPacket:
    def __init__(self, version, type_id, length_type, length):
        self.version = version
        self.type_id = type_id
        self.length_type = length_type
        self.length = length
        self.subpackets = []

    def add_subpacket(self, packet):
        self.subpackets.append(packet)

    def get_value(self):
        if self.type_id == OPERATOR_TYPE_SUM:
            return sum(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_PROD:
            return prod(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_MIN:
            return min(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_MAX:
            return max(p.get_value() for p in self.subpackets)
        elif self.type_id == OPERATOR_TYPE_GT:
            if len(self.subpackets) != 2:
                raise AssertionError(
                    "Operator '>' needs exactly two subpackets")
            return (
                1
                if self.subpackets[0].get_value() > self.subpackets[1].get_value()
                else 0
            )
        elif self.type_id == OPERATOR_TYPE_LT:
            if len(self.subpackets) != 2:
                raise AssertionError(
                    "Operator '<' needs exactly two subpackets")
            return (
                1
                if self.subpackets[0].get_value() < self.subpackets[1].get_value()
                else 0
            )
        elif self.type_id == OPERATOR_TYPE_EQ:
            if len(self.subpackets) != 2:
                raise AssertionError(
                    "Operator '==' needs exactly two subpackets")
            return (
                1
                if self.subpackets[0].get_value() == self.subpackets[1].get_value()
                else 0
            )

    def get_version_sum(self):
        return self.version + sum(p.get_version_sum() for p in self.subpackets)


def read_packet(data, pointer):
    if data.find("1", pointer) == -1:
        return None, pointer

    version = int(data[pointer: pointer + 3], 2)
    type_id = int(data[pointer + 3: pointer + 6], 2)
    pointer += 6

    if type_id == PACKET_TYPE_LITERAL_VALUE:
        number_bits = ""
        read_next = True
        while read_next:
            read_next = data[pointer] == "1"
            number_bits += data[pointer + 1: pointer + 5]
            pointer += 5
        number = int(number_bits, 2)
        return LiteralPacket(version, type_id, number), pointer
    else:
        length_type_id = int(data[pointer])
        pointer += 1
        length_size = 15 if length_type_id == LENGTH_TYPE_BITS else 11
        length = int(data[pointer: pointer + length_size], 2)
        pointer += length_size
        packet = OperatorPacket(version, type_id, length_type_id, length)
        if length_type_id == LENGTH_TYPE_PACKETS:
            for _ in range(length):
                subpacket, pointer = read_packet(data, pointer)
                packet.add_subpacket(subpacket)
        else:
            to_read = length
            while to_read > 0:
                subpacket, new_pointer = read_packet(data, pointer)
                packet.add_subpacket(subpacket)
                to_read -= new_pointer - pointer
                pointer = new_pointer
        return packet, pointer


with open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day16\\inp16.txt") as f:
    rawdata = f.readline().strip()
    fulldata = bin(int(rawdata, 16))[2:].rjust(4 * len(rawdata), "0")

expression, _ = read_packet(fulldata, 0)
print(f"ans : {expression.get_value()}")
