# 5.2 - Given a real number between 0 and 1 that is passed in as a double, print the binary representation. If the
# number cannot be expressed accurately in binary with at most 32 characters, print "ERROR".

def binary_to_string(n: float):
    # 0.72 -> 2** -1 + 2 ** -2 + 2 ** -3
    if n > 1 or n < 0:
        return "INVALID"
    sum = 0

    power_of_two = 1 / 2
    string = ["0", "."]
    while n > 0:
        if len(string) >= 32 + 2:
            return "ERROR"

        if n >= power_of_two:
            string.append("1")
            n -= power_of_two
        else:
            string.append("0")
        power_of_two /= 2


    return "".join(string)


def test_binary_to_string():
    assert binary_to_string(0.5) == "0.1"
    assert binary_to_string(0.72) == "ERROR"
    assert binary_to_string(0.1) == "ERROR"
    assert binary_to_string(0.25) == "0.01"

