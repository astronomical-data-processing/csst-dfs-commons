def get_header_value(key: str, header, default_value = None):
    try:
        v = header[key]
        if type(v) == str:
            return v.strip()
        return v
    except Exception as e:
        return default_value