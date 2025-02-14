# Use official PyTorch base image
FROM pytorch/pytorch:latest

# Install required dependencies
RUN apt-get update && apt-get install -y \
    cmake g++ python3 python3-pip

# Set working directory inside the container
WORKDIR /app

# Copy Python dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install pybind11 using system package manager & pip
RUN apt-get update && apt-get install -y pybind11-dev && \
    pip install --no-cache-dir pybind11

# Copy the entire project into the container
COPY . /app

# Ensure a clean build by removing previous CMakeCache.txt
RUN rm -rf build CMakeCache.txt

# Set CMake prefix path for pybind11
ENV CMAKE_PREFIX_PATH="/usr/local/lib/python3.10/dist-packages/pybind11/share/cmake"

# Build the C++ optimization module
RUN mkdir -p build && cd build && cmake .. -DCMAKE_BUILD_TYPE=Release && make 

# Run training and then testing
CMD ["bash", "/app/run.sh"]