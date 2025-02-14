cmake_minimum_required(VERSION 3.10)
project(Optimize)

find_package(pybind11 REQUIRED)

add_library(optimize MODULE bindings.cpp)
target_link_libraries(optimize PRIVATE pybind11::module)
