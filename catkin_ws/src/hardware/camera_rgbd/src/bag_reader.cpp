#include "ros/ros.h"
#include "rosbag/bag.h"
#include "rosbag/view.h"
#include "sensor_msgs/PointCloud2.h"
#include "sensor_msgs/Image.h"
#include "tf/transform_listener.h"
#include <boost/foreach.hpp>
#define foreach BOOST_FOREACH

int main(int argc, char** argv)
{
    std::string bag_name = "";
    for(int i=0; i < argc; i++)
    {
        std::string strParam(argv[i]);
        if(strParam.compare("--bag") == 0)
            bag_name = argv[++i];
    }

    std::cout << "INITIALIZING RGBD_CAMERA BY MARCOSOF ..." << std::endl;
    std::cout << "Rgbd_Camera.->Using BAG file: " << bag_name << std::endl;

    ros::init(argc, argv, "camera_rgbd");
    ros::NodeHandle n;
    ros::Publisher pubPointCloud =n.advertise<sensor_msgs::PointCloud2>("/point_cloud",1);
    ros::Rate loop(30);

    rosbag::Bag bag;
    sensor_msgs::PointCloud2::Ptr msgFromBag;
    bag.open(bag_name, rosbag::bagmode::Read);
    rosbag::View view(bag, rosbag::TopicQuery("/hardware/point_cloud_man/rgbd_wrt_kinect"));
    while(ros::ok())
    {
        foreach(rosbag::MessageInstance const m, view)
        {
            msgFromBag = m.instantiate<sensor_msgs::PointCloud2>();
            if(msgFromBag == NULL)
            {
                loop.sleep();
                continue;
            }
            msgFromBag->header.stamp = ros::Time::now();
            pubPointCloud.publish(*msgFromBag);
            ros::spinOnce();
            loop.sleep();
        }
    }
    bag.close();
        
    return 0;
}
