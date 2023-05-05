package utils;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Map;

public class FileUtils {
    public static void writeMapToFile(String fileName, String fileComment, Map<Integer, Integer> map) throws IOException {
        FileWriter fileWriter = new FileWriter(fileName);
        PrintWriter printWriter = new PrintWriter(fileWriter);
        printWriter.println(fileComment);
        for (var entry : map.entrySet()) {
            printWriter.println(entry.getKey() + " " + entry.getValue());
        }
        printWriter.close();
    }
}
