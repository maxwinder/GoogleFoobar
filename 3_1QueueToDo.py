# Built on Python 2.7.13
# Google Foobar Queue To Do

def getXOR(start, end):
    if (end - start) == 0:
        return 0
    if (end - start) == 1:
        return start
    if (end - start) <= 4:
        return reduce(lambda x,y: x ^ y, range(start, end))
    else:
        begin_range = (start, start / 4 * 4 + 4)
        end_range = (end / 4 * 4, end)
        return getXOR(*begin_range) ^ getXOR(*end_range)


def solution(start, length):
    workers_list = [(start + (length - l) * length, start + (length - l)*length + l) for l in range(length, 0, -1)]
    new_xor = [getXOR(start, end) for start, end in workers_list]

    return reduce(lambda x,y: x ^ y, new_xor)


#solution(1234,2532)
#solution(0, 3)
#solution(17, 4)