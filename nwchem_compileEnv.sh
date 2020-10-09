#source this file prior to compiling NWChem v7.0.1
#confirmed this worked on Ubuntu 20.04.1
#Intel Core i5-6200U

export PYTHONHOME=/usr/bin/python3.8
export PYTHONVERSION=3.8
export USE_PYTHON64=y
export NWCHEM_TOP=~/_programs/nwchem
export NWCHEM_TARGET=LINUX64
export NWCHEM_MODULES="all python"
export USE_INTERNALBLAS=y
export USE_MPI=y
export MPI_INCLUDE="/usr/lib/x86_64-linux-gnu/openmpi/include -I/usr/lib/x86_64-linux-gnu/openmpi/lib"
export MPI_LIB="/usr/lib/x86_64-linux-gnu/openmpi/lib"
export LIBMPI="-lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi"

