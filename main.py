import random
from polynomial import Polynomial


def random_poly(count=5, max_pow=5):
    """
    Создание случайного полинома.
    """
    p = Polynomial()

    for _ in range(count):
        coef = random.randint(-5, 5)
        power = random.randint(0, max_pow)
        p.add_term(coef, power)

    return p


if __name__ == "__main__":
    p1 = random_poly()
    p2 = random_poly()

    print("Polynome 1 =", p1)
    print("Polynome 2 =", p2)

    print("\nPolynome 1 + Polynome 2 =", p1 + p2)
    print("Polynome 1 * Polynome 2 =", p1 * p2)

    print("\nPolynome 1' =", p1.diff())
    print("Polynome 2' =", p2.diff())

    print("\nPolynome 1 == Polynome 2 ?", p1 == p2)