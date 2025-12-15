class Node:
    """
    Узел односвязного списка
    """

    def __init__(self, coef, power):
        """
        Создание узла.

        :coef: коэффициент
        :power: степень
        """
        self.coef = coef
        self.power = power
        self.next = None