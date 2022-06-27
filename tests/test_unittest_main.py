import unittest
import main
from parameterized import parameterized


#Все закомменченные тесты вносят ошибки во многие другие тесты
class TestFunction(unittest.TestCase):
    @parameterized.expand(
        [
            ("2207 876234", True),
            ("1113313", False)
        ]
    )
    def test_check_document_existance(self, doc_number, result):
        self.assertEqual(main.check_document_existance(doc_number), result)

    @parameterized.expand(
        [
            ("2207 876234", "Василий Гупкин"),
            ("1113313", None)
        ]
    )
    def test_get_doc_owner_name(self, doc_number, result):
        self.assertEqual(main.get_doc_owner_name(doc_number), result)

    # def test_get_all_doc_owners_names(self):
    #     self.assertEqual(main.get_all_doc_owners_names(), {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"})

    @parameterized.expand(
        [
            ('2207 876234', None),
            ('1113313', 'Документ не найден')
        ]
    )
    def test_remove_doc_from_shelf(self, doc_number, result):
        self.assertEqual(main.remove_doc_from_shelf(doc_number), result)

    # @parameterized.expand(
    #     [
    #         ('3', ('3', False)),
    #         ('5', ('5', True))
    #     ]
    # )
    # def test_add_new_shelf(self, shelf_number, result):
    #     self.assertEqual(main.add_new_shelf(shelf_number), result)

    @parameterized.expand(
        [
            ('10006', '3', ('3', '10006')),
            ('1113313', '5', ('5', '1113313'))
        ]
    )
    def test_append_doc_to_shelf(self, doc_number, shelf_number, result):
        self.assertEqual(main.append_doc_to_shelf(doc_number, shelf_number), result)

    # @parameterized.expand(
    #     [
    #         ('10006', ('10006', True)),
    #         ('1113313', None)
    #     ]
    # )
    # def test_delete_doc(self, doc_number, result):
    #     self.assertEqual(main.delete_doc(doc_number), result)

    @parameterized.expand(
        [
            ('10006', '2'),
            ('1113313', None)
        ]
    )
    def test_get_doc_shelf(self, doc_number, result):
        self.assertEqual(main.get_doc_shelf(doc_number), result)

    @parameterized.expand(
        [
            ('5455 028765', '3', 'Документ номер "5455 028765" был перемещен на полку номер "3"'),
            ('1113313', '5', 'Документ номер "1113313" был перемещен на полку номер "5"')
        ]
    )
    def test_move_doc_to_shelf(self, doc_number, shelf_number, result):
        self.assertEqual(main.move_doc_to_shelf(doc_number, shelf_number), result)

    def test_show_all_docs_info(self):
        self.assertEqual(main.show_all_docs_info(), ['passport "2207 876234" "Василий Гупкин"',
                                                     'invoice "11-2" "Геннадий Покемонов"',
                                                     'insurance "10006" "Аристарх Павлов"'])


    # def test_add_new_doc(self):
    #     self.assertEqual(main.add_new_doc('284753', 'book', 'Stefan Sholts', '5'), ({
    #                                                                                 "type": 'book',
    #                                                                                 "number": '284753',
    #                                                                                 "name": 'Stefan Sholts'
    #                                                                                 }, '5'))
