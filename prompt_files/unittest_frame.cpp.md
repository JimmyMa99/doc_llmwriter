

#include <memory>

#include "gtest/gtest.h"
#include "gflags/gflags.h"
#include "glog/logging.h"

#include "perception_common/log/common_log.hpp"
#include "perception_common/log/error.hpp"

#include "perception_aggregator/data_type/object.hpp"
#include "perception_aggregator/data_type/object_observation.hpp"
#include "perception_aggregator/data_type/frame.hpp"

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

TEST(FrameTest, InitAndSet) {
    auto frame_ptr = std::make_shared<Frame>();
    frame_ptr->SetSensorName("center_camera_fov120");
    frame_ptr->SetFrameID(1);
    frame_ptr->SetNewComing();
    frame_ptr->SetTimeStampNS(1e8);

    auto object_obs_ptr = std::make_shared<ObjectObservation>();
    object_obs_ptr->SetSensorName("center_camera_fov120");
    object_obs_ptr->SetObjectLabel(ObjectLabel::VEHICLE);

    CHECK_EQ(AP_SUCCESS, frame_ptr->AddObject(object_obs_ptr));
}

}  }  }  
请给出以上代码的xx以及xxxaa