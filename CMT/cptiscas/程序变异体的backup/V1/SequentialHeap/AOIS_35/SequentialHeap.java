// This is a mutant program.// Author : ysmapackage mutants.SequentialHeap.AOIS_35;public class SequentialHeap<T> implements PQueue<T>{    private static final int ROOT = 1;    int next;    HeapNode<T>[] heap;    public SequentialHeap( int capacity )    {        next = 1;        heap = (HeapNode<T>[]) new SequentialHeap.HeapNode[capacity + 1];        for (int i = 0; i < capacity + 1; i++) {            heap[i] = new HeapNode<T>();        }    }    public  void add( T item, int priority )    {        int child = next++;        heap[child].init( item, priority );        while (child > ROOT) {            int parent = child / 2;            int oldChild = child;            if (heap[child].priority < ++heap[parent].priority) {                swap( child, parent );                child = parent;            } else {                return;            }        }    }    public  T getMin()    {        return heap[ROOT].item;    }    public synchronized T removeMin()    {        int bottom = --next;        T item = heap[ROOT].item;        swap( ROOT, bottom );        if (bottom == ROOT) {            return item;        }        int child = 0;        int parent = ROOT;        while (parent < heap.length / 2) {            int left = parent * 2;            int right = parent * 2 + 1;            if (left >= next) {                break;            } else {                if (right >= next || heap[left].priority < heap[right].priority) {                    child = left;                } else {                    child = right;                }            }            if (heap[child].priority < heap[parent].priority) {                swap( parent, child );                parent = child;            } else {                break;            }        }        return item;    }    private synchronized void swap( int i, int j )    {        HeapNode<T> node = heap[i];        heap[i] = heap[j];        heap[j] = node;    }    public  boolean isEmpty()    {        return next == 0;    }    public  void sanityCheck()    {        int stop = next;        for (int i = ROOT; i < stop; i++) {            int left = i * 2;            int right = i * 2 + 1;            if (left < stop && heap[left].priority < heap[i].priority) {                System.out.println( "Heap property violated:" );                System.out.printf( "\theap[%d] = %d, left child heap[%d] = %d\n", i, heap[i].priority, left, heap[left].priority );            }            if (right < stop && heap[right].priority < heap[i].priority) {                System.out.println( "Heap property violated:" );                System.out.printf( "\theap[%d] = %d, right child heap[%d] = %d\n", i, heap[i].priority, right, heap[right].priority );            }        }    }    private static class HeapNode<S>    {        int priority;        S item;        public  void init( S myItem, int myPriority )        {            item = myItem;            priority = myPriority;        }    }}