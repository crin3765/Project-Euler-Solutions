package problem3;

/**
 * Project Euler Problem 3 Solution Takes a number in as long, and prints to
 * console its largest prime factor. Every number has a unique prime
 * factorization. Thus, a given number n can be represented as n =
 * (a^k)(b^l)...(c^m), where a, b, and c are primes. The algorithm in this
 * program utilizes this pinciple. Starting from 2, check if the number n is
 * divisible by 2. If so, then the number n = 2(m) for some m. Now check if m is
 * divisible by 2. If so, then n = 2*(2p) = 2^2p. Continue to break down the
 * number until division by 2 is no longer possible. Then n = (2^k)g for some
 * number g. Check if g is divisible by three, and follow the same process as
 * for 2. After enough iterations, you will get that n = (a^k)(b^l)...(c^m).
 * 
 * @author Cory Rindlisbacher
 *
 */
public class Problem3 {

	public static void main(String[] args) {
		// Gets the time in nanoseconds at the start of the program.
		final long startTime = System.nanoTime();

		long number = 600851475143L;
		//long number = 60L;
		//long number = 1029384834823858L;
		long largestPrime = 0L;
		for (long i = 2L; i <= number; i++) {
			while (number % i == 0) {
				number = number / i;
				if (i > largestPrime) {
					largestPrime = i;
				}
			}
		}
		System.out.println(largestPrime);
		// Calculates the time in nano seconds that the program took to run.
		final long duration = System.nanoTime() - startTime;
		// Prints to console the running time in seconds.
		System.out.println(duration / 1000000000.0);
	}

}
