

#include <string>
#include <vector>
#include "gtest/gtest.h"
#include "gflags/gflags.h"
#include "glog/logging.h"

#include "plugin/common/common/string_util.hpp"

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
TEST(StringUtilTest1, GeneratePointsInPolygonTest) {
    std::string input = std::string("abd+efg");
    std::string delim = std::string("+");
    std::vector<std::string> tokens;
    StringSplit(input, delim, &tokens);
    for (size_t i = 0; i < tokens.size(); i++) {
        EXPECT_EQ("abd", tokens[0]);
        EXPECT_EQ("efg", tokens[1]);
    }
}

TEST(StringUtilTest2, String2DoubleTest) {
    std::string string_value = std::string("12.34");
    double double_value = String2Double(string_value);
    EXPECT_NEAR(double_value, 12.34, 0.001);
}

TEST(StringUtilTest3, Eigen2f2StringTest) {
    Eigen::Vector2f pos(2.02, 3.09);
    int precise = 2;
    std::string delim = std::string("+");
    std::string result = Eigen2f2String(pos, precise, delim);
    EXPECT_EQ(result, "2.02+3.09");
}
}  }  }  
请给出以上代码的xx以及xxxaa