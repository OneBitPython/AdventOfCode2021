class LiteralPacket:
    def __init__(self, version, type_id, number):
        self.version = version
        self.type_id = type_id
        self.number = number


class OperatorPacket:
    def __init__(self, version, type_id, length_type, length):
        self.version = version
        self.type_id = type_id
        self.length_type = length_type
        self.length = length


PACKET_TYPE_LITERAL_VALUE = 4
LENGTH_TYPE_BITS = 0
LENGTH_TYPE_PACKETS = 1

with open("C:\\Users\\anant\\PythonProjects\\AdventOfCode\\day16\\inp16.txt") as f:
    rawdata = f.readline().strip()
    data = bin(int(rawdata, 16))[2:].rjust(4 * len(rawdata), "0")

pointer = 0
packets = []
while pointer < len(data) - 6:
    if data.find("1", pointer) == -1:
        print(
            f"Reached padding at the end ({len(data)-pointer} bits remaining)")
        break
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
        packets.append(LiteralPacket(version, type_id, number))
    else:
        length_type_id = int(data[pointer])
        pointer += 1
        length_size = 15 if length_type_id == LENGTH_TYPE_BITS else 11
        length = int(data[pointer: pointer + length_size], 2)
        packets.append(OperatorPacket(
            version, type_id, length_type_id, length))
        pointer += length_size


print(f"Ans: {sum(p.version for p in packets)}")
