contextual-match
=====================

Parse device configuration files that are retrieved with rancid

It works with configuration files that are indented with spaces or tabs

Tested on a very old Ubuntu 8.04 for configuration files of the following vendors:
- Nokia (previously Alcatel-Lucent)
- Fortigate
- juniper

Example of output for the command "cmatch.py VDOM * "

```
device1.cfg: service > vpls 00001 customer 1001 create > sap 1/1/1:100 create > description "Service VDOM 00001"
device2.cfg: service > vpls 00002 customer 1002 create > description "Internal VDOM"
device3.cfg: service > vpls 00003 customer 1003 create > sap 1/2/1:101 create > description "Service VDOM 00002"
```


