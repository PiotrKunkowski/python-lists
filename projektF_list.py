# -*- coding: utf-8 -*-

class PriorityQueueList:
    '''
    Klasa implementująca kolejkę priorytetową na liscie Pythona.
    Kolejka priorytetowa jest to kolejka, która oprócz wartosci elementów przechowuje też ich priorytet.
    W pierwszej kolejnosci usuwane są elementy z najwyższym priorytetem.
    Jesli dwa elementy mają ten sam priorytet to pierwszy zostanie usuniety ten, ktory jako pierwszy
    zostal dodany do kolejki (first in - forst out).
    '''
    #inicjator klasy
    def __init__(self):
        self.queue = []
    
    #wywietla zawartosć kolejki    
    def __str__(self): 
        return str(self.queue)
    
    #sprawdza czy koeljka jest pusta
    def is_empty(self):
        if len(self.queue) == 0:
            print ('kolejka jest pusta')
        return self.queue == []
    
    #dodaje element do kolejki (na koniec) 
    def enqueue(self, item): 
        self.queue.append(item) 
  
    #usuwa z kolejki element o najwyższym priorytecie (największy element)
    def dequeue(self): 
        try: 
            priority = 0
            for i in range(len(self.queue)):
                #iteruje po elementach kolejki
                if self.queue[i] > self.queue[priority]: 
                    #szuka elementu o najwyższym priorytecie
                    priority = i
            item = self.queue[priority]
            del self.queue[priority] 
            return item 
        except IndexError: 
            print('operacja dequeue nie powiodla sie') 
            exit()
    
    def size(self):
        return len(self.queue)

#testy poprawnosci funkcji:    
if __name__ == '__main__':
    print("______TEST POPRAWNOSCI IMPLEMENTACJI________")
    myQueue = PriorityQueueList()
    assert(myQueue.is_empty()==1), 'zle sprawdza czy jest pusta'
    myQueue.enqueue(1)
    myQueue.enqueue(5)
    myQueue.enqueue(2)
    myQueue.enqueue(4)
    assert(myQueue.is_empty()==0), 'zle sprawdza czy jest pusta'
    assert((myQueue.size())==4), 'zle sprawdza rozmiar'
    print('Przed usunieciem elementu: ' + str(myQueue))
    assert(myQueue.dequeue()==5), 'zle usuwa element z kolejki'
    print('Po usunieciu elementu: ' + str(myQueue))
    assert((myQueue.size())==3), 'nie usuwa elementu z kolejki'
    print("____________________________________________")

