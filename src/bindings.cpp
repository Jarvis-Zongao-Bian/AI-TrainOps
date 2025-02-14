#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "optimize.cpp"  // Include optimized function

namespace py = pybind11;

PYBIND11_MODULE(optimize, m) {
    m.def("scale_gradients", &scale_gradients, "Scale gradient values by a factor");
}
