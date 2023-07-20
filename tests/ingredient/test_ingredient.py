from src.models.ingredient import Ingredient, Restriction


def test_ingredient_initialization():
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


def test_ingredient_hashes():
    salmao_ingredient = Ingredient("salmão")
    farinha_ingredient = Ingredient("farinha")
    manteiga_ingredient = Ingredient("manteiga")

    assert hash(salmao_ingredient) == hash("salmão")
    assert hash(farinha_ingredient) == hash("farinha")
    assert hash(manteiga_ingredient) == hash("manteiga")

    # Test if different ingredients have different hashes
    assert hash(manteiga_ingredient) != hash(salmao_ingredient)
    # Test if the same ingredient has the same hash
    assert hash(farinha_ingredient) == hash(Ingredient("farinha"))


def test_ingredient_equality():
    salmao_ingredient = Ingredient("salmão")
    farinha_ingredient = Ingredient("farinha")
    manteiga_ingredient = Ingredient("manteiga")
    tomate_ingredient = Ingredient("tomate")

    assert salmao_ingredient == salmao_ingredient
    assert manteiga_ingredient == Ingredient("manteiga")
    assert salmao_ingredient != farinha_ingredient
    assert tomate_ingredient != farinha_ingredient


def test_ingredient_repr():
    salmao_ingredient = Ingredient("salmão")
    farinha_ingredient = Ingredient("farinha")
    manteiga_ingredient = Ingredient("manteiga")
    tomate_ingredient = Ingredient("tomate")

    assert repr(salmao_ingredient) == "Ingredient('salmão')"
    assert repr(farinha_ingredient) == "Ingredient('farinha')"
    assert repr(manteiga_ingredient) == "Ingredient('manteiga')"
    assert repr(tomate_ingredient) == "Ingredient('tomate')"
