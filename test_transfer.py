import unittest
from gen_json import transfer
import common  # 导入依赖模块

class TestTransferFunction(unittest.TestCase):
    def test_string_conversion(self):
        """测试字符串类型转换"""
        # 数字转字符串（带引号）
        self.assertEqual(transfer(123, "string"), "123")
        # 字符串直接返回
        self.assertEqual(transfer("test", "string"), "test")
        # 布尔值转字符串
        self.assertEqual(transfer(True, "string"), "True")

    def test_int_slice_conversion(self):
        """测试整数切片类型转换"""
        # 单个数字转列表
        self.assertEqual(transfer(456, "int[]"), [456])
        # 逗号分隔字符串转混合类型列表
        self.assertEqual(transfer("7,8.5,9", "int[]"), [7, 8.5, 9])
        # 空字符串处理
        self.assertEqual(transfer("", "int[]"), [])

    def test_numeric_conversion(self):
        """测试数值类型转换"""
        # 整数转换
        self.assertEqual(transfer("100", "int"), 100)
        # 浮点数转换
        self.assertEqual(transfer("3.14", "float"), 3.14)
        # 数值字符串自动识别
        self.assertEqual(transfer("123.45", "unknown"), 123.45)

    def test_boolean_conversion(self):
        """测试布尔值类型转换"""
        self.assertEqual(transfer("true", "bool"), True)
        self.assertEqual(transfer("False", "bool"), False)
        # 非布尔字符串保持原样
        self.assertEqual(transfer("yes", "bool"), "yes")

if __name__ == '__main__':
    unittest.main()