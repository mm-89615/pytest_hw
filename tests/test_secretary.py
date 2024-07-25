import pytest

from secretary import get_name, get_directory, add


class TestSecretary:
    def setup_method(self) -> None:
        self.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
            {"type": "driver license", "number": "5455 028765",
             "name": "Василий Иванов"},
        ]

        self.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    @pytest.mark.parametrize(
        "doc_number, expected",
        [
            ("10006", "Аристарх Павлов"),
            ("101", "Документ не найден")
        ]
    )
    def test_get_name_by_number(self, doc_number, expected):
        assert get_name(self.documents, doc_number) == expected

    @pytest.mark.parametrize(
        "doc_number, expected",
        [
            ("11-2", "1"),
            ("311 020204", "Полки с таким документом не найдено")
        ]
    )
    def test_get_directory(self, doc_number, expected):
        assert get_directory(self.directories, doc_number) == expected

    @pytest.mark.parametrize(
        "document_type, number, name, shelf_number",
        [
            ("international passport", "311 020203", "Александр Пушкин", 3),
        ]
    )
    def test_add(self, document_type, number, name, shelf_number):
        add(self.documents, self.directories, document_type, number, name, shelf_number)
        assert get_name(self.documents, number) == name
        assert get_directory(self.directories, number) == shelf_number
