#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from RESTAPI.restapi_0_login import get_session, apic_host, my_headers, pprint_json


def query_tenants(ip):
    request_url = 'https://' + ip + '/api/node/class/fvTenant.json?'
    session = get_session(ip)
    result = session.get(request_url, headers=my_headers)
    # print(result.text)
    return result.json()


def tenants_show(ip):
    tenants_list = query_tenants(ip)['imdata']
    for tenant in tenants_list:
        print(tenant['fvTenant']['attributes']['name'])


def tenant_show(ip, tenant_name):
    request_url = 'https://' + ip + '/api/node/class/fvTenant.json?query-target-filter=and(eq(fvTenant.name,"' + tenant_name + '"))'
    session = get_session(ip)
    result = session.get(request_url, headers=my_headers)
    return result.json()


def tenant_children_show(ip, tenant_name):
    request_url = 'https://' + ip + '/api/node/mo/uni/tn-' + tenant_name + '.json?query-target=children'
    session = get_session(ip)
    result = session.get(request_url, headers=my_headers)
    return result.json()


if __name__ == '__main__':
    # print(query_tenants(apic_host))
    # tenants_show(apic_host)
    # pprint_json(tenant_show(apic_host, "Heroes"))
    pprint_json(tenant_children_show(apic_host, "Heroes"))

