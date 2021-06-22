from typing import List


def create_validation_error_msg(fields: List) -> str:
    """
    creates a message string for missing form fields.

    Returns:
        str: the json string with all the fields to be displayed in from.
    """
    msg = "Following mandatory fields are empty and needs to be filled:<br>"
    # Adding missing fields.
    fields = [(str(ind + 1) + ". " + s.replace("_", " ").title()) for ind, s in enumerate(fields)]
    msg += "<br>".join(fields)
    return msg