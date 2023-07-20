import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction

# Req 2


def test_dish():
    # Alimentos do dicionário restriction_map()
    queijo_mussarela = Ingredient("queijo mussarela")
    bacon = Ingredient("bacon")
    creme_de_leite = Ingredient("creme de leite")

    lasanha_queijo = Dish("lasanha de queijo", 28.45)
    feijoada = Dish("feijoada", 35.80)

    assert lasanha_queijo.name == "lasanha de queijo"
    assert lasanha_queijo.price == 28.45
    assert lasanha_queijo.recipe == {}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("pizza", "25%")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("salada", 0)
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("arroz", -25)

    assert repr(lasanha_queijo) == "Dish('lasanha de queijo', R$28.45)"

    assert hash(lasanha_queijo) == hash("Dish('lasanha de queijo', R$28.45)")
    assert hash(lasanha_queijo) != hash(feijoada)
    assert hash(lasanha_queijo) == hash(Dish("lasanha de queijo", 28.45))

    assert (lasanha_queijo == lasanha_queijo) is True
    assert (lasanha_queijo == feijoada) is False
    assert (lasanha_queijo != feijoada) is True

    lasanha_queijo.add_ingredient_dependency(queijo_mussarela, 5)
    lasanha_queijo.add_ingredient_dependency(bacon, 15)
    lasanha_queijo.add_ingredient_dependency(creme_de_leite, 7)

    assert queijo_mussarela in lasanha_queijo.recipe
    assert bacon in lasanha_queijo.recipe
    assert creme_de_leite in lasanha_queijo.recipe

    assert lasanha_queijo.recipe[queijo_mussarela] == 5
    assert lasanha_queijo.recipe[bacon] == 15
    assert lasanha_queijo.recipe[creme_de_leite] == 7

    assert lasanha_queijo.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
        Restriction.ANIMAL_MEAT,
    }

    assert lasanha_queijo.get_ingredients() == {
        queijo_mussarela,
        bacon,
        creme_de_leite,
    }
