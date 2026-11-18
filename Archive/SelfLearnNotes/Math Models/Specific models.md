# Specific Engineering Models

## 姿态控制模型 - Attitude Control Model

the attitude control model is used to describe how a rotation is excuted, not the space coordinates.

- Euler Angles Model

| Angle | Symbol | CN |
| --- | --- | --- |
| Yaw angle | $\phi$ | 偏航角 |
| Pitch angle | $\theta$ | 俯仰角 |
| Roll angle | $\psi$ | 横滚角 |

use Euler angles as a system parameters set will have "Gimbal Lock" problem, which means when a middle angle rolling $\pm 90$ degrees, the parameter system will lose one of the rotational degree of freedom.

- Quaternion Model

## 
