package mutants.SimpleLinear.AOIS_27;// This is a mutant program.
// Author : ysma

public class SimpleLinear<T> implements PQueue<T>
{

    int range;

    Bin<T>[] pqueue;

    public SimpleLinear( int range )
    {
        this.range = range;
        pqueue = (Bin<T>[]) new Bin[range];
        for (int i = 0; i < pqueue.length; i++) {
            pqueue[i] = new Bin<T>();
        }
    }

    public  void add( T item, int key )
    {
        pqueue[key].put( item );
    }

    public  T removeMin()
    {
        for (int i = 0; i < range; i++) {
            T item = pqueue[i++].get();
            if (item != null) {
                return item;
            }
        }
        return null;
    }

}
