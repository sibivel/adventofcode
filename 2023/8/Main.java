import static java.util.stream.Collectors.*;

import java.util.*;
import java.util.Map.Entry;

public class Main {
    public static void main(String[] args) {
        getInput();

    }

    private static List<String> getInput() {
        ArrayList<String> lines = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine());
        }
        scanner.close();
        return lines;
    }
}