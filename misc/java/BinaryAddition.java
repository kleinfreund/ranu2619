class BinaryAddition {
    public static void main(String[] args) {
        int[] summandsArray = getValidSummands(args);

        System.out.println(addBinary(summandsArray[0], summandsArray[1]));
    }

    public static int addBinary(int a, int b) {
        int carry = (a & b) << 1;
        int result = a ^ b;
        return ((result & carry) != 0) ? addBinary(result, carry) : (result ^ carry);
    }

    /**
     * Validating user input.
     *
     * @param args Arguments that were originally passed to the program
     * @return     Integer array containing two natural numbers
     */
    private static int[] getValidSummands(String[] args) {
        if (args.length < 2) {
            fatal("Not enough arguments. Please enter two natural numbers.");
        }

        if (args.length > 2) {
            fatal("Too many arguments were provided. Please enter two natural numbers.");
        }

        int[] intArray = new int[args.length];

        for (int i = 0; i < intArray.length; i++) {
            try {
                intArray[i] = Integer.parseInt(args[i]);
            } catch (NumberFormatException nfe) {
                fatal("The entered value (" + args[i] + ") was not an integer.");
            }

            if (intArray[i] < 0) {
                fatal("Please enter a non-negative number.");
            }
        }

        return intArray;
    }

    /**
     * A small wrapper to produce error messages and quit the programm
     *
     * @param message Error message to spit out before quitting
     */
    private static void fatal(String message) {
        System.out.println(message);
        System.exit(1);
    }
}
