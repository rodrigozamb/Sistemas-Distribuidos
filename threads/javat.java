package threads;

class Counter extends Thread{
    private int c = 0;

    public int increment() {
        return ++c;
    }

    public int decrement() {
        return --c;
    }

    public int value() {
        return c;
    }

    public void run(){

        
    }

    public static void main(String args[]) {
        Thread t = new Counter();
        t.start();
    }
}