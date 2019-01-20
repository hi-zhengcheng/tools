# Auto Reconnect VPN on Ubuntu

## 1. Figure out vpn name
Run:

```bash
nmcli con
```

From the first column, pick the name of target vpn.
    
## 2. Write a simple python script

```python
import os
import time

while True:
    # replace ${VPN_NAME} with the real one.
    os.popen('nmcli con up id "${VPN_NAME}"')
    time.sleep(60)
```

This script tries to reconnect VPN every 60 seconds. Save it as `auto_connect_vpn.py`.

## 3. Run the script

Run:

```bash
python auto_connect_vpn.py > /dev/null 2>&1 &
```