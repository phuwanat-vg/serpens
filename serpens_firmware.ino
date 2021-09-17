#include "Arduino.h"
#include <ros.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <sensor_msgs/JointState.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
//0 degree 150
//180 degree 540
//mean 345
ros::NodeHandle  nh;
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates

double j1_angle = 180;
double j2_angle = 90;
double j3_angle = 90;
double j4_angle = 90;
double j5_angle = 85;
double j6_angle = 90;
double tool_angle = 90;

void jointState_cb(const sensor_msgs::JointState& cmd_msg) {

  j1_angle = radToDegree(cmd_msg.position[0])+90;
  j2_angle = radToDegree(cmd_msg.position[1])+90;
  j3_angle = 180-radToDegree(cmd_msg.position[2]);
  j4_angle = radToDegree(cmd_msg.position[3])+90;
  j5_angle = radToDegree(cmd_msg.position[4])+90;
  j6_angle = radToDegree(cmd_msg.position[5])+90;
  tool_angle = radToDegree(cmd_msg.position[6])+90;
  

  pwm.setPWM(0, 0, degreeToPWM(j1_angle)); //0 CW
  pwm.setPWM(1, 0, degreeToPWM(j2_angle)); //0 forward
  pwm.setPWM(2, 0, degreeToPWM(j3_angle)); //0 backward
  pwm.setPWM(3, 0, degreeToPWM(j4_angle)); //0 CW
  pwm.setPWM(4, 0, degreeToPWM(j5_angle)); //0 CW
  pwm.setPWM(5, 0, degreeToPWM(j6_angle)); //0 CW
  pwm.setPWM(6, 0, degreeToPWM(tool_angle)); //0 CW
}

ros::Subscriber<sensor_msgs::JointState> sub_joint("joint_states", jointState_cb);

void setup() {
  nh.getHardware()->setBaud(115200);
  nh.initNode();
  nh.subscribe(sub_joint);

  pwm.begin();

  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates
  
  delay(10);
  
  pwm.setPWM(0, 0, degreeToPWM(j1_angle)); //0 CW
  pwm.setPWM(1, 0, degreeToPWM(j2_angle)); //0 forward
  pwm.setPWM(2, 0, degreeToPWM(j3_angle)); //0 backword
  pwm.setPWM(3, 0, degreeToPWM(j4_angle)); //0 CW
  pwm.setPWM(4, 0, degreeToPWM(j5_angle)); //0 CW
  pwm.setPWM(5, 0, degreeToPWM(j6_angle)); //0 CW
  pwm.setPWM(6, 0, degreeToPWM(tool_angle)); //0 forward
}
float radToDegree(float radian) {

  float degree = radian * 0.3183 * 180; //degree = rad/Pi *180
  Serial.println(radian);
  Serial.println("degree");
  Serial.println(degree);
  return degree;
}

int degreeToPWM(float degree) {

  //int pwm_signal = (degree/180*390)+150;
  int pwm_signal = (degree * 0.00556 * 390) + 150; //0.00556 = 1/180
  return pwm_signal;
}
void loop() {
  nh.spinOnce();
  delay(1);
}
