# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:43:07 2020

@author: dambu
"""

import requests as req

url = "https://mma-gmgwm-service-uat.platform-test.allstate.com/gm/warrantyInformation?callId=87847866&vin=1G6AA5RX5J0161107&userId=skleq&jobId=1"

res = req.get(url)

print(res)