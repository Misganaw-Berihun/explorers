import os
import pytest
from model.explorer import Explorer
from errors import Missing, Duplicate
os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(
        name="yeti",
        country="CN",
        description="Harmless Himalayan"
        )


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)


def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("tur")


def test_modify(sample):
    sample.description = "Belete"
    resp = explorer.modify(sample)
    assert resp == sample


def test_modify_missing():
    thing: Explorer = Explorer(
        name="ere wegen",
        country="ET",
        description="kdj"
    )
    with pytest.raises(Missing):
        _ = explorer.modify(thing)


def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)
