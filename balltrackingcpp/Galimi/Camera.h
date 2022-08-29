#pragma once

#include <string>
#include <iostream>

namespace Galimi {
    std::string version();

    class Camera {
        public:
            Camera(int, std::string, int, int, int, int, int);
        private:
            int id, exposure, captureAPI, x, y, angle, width, height;
            std::string name;
            bool isSavingVideo;
    };
}