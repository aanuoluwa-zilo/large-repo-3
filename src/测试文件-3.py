#!/usr/bin/env python3

# 这是第三个大文件测试，包含Unicode字符
# This is the third large file test with Unicode characters

import random
import string

# Generate large content with Unicode
unicode_chars = '测试数据тестданные文件' + string.ascii_letters + string.digits

# Create large content
large_content = ''.join(random.choice(unicode_chars) for _ in range(1000000))

print('Large Unicode file generated successfully!')
print(f'Content length: {len(large_content)} characters')