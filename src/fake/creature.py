from model.creature import Creature


_creatures = [
    Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
    ),
    Creature(
        name="Bigfoot",
        description="Yeti's Cousin Eddie",
        country="US",
        area="*",
        aka="Sasquatch"
        ),
    ]


def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures


def get_one(name: str) -> Creature | None:
    """Return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially modify a creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace a creature"""
    return creature


def delete(name: str) -> bool:
    """Delete a creature"""
    return None
