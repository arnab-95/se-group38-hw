# Installing dependencies

This document gives the instructions to install all the dependencies for the project.

## Installing NumPy

The only prereq to installing NumPy is Python itself. If you don't have Python yet and want the simplest way to get started, we recommend you use the [Anacoda Distribution](https://github.com/arnab-95/se-group38-hw.git).

### Using CONDA

If you use `conda`, you can install NumPy from the `defaults` or `conda-forge` channels:

```sh
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
```

### Using PIP

If you use `pip`, you can install NumPy with:

```sh
pip install numpy
```

For further instructions regarding management of numpy package, refer to the [official documentation](https://numpy.org/install).
