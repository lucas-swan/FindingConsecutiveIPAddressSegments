# 使用python编写程序,实现查找连续的未使用的IP地址段
# 1.输入您使用的IP地址,以空格隔开
# 2.输出最大连续的未使用的IP地址段
# 3.输出最大连续的未使用的IP地址段的个数
# 4.输出含一个中断的最大连续的未使用的IP地址段(未完善)
import re

def is_valid_ip(ip):
    pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])$")
    return pattern.match(ip) is not None

def ip_to_int(ip):
    return int(ip.split('.')[3])

def int_to_ip(ip_int, base_ip):
    return f"{base_ip}.{ip_int}"

def find_unused_ips(used_ips, min_range, max_range):
    all_ips = set(range(min_range, max_range + 1))
    return sorted(list(all_ips.difference(used_ips)))

def find_max_continuous_ips(unused_ips_int, break_count=0):
    start_index = 0
    end_index = 0
    max_length = 0
    max_start = 0
    max_end = 0

    for i in range(len(unused_ips_int) - 1):
        if unused_ips_int[i + 1] - unused_ips_int[i] == 1:
            end_index = i + 1
            current_length = end_index - start_index + 1
            if current_length > max_length:
                max_length = current_length
                max_start = start_index
                max_end = end_index
        else:
            break_count -= 1
            if break_count < 0:
                start_index = i + 1

    return unused_ips_int[max_start:max_end + 1], max_length

# 输入您使用的IP地址,以空格隔开
used_ip_str_list = input("请输入您使用的IP地址,以空格隔开: ").split()

valid_ips = [ip for ip in used_ip_str_list if is_valid_ip(ip)]

if not valid_ips:
    print("输入的IP地址格式有误,请检查")
else:
    base_ip = '.'.join(valid_ips[0].split('.')[:-1])

    used_ips = {ip_to_int(ip) for ip in valid_ips}

    min_range = 1
    max_range = 254

    unused_ips_int = find_unused_ips(used_ips, min_range, max_range)

    max_continuous_ips_int, max_continuous_length = find_max_continuous_ips(unused_ips_int)
    max_continuous_ips = [int_to_ip(ip_int, base_ip) for ip_int in max_continuous_ips_int]
    print(f"最大连续的未使用的IP地址段: {max_continuous_ips}")
    print(f"最大连续的未使用的IP地址段的个数: {max_continuous_length}")

    max_continuous_ips_with_break_int, max_continuous_length_with_break = find_max_continuous_ips(unused_ips_int, break_count=1)
    max_continuous_ips_with_break = [int_to_ip(ip_int, base_ip) for ip_int in max_continuous_ips_with_break_int]
    print(f"含一个中断的最大连续的未使用的IP地址段: {max_continuous_ips_with_break}")
