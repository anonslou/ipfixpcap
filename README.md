# Parse IPFIX data from pcap file

Proof of concept

## usage

1. get template from your cisco (show flow exporter templates detail) and save it in file
2. parse file with parse_templates.py - spec and cisco_templates.py files will be created automaticly
3. run read_IPFIX_form_PCAP.py for pcap dump

## limitations

1. don't work for packet with template - only for data packets
2. show field name and raw data - value decode added for ipv4 only

### output example

```
...
6666: 00:08:2f:2c:b7:41 10.101.255.2:52788 -> 00:15:5d:16:14:08 10.10.28.57:2055
connectionclientipv4address: 10.205.101.20
connectionserveripv4address: 91.226.80.240
connectionclienttransportport: b'\xc2\xea'
connectionservertransportport: b'\x00P'
routingvrfinput: b'\x00\x00\x00\x00'
interfaceinputsnmp: b'\x00\x00\x00\n'
connectioninitiator: b'\x02'
connectionid: b'\x8d8\xea\xb0'
applicationid: b'\x03\x00\x00P'
interfaceoutputsnmp: b'\x00\x00\x00\r'
flowsampler: b'\t'
serviceswaassegment: b'\x10'
serviceswaaspassthrough-reason: b'\x00'
applicationhttpuristatistics: b'/visit\x00\x00\x01'
applicationhttphost: b'\x03\x00\x00P4\x02ws.callibri.ru'
timestampsys-uptimefirst: b'!\xa1\x1f{'
timestampsys-uptimelast: b'!\xa78\x88'
connectionnew-connections: b'\x00\x00\x00\x01'
connectionservercounterbyteslong: b'\x00\x00\x00\x00\x00\x00>\xca'
connectionservercounterpacketslong: b'\x00\x00\x00\x00\x00\x00\x003'
connectionclientcounterbyteslong: b'\x00\x00\x00\x00\x00\x00S\xa9'
connectionclientcounterpacketslong: b'\x00\x00\x00\x00\x00\x00\x00X'
connectiondelayresponseto-serversum: b'\x00\x00\x05\xed'
connectionservercounterresponses: b'\x00\x00\x00.'
connectiondelayresponseto-serverhistogramlate: b'\x00\x00\x00\x00'
connectiondelaynetworkto-serversum: b'\x00\x00\x00\x1c'
connectiondelaynetworkto-clientsum: b'\x00\x00\x00\x02'
connectionclientcounterpacketsretransmitted: b'\x00\x00\x00\x00'
connectiondelaynetworkclient-to-serversum: b'\x00\x00\x00\x1e'
connectiondelayapplicationsum: b'\x00\x00\x00\xe5'
connectiondelayapplicationmax: b'\x00\x00\x00\x15'
connectiondelayresponseclient-to-serversum: b'\x00\x00\x06I'
connectiontransactiondurationsum: b'\x00\x00\x05\xed'
connectiontransactioncountercomplete: b'\x00\x00\x00.'
```
