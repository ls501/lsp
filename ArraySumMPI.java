

import mpi.*;

public class ArraySumMPI {

    public static void main(String[] args) throws Exception {

        MPI.Init(args);

        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        int[] array = {1,2,3,4,5,6,7,8,9,10};

        int n = array.length;

        int localSum = 0;

        int startIndex = rank * (n / size);

        int endIndex;

        if(rank == size - 1) {
            endIndex = n;
        } else {
            endIndex = startIndex + (n / size);
        }

        // Calculate local sum
        for(int i = startIndex; i < endIndex; i++) {
            localSum += array[i];
        }

        int[] globalSum = new int[1];

        // Reduce all local sums
        MPI.COMM_WORLD.Reduce(
                new int[]{localSum},
                0,
                globalSum,
                0,
                1,
                MPI.INT,
                MPI.SUM,
                0
        );

        // Print final sum
        if(rank == 0) {
            System.out.println("Global Sum = " + globalSum[0]);
        }

        MPI.Finalize();
    }
}







//import mpi.*;

public class ArraySumMPI {

    public static void main(String[] args) {

        MPI.Init(args);

        int rank = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        int n = array.length;

        int localSum = 0;
        int globalSum = 0;

        // Calculate the local sum
        int startIndex = rank * (n / size);

        int endIndex = (rank == size - 1)
                ? (n - 1)
                : (startIndex + (n / size) - 1);

        for (int i = startIndex; i <= endIndex; i++) {
            localSum += array[i];
        }

        // Compute the global sum by reducing local sums
        MPI.COMM_WORLD.Reduce(
                new int[]{localSum}, 0,
                new int[]{globalSum}, 0,
                1,
                MPI.INT,
                MPI.SUM,
                0
        );

        if (rank == 0) {
            System.out.println("Global sum: " + globalSum);
        }

        MPI.Finalize();
    }
}
