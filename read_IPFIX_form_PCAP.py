import dpkt
import socket
from dpkt.compat import compat_ord

import ipfix.ie
from ipfix.types import IpfixTypeError
from ipfix.message import IpfixDecodeError

import cisco_templates


def mac_addr(address):
    return ':'.join('%02x' % compat_ord(b) for b in address)


def inet_to_str(inet):
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)


def print_msg(msg):
    for rec in msg.namedict_iterator():
        for k, v in rec.items():
            if 'ipv4' in k:
                v = '.'.join(map(str, v))
            print("{}: {}".format(k, v))


packetnumber = 0
for ts, pkt in dpkt.pcap.Reader(open('IPFIX.pcap', 'rb')):
    packetnumber += 1
    eth = dpkt.ethernet.Ethernet(pkt)
    if not isinstance(eth.data, dpkt.ip.IP):
        continue
    ip = eth.data
    if isinstance(ip.data, dpkt.udp.UDP):
        udp = ip.data
        cflow = udp.data
        ipfix.ie.use_iana_default()
        ipfix.ie.use_5103_default()
        msg = ipfix.message.MessageBuffer()
        try:
            msg.from_bytes(cflow)
        except IpfixDecodeError:
            continue

        if len(msg.setlist) == 1:
            tmpl_number = msg.setlist[0][1]
            if 'tmpl' + str(tmpl_number) in dir(cisco_templates):
                msg.add_template(getattr(cisco_templates, 'tmpl' + str(tmpl_number)))
                msg.tuple_iterator(getattr(cisco_templates, 'slist' + str(tmpl_number)))

        print('\n{0}: {1} {2}:{3} -> {4} {5}:{6}'.format(packetnumber, mac_addr(eth.src), inet_to_str(ip.src), udp.sport,
                                                                     mac_addr(eth.dst), inet_to_str(ip.dst), udp.dport))
        try:
            print_msg(msg)
        except IpfixTypeError:
            print('IpfixTypeError in', packetnumber)
            continue
