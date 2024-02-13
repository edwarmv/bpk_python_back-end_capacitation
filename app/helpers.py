from uuid import UUID


def is_valid_uuid(value: str) -> bool:
    try:
        UUID(str(value))
        return True
    except ValueError:
        return False
