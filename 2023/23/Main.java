import static java.util.stream.Collectors.*;

import java.util.*;

public class Main {

    static char[][] inputs;
    static int R;
    static int C;
    static int[][] dirs = {
            { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 }
    };

    public static void main(String[] args) {
        inputs = getInputChars();
        R = inputs.length;
        C = inputs[0].length;
        System.out.println(Main.longest(0, 1, 0));
        Stack<int[]> stack = new Stack<>();
        while (!stack.empty()) {
            int[] t = stack.pop();
            int r = t[0];
            int c = t[1];
            if (r < 0 || c < 0 || r >= R || c >= C) {
                continue;
            }
            if (inputs[r][c] == '#') {
                continue;
            }
            if (r == R - 1 && c == C - 2) {
                continue;
            }
            char prevc = inputs[r][c];
            inputs[r][c] = '#';
            Integer fres = null;
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                stack.push(new int[]);
                if (res != null) {
                    if (fres == null) {
                        fres = res;
                    } else {
                        fres = Math.max(fres, res);
                    }
                }
            }
        }
    }

    private static Integer longest(int r, int c, int length) {
        if (r < 0 || c < 0 || r >= R || c >= C) {
            return null;
        }
        if (inputs[r][c] == '#') {
            return null;
        }
        if (r == R - 1 && c == C - 2) {
            return length;
        }
        char prevc = inputs[r][c];
        inputs[r][c] = '#';
        Integer fres = null;
        for (int[] dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            Integer res = longest(nr, nc, length + 1);
            if (res != null) {
                if (fres == null) {
                    fres = res;
                } else {
                    fres = Math.max(fres, res);
                }
            }
        }
        inputs[r][c] = prevc;
        return fres;
    }

    private static ArrayList<String> getInput() {
        ArrayList<String> lines = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine());
        }
        scanner.close();
        return lines;
    }

    private static char[][] getInputChars() {
        List<String> lines = getInput();
        int R = lines.size();
        int C = lines.get(0).length();
        char[][] res = new char[R][C];
        for (int i = 0; i < R; i++) {
            res[i] = lines.get(i).toCharArray();
        }
        return res;
    }
}