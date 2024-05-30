import os
from model.creature import Creature

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as data
else:
    import data.creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Creature | None:
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def replace(id, creature: Creature) -> Creature:
    return data.replace(id, creature)


def modify(creature: Creature) -> Creature:
    return data.modify(creature)


def delete(name: str) -> bool:
    return data.delete(name)
