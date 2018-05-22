import hashlib


def calculatechecksum(filepath):
    try:
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    except Exception as e:
        print("Exception while calculating checkSum \n", e)
