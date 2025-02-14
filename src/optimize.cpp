#include <vector>

// Multiply gradients by a scaling factor
std::vector<float> scale_gradients(const std::vector<float>& gradients, float factor) {
    std::vector<float> scaled(gradients.size());
    for (size_t i = 0; i < gradients.size(); i++) {
        scaled[i] = gradients[i] * factor;
    }
    return scaled;
}
