# PPTP on macOS Sierra

## 1. Connect by command

1. Create a file in `/etc/ppp/peers`, name it what you like. for example: `test-config`

1. Fill the file with:
    ```text
    plugin PPTP.ppp
    noauth
    logfile /tmp/ppp.log
    remoteaddress "your address"
    user "your username"
    password "your password"
    redialcount 1
    redialtimer 5
    idle 1800
    # mru 1368
    # mtu 1368
    receive-all
    novj 0:0
    ipcp-accept-local
    ipcp-accept-remote
    # noauth
    refuse-eap
    refuse-pap
    refuse-chap-md5
    hide-password
    mppe-stateless
    mppe-128
    # require-mppe-128
    looplocal
    nodetach
    # ms-dns 8.8.8.8
    usepeerdns
    # ipparam gwvpn
    defaultroute
    debug
    ```
    
    Replace `remoteaddress`, `user` and `password` with right values.  Replace `logfile` path if necessary.
    
1. `sudo pppd call test-config`


## 2. By Client software

[Download from here!](https://www.flowvpn.com/download-mac/)
