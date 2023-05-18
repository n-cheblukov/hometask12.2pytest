from utils import dicts


def test_get_val(dicts_fixture):
    assert dicts.get_val(dicts_fixture, "марафон") == "гонка бегунов длиной около 26 миль"
    assert dicts.get_val(dicts_fixture, "vsc") == "git"
    assert dicts.get_val(dicts_fixture, "vsc", "miss") == "miss"
    assert dicts.get_val({}, "like", "common") == "common"
