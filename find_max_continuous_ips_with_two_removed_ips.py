# 主要功能是查找并输出去掉两个不可选 IP 后的最大连续 IP 地址段及相关信息
# 使用python编写程序,实现查找连续的未使用的IP地址段
# 1.输入您使用的IP地址,以空格隔开
# 2.去掉两个不可选IP后的最大连续IP地址段
# 3.去掉两个不可选IP后的最大连续IP地址段长度
# 4.被去掉的两个IP
from itertools import combinations
def ip_to_int(ip):
    return int(ip.split('.')[3])

def int_to_ip(ip_int, base_ip):
    return f"{base_ip}.{ip_int}"

def find_continuous_ips(ips, not_allowed_ips):
    continuous_ips = []
    temp_ips = []

    for ip in ips:
        if ip not in not_allowed_ips:
            temp_ips.append(ip)
        else:
            if temp_ips:
                continuous_ips.append(temp_ips)
                temp_ips = []

    if temp_ips:
        continuous_ips.append(temp_ips)

    return continuous_ips

def find_max_continuous(ips_list):
    max_length = 0
    max_continuous_ips = []

    for ips in ips_list:
        if len(ips) > max_length:
            max_length = len(ips)
            max_continuous_ips = ips

    return max_continuous_ips, max_length
def find_max_continuous_with_two_removed(ips_list, not_allowed_ips):
    max_length = 0
    max_continuous_ips = []
    removed_ips = ()

    for ip_pair in combinations(not_allowed_ips, 2):
        temp_ips_list = ips_list.copy()
        for ip in ip_pair:
            if ip in temp_ips_list:
                temp_ips_list.remove(ip)
        temp_continuous_ips_list = find_continuous_ips(temp_ips_list, not_allowed_ips)
        temp_max_continuous_ips, temp_max_length = find_max_continuous(temp_continuous_ips_list)

        if temp_max_length > max_length:
            max_length = temp_max_length
            max_continuous_ips = temp_max_continuous_ips
            removed_ips = ip_pair

    return max_continuous_ips, max_length, removed_ips

# 10.143.6.0/24 IP段的所有IP
base_ip = '10.143.6'
all_ips = [int_to_ip(i, base_ip) for i in range(1, 255)]

# 输入不可选中的IP地址, 以空格隔开
used_ip_str_list = input("请输入不可选中的IP地址, 以空格隔开: ").split()
not_allowed_ips = [ip for ip in used_ip_str_list]

continuous_ips_list = find_continuous_ips(all_ips, not_allowed_ips)
max_continuous_ips, max_length = find_max_continuous(continuous_ips_list)

max_continuous_ips_with_two_removed, max_length_with_two_removed, removed_ips = find_max_continuous_with_two_removed(all_ips, not_allowed_ips)

print(f"去掉两个不可选IP后的最大连续IP地址段: {max_continuous_ips_with_two_removed}")
print(f"去掉两个不可选IP后的最大连续IP地址段长度: {max_length_with_two_removed}")
print(f"被去掉的两个IP: {removed_ips}")
