def generate_error_message_from_serializer_errors(serializer_errors):
    messages = []

    for field in serializer_errors.keys():
        for error_detail in serializer_errors[field]:
            messages.append(error_detail)

    return ';'.join(messages)
