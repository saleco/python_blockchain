import hashlib as hl  # creating an alias to an import and then in the code we should use the alias
import json


def hash_string_256(string):
    return hl.sha256(string).hexdigest()


def hash_block(block):
    """ Hashes a block and returns a string representation of it.

        Arguments:
            :block: The block that should be hashed.
    """
    return hash_string_256(json.dumps(block, sort_keys=True).encode())
