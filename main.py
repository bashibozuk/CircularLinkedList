from linked_list import CircularLinkedList


def main():
    cll = CircularLinkedList()

    cll.append(0)
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)

    for val in cll:
        print(val.value)

    cll.delete(2)

    for val in cll:
        print(val.value, val.deleted)

if __name__ == '__main__':
    main()
