import pytest
from pytesthomework.test_cal import Calculator


@pytest.fixture()
def get_start():
    print("【开始计算】")
    # 计算器类实例化
    cal = Calculator()
    yield cal
    print("【计算结束】")
