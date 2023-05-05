package network;

import java.util.ArrayList;

public class Network {
    private final int size;
    private final int sizeUpperBound;
    private final ArrayList<Node> nodes = new ArrayList<>();


    public Network(int size, int sizeUpperBound) {
        this.size = size;
        for (int i = 0; i < size; i++) { nodes.add(new Node()); }
        this.sizeUpperBound = sizeUpperBound;
    }

    public int getSize() {
        return size;
    }

    public int getSizeUpperBound() {
        return sizeUpperBound;
    }

    public ArrayList<Node> getNodes() {
        return nodes;
    }


}
