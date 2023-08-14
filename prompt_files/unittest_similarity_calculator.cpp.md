

#include <memory>

#include "gtest/gtest.h"
#include "gflags/gflags.h"
#include "glog/logging.h"

#include "perception_common/log/common_log.hpp"
#include "perception_common/log/error.hpp"

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

TEST(SimilarityTest, log_test) {
        AP_LDEBUG(SimilarityTest) << "TODO";
}

}  }  }  
请给出以上代码的xx以及xxxaa