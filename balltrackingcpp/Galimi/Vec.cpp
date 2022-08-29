#include <math.h>
#include "Vec.h"

struct Vec {
    float x, y;
    Vec(float x, float y) : x(x), y(y) {}
    Vec(float x, float y) {
        this->x = x;
        this->y = y;
    }
    Vec() {
        this->x = 0;
        this->y = 0;
    }
    Vec(Vec &v) {
        this->x = v.x;
        this->y = v.y;
    }
    Vec(Vec *v) {
        this->x = v->x;
        this->y = v->y;
    }
    Vec add(float x, float y) {
        this->x + x;
        this->y + y;
        return this;
    }
    Vec add(Vec v) {
        this->x + v.x;
        this->y + v.y;
        return this;
    }
    Vec sub(float x, float y) {
        this->x - x;
        this->y - y;
        return this;
    }
    Vec sub(Vec v) {
        this->x - v.x;
        this->y - v.y;
        return this;
    }
    Vec mul(float x, float y) {
        this->x * x;
        this->y * y;
        return this;
    }
    Vec mul(Vec v) {
        this->x * v.x;
        this->y * v.y;
        return this;
    }
    float mag() {
        return sqrt(this->x * this->x + this->y * this->y);
    }
    Vec normalize() {
        float mag = this->mag();
        this->x / mag;
        this->y / mag;
        return this;
    }
};