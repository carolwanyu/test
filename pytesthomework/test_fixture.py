import pytest
import yaml


# 打开yaml配置文件
def get_yaml_data(name):
    with open("data.yml") as f:
        yaml_data = yaml.safe_load(f)
        data = yaml_data[name]
        return data


# 被测除法参数化
@pytest.fixture(params=get_yaml_data("div"))
def get_div_data(request):
    return request.param


# 被测加法参数化
@pytest.fixture(params=get_yaml_data("add")["int"])
def get_add_int_data(request):
    return request.param


@pytest.fixture(params=get_yaml_data("add")["float"])
def get_add_float_data(request):
    return request.param


class Calculator:
    def code_add(self, a, b):
        return a + b

    def code_div(self, a, b):
        return a / b


# 被测代码：计算器
class TestCal:

    def test_add_int(self, get_start, get_add_int_data):
        assert get_start.code_add(get_add_int_data[0], get_add_int_data[1]) == get_add_int_data[2]

    def test_add_float(self, get_start, get_add_float_data):
        # 浮点数相加，取两位小数。python小数相加是换算成二进制计算的，0.1+0.2的结果是0.30000000000000004
        assert round(get_start.code_add(get_add_float_data[0], get_add_float_data[1]), 2) == get_add_float_data[2]

    def test_div(self, get_start, get_div_data):
        try:
            assert get_start.code_div(get_div_data[0], get_div_data[1]) == get_div_data[2]
        # 捕获除数为0的异常
        except ZeroDivisionError:
            pass
        else:
            pass
