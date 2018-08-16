import ipfix.ie

ipfix.ie.use_specfile('spec')

slist256 = ipfix.ie.spec_list(('INTERFACEINPUTSNMP', 'interfacenameshort', 'interfacenamelong'))
tmpl256 = ipfix.template.from_ielist(256, slist256)

slist257 = ipfix.ie.spec_list(('ROUTINGVRFINPUT', 'routingvrfname'))
tmpl257 = ipfix.template.from_ielist(257, slist257)

slist258 = ipfix.ie.spec_list(('FLOWSAMPLER', 'flowsamplername', 'flowsampleralgorithmexport', 'flowsamplerinterval'))
tmpl258 = ipfix.template.from_ielist(258, slist258)

slist259 = ipfix.ie.spec_list(('APPLICATIONID', 'applicationname', 'applicationdescription'))
tmpl259 = ipfix.template.from_ielist(259, slist259)

slist260 = ipfix.ie.spec_list(('C3PLCLASSCCE-ID', 'c3plclassname', 'c3plclasstype'))
tmpl260 = ipfix.template.from_ielist(260, slist260)

slist261 = ipfix.ie.spec_list(('C3PLPOLICYCCE-ID', 'c3plpolicyname', 'c3plpolicytype'))
tmpl261 = ipfix.template.from_ielist(261, slist261)

slist262 = ipfix.ie.spec_list(('APPLICATIONID', 'SUBAPPLICATIONTAG', 'subapplicationname', 'subapplicationdescription'))
tmpl262 = ipfix.template.from_ielist(262, slist262)

slist263 = ipfix.ie.spec_list(('APPLICATIONID', 'applicationcategoryname', 'applicationsubcategoryname', 'applicationgroupname', 'applicationtraffic-class', 'applicationbusiness-relevance', 'p2ptechnology', 'tunneltechnology', 'encryptedtechnology'))
tmpl263 = ipfix.template.from_ielist(263, slist263)

slist264 = ipfix.ie.spec_list(('routingvrfinput', 'ipv4sourceaddress', 'ipv4destinationaddress', 'transportrtpssrc', 'interfaceinputsnmp', 'transportsource-port', 'transportdestination-port', 'ipprotocol', 'connectioninitiator', 'transportrtppayload-type', 'ipdscp', 'ipttl', 'datalinksource-vlan-id', 'transportpacketslostcounter', 'transportrtpjittermaximum', 'counterpackets', 'timestampsys-uptimefirst', 'timestampsys-uptimelast', 'connectionnew-connections', 'routingvrfoutput', 'applicationid', 'interfaceoutputsnmp', 'counterbyteslong', 'transportrtpjittermeansum'))
tmpl264 = ipfix.template.from_ielist(264, slist264)

slist265 = ipfix.ie.spec_list(('ipv4sourceaddress', 'ipv4destinationaddress', 'transportrtpssrc', 'routingvrfoutput', 'interfaceoutputsnmp', 'transportsource-port', 'transportdestination-port', 'ipprotocol', 'connectioninitiator', 'transportrtppayload-type', 'ipdscp', 'ipttl', 'datalinksource-vlan-id', 'routingvrfinput', 'transportpacketslostcounter', 'transportrtpjittermaximum', 'counterpackets', 'timestampsys-uptimefirst', 'timestampsys-uptimelast', 'connectionnew-connections', 'applicationid', 'interfaceinputsnmp', 'counterbyteslong', 'transportrtpjittermeansum'))
tmpl265 = ipfix.template.from_ielist(265, slist265)

slist266 = ipfix.ie.spec_list(('ipversion', 'ipprotocol', 'ipdscp', 'routingvrfinput', 'interfaceinputsnmp', 'applicationid', 'datalinksource-vlan-id', 'connectioninitiator', 'flowdirection', 'serviceswaassegment', 'interfaceoutputsnmp', 'routingvrfoutput', 'serviceswaaspassthrough-reason', 'counterbyteslong', 'counterpackets', 'timestampsys-uptimefirst', 'timestampsys-uptimelast', 'connectionnew-connections', 'connectionsum-duration'))
tmpl266 = ipfix.template.from_ielist(266, slist266)

slist267 = ipfix.ie.spec_list(('connectionclientipv4address', 'connectionserveripv4address', 'ipprotocol', 'ipdscp', 'ipttl', 'connectionservertransportport', 'routingvrfinput', 'applicationid', 'datalinksource-vlan-id', 'interfaceinputsnmp', 'connectioninitiator', 'serviceswaassegment', 'interfaceoutputsnmp', 'serviceswaaspassthrough-reason', 'timestampsys-uptimefirst', 'timestampsys-uptimelast', 'connectionnew-connections', 'connectionsum-duration', 'connectiondelayresponseto-serversum', 'connectionservercounterresponses', 'connectiondelayresponseto-serverhistogramlate', 'connectiondelaynetworkto-serversum', 'connectiondelaynetworkto-clientsum', 'connectionclientcounterpacketsretransmitted', 'connectiondelaynetworkclient-to-serversum', 'connectiondelayapplicationsum', 'connectiondelayapplicationmax', 'connectiondelayresponseclient-to-serversum', 'connectiontransactiondurationsum', 'connectiontransactioncountercomplete', 'connectionservercounterbyteslong', 'connectionservercounterpacketslong', 'connectionclientcounterbyteslong', 'connectionclientcounterpacketslong'))
tmpl267 = ipfix.template.from_ielist(267, slist267)

slist268 = ipfix.ie.spec_list(('connectionclientipv4address', 'connectionserveripv4address', 'connectionclienttransportport', 'connectionservertransportport', 'routingvrfinput', 'interfaceinputsnmp', 'connectioninitiator', 'connectionid', 'applicationid', 'interfaceoutputsnmp', 'flowsampler', 'serviceswaassegment', 'serviceswaaspassthrough-reason', 'applicationhttpuristatistics', 'applicationhttphost', 'timestampsys-uptimefirst', 'timestampsys-uptimelast', 'connectionnew-connections', 'connectionservercounterbyteslong', 'connectionservercounterpacketslong', 'connectionclientcounterbyteslong', 'connectionclientcounterpacketslong', 'connectiondelayresponseto-serversum', 'connectionservercounterresponses', 'connectiondelayresponseto-serverhistogramlate', 'connectiondelaynetworkto-serversum', 'connectiondelaynetworkto-clientsum', 'connectionclientcounterpacketsretransmitted', 'connectiondelaynetworkclient-to-serversum', 'connectiondelayapplicationsum', 'connectiondelayapplicationmax', 'connectiondelayresponseclient-to-serversum', 'connectiontransactiondurationsum', 'connectiontransactioncountercomplete'))
tmpl268 = ipfix.template.from_ielist(268, slist268)

slist269 = ipfix.ie.spec_list(('connectionclientipv4address', 'connectionserveripv4address', 'ipprotocol', 'ipdscp', 'ipttl', 'connectionservertransportport', 'routingvrfinput', 'applicationid', 'datalinksource-vlan-id', 'interfaceinputsnmp', 'connectioninitiator', 'serviceswaassegment', 'interfaceoutputsnmp', 'serviceswaaspassthrough-reason', 'timestampsys-uptimefirst', 'timestampsys-uptimelast', 'connectionnew-connections', 'connectionsum-duration', 'connectionservercounterbyteslong', 'connectionservercounterpacketslong', 'connectionclientcounterbyteslong', 'connectionclientcounterpacketslong'))
tmpl269 = ipfix.template.from_ielist(269, slist269)

slist270 = ipfix.ie.spec_list(('ipversion', 'ipprotocol', 'ipdscp', 'applicationid', 'datalinksource-vlan-id', 'routingvrfinput', 'interfaceinputsnmp', 'connectioninitiator', 'interfaceoutputsnmp', 'flowdirection', 'routingvrfoutput', 'serviceswaassegment', 'serviceswaaspassthrough-reason', 'counterbyteslong', 'counterpackets', 'timestampsys-uptimefirst', 'timestampsys-uptimelast', 'connectionnew-connections', 'connectionsum-duration'))
tmpl270 = ipfix.template.from_ielist(270, slist270)

