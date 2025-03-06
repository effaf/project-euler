# Contributing to project-euler-utils

Thank you for considering contributing to this package. My focus is on inncreasing the efficiency of functions
using **NumPy** and increase their test coverage.

## How to Contribute

### 1. **Fork the Repository**
   - First, fork the repository by clicking on the **Fork** button at the top-right of the repository page.

### 2. **Clone Your Fork**
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/effaf/project_euler_utils.git
     cd your-repo-name
     ```

### 3. **Create a New Branch**
   - Always create a new branch for each feature or fix:
     ```bash
     git checkout -b improve-efficiency
     ```

### 4. **Make Changes**
   - **Improve efficiency**: Use **NumPy** to optimize any parts of the code that are computationally expensive. If you're unsure, look for **loops** or **vectorized operations** that could benefit from NumPy.
   - **Add tests**: Write tests for the new or existing functions. 
   
   I currently do not have pytest as a dependency, but recommend using pytest for developing tests.

     - Tests should be added in the `tests/` directory.
     - Make sure all tests pass before submitting.

### 5. **Run Tests**
   - Before submitting, make sure all tests pass:
     ```bash
     pytest
     ```

### 6. **Commit Changes**
   - Add and commit your changes:
     ```bash
     git add .
     git commit -m "Optimized function using NumPy and added tests"
     ```

### 7. **Push Changes**
   - Push your changes to your fork:
     ```bash
     git push origin improve-efficiency
     ```

### 8. **Open a Pull Request**
   - Go to the original repository and open a **pull request** from your fork's `improve-efficiency` branch to `main`.
   - In the pull request description, explain what you did and the impact it will have (e.g., improved performance with NumPy, added coverage with new tests).


## Thank You!
Appreciate your contributions to make this package better!

Contact - shlok.kothari@gmail.com (for any questions)