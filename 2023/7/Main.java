import static java.util.stream.Collectors.*;

import java.util.*;
import java.util.Map.Entry;

public class Main {
    public static void main(String[] args) {
        List<String[]> hands = getInput().stream().map(input -> input.split("\s+"))
                .sorted((hand1, hand2) -> {
                    int t1 = getHandType(hand1[0]);
                    int t2 = getHandType(hand2[0]);
                    if (t1 != t2) {
                        return t1 - t2;
                    }

                    return compareHands(hand1[0], hand2[0]);
                })
                .peek(s -> System.out.println(Arrays.deepToString(s)))
                .toList();

        long total = 0;
        for (int i = 0; i < hands.size(); i++) {
            total += (i + 1) * Long.parseLong(hands.get(i)[1]);
        }
        System.out.println(total);
        for (String[] hand: hands) {
            getHandType(hand[0]);
        }

    }

    static int getHandType(String hand) {
        HashMap<Character, Integer> charCounts = new HashMap<>();
        int maxCount = 0;
        for (char c : hand.toCharArray()) {
            charCounts.put(c, charCounts.getOrDefault(c, 0) + 1);
            if (c != 'J') {
                maxCount = Math.max(maxCount, charCounts.get(c));
            }
        }
        int[] counts = new int[6];
        for (Entry<Character, Integer> entry : charCounts.entrySet()) {
            if (!entry.getKey().equals('J')) {
                counts[entry.getValue()]++;
            }
        }
        int jCount = charCounts.getOrDefault('J', 0);
        // System.out.println(maxCount);
        if (counts[5] > 0 || (maxCount + jCount == 5)) {
            return 5;
        }
        if (counts[4] > 0 || (maxCount + jCount == 4)) {
            return 4;
        }
        if ((counts[3] > 0 && counts[2] > 0) || (counts[3] > 0 && jCount > 0) || (counts[2] == 2 && jCount > 0) || (counts[2] == 1 && jCount > 1) || (jCount == 3)) {
            return 3;
        }
        if (counts[3] > 0 || (counts[2] > 0 && jCount > 0) || (jCount == 2)) {
            return 2;
        }
        if (counts[2] > 1) {
            return 1;
        }
        if (counts[2] > 0 || jCount > 0) {
            return 0;
        }
        return -1;
    }

    private static List<Character> CHARS = List.of(
            'A',
            'K',
            'Q',
            'T',
            '9',
            '8',
            '7',
            '6',
            '5',
            '4',
            '3',
            '2',
            'J');

    static int compareHands(String hand1, String hand2) {
        for (int i = 0; i < 5; i++) {
            char c1 = hand1.charAt(i);
            char c2 = hand2.charAt(i);
            if (c1 != c2) {
                return CHARS.indexOf(c2) - CHARS.indexOf(c1);
            }
        }
        return 1;
    }

    private static List<String> getInput() {
        ArrayList<String> lines = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine());
        }
        return lines;
    }
}