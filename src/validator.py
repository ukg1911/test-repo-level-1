def validate_age(age):
    if age < 0:
    return False # BUG: INDENTATION - Must be indented

def process_id(user_id):
    # BUG: TYPE_ERROR - user_id is expected as int, but treated as string here
    return user_id.upper()