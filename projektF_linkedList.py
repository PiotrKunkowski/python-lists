# -*- coding: utf-8 -*-
 
class Node:
    '''
   Klasa Node przechowuje aktualnie rozpatrywany element oraz element następny.
   Zawiera też funkcje pozwalające na manipulację danymi.
   '''
    def __init__(self, data):
        self.data = data
        self.next = None
 
    def __str__(self):
        return str(self.data)
 
    def getData(self):
        return self.data
 
    def getNext(self):
        return self.next
 
    def setData(self, newdata):
        self.data = newdata
 
    def setNext(self, newnext):
        self.next = newnext
 
 
class PriorityQueueLinkedList:
    '''
   Klasa implementująca kolejkę priorytetową na liscie z dowiązaniami.
   '''
 
    # inicjator klasy
    def __init__(self):
        self.queue = []
        self.head = Node(self)
 
    # wywietla zawartosć kolejki
    # tworzy pustą listę queue do której dodaje aktualny element przechowywany w klasie Node
    def __str__(self):
        queue = []
        current = self.head
        while current.next != None:
            # iteruje dopóki nie znajdzie elementu, który nie ma następcy
            # w liscie z dowiązaniami wiemy, że doszlismy do końca kiedy element nie będzie wskazywal na żaden następny
            current = current.next
            queue.append(current.data)
        return str(queue)
 
    # sprawdza czy koeljka jest pusta
    def is_empty(self):
        if len(self.queue) == 0:
            print('kolejka jest pusta')
        return self.queue == []
 
    # dodaje element do kolejki (na koniec)
    def enqueue(self, item):
        new_node = Node(item)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        self.queue.append(new_node)
        return self.queue
 
    # usuwa z kolejki największy element przez porównywanie kolejnych elementów z największym dotychczas znalezionym
    def dequeue(self):
        ptr = self.head.next
        max = ptr.data
        while ptr != None:
            if ptr.data > max:
                max = ptr.data
            ptr = ptr.next
 
        prev = self.head
        ptr = self.head.next
        while ptr != None:
            if ptr.data == max:
                prev.next = ptr.next
                break
            prev = ptr
            ptr = ptr.next
 
    # liczy rozmiar kolejki patrząc ile razy wykona się pętla while dopóki nie napotka na ostatni element
    def size(self):
        current = self.head
        total_size = 0
        while current.next != None:
            total_size += 1
            current = current.next
        return total_size
 
 
#testy poprawnosci funkcji:    
if __name__ == '__main__':
    print("______TEST POPRAWNOSCI IMPLEMENTACJI________")
    myQueue = PriorityQueueLinkedList()
    assert(myQueue.is_empty()==1), 'zle sprawdza czy jest pusta'
    myQueue.enqueue(1)
    myQueue.enqueue(5)
    myQueue.enqueue(2)
    myQueue.enqueue(4)
    assert(myQueue.is_empty()==0), 'zle sprawdza czy jest pusta'
    assert((myQueue.size())==4), 'zle sprawdza rozmiar'
    print('Przed usunieciem elementu: ' + str(myQueue))
    myQueue.dequeue()
    print('Po usunieciu elementu: ' + str(myQueue))
    assert((myQueue.size())==3), 'nie usuwa elementu z kolejki'
    print("____________________________________________")