// bindings.cpp
#include <pybind11/pybind11.h>
#include "text.h"
#include "math.h"

namespace py = pybind11;

PYBIND11_MODULE(pymodule, m) {
    // Text class bindings
    py::class_<Text>(m, "Text")
        .def(py::init<const std::string&>())
        .def("getText", &Text::getText);

    // Math class bindings
    py::class_<Math>(m, "Math")
        .def(py::init<>())
        .def("add", &Math::add)
        .def("multiply", &Math::multiply);
}
