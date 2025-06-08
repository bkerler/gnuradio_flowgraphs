#!/usr/bin/env python3

import uhd
import time
usrp = uhd.usrp.MultiUSRP()
usrp.set_clock_source("external")
time.sleep(1)
ref_locked = usrp.get_mboard_sensor("ref_locked")
print("Reference locked:", ref_locked.to_bool())
print("Clock source:", usrp.get_clock_source(0))
print("Master clock rate:", usrp.get_master_clock_rate() / 1e6, "MHz")

