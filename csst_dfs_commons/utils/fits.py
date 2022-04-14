def get_header_value(key: str, header, default_value = None):
    try:
        return header[key]
    except Exception as e:
        return default_value