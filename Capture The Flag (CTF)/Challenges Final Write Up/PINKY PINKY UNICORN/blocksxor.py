# Block size is 16 (I think this is 16 bits which is 2 bytes)
# Total length is 1188

def read_file(file_name):
    with open('challenge.ppm', 'rb') as f:
        finished = False
        ls = []
        while not finished:
            # Do stuff with byte.
            byte = f.read(16)  # Read in 16 bytes which is 16 bits
            ls.append(byte)
            if byte == b"":
                finished = True
    return ls

def to_bytes(n):
    s = hex(n)
    s_n = s[2:]
    if 'L' in s_n:
        s_n = s_n.replace('L', '')
    if len(s_n) % 2 != 0:
        s_n = '0' + s_n
    decoded = s_n.decode('hex') # UNCOMMENT THIS IN PYTHON 2
    # decoded = bytes.fromhex(s_n).decode('utf-8')

    pad = (len(decoded) % BLOCK_SIZE)
    if pad != 0:
        decoded = "\0" * (BLOCK_SIZE - pad) + decoded
    return decoded

def parse_header_ppm(f):
    data = f.read()
    header = b""



    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data

def remove_line(s):
    # returns the header line, and the rest of the file
    print(type(s))
    # print(s.index('\n'))
    return s[:s.index(b'\n') + 1], s[s.index(b'\n') + 1:]

if __name__ == "__main__":
    '''
    Separate the headers from the main text
    For the main text perform the XOR
    '''
    BLOCK_SIZE = 16
    with open('challenge.ppm', 'rb') as f:
        header, data = parse_header_ppm(f)
    print(header)
    print(len(data))
    print(len(data)/16)
    print(type(data))
    blocks = []
    for i in range(int(len(data)/BLOCK_SIZE)):
        start = i * BLOCK_SIZE
        stop = (i + 1) * BLOCK_SIZE
        blocks.append(data[start:stop])
    print(len(blocks))
    '''
    Iterate through the blocks starting from the back
    XOR with the previous block
    '''
    # for i in range(len(blocks) - 1):
    #     # prev_blk = int(blocks[i].hex(), 16)
    #     # curr_blk = int(blocks[i + 1].hex(), 16)
    #     # UNCOMMENT BELOW FOR PYTHON 2
    #     prev_blk = int(blocks[i].encode('hex'), 16)
    #     curr_blk = int(blocks[i + 1].encode('hex'), 16)

    #     n_curr_blk = prev_blk  ^ curr_blk
    #     blocks[i + 1] = to_bytes(n_curr_blk)
    for i in range(len(blocks)-1, 0, -1):
        # prev_blk = int(blocks[i].hex(), 16)
        # curr_blk = int(blocks[i + 1].hex(), 16)
        # UNCOMMENT BELOW FOR PYTHON 2

        prev_blk = int(blocks[i-1].encode('hex'), 16)
        curr_blk = int(blocks[i].encode('hex'), 16)

        n_curr_blk = prev_blk  ^ curr_blk
        blocks[i] = to_bytes(n_curr_blk)
    output = ''
    for i in range(1, len(blocks)):
        output += blocks[i]
    # ct_abc = "".join(blocks)
    with open('original2.ppm', 'wb') as fout:
        fout.write(header)
        fout.write(output)


    # ls = read_file('challenge.ppm') # each element in a byte
    # # ans_ls = []
    # for i in range(len(ls) - 1):
    #     prev_blk = int(ls[i].encode('hex'), 16)
    #     curr_blk = int(ls[i + 1].encode('hex'), 16)

    #     # prev_blk = int(ls[i].hex(), 16)
    #     # curr_blk = int(ls[i + 1].hex(), 16)

    #     n_curr_blk = prev_blk  ^ curr_blk
    #     ls[i + 1] = to_bytes(n_curr_blk)

    # ct_abc = "".join(ls)
    # print(ct_abc)
    # with open('original.ppm', 'rb') as fout:
    #     fout.write(ct_abc)
    # for blocks in ls:
    #     ans_ls.append(blocks)
    # print(len(ls))
    # print(type(ls[0]))
    # print(ls[0])
    # print(ls[-1])
    # print(len(ls[-1]))