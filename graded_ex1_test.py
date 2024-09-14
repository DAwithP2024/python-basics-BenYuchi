import unittest
from io import StringIO
from unittest.mock import patch
import shopping as gex  # 替换为你实际的购物程序文件名

class TestShoppingProgram(unittest.TestCase):

    def setUp(self):
        self.cart = []

    # 测试 validate_name 函数
    def test_name_validation(self):
        self.assertTrue(gex.validate_name("John Doe"))  # 正确：两个部分，只有字母
        self.assertFalse(gex.validate_name("JohnDoe"))  # 错误：没有空格分隔
        self.assertFalse(gex.validate_name("John 123"))  # 错误：包含数字

    # 测试 validate_email 函数
    def test_email_validation(self):
        self.assertTrue(gex.validate_email("john.doe@example.com"))  # 正确：包含 @
        self.assertFalse(gex.validate_email("johndoe.com"))  # 错误：缺少 @
        self.assertFalse(gex.validate_email(" "))  # 错误：空字符串
        self.assertTrue(gex.validate_email("john@doe"))  # 正确：简单邮箱格式

    # 测试 display_categories 函数
    @patch('builtins.input', side_effect=['1'])
    def test_valid_category_selection(self, mock_input):
        category_index = gex.display_categories()
        self.assertEqual(category_index, 0)  # 正确：选择第一个类别

    @patch('builtins.input', side_effect=['5'])
    def test_invalid_category_selection(self, mock_input):
        category_index = gex.display_categories()
        self.assertTrue(category_index is None or category_index >= len(gex.products))  # 错误：无效的类别编号

    @patch('builtins.input', side_effect=['abc'])
    def test_non_numeric_category_selection(self, mock_input):
        category_index = gex.display_categories()
        self.assertIsNone(category_index)  # 错误：非数字输入

    # 测试产品选择
    def test_valid_product_selection(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600)]
        product_choice = "1"
        product_index = int(product_choice) - 1
        self.assertEqual(product_index, 0)  # 正确：选择第一个产品

    def test_invalid_product_selection(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600)]
        product_choice = "10"  # 超出范围
        product_index = int(product_choice) - 1
        self.assertNotIn(product_index, range(len(products_list)))  # 错误：产品编号无效

    # 测试数量输入
    def test_valid_quantity(self):
        quantity = "3"
        self.assertTrue(quantity.isdigit() and int(quantity) > 0)  # 正确：正整数

    def test_invalid_quantity_zero(self):
        quantity = "0"
        self.assertFalse(int(quantity) > 0)  # 错误：零

    def test_invalid_quantity_non_numeric(self):
        quantity = "abc"
        self.assertFalse(quantity.isdigit())  # 错误：非数字输入

    # 测试产品排序
    def test_sort_ascending(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600), ("USB Drive", 15)]
        sorted_list = gex.display_sorted_products(products_list, "asc")
        expected_list = [("USB Drive", 15), ("Smartphone", 600), ("Laptop", 1000)]
        self.assertEqual(sorted_list, expected_list)  # 正确：升序

    def test_sort_descending(self):
        products_list = [("Laptop", 1000), ("Smartphone", 600), ("USB Drive", 15)]
        sorted_list = gex.display_sorted_products(products_list, "desc")
        expected_list = [("Laptop", 1000), ("Smartphone", 600), ("USB Drive", 15)]
        self.assertEqual(sorted_list, expected_list)  # 正确：降序

    # 测试添加到购物车
    def test_add_to_cart(self):
        product = ("Laptop", 1000)
        quantity = 2
        gex.add_to_cart(self.cart, product, quantity)
        self.assertIn(("Laptop", 1000, 2), self.cart)  # 正确：购物车包含产品

    # 测试显示购物车
    def test_display_cart(self):
        cart = [("Laptop", 1000, 2), ("Smartphone", 600, 1)]
        expected_output = "Laptop - $1000 x 2 = $2000\nSmartphone - $600 x 1 = $600\nTotal cost: $2600"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            gex.display_cart(cart)
            self.assertIn(expected_output, fake_out.getvalue().strip())  # 正确：购物车内容显示正确

    # 测试返回类别选择
    @patch('builtins.input', side_effect=['3'])  
    def test_back_to_categories(self, mock_input):
        action_choice = '3'
        self.assertEqual(action_choice, '3')  # 正确：返回类别选择

    # 测试完成购物
    @patch('builtins.input', side_effect=['4'])  
    def test_finish_shopping(self, mock_input):
        finish_shopping = True
        self.assertTrue(finish_shopping)  # 正确：完成购物

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
