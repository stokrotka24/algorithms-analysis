package simulations;

import network.Network;
import utils.MathUtils;

public class Scenario3 extends Simulation {
    private final int roundLen;

    public Scenario3(Network network) {
        super(network);
        this.roundLen = (int) Math.ceil(MathUtils.log2(network.getSizeUpperBound()));
    }

    @Override
    double transmissionProbability(int slot) {
        int i = (slot - 1) % roundLen + 1;
        return Math.pow(2, -i);
    }
}
