# 输入的不可选ip和指定的连续长度,查找满足要求的连续ip段.如果没有找到满足要求的连续ip段,程序将逐步尝试去掉不可选ip来查找满足要求的连续ip段.
from itertools import combinations

def ip_to_int(ip):
    return int(ip.split('.')[3])

def int_to_ip(ip_int, base_ip):
    return f"{base_ip}.{ip_int}"

def find_continuous_of_length(ips_list, not_allowed_ips, target_length):
    for i in range(len(ips_list) - target_length + 1):
        sub_list = ips_list[i:i+target_length]
        if set(sub_list).isdisjoint(set(not_allowed_ips)):
            return sub_list
    return None

def find_continuous_with_removed_nums(ips_list, not_allowed_ips, target_length):
    for i in range(1, len(not_allowed_ips) + 1):
        for removed_ips in combinations(not_allowed_ips, i):
            temp_ips_list = [ip for ip in ips_list if ip not in removed_ips]
            continuous_ips = find_continuous_of_length(temp_ips_list, not_allowed_ips, target_length)
            if continuous_ips:
                return continuous_ips, removed_ips
    return None, None

# 输入不可选中的 IP 地址,以空格隔开
not_allowed_ips_str_list = input("请输入不可选中的 IP 地址,以空格隔开: ").split()
not_allowed_ips = [ip_to_int(ip) for ip in not_allowed_ips_str_list]

# 输入指定连续长度
target_length = int(input("请输入指定连续长度: "))

ips_list = list(range(1, 255))
base_ip = "10.143.6"
continuous_ips = find_continuous_of_length(ips_list, not_allowed_ips, target_length)

if continuous_ips:
    continuous_ips_str = [int_to_ip(ip, base_ip) for ip in continuous_ips]
    print(f"找到的连续 IP 地址段:{continuous_ips_str}")
else:
    continuous_ips, removed_nums = find_continuous_with_removed_nums(ips_list, not_allowed_ips, target_length)
    if continuous_ips:
        continuous_ips_str = [int_to_ip(ip, base_ip) for ip in continuous_ips]
        removed_ips_str = [int_to_ip(ip, base_ip) for ip in removed_nums]
        print(f"去掉不可选 IP 地址后找到的连续 IP 地址段:{continuous_ips_str}")
        print(f"被去掉的 IP 地址:{removed_ips_str}")
    else:
        print("没有找到满足要求的连续 IP 地址段.")
