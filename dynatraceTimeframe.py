#!/usr/bin/env python3
# Takes in input an UTC date and transform in a dynatrace timeframe instruction
# if no input, it will take now as time
# Example:
# > dynatraceTimeframe.py 2024-11-13T10:01:39Z
# timeframe:"2024-11-13T09:56:39Z/2024-11-13T10:06:39Z"

import datetime
import sys

datetime_object = datetime.datetime.now(datetime.timezone.utc)
if len(sys.argv) == 2:
    datetime_str = sys.argv[1]
    datetime_object = datetime.datetime.fromisoformat(datetime_str)

before = datetime_object - datetime.timedelta(seconds=300)
after = datetime_object + datetime.timedelta(seconds=300)

print("timeframe:\"{0}Z/{1}Z\"".format(before.isoformat()[:-6], after.isoformat()[:-6]))
