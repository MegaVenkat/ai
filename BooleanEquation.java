import java.util.*;

public class BooleanEquation {
    public static int[] p = { 0, 0, 0, 0, 1, 1, 1, 1 }, pComp = { 1, 1, 1, 1, 0, 0, 0, 0 };
    public static int[] q = { 0, 0, 1, 1, 0, 0, 1, 1 }, qComp = { 1, 1, 0, 0, 1, 1, 0, 0 };
    public static int[] r = { 0, 1, 0, 1, 0, 1, 0, 1 }, rComp = { 1, 0, 1, 0, 1, 0, 1, 0 };
    public static int[] res = { 0, 0, 0, 0, 0, 0, 0, 0 };
    public static String eqn = "P' v Q ^ R' ^ P";
    public static String[] exp = eqn.split("\\s+");

    public static void main(String[] args) {

        calculateFirst();
        calculateTruthTable();
        display();

    }

    private static void calculateTruthTable() {

        for (int i = 3; i < exp.length; i += 2) {
            // checks for all possibilities of P
            if (exp[i].equals("^") && exp[i + 1].equals("P")) {
                fillAnd(res, p);
            }
            if (exp[i].equals("v") && exp[i + 1].equals("P")) {
                fillOr(res, p);
            }
            if (exp[i].equals("^") && exp[i + 1].equals("P'")) {
                fillAnd(res, pComp);
            }
            if (exp[i].equals("v") && exp[i + 1].equals("P'")) {
                fillOr(res, pComp);
            }
            // checks for all possibilities of Q

            if (exp[i].equals("^") && exp[i + 1].equals("Q")) {
                fillAnd(res, q);
            }
            if (exp[i].equals("v") && exp[i + 1].equals("Q")) {
                fillOr(res, q);
            }
            if (exp[i].equals("^") && exp[i + 1].equals("Q'")) {
                fillAnd(res, qComp);
            }
            if (exp[i].equals("v") && exp[i + 1].equals("Q'")) {
                fillOr(res, qComp);
            }
            // checks for all possibilities of R

            if (exp[i].equals("^") && exp[i + 1].equals("R")) {
                fillAnd(res, r);
            }
            if (exp[i].equals("v") && exp[i + 1].equals("R")) {
                fillOr(res, r);
            }
            if (exp[i].equals("^") && exp[i + 1].equals("R'")) {
                fillAnd(res, rComp);
            }
            if (exp[i].equals("v") && exp[i + 1].equals("R'")) {
                fillOr(res, rComp);
            }

        }

    }

    private static void fillAnd(int[] a, int[] b) {
        for (int i = 0; i < 8; i++) {
            res[i] = a[i] & b[i];

        }
    }

    private static void fillOr(int[] a, int[] b) {
        for (int i = 0; i < 8; i++) {
            res[i] = a[i] | b[i];

        }
    }

    private static void calculateFirst() {

        // checks for all possibilities of P and Q

        if (exp[0].equals("P") && exp[1].equals("^") && exp[2].equals("Q")) {
            fillAnd(p, q);
        }
        if (exp[0].equals("P") && exp[1].equals("v") && exp[2].equals("Q")) {
            fillOr(p, q);
        }
        if (exp[0].equals("P'") && exp[1].equals("^") && exp[2].equals("Q")) {
            fillAnd(pComp, q);
        }
        if (exp[0].equals("P'") && exp[1].equals("v") && exp[2].equals("Q")) {
            fillOr(pComp, q);
        }
        if (exp[0].equals("P'") && exp[1].equals("^") && exp[2].equals("Q'")) {
            fillAnd(pComp, qComp);
        }
        if (exp[0].equals("P'") && exp[1].equals("v") && exp[2].equals("Q'")) {
            fillOr(pComp, qComp);
        }

        // checks for all possibilities of Q and R

        if (exp[0].equals("Q") && exp[1].equals("^") && exp[2].equals("R")) {
            fillAnd(q, r);
        }
        if (exp[0].equals("Q") && exp[1].equals("v") && exp[2].equals("R")) {
            fillOr(q, r);
        }
        if (exp[0].equals("Q'") && exp[1].equals("^") && exp[2].equals("R")) {
            fillAnd(qComp, r);
        }
        if (exp[0].equals("Q'") && exp[1].equals("v") && exp[2].equals("R")) {
            fillOr(qComp, r);
        }
        if (exp[0].equals("Q'") && exp[1].equals("^") && exp[2].equals("R'")) {
            fillAnd(qComp, rComp);
        }
        if (exp[0].equals("Q'") && exp[1].equals("v") && exp[2].equals("R'")) {
            fillOr(qComp, rComp);
        }

        // checks for all possibilities of P and R

        if (exp[0].equals("P") && exp[1].equals("^") && exp[2].equals("R")) {
            fillAnd(p, r);
        }
        if (exp[0].equals("P") && exp[1].equals("v") && exp[2].equals("R")) {
            fillOr(p, r);
        }
        if (exp[0].equals("P'") && exp[1].equals("^") && exp[2].equals("R")) {
            fillAnd(pComp, r);
        }
        if (exp[0].equals("P'") && exp[1].equals("v") && exp[2].equals("R")) {
            fillOr(pComp, r);
        }
        if (exp[0].equals("P'") && exp[1].equals("^") && exp[2].equals("R'")) {
            fillAnd(pComp, rComp);
        }
        if (exp[0].equals("P'") && exp[1].equals("v") && exp[2].equals("R'")) {
            fillOr(pComp, rComp);
        }
    }

    private static void display() {
        System.out.println("\nDesired truth table for the given boolean expression is : \n");
        System.out.println(" P\t Q\t R\t" + eqn);

        System.out.println("--------------------------------");

        for (int i = 0; i < 8; i++) {
            System.out.println(" " + p[i] + "\t " + q[i] + "\t " + r[i] + "\t   " + res[i]);
        }
        System.out.println();
    }
}