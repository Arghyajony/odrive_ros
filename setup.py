from setuptools import setup

package_name = 'odrive_ros'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Arghya Chatterjee',
    maintainer_email='arghyame20buet@gmail.com',
    description='ODrive motor controller driver for ROS2',
    license='Modified BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odrive_node = odrive_ros.nodes.odrive_node:main'
        ],
    },
)