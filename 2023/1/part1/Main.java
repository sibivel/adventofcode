import static java.util.stream.Collectors.*;
import java.util.List;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    for (String line: getInput()) {
      line.chars().mapToObj(c -> Character.valueOf(c))
    }
  }

  private static List<String> getInput() {
    return new Scanner(System.in).tokens().collect(toList());
  }
}