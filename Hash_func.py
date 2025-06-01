def simple_hash(data: bytes) -> bytes:

    hash_bytes = [0] * 32

    for i, byte in enumerate(data):
        index = i % 32
        hash_bytes[index] = (hash_bytes[index] + byte + (index ^ byte)) % 256

    for i in range(32):
        hash_bytes[i] = (hash_bytes[i] ^ ((i * 31) % 256)) ^ len(data) % 256

    return bytes(hash_bytes)


if __name__ == "__main__":
    sample_data = b"Hello, this is a test input for the hash function."
    hashed = simple_hash(sample_data)
    print("Input:", sample_data)
    print("Hash (hex):", hashed.hex())