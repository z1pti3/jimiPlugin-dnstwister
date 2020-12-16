import hashlib

blockSize = 65535

def fileHashSHA256(filename):
    hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            fBlock = f.read(blockSize)
            while len(fBlock) > 0:
                hash.update(fBlock)
                fBlock = f.read(blockSize)
    except PermissionError:
        return None
    return str(hash.hexdigest())