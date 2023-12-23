import static java.util.stream.Collectors.*;

import java.util.*;

public class Main {
    public static void main(String[] args) {

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