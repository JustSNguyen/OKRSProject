def sanitize_data(data, allowed_fields):
    sanitized_data = dict()
    for field in data.keys():
        if field in allowed_fields:
            sanitized_data[field] = data[field]

    return sanitized_data
