def get_val(collection, key, default='git'):
    if not collection:
        return default
    if key not in collection:
        return default
    return collection[key]