#pragma once

struct Vec {
    float x;
    float y;
    Vec(float x, float y);
    Vec();
    Vec(Vec &v);
    Vec(Vec *v);
    Vec add(float x, float y);
    Vec sub(float x, float y);
    Vec mul(float x, float y);
    Vec add(Vec v);
    Vec sub(Vec v);
    Vec mul(Vec v);
};