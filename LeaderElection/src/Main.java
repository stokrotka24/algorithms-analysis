import network.Network;
import simulations.Scenario2;
import simulations.Scenario3;
import simulations.Simulation;
import utils.FileUtils;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static Simulation getSimulation(String simulationType, Network network){
        if (simulationType == null){
            return null;
        }
        if (simulationType.equalsIgnoreCase("Scenario2")){
            return new Scenario2(network);

        } else if(simulationType.equalsIgnoreCase("Scenario3")){
            return new Scenario3(network);

        }
        return null;
    }
    private static void repeatSimulation(int n, int u, String simulationType, int noExperiments, String resultFile) {
        Network network = new Network(n, u);
        Simulation simulation = getSimulation(simulationType, network);

        Map<Integer, Integer> resultsFreq = new HashMap<>();
        for (int i = 0; i < noExperiments; i++) {
            int noSlots = simulation.execute();
            resultsFreq.merge(noSlots, 1, Integer::sum);
        }

        String fileComment = String.format(
                "Freq.distribution of L, %s, n=%d, u=%d, no.experiments=%d", simulationType, n, u, noExperiments);
        try {
            FileUtils.writeMapToFile(
                    resultFile,
                    fileComment,
                    resultsFreq);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    
    private static void task2() {
        int noExperiments = 10000;

        // Scenario 2
        int n = 1000;
        repeatSimulation(n, n, "Scenario2", noExperiments,"results/task2/scenario2");

        // Scenario 3
        int u = 1024;
        n = 2;
        repeatSimulation(n, u, "Scenario3", noExperiments,"results/task2/scenario3_n=2");
        n = u/2;
        repeatSimulation(n, u, "Scenario3", noExperiments,"results/task2/scenario3_n=half_u");
        n = u;
        repeatSimulation(n, u, "Scenario3", noExperiments,"results/task2/scenario3_n=u");
    }

    private static void task3() {
        int noExperiments = 100000;
        int[] nValues = {5, 50, 100, 500, 1000};

        for (int n: nValues) {
            System.out.println(n);
            repeatSimulation(n, n, "Scenario2", noExperiments, String.format("results/task3/scenario2_n=%d", n));
        }
    }

    private static void task4() {
        int noExperiments = 1000;
        int u = 1000;
        int[] nValues = {2, u/8, u/4, u/2, u};

        for (int n: nValues) {
            System.out.println(n);
            repeatSimulation(n, u, "Scenario3", noExperiments, String.format("results/task4/scenario3_n=%d", n));
        }
    }

    public static void main(String[] args) {
//        task2();
//        task3();
        task4();
    }
}