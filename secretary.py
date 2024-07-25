documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765",
     "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(docs: list[dict], doc_number: str) -> str:
    for i in range(len(docs)):
        if doc_number == docs[i]['number']:
            return docs[i]['name']
    return "Документ не найден"


def get_directory(dirs: dict, doc_number: str) -> str:
    for i in dirs:
        if doc_number in dirs[i]:
            return i
    return "Полки с таким документом не найдено"


def add(docs: list[dict],
        dirs: dict,
        document_type: str, 
        number: str,
        name: str,
        shelf_number: int) -> None:
    docs.append({'type': document_type, 'number': number, 'name': name})
    dirs[shelf_number] = number


if __name__ == '__main__':
    print(get_name(documents, "10006"))
    print(get_directory(directories, "11-2"))
    print(get_name(documents, "101"))
    add(documents, directories, 'international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory(directories, "311 020203"))
    print(get_name(documents, "311 020203"))
    print(get_directory(directories, "311 020204"))
