(continuation of cot-4500-as3 repo...)

This entire repository is designed to reshow two methods and introduce matrix concepts:

List:
1. Euler's method
2. Runge-Kutta method
3. Gauss-Jordan elimination
4. Determinant of matrices
5. LU Factorization
6. Determining diagonally dominant matrices
7. Determining positive definite matrices

in regards to how they are supposed to respond given their Python implementation.

The best way to fully explore the project is by deploying this repo into Replit, link below for instructions:
https://docs.replit.com/cloud-services/deployments/deploying-a-github-repository#:~:text=Import%20a%20Repl%20from%20GitHub,top%20right%20of%20the%20modal.

Once done, you will see on the left the following project structure:

src/main/__init__.py 

src/main/assignment_3.py

src/test/__init__.py

src/test/test_assignment_3.py

requirements.txt 

README.md

in which assignment_3.py in main is the Python code for the methods and matrix concepts. For test_assignment_3.py, we use this to test the methods and matrix concepts. For methods, we test that when given a range, number of iterations, and an initial point, it will match the correct approxmiation value. For the matrix concepts, we test them by giving example matrices and making sure it reaches to its correct result, whether that is a value, matrix, or True or False outcome.

To compile and be able to see all of it yourself, here are the steps:
1. Make sure shell is on the right side (not console)
2. Type in "pip install pytest" (you will see it install with plenty of text)
3. After that, type in "pip freeze > requirements.txt", this should output for you in requirements.txt the third-party libraries in Python you (or the system) have installed in Replit, the libraries can vary depending on if you installed libraries before but what is important is you having pytest and its associated version
4. Now, type in the console "pytest src/test/test_assignment_3.py", this should output in the shell the pytest session starting and showing green with 7 test cases passed in an allocated timeframe

If you want, you can alter values, expected results, or matrices in test_assignment_3.py (can change whatever in assignment_3.py as well) and do step 4 again and see that the test cases can also debug code for you to see what you got wrong and what needs fixing.

Use the project to your heart's intent and hope you enjoy it!