def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "not found"
        case 500:
            return "Server error"
        case _:
            return "unknown"

print(http_status(4045))