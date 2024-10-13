import typing as t
import collections.abc as c

def Hello(names: c.Iterable[str]) -> None:
    for name in names:
        print(name)


def main():
    Hello(['Ben', 'Kai', 'Lek'])

if __name__ == "__main__":
    main()

