# Copyright 2019 - 2020 The ROMAN ROADS Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

r"""Sample code to run training using Element platform
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import json

try:
    from pynng import Sub0, Pair0
except ModuleNotFoundError:
    pass

LOG_IP = '127.0.0.1'
LOG_PORT = 5555
CONTROL_PORT = 5556
LOG_IP_PORT = "tcp://%s:%s" % (LOG_IP, LOG_PORT)
CONTROL_IP_PORT = "tcp://%s:%s" % (LOG_IP, CONTROL_PORT)
TIME_TO_RESTART = 10


def test_using_nanomsg_socket():
    topic = "my_ego_vehicle"
    header_bytes = str.encode(topic)
    header_length = len(header_bytes)

    try:
        socket_nanomsg = Sub0(dial=LOG_IP_PORT, recv_timeout=10000, send_timeout=10000)
        socket_nanomsg.subscribe(topic)

        socket_control = Pair0(dial=CONTROL_IP_PORT, recv_timeout=100, send_timeout=100)

        while True:
            packet = socket_nanomsg.recv()
            payload = packet[header_length:]
            payload = payload.decode('unicode_escape')
            dictionary = json.loads(payload)
            timestamp = int(dictionary["Timestamp"])

            if "initial_time" not in locals():
                initial_time = timestamp

            print("[INFO] timestamp %s" % timestamp)
            decision_command = {
                "Timestamp": timestamp,
                "Behavior": "KeepLane",
                "Duration": 1.0,
                "Acceleration": 1.2
            }

            if (timestamp - initial_time) / 1000. > TIME_TO_RESTART:
                decision_command["Restart"] = True
                initial_time = timestamp

            msg = json.dumps(decision_command).encode('unicode_escape')
            socket_control.send(msg)
    except:
        print("[ERROR] caught exception: ", sys.exc_info()[0])
        pass


def main():
    test_using_nanomsg_socket()


if __name__ == "__main__":
    main()
