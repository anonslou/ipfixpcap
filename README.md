## Parse IPFIX data from pcap file

Proof of concept

# usage

1. get template from your cisco (show flow exporter templates detail) and save it in file
2. parse file with parse_templates.py - spec and cisco_templates.py files will be created automaticly
3. run read_IPFIX_form_PCAP.py for pcap dump

# limitations

1. don't work for packet with template - only for data packets
2. show field name and raw data - value decode added for ipv4 only
