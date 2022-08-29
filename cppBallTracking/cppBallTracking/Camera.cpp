#include "Camera.h"
// #include <cv.h>


namespace Galimi {
    std::string version() {
        return "1.0.0 Galimi";
    }
    /**
     * This function is a constructor for the Camera class. It takes in 7 parameters and assigns them
     * to the class variables.
     *
     * @param id the id of the camera, used to identify the camera in the program
     * @param name the name of the camera, used for debugging
     * @param exposure the exposure of the camera.
     * @param captureAPI the capture API of the camera, used to identify the camera in the program
     * @param offsetX The x offset of the camera from the center of the screen.
     * @param offsetY The y offset of the camera from the top of the screen.
     * @param angle the angle of the camera in degrees
     */
    Camera::Camera(int id = 0, std::string name = "default", int exposure = 0, int captureAPI = 0, int offsetX = 0, int offsetY = 0, int angle = 0) {
        this->id = id;
        this->name = name;
        std::cout << this->name << "camera loading..." << std::endl;
        this->exposure = exposure;
        this->captureAPI = captureAPI;
        //configureCapture();
        this->x = offsetX;
        this->y = offsetY;
        this->angle = angle;
        this->isSavingVideo = false;
        std::cout << this->name << "camera loaded" << std::endl;
    }

    //void setPipeline() {

    //}

    //// void configurecapture() {
    ////     std::cout << "configuring capture..." << std::endl;
    ////     this->capture = cv::VideoCapture(this->id);
    ////     this->capture.set(cv::CAP_PROP_EXPOSURE, this->exposure);
    ////     this->capture.set(cv::CAP_PROP_FRAME_WIDTH, this->width);
    ////     this->capture.set(cv::CAP_PROP_FRAME_HEIGHT, this->height);
    ////     this->capture.set(cv::CAP_PROP_FPS, this->fps);
    ////     this->capture.set(cv::CAP_PROP_FOURCC, this->fourcc);
    ////     this->capture.set(cv::CAP_PROP_AUTO_EXPOSURE, this->autoExposure);
    ////     this->capture.set(cv::CAP_PROP_AUTO_WB, this->autoWB);
    ////     this->capture.set(cv::CAP_PROP_WB_TEMPERATURE, this->wbTemperature);
    ////     this->capture.set(cv::CAP_PROP_WB_MODE, this->wbMode);
    ////     this->capture.set(cv::CAP_PROP_BRIGHTNESS, this->brightness);
    ////     this->capture.set(cv::CAP_PROP_CONTRAST, this->contrast);
    ////     this->capture.set(cv::CAP_PROP_SATURATION, this->saturation);
    ////     this->capture.set(cv::CAP_PROP_HUE, this->hue);
    ////     this->capture.set(cv::CAP_PROP_GAMMA, this->gamma);
    ////     this->capture.set(cv::CAP_PROP_GAIN, this->gain);
    ////     this->capture.set(cv::CAP_PROP_EXPOSURE, this->exposure);
    ////     this->capture.set(cv::CAP_PROP_SHARPNESS, this->sharpness);
    ////     this->capture.set(cv::CAP_PROP_BACKLIGHT, this->backlight);
    ////     this->capture.set(cv::CAP_PROP_PAN, this->pan);

    void Camera::configureCapture() {
         /*this->capture = cv::videocapture(this->id, this->captureapi);
         this->capture.set(cv_cap_prop_exposure, this->exposure);
         this->capture.set(cv_cap_prop_auto_exposure, -1);
         if (!this->capture.isopened()) {
             cout << "error: " << this->name << " camera not found" << endl;
         }

         this->width = this->capture.get(3);
         this->height = this->capture.get(4);*/
    }
}