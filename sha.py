def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


def sha1(message):
    # Initialize variables
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Pre-processing
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_bit_len.to_bytes(8, 'big')

    # Process message in 512-bit chunks
    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        words = [0] * 80

        # Break chunk into 16 32-bit big-endian words
        for j in range(16):
            words[j] = int.from_bytes(chunk[j * 4:j * 4 + 4], 'big')

        # Extend the 16 32-bit words to 80 32-bit words
        for j in range(16, 80):
            words[j] = left_rotate((words[j - 3] ^ words[j - 8] ^ words[j - 14] ^ words[j - 16]), 1)

        # Initialize hash value for this chunk
        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for j in range(80):
            if j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + words[j]
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp & 0xFFFFFFFF

        # Update hash value
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Produce the final hash value
    final_hash = (h0 << 128) | (h1 << 96) | (h2 << 64) | (h3 << 32) | h4
    return hex(final_hash)[2:]


# Example usage
message = input("Enter messege - ")

hashed_message = sha1(message.encode('ascii'))
print("SHA-1 Hash:", hashed_message)
