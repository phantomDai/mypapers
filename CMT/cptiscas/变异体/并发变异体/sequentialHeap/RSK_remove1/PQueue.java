package mutants.SequentialHeap.RSK_remove1;

/**
 * Unbounded priority queue interface
 * @param T item type
 * @author Maurice Herlihy
 */
public interface PQueue<T> {

    void add(T item, int priority) throws InterruptedException;

    T removeMin();

}

