package mutants.SimpleLinear.STD_17;

/**
 * Unbounded priority queue interface
 * @param T item type
 * @author Maurice Herlihy
 */
public interface PQueue<T> {

    void add(T item, int priority);

    T removeMin();

}

