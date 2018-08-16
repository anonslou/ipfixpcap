import re


templates = []
with open('show_flow_exporter_templates') as templ:
    itr = iter(templ)
    tmp = odid = 0
    with open('spec', 'w') as spec:  # create spec file
        pass
    for line in itr:
        if 'Template ID' in line:
            tmp = line[line.rfind(' ')+1:-1]
            line = next(itr)
            odid = line[line.rfind(' ')+1:-1]
            line = next(itr)
        if tmp and odid and '____' in line:
            for i in range(3):
                next(itr)
            temp = {(tmp, odid): []}
            with open('spec', 'a') as spec:
                while True:
                    line = next(itr)
                    if '----' in line:
                        break
                    _, name, pen, id, fullid, offset, size, _, _, _, _ = re.sub(r' *', '', line).split('|')
                    sp = '{0}({1}/{2})<octetArray>[{3}]\n'.\
                        format(name, id, 0 if not pen else pen, 65535 if size == 'var' else size)
                    spec.write(sp)
                    temp[(tmp, odid)].append(name)
                templates.append(temp)

with open('cisco_templates.py', 'w') as cisco_templ:
    cisco_templ.write("import ipfix.ie\n\n")
    cisco_templ.write("ipfix.ie.use_specfile('spec')\n\n")
    for temp in templates:
        for (tmp, odid), val in temp.items():
            cisco_templ.write('slist{0} = ipfix.ie.spec_list({1})\n'.format(tmp, tuple(val)))
            cisco_templ.write('tmpl{0} = ipfix.template.from_ielist({0}, slist{0})\n\n'.format(tmp))

