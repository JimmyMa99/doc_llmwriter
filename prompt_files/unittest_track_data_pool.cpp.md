

#include <memory>

#include "gtest/gtest.h"
#include "gflags/gflags.h"
#include "glog/logging.h"

#include "perception_common/log/common_log.hpp"
#include "perception_common/log/error.hpp"

#include "perception_aggregator/data_type/track_data_pool.hpp"

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
        TrackDataPoolPtr track_data_pool_ptr = std::make_shared<TrackDataPool>();
    auto track_cluster_ptr = track_data_pool_ptr->GetObjectTrackCluster();
    CHECK_EQ(nullptr == track_cluster_ptr, false);
    const uint64_t timestamp_ns = 1e8;
    track_data_pool_ptr->SetCurrentTimeStampNS(timestamp_ns);
    CHECK_EQ(timestamp_ns, track_data_pool_ptr->GetCurrentTimeStampNS());

        const std::string test_sensor_name = "center_camera_fov120";
    auto track_ptr =
        track_cluster_ptr->CreateNewTrack(test_sensor_name, timestamp_ns);
    AP_LDEBUG(TrackDataPoolTest) << "init one object with object id -> "
                                << track_ptr->GetObjectID();
}

}  }  }  
请给出以上代码的xx以及xxxaa