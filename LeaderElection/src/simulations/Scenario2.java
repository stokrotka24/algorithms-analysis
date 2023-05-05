package simulations;

import network.Network;

public class Scenario2 extends Simulation {
    private final double transmissionProbability;
    public Scenario2(Network network) {
        super(network);
        transmissionProbability = 1.0/network.getSize();
    }

    @Override
    double transmissionProbability(int slot) {
        return transmissionProbability;
    }
}
