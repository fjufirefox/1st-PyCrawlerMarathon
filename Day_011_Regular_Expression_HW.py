# import re

# def RegexMatchingIP(regex, input_text):
#     ip_pattern = re.compile(regex)

#     ip_result = re.search(ip_pattern, input_text)

#     if ip_result:
#         print("Matched: %s" % (ip_result.group()))

#         if ip_result.lastindex is not None:
#             for i in range(0, ip_result.lastindex + 1):
#                 print("group(%d): %s" % (i, ip_result.group(i)))
#     else:
#         print("Not Matched.")

# test_string = "Google IP address is 216.58.200.227"
# regex = '(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})'

# RegexMatchingIP(regex, test_string)

# #檢查ip
# from netaddr import valid_ipv4

# ip = '216.58.200.227'
# if valid_ipv4(ip):
#     print('true')
# else:
#     print('false')

import validators
#https://validators.readthedocs.io/en/latest/#
#檢查ip
ip = '216.58.200.227'
result = validators.ipv4(ip)
print(result)

#檢查url

url = 'wwwgooglecom'
result = validators.domain(url)
print(result)
