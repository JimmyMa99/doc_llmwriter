
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

#include "gtest/gtest.h"
#include "gflags/gflags.h"
#include "glog/logging.h"

#include "plugin/common/common/polygon_iou.hpp"
#ifndef GFLAGS_GFLAGS_H_
namespace gflags = google;
#endif  
int main(int argc, char *argv[]) {
    google::InitGoogleLogging(argv[0]);
    testing::InitGoogleTest(&argc, argv);
    gflags::ParseCommandLineFlags(&argc, &argv, true);
    return RUN_ALL_TESTS();
}

namespace senseAD {
namespace perception {
namespace aggregator {
TEST(PolygonIouTest, IntersectAreaTest) {
    PolygonIou polygon_iou;

    PolygonIou::Point ps1[5];
    PolygonIou::Point ps2[3];
    ps1[0].x = 0;
    ps1[0].y = 3;
    ps1[1].x = 1;
    ps1[1].y = 1;
    ps1[2].x = 3;
    ps1[2].y = 1;
    ps1[3].x = 3;
    ps1[3].y = 5;
    ps1[4].x = 1;
    ps1[4].y = 5;

    ps2[0].x = 1;
    ps2[0].y = 3;
    ps2[1].x = 5;
    ps2[1].y = 3;
    ps2[2].x = 3;
    ps2[2].y = 6;
    double area_1 = polygon_iou.IntersectArea(ps1, 5, ps2, 3);
    EXPECT_NEAR(area_1, 2.6667, 0.01);

    PolygonIou::Point ps3[3];
    PolygonIou::Point ps4[3];
    ps3[0].x = -1;
    ps3[0].y = -1;
    ps3[1].x = -2;
    ps3[1].y = -1;
    ps3[2].x = -1;
    ps3[2].y = -2;

    ps4[0].x = 1;
    ps4[0].y = 1;
    ps4[1].x = 2;
    ps4[1].y = 1;
    ps4[2].x = 1;
    ps4[2].y = 2;
    double area_2 = polygon_iou.IntersectArea(ps3, 3, ps4, 3);
    EXPECT_NEAR(area_2, 0.0, 0.01);
}

}  }  }  
请给出以上代码的xx以及xxxaa