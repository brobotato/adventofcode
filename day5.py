import hashlib

door_id = 'ojvtpuvg'
valid = ['0', '1', '2', '3', '4', '5', '6', '7']


def hash1(id):
    chars = 0
    key = {}
    for x in range(8223372036854775807):
        if chars < 8:
            temp = id + str(x)
            if hashlib.md5(temp.encode('utf-8')).hexdigest()[:5] == '00000':
                print(hashlib.md5(temp.encode('utf-8')).hexdigest())
                key += str(hashlib.md5(temp.encode('utf-8')).hexdigest()[6])
                chars += 1
        else:
            break
    print(key)


def hash2(id):
    chars = 0
    key = {}
    for x in range(0, 8, 1):
        key[str(x)] = 'lobster'
    print(key)
    for x in range(8223372036854775807):
        if chars < 8:
            temp = id + str(x)
            if hashlib.md5(temp.encode('utf-8')).hexdigest()[:5] == '00000':
                if hashlib.md5(temp.encode('utf-8')).hexdigest()[5] in valid:
                    if key[str(hashlib.md5(temp.encode('utf-8')).hexdigest()[5])] == 'lobster':
                        key[str(hashlib.md5(temp.encode('utf-8')).hexdigest()[5])] = str(
                            hashlib.md5(temp.encode('utf-8')).hexdigest()[6])
                        chars += 1
        else:
            break
    print(key)


hash1(door_id)
hash2(door_id)

# answer part 1: 4543c154
# answer part 2: 1050cbbd
