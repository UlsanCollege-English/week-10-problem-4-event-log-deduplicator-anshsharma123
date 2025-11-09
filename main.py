"""
HW04 — Event Log Deduplicator (Custom Set via Chaining)
"""

# -------------------------------
# 1. Helper hash function
# -------------------------------
def _hash(key, m):
    """Simple deterministic hash function."""
    h = 0
    for ch in key:
        h = (h * 31 + ord(ch)) % m
    return h


# -------------------------------
# 2. Core functions
# -------------------------------
def make_set(m):
    """Return a new hash table with m empty buckets."""
    return {"buckets": [[] for _ in range(m)], "count": 0}


def add(s, key):
    """Add key if not present. Return True if added, False if already exists."""
    h = _hash(key, len(s["buckets"]))
    bucket = s["buckets"][h]
    if key in bucket:
        return False
    bucket.append(key)
    s["count"] += 1
    return True


def contains(s, key):
    """Return True if key exists in the set."""
    h = _hash(key, len(s["buckets"]))
    return key in s["buckets"][h]


def remove(s, key):
    """Remove key if present. Return True if removed, False if missing."""
    h = _hash(key, len(s["buckets"]))
    bucket = s["buckets"][h]
    if key in bucket:
        bucket.remove(key)
        s["count"] -= 1
        return True
    return False


def size(s):
    """Return number of keys in the set."""
    return s["count"]


# -------------------------------
# Optional manual check
# -------------------------------
if __name__ == "__main__":
    s = make_set(5)
    print(add(s, "a"), add(s, "b"), add(s, "a"))
    print(contains(s, "b"), remove(s, "b"), contains(s, "b"))
    print(size(s))
