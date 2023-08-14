


#include <pcl/point_cloud.h>
#include <pcl/kdtree/kdtree_flann.h>

#include <memory>

#include "gtest/gtest.h"
#include "gflags/gflags.h"
#include "glog/logging.h"

#include "perception_common/log/common_log.hpp"
#include "perception_common/log/error.hpp"

#include "perception_aggregator/data_type/offline_noise_estimator_with_decision_tree.hpp"

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

TEST(TrackDataPoolTest, InitAndPointer) {
        EstimatorNoiseParamsParameter params;
    std::string gussian_params_path = "/DATA/params.pb";
    std::string tree_params_path = "/DATA/tree_pb.dot";
    OfflineNoiseEstimatorWithDTPtr noise_estimator(
        new OfflineNoiseEstimatorWithDT());
    noise_estimator->Init("", params);
}
}  }  }  
请给出以上代码的xx以及xxxaa