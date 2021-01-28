# -*- coding: utf-8 -*-

class PriorityQueueMaxHeap:
    '''
    Klasa implementująca kolejkę priorytetową na kopcu max.
    Kopiec max jest to struktura drzewa binarnego, w której każdy node jest mniejszy lub równy co jego rodzic.
    Elementy do kopca dodajemy jako liscie, a następnie przesuwamy je wgłąb drzewa porównując ich wartosć z
    wartosciami rodzica.
    Wyciąganie elementów z kopca polega na usunięciu korzenia (zawsze największy element), 
    a następnie uporządkowaniu drzewa.
    '''
    #inicjator klasy
    def __init__(self):
        self.maxheap = []
        if __name__ == '__main__':
            print("Konstruktor klasy zostal stworzony")
        
     #destruktor klasy    
    def __del__(self):
        self.maxheap.clear()
        if __name__ == '__main__':
            print("Destruktor klasy zostal stworzony")
    
    def __str__(self): 
        return str(self.maxheap)
    
    #sprawdza czy koeljka jest pusta
    def is_empty(self):
        if len(self.maxheap) == 0:
            print ('kolejka jest pusta')
        return self.maxheap == []
    
    #dodaje do kolejki element i umieszcza go na końcu kolejki
    #następnie używa funkcji element_up(), żeby umiescic element we wlasciwym miejscu na drzewie
    def enqueue(self, item):
        self.maxheap.append(item)
        self.element_up(len(self.maxheap) - 1)
                    
    #pobiera element o najwiekszym kluczu (z korzenia kopca), zwraca jego wartosc i usuwa go z kopca
    def dequeue(self):
        if len(self.maxheap) >= 2:
            self.swap(0, len(self.maxheap)-1) #zamieniamy miejscami pierwszy (największy) element z ostatnim w kolejce
            root=self.maxheap.pop()
            self.element_down(0)
        elif len(self.maxheap) == 2:
            root=self.maxheap.pop()
        else:
            return False
        return root
    
    #zamienia miejscami elementy i oraz j
    def swap(self, i, j):
        self.maxheap[i], self.maxheap[j] = self.maxheap[j], self.maxheap[i]
    
    #daje możliwosć "podejrzenia" pierwszego elementu
    def peek(self):
        if self.maxheap[0]:
            return self.maxheap[0]
        else: #w przypadku kiedy kolejka jest pusta
            return False 

    #wyciąga wybrany element ze stosu
    def __getitem__(self, item):
        return self.maxheap[item]
    
    #zwraca długosć kolejki
    def size(self):
        return len(self.maxheap)   
    
    def element_up(self, index):
        '''po dolaczeniu nowego elementu do kolejki naprawia kopiec max od dolu,
        aby najwieksze wartosci znajdowaly sie w korzeniu, a najmniejsze w lisciach'''
        assert index >= 0, "indeks elementu nie moze byc ujemny"
        parent = index//2 # wyrazenie zwracajace indeks ojca elementu w kopcu max
        while index > 0 and self.maxheap[index] > self.maxheap[parent]:
            #jesli nasz element jest wiekszy niż jego rodzic przenosi go w góre drzewa aż znajdzie własciwa pozycje
            self.swap(index, parent)
            self.element_up(parent)  #funkcja rekurencyjnie wywołuje się dopóki element nie znajdzie się na własciwej pozycji
    
    def element_down(self, index):
        '''po usunieciu elementu z korzenia kolejki naprawia kopiec max od gory,
        aby najwieksze wartosci znajdowaly sie w korzeniu, a najmniejsze w lisciach'''
        assert index >= 0, "indeks elementu nie moze byc ujemny"
        left = 2*index+1 #indeks lewego syna elementu
        right = 2*index+2 #indeks prawego syna elementu
        largest = index
        #porównujemy indeks naszego elementu do jego lewego i prawego dziecka, aby stwierdzić który jest największy 
        if len(self.maxheap) > left and self.maxheap[largest] < self.maxheap[left]:
            largest=left #przypizuje zmiennej 
        if len(self.maxheap) > right and self.maxheap[largest] < self.maxheap[right]:
            largest=right
        if largest != index:
            self.swap(index, largest)
            self.element_down(largest)

    
#testy poprawnosci funkcji:    
if __name__ == '__main__':
    print("______TEST POPRAWNOSCI IMPLEMENTACJI________")
    myQueue = PriorityQueueMaxHeap()
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
