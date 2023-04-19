"""Здесь надо написать тесты с использованием pytest для модуля item."""
# from src.item import calculate_total_price
import pytest
from src.item import Item


def test_calculate_total_price():
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert 10000 * Item.pay_rate == 8000.0


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item1_calculate_total_price(item1):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item1.calculate_total_price() == 'Общая стоимость Смартфон в магазине составляет: 200000'


def test_item1_apply_discount(item1):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item1.apply_discount() == 'Цена с учетом скидки 19% составляет 8000.0'


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_item2_calculate_total_price(item2):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item2.calculate_total_price() == 'Общая стоимость Ноутбук в магазине составляет: 100000'


def test1_item2_apply_discount(item2):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item2.apply_discount() == 'Цена с учетом скидки 19% составляет 16000.0'
