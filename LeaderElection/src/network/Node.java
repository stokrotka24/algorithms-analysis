package network;

public class Node {
    public int isTransmitting(double probability) {
        return (Math.random() < probability) ? 1 : 0;
    }
}
