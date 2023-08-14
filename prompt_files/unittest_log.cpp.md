

#include "gtest/gtest.h"
#include "gflags/gflags.h"
#include "glog/logging.h"

#include "perception_common/log/common_log.hpp"

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

TEST(LogTest, IDWElog) {
    AP_LDEBUG(FrameUnittest) << "This is a info log!";
    AP_LDEBUG(FrameUnittest) << "This is a debug log!";
    AP_LWARN(FrameUnittest) << "This is a warn log!";
    AP_LERROR(FrameUnittest) << "This is a error log!";
}

}  }  }  
请给出以上代码的xx以及xxxaa