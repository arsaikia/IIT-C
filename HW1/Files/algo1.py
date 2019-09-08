import time
import numpy as np


def matrix_multiply_int():

	matrix_A = np.random.randint(0,99,(200,300))
	matrix_B = np.random.randint(0,99,(300,400))
	result = np.empty(shape=(200,400))
	
	start_time = time.time()

	# iterate through rows of matrix_A 
	for i in range(len(matrix_A)): 
	
		# Iterate through column of matrix_B
		for j in range(len(matrix_B[0])): 
	  
			# iterating by rows of B 
			for k in range(len(matrix_B)): 
				result[i][j] += matrix_A[i][k] * matrix_B[k][j] 

				
	end_time = time.time()
	time_taken = end_time - start_time

	print("--- Matrix with Int: %s seconds ---" % (time_taken))


def matrix_multiply_double():

	matrix_A = np.random.uniform(0, 99.9, size=(200, 300))
	matrix_B = np.random.uniform(0, 99.9, size=(300, 400))
	result = np.empty(shape=(200,400))
	
	start_time = time.time()

	# iterating by row of A 
	for i in range(len(matrix_A)): 
	
		# iterating by coloum by B  
		for j in range(len(matrix_B[0])): 
	  
			# iterating by rows of B 
			for k in range(len(matrix_B)): 
				result[i][j] += matrix_A[i][k] * matrix_B[k][j] 

				
	end_time = time.time()
	time_taken = end_time - start_time

	print("--- Matrix with Doubles : %s seconds ---" % (time_taken))


def main():
	matrix_multiply_int()
	matrix_multiply_double()

	



if __name__ == "__main__":
    main()
