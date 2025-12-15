from node import Node


class LinkedList:
    """
    Базовый класс односвязного списка.
    """

    def __init__(self):
        """
        Создание пустого списка.
        """
        self.head = None

    def is_empty(self):
        """
        Проверка списка на пустоту.

        :return: True, если список пуст
        """
        return self.head is None