package simulations;
import network.*;

public abstract class Simulation {
    protected Network network;

    public Simulation(Network network) {
        this.network = network;
    }
    public int execute() {
        int slot = 0;

        while (true) {
            slot++;

            int transmittingNodes = 0;
            for (Node node: network.getNodes()) {
                transmittingNodes +=
                        node.isTransmitting(transmissionProbability(slot));
            }

            if (transmittingNodes == 1){
                return slot;
            }
        }
    }
    abstract double transmissionProbability(int slot);
}
