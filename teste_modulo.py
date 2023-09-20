import date_main
import unittest
import date_dif




class TestFatorial(unittest.TestCase):
    #Data time checking
    def test_input_value_type(self):
        self.assertEqual(date_dif.diferenca_date_console("27 de março de 2023 - 27 de março de 2024"), 366)
        #self.assertEqual(date_dif.diferenca_date_console(), )

    def test_input_value(self):
        self.assertEqual(date_dif.diferenca_date_console(" 7 de março de 2023-27 de março de 2024 "), 366)
        
    def test_input_value_form(self):   
        #self.assertEqual(date_dif.diferenca_date_console("7 de março de 2023-27 de março de 2024 "), 366)
        self.assertRaises(TypeError, date_dif.diferenca_date_console, "oi")




if __name__ == "__main__":
    unittest.main()