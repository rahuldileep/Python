#!/usr/bin/env python

##################################################
## Author: Rahul Dileep Jadhav
## Version: 1.0
## Copyright (c) 2019 by Cisco Systems, Inc.
##################################################

import os
import re
import sys
import json
import argparse
import subprocess
sys.path.append("/pkg/bin")
from ztp_helper import ZtpHelpers
os.environ["PATH"] = "/pkg/bin:/pkg/sbin/:/usr/bin:/bin/:/usr/sbin:/sbin"
os.environ["LD_LIBRARY_PATH"] = "/pkg/lib:/pkg/lib/cerrno:/pkg/lib/mib:/pkg/lib/spp_plugins"

def shutdown_interface(interface_list):
    # Accepts a list of interfaces to shutdown.
    # Iterates over each interface and creates a config file.
    # Applies the config file to bring down the interfaces.
    config_file = ""
    for interface in interface_list:
      cmd = 'Bringing down interface %s due to multiple CRC errors'%(interface)
      subprocess.call(['logger',cmd])
      file_content="""
        !
        interface %s
          shutdown
        !
        end
        """
      config_file += file_content%(interface)
    
    file_path="/root/int_down.conf"
    with open(file_path, 'w') as fd:
      fd.write(config_file)
    fd.close()
    ztp_obj=ZtpHelpers()
    ztp_obj.xrapply(filename=file_path)


def crc_error_check(warning_threshold, action_threshold):
    # Check for CRC errors on every interface.
    # Generate syslog if CRC errors are observed.
    # Check for incremental CRC errors.
    # If CRC errors increment over 3 poll cycles, the interface will be shutdown.
    # Uses JSON file to store and keep track of CRC errors on every interface. 

    file_path = '/root/data.json'
    if not os.path.exists(file_path):
      with open(file_path, 'w') as f:
        json.dump({}, f,indent = 4)
      f.close()
    interface_list = []
    sh_int_br_output = subprocess.check_output(['xr_cli', 'show interface brief | i up | ex Mg']).strip().splitlines()[1:]
    for line in sh_int_br_output:
        try:
          interface = line.split()[0]
          crc_check = subprocess.check_output(['xr_cli', 'show interface %s | i CRC'%(interface)]).strip()
          current_crc_value = int(re.search(r'(\d+)\sCRC,',crc_check).group(1))
          if current_crc_value:
            if current_crc_value > action_threshold:
              cmd = 'Interface %s observed %d CRC errors. \
                           Shutting down the interface.'%(interface, current_crc_value)
              subprocess.call(['logger',cmd])
              interface_list.append(interface)
            elif current_crc_value > warning_threshold:
              cmd = 'Interface %s observed %d CRC errors.'%(interface, current_crc_value)
              subprocess.call(['logger',cmd])
            with open(file_path) as fp:
              data = json.load(fp)
              if interface in data:
                prev_crc_val = data[interface]['prev_crc_value']
                if current_crc_value > prev_crc_val:
                  data[interface]['increment_count'] += 1
                  data[interface]['prev_crc_value'] = current_crc_value
              else:
                data[interface] = dict()
                data[interface]['increment_count'] = 1
                data[interface]['prev_crc_value'] = current_crc_value
          else:
            with open(file_path) as fp:
              data = json.load(fp)
              if interface in data:
                prev_crc_val = data[interface]['prev_crc_value']
                if prev_crc_val > 0 and current_crc_value == 0:
                  data[interface]['prev_crc_value'] = 0
                  data[interface]['increment_count'] = 0 
          with open(file_path,'w') as fp:
            json.dump(data, fp, indent = 4)
        except:
          continue
    if interface_list:
        shutdown_interface(interface_list)

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-wt", "--warning_threshold", 
                            help="set threshold for crc errors", type = int, default=100)
    parser.add_argument("-at", "--action_threshold", 
                            help="define action if threshold reached: warning/shutdown", type = int, default=1000)
    args = parser.parse_args()
    crc_error_check(args.warning_threshold, args.action_threshold)