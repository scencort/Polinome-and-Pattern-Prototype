from linked_list import LinkedList
from node import Node


class Polynomial(LinkedList):
    """
    Класс «Полином», наследуется от односвязного списка.
    """

    def add_term(self, coef, power):
        """
        Добавление одночлена в полином.

        :coef: коэффициент
        :power: степень
        """
        if coef == 0:
            return

        tmp = Node(coef, power)

        if self.head is None or self.head.power < power:
            tmp.next = self.head
            self.head = tmp
            return

        prev = None
        cur = self.head

        while cur and cur.power > power:
            prev = cur
            cur = cur.next

        if cur and cur.power == power:
            cur.coef += coef
            if cur.coef == 0:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
        else:
            tmp.next = cur
            prev.next = tmp

    def __add__(self, other):
        """
        Сложение полиномов.
        """
        res = Polynomial()
        p1 = self.head
        p2 = other.head

        while p1 or p2:
            if p2 is None or (p1 and p1.power > p2.power):
                res.add_term(p1.coef, p1.power)
                p1 = p1.next
            elif p1 is None or p2.power > p1.power:
                res.add_term(p2.coef, p2.power)
                p2 = p2.next
            else:
                res.add_term(p1.coef + p2.coef, p1.power)
                p1 = p1.next
                p2 = p2.next

        return res

    def __mul__(self, other):
        """
        Умножение полиномов.
        """
        res = Polynomial()
        p1 = self.head

        while p1:
            p2 = other.head
            while p2:
                res.add_term(
                    p1.coef * p2.coef,
                    p1.power + p2.power
                )
                p2 = p2.next
            p1 = p1.next

        return res

    def __eq__(self, other):
        """
        Сравнение полиномов.
        """
        p1 = self.head
        p2 = other.head

        while p1 and p2:
            if p1.coef != p2.coef or p1.power != p2.power:
                return False
            p1 = p1.next
            p2 = p2.next

        return p1 is None and p2 is None

    def diff(self):
        """
        Дифференцирование полинома.
        """
        res = Polynomial()
        cur = self.head

        while cur:
            if cur.power != 0:
                res.add_term(
                    cur.coef * cur.power,
                    cur.power - 1
                )
            cur = cur.next

        return res

    def __str__(self):
        """
        Преобразование полинома в строку.
        """
        if self.head is None:
            return "0"

        s = ""
        cur = self.head

        while cur:
            if cur.power == 0:
                part = f"{cur.coef}"
            elif cur.power == 1:
                part = f"{cur.coef}x"
            else:
                part = f"{cur.coef}x^{cur.power}"

            if s:
                s += " + " + part
            else:
                s = part

            cur = cur.next

        return s