from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1 - init
def test_ingredient():
    pass
    salmao_ingredient = Ingredient("salmão")
    farinha_ingredient = Ingredient("farinha")
    manteiga_ingredient = Ingredient("manteiga")
    tomate_ingredient = Ingredient("tomate")

    assert salmao_ingredient.name == "salmão"
    assert manteiga_ingredient.name == "manteiga"
    assert farinha_ingredient.name == "farinha"
    assert tomate_ingredient.name == "tomate"

    assert salmao_ingredient.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_MEAT,
    }
    assert manteiga_ingredient.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }
    assert farinha_ingredient.restrictions == {Restriction.GLUTEN}
    assert tomate_ingredient.restrictions == set()

    assert hash(salmao_ingredient) == hash("salmão")
    assert hash(farinha_ingredient) == hash("farinha")
    assert hash(manteiga_ingredient) == hash("manteiga")
    assert hash(tomate_ingredient) == hash("tomate")

    assert hash(manteiga_ingredient) != hash(salmao_ingredient)
    assert hash(farinha_ingredient) == hash(Ingredient("farinha"))

    assert (salmao_ingredient == farinha_ingredient) is False
    assert (manteiga_ingredient == Ingredient("manteiga")) is True
    assert (salmao_ingredient == salmao_ingredient) is True
    assert (tomate_ingredient != farinha_ingredient) is True

    assert repr(salmao_ingredient) == "Ingredient('salmão')"
    assert repr(farinha_ingredient) == "Ingredient('farinha')"
    assert repr(manteiga_ingredient) == "Ingredient('manteiga')"
    assert repr(tomate_ingredient) == "Ingredient('tomate')"
