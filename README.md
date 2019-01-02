 # Remote Camera Pod
 A 2015 experiment in remotely controlling cameras for HDRunners.com
 This was my first project working with Python back in 2015. 
 I almost lost this project, so putting it here for safekeeping, not planning to improve it (although it could be improved and cleaned up in a multitude of ways). This was only a small scripting project but easily could be a very ambitious operation.
It provides a mouse-click GUI (with Tkinter) for sending LANC commands <sup>1</sup> to a Canon G30 camcorder for:
- zoom (1X to 20X)
- start/stop recording
- cam wake/sleep

 Ways it could be improved:
 * manual/auto focus
 * faster, easier control interface (keyboard input, or other?)
 * low-latency remote control over SSH; perhaps an in-terminal control (maybe using Python *curses* instead of Tkinter)
 * saving a user-defined "home" configuration (for now, that means only a chosen zoom) to return to quickly when requested (a *Reset Home Config* feature)
 * stepper motors to pan and tilt the camcorder
 
 <sup>1</sup> via [ELM624](http://www.appliedlogiceng.com/index_files/Page1389.htm)
