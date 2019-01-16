 # Remote Camera Pod
 
 
Provides a mouse-click GUI (with Tkinter) for sending LANC commands <sup>1</sup> to a Canon G30 camcorder for:
- zoom (1X to 20X)
- start/stop recording
- cam wake/sleep

 Ways it could be improved:
 * manual/auto focus
 * faster, easier control interface (keyboard input, or other?)
 * low-latency remote control over SSH
 * saving a user-defined "home" configuration (for now, that means only a chosen zoom) to return to quickly when requested (a *Reset Home Config* feature)
 * stepper motors to pan and tilt the camcorder
 
 <sup>1</sup> via [ELM624](http://www.appliedlogiceng.com/index_files/Page1389.htm)


# Additional Information

This was my first project working with Python back in 2015, intended for HDRunners.com. I tested it back in Sept 2015 but haven't touched it since.
I created this repo to avoid losing this project; I'm not currently planning to improve it (although it could be improved and cleaned up in a multitude of ways). This was a small scripting project but easily could be grown into a very ambitious project if features that require networking & socket programming or robotics are implemented.
