import time
from numpy.random import randint
import matplotlib.pyplot as plt
import streamlit as st
def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def heapSize(A):
    return len(A) - 1

def MaxHeapify(A, i):
    l = left(i)
    r = right(i)
    if l <= heapSize(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= heapSize(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest)

def BuildMaxHeap(A):
    for i in range(int(heapSize(A) / 2) - 1, -1, -1):
        MaxHeapify(A, i)

def HeapSort(A):
    BuildMaxHeap(A)
    B = list()
    heapSize1 = heapSize(A)
    for i in range(heapSize(A), 0, -1):
        A[0], A[i] = A[i], A[0]
        B.append(A[heapSize1])
        A = A[:-1]
        heapSize1 = heapSize1 - 1
        MaxHeapify(A, 0)

def InsertHeap(A, key):
    A.append(key)
    i = len(A) - 1
    while i > 0 and A[(i - 1) // 2] < A[i]:
        A[(i - 1) // 2], A[i] = A[i], A[(i - 1) // 2]
        i = (i - 1) // 2

def DeleteHeap(A, key):
    try:
        i = A.index(key)
        A[i], A[-1] = A[-1], A[i]
        A.pop()
        MaxHeapify(A, i)
    except ValueError:
        pass

def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return QuickSort(left) + middle + QuickSort(right)

# Streamlit app
st.title('Sorting and Heap Operations Time Complexity Analysis')

# Button selection
option = st.selectbox(
    'Select the type of analysis:',
    ['Sorting Time Complexity', 'Insertion and Deletion Time Complexity']
)

elements = list()
heap_times = list()
merge_times = list()
quick_times = list()
heap_insert_times = list()
heap_delete_times = list()
merge_insert_times = list()
merge_delete_times = list()
quick_insert_times = list()
quick_delete_times = list()

if option == 'Sorting Time Complexity':
    for i in range(1, 10):
        a = randint(0, 1000 * i, 1000 * i)
        
        # Time Heap Sort
        heap_a = a.copy()
        start = time.perf_counter()
        HeapSort(heap_a)
        end = time.perf_counter()
        heap_times.append(end - start)
        
        # Time Merge Sort
        merge_a = a.copy()
        start = time.perf_counter()
        MergeSort(merge_a)
        end = time.perf_counter()
        merge_times.append(end - start)
        
        # Time Quick Sort
        quick_a = a.copy()
        start = time.perf_counter()
        quick_sorted = QuickSort(quick_a)
        end = time.perf_counter()
        quick_times.append(end - start)
        
        elements.append(len(a))
        st.write(f'{len(a)} Elements Sorted by HeapSort in {heap_times[-1]:.6f} seconds')
        st.write(f'{len(a)} Elements Sorted by MergeSort in {merge_times[-1]:.6f} seconds')
        st.write(f'{len(a)} Elements Sorted by QuickSort in {quick_times[-1]:.6f} seconds')

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(elements, heap_times, label='Heap Sort')
    ax.plot(elements, merge_times, label='Merge Sort')
    ax.plot(elements, quick_times, label='Quick Sort')
    ax.set_xlabel('List Length')
    ax.set_ylabel('Time Complexity')
    ax.legend()
    ax.grid()
    st.pyplot(fig)

elif option == 'Insertion and Deletion Time Complexity':
    for i in range(1, 10):
        a = randint(0, 1000 * i, 1000 * i).tolist()
        key_to_insert = randint(0, 1000 * i)
        key_to_delete = a[randint(0, len(a) - 1)]
        
        # Time Heap Insertion
        heap_a = a.copy()
        start = time.perf_counter()
        InsertHeap(heap_a, key_to_insert)
        end = time.perf_counter()
        heap_insert_times.append(end - start)
        
        # Time Heap Deletion
        start = time.perf_counter()
        DeleteHeap(heap_a, key_to_delete)
        end = time.perf_counter()
        heap_delete_times.append(end - start)
        
        # Time Merge Sort Insertion (with re-sorting)
        merge_a = a.copy()
        start = time.perf_counter()
        merge_a.append(key_to_insert)
        MergeSort(merge_a)
        end = time.perf_counter()
        merge_insert_times.append(end - start)
        
        # Time Merge Sort Deletion (with re-sorting)
        merge_a = a.copy()
        start = time.perf_counter()
        merge_a.remove(key_to_delete)
        MergeSort(merge_a)
        end = time.perf_counter()
        merge_delete_times.append(end - start)
        
        # Time Quick Sort Insertion (with re-sorting)
        quick_a = a.copy()
        start = time.perf_counter()
        quick_a.append(key_to_insert)
        quick_a = QuickSort(quick_a)
        end = time.perf_counter()
        quick_insert_times.append(end - start)
        
        # Time Quick Sort Deletion (with re-sorting)
        quick_a = a.copy()
        start = time.perf_counter()
        quick_a.remove(key_to_delete)
        quick_a = QuickSort(quick_a)
        end = time.perf_counter()
        quick_delete_times.append(end - start)
        
        elements.append(len(a))
        st.write(f'{len(a)} Elements - Heap Insertion in {heap_insert_times[-1]:.6f} seconds')
        st.write(f'{len(a)} Elements - Heap Deletion in {heap_delete_times[-1]:.6f} seconds')
        st.write(f'{len(a)} Elements - Merge Insertion in {merge_insert_times[-1]:.6f} seconds')
        st.write(f'{len(a)} Elements - Merge Deletion in {merge_delete_times[-1]:.6f} seconds')
        st.write(f'{len(a)} Elements - Quick Insertion in {quick_insert_times[-1]:.6f} seconds')
        st.write(f'{len(a)} Elements - Quick Deletion in {quick_delete_times[-1]:.6f} seconds')

    # Plotting
    fig, ax = plt.subplots()
    ax.plot(elements, heap_insert_times, label='Heap Insertion')
    ax.plot(elements, heap_delete_times, label='Heap Deletion')
    ax.plot(elements, merge_insert_times, label='Merge Insertion')
    ax.plot(elements, merge_delete_times, label='Merge Deletion')
    ax.plot(elements, quick_insert_times, label='Quick Insertion')
    ax.plot(elements, quick_delete_times, label='Quick Deletion')
    ax.set_xlabel('List Length')
    ax.set_ylabel('Time Complexity')
    ax.legend()
    ax.grid()
    st.pyplot(fig)
