from model.explorer import Explorer

_explorers = [
    Explorer(
        name="Claude Hande",
        country="FR",
        description="Scarce during full moons"
    ),
    Explorer(
        name="Noah Weiser",
        country="DE",
        description="Myopic machete man"
        ),
]


def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        print(_explorer.name, name)
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """partially modify an explorere"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """completely replace an explorer"""
    return explorer


def delete(name: str) -> bool:
    """Delete an explorer; return none if it existed"""
    return None
