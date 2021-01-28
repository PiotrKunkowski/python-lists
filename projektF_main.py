# -*- coding: utf-8 -*-

import random
import time
import matplotlib.pyplot as plt
import projektF_list as lis
import projektF_maxheap as maxheap
import projektF_linkedList as linked

'''
Każda z funkcji wykonuje pomiar czasu jaki przebiega od początku do końca tworzenia kolejki
priorytetowej dla rozmiarów od 2^10 do 2^16. 
'''

def normal_list_queue(): 
    i = 10
    my_time1 = []
    my_time2 = []
    n_list = []
    while i <= 16:
        n = 2**i
        n_list.append(n)
        start_c = time.time() #czas rozpoczęcia tworzenia kolejki
        myQueue = lis.PriorityQueueList()
        for a in range(2**i):
            myQueue.enqueue(random.randint(1,1000))
        finish_c = time.time() #czas zakończenia tworzenia kolejki
        
        start_f = time.time() #czas rozpoczęcia usuwania elementów z listy
        for a in range(2**i):
            myQueue.dequeue()
        finish_f = time.time() #czas zakończenia usuwania elementów z listy
        
        i+=1
        time_of_iteration = finish_c-start_c
        time_of_deletion = finish_f-start_f
        my_time1.append(time_of_iteration)
        my_time2.append(time_of_deletion)
    print('\nczas wykonania kolejnych iteracji dla listy Pythona: ', my_time1)
    print('\nczas usuwania kolejnych iteracji dla listy Pythona: ', my_time2)
    return (my_time1, my_time2, n_list)   

def maxheap_queue(): 
    i = 10
    my_time1 = []
    my_time2 = []
    n_maxheap = []
    while i <= 16:
        n = 2**i
        n_maxheap.append(n)
        start_c = time.time() #czas rozpoczęcia tworzenia kolejki
        myQueue = maxheap.PriorityQueueMaxHeap()
        for a in range(2**i):
            myQueue.enqueue(random.randint(1,1000))
        finish_c = time.time() #czas zakończenia tworzenia kolejki
        
        start_f = time.time() #czas rozpoczęcia usuwania elementów z listy
        for a in range(2**i):
            myQueue.dequeue()
        finish_f = time.time() #czas zakończenia usuwania elementów z listy
        
        i+=1
        time_of_iteration = finish_c-start_c
        time_of_deletion = finish_f-start_f
        my_time1.append(time_of_iteration)
        my_time2.append(time_of_deletion)
    print('\nczas wykonania kolejnych iteracji dla kopca max: ', my_time1)
    print('\nczas usuwania kolejnych iteracji dla kopca max: ', my_time2)
    return (my_time1, my_time2, n_maxheap)    

def linked_list_queue():
    i = 10
    my_time1 = []
    my_time2 = []
    n_linked = []
    while i <= 16:
        n = 2**i
        n_linked.append(n)
        start_c = time.time() #czas rozpoczęcia tworzenia kolejki
        myQueue = linked.PriorityQueueLinkedList()
        for a in range(2**i):
            myQueue.enqueue(random.randint(1,1000))
        finish_c = time.time() #czas zakończenia tworzenia kolejki
        
        start_f = time.time() #czas rozpoczęcia usuwania elementów z listy
        for a in range(2**i):
            myQueue.dequeue()
        finish_f = time.time() #czas zakończenia usuwania elementów z listy
        
        i+=1
        time_of_iteration = finish_c-start_c
        time_of_deletion = finish_f-start_f
        my_time1.append(time_of_iteration)
        my_time2.append(time_of_deletion)
    print('\nczas wykonania kolejnych iteracji dla listy z dowiazaniami: ', my_time1)
    print('\nczas usuwania kolejnych iteracji dla listy z dowiazaniami: ', my_time2)
    return (my_time1, my_time2, n_linked)


list_enqueue, list_dequeue, n_list = normal_list_queue()
maxheap_enqueue, maxheap_dequeue, n_maxheap = maxheap_queue()
linked_enqueue, linked_dequeue, n_linked = linked_list_queue()

plt.loglog(n_list, list_enqueue, basex = 2, basey = 2, color = 'b')
plt.loglog(n_maxheap, maxheap_enqueue, basex = 2, basey = 2, color = 'g')
plt.loglog(n_linked, linked_enqueue, basex = 2, basey = 2, color = 'r')
plt.title('Zlogarytmowany czas doodawania elementow z kolejki w poszczegolnych strukturach danych')
plt.xlabel('liczba elementów')
plt.ylabel('log(czas)')
plt.legend(['lista', 'kopiec max', 'lista z dowiązaniami'], loc='upper left')
plt.show()

plt.loglog(n_list, list_dequeue, basex = 2, basey = 2, color = 'b')
plt.loglog(n_maxheap, maxheap_dequeue, basex = 2, basey = 2, color = 'g')
plt.loglog(n_linked, linked_dequeue, basex = 2, basey = 2, color = 'r')
plt.title('Zlogarytmowany czas usuwania elementow z kolejki w poszczegolnych strukturach danych')
plt.xlabel('liczba elementów')
plt.ylabel('log(czas)')
plt.legend(['lista', 'kopiec max', 'lista z dowiązaniami'], loc='upper left')
plt.show()


