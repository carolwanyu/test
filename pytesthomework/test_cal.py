import pytest
import yaml


# 被测代码：计算器
class Calculator:
    def code_add(self, a, b):
        return a + b

    def code_div(self, a, b):
        return a/b

# 打开yaml配置文件
def get_data():
    with open("data.yml") as f:
        data = yaml.safe_load(f)
        return data


class TestCal:
    def setup(self):
        # 计算器类实例化
        self.cal = Calculator()
        print("【开始计算】")

    def teardown(self):
        print("【计算结束】")

    # 测试数据参数化
    @pytest.mark.parametrize("a,b,result", get_data()["add"]["int"])
    def test_add_int(self, a, b, result):
        assert self.cal.code_add(a, b) == result

    @pytest.mark.parametrize("a,b,result", get_data()["add"]["float"])
    def test_add_float(self, a, b, result):
        # 浮点数相加，取两位小数。python小数相加是换算成二进制计算的，0.1+0.2的结果是0.30000000000000004
        assert round(self.cal.code_add(a, b), 2) == result

    # 测试数据参数化
    @pytest.mark.parametrize("a,b,result", get_data()["div"])
    def test_div(self, a, b, result):
        try:
            assert self.cal.code_div(a, b) == result
        # 捕获除数为0的异常
        except ZeroDivisionError:
            pass
        else:
            pass
