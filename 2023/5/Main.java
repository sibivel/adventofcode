import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.Map.Entry;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long[] seeds = Arrays.stream(scanner.nextLine().split(":")[1].split("\s+")).filter(s -> s.length() > 0)
                .mapToLong(Long::parseLong).toArray();
        long[][] seedRanges = new long[seeds.length / 2][2];
        for (int i = 0; i < seeds.length; i += 2) {
            seedRanges[i / 2] = new long[] { seeds[i], seeds[i] + seeds[i + 1] };
        }
        System.out.println(Arrays.deepToString(seedRanges));
        scanner.nextLine();
        TreeMap<Long, long[]>[] maps = new TreeMap[7];
        String next = scanner.nextLine();
        for (int i = 0; i < 7; i++) {
            next = scanner.nextLine();
            System.out.println(next);
            TreeMap<Long, long[]> map = new TreeMap<>();
            while (next.length() > 0) {
                long[] ints = Arrays.stream(next.split("\s+")).filter(s -> s.length() > 0).mapToLong(Long::parseLong)
                        .toArray();
                map.put(ints[1], new long[] { ints[0], ints[2] });
                next = (scanner.hasNextLine()) ? scanner.nextLine() : "";
            }
            maps[i] = map;
            if (scanner.hasNextLine()) {
                scanner.nextLine();
            }
        }

        HashSet<Long> pointsOfInterest = new HashSet<>();
        pointsOfInterest.add(0L);
        for (int i = 6; i >= 0; i--) {
            TreeMap<Long, long[]> map = maps[i];
            HashSet<Long> newPointsOfInterest = new HashSet<>();
            newPointsOfInterest.add(0L);
            for (Entry<Long, long[]> entry: map.entrySet()) {
                newPointsOfInterest.add(entry.getKey());
                newPointsOfInterest.add(entry.getKey() - 1);

                newPointsOfInterest.add(entry.getKey() + entry.getValue()[1] - 1);
                newPointsOfInterest.add(entry.getKey() + entry.getValue()[1]);
            }
            for (long poi: pointsOfInterest) {
                newPointsOfInterest.add(reverseEvaluateMap(poi, map));
            }
            pointsOfInterest = newPointsOfInterest;
        }
        System.out.println(pointsOfInterest.stream().sorted().toList());
        for (long[] r: seedRanges) {
            pointsOfInterest.add(r[0]);
            pointsOfInterest.add(r[1]-1);
        }
        System.out.println(pointsOfInterest.stream().mapToLong(i -> i).filter(poi -> inRanges(poi, seedRanges)).map(poi -> evaluateMaps(poi, maps)).min().getAsLong());
    }

    private static boolean inRanges(long x, long[][] ranges) {
        for (long[] r: ranges) {
            if (r[0] <= x && x < r[1]) {
                return true;
            }
        }
        return false;
    }

    private static long evaluateMap(long x, TreeMap<Long, long[]> map) {
        Entry<Long, long[]> floorEntry = map.floorEntry(x);
        if (floorEntry != null && floorEntry.getKey() + floorEntry.getValue()[1] > x) {
            return floorEntry.getValue()[0] + x - floorEntry.getKey();
        }
        return x;
    }

    private static long evaluateMaps(long x, TreeMap<Long, long[]>[] maps) {
        for (TreeMap<Long, long[]> map: maps) {
            x = evaluateMap(x, map);
        }
        return x;
    }

    private static long reverseEvaluateMap(long d, TreeMap<Long, long[]> map) {
        for (Entry<Long, long[]> entry : map.entrySet()) {
            if (d >= entry.getValue()[0] && d < entry.getValue()[0] + entry.getValue()[1]) {
                return entry.getKey() + (d - entry.getValue()[0]);
            }
        }
        return d;
    }
}