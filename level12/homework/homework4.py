a = 10
b = 20
c = 10
d = 5

# 1
result1 = a > b  # False, რადგან 10-ი 20-ზე ნაკლებია
result2 = b > a  # True, რადგან 20-ი 10-ზე მეტია

# 2
result3 = a < b  # True, რადგან 10-ი 20-ზე ნაკლებია
result4 = b < a  # False, რადგან 20-ი 10-ზე მეტია

# 3
result5 = a >= c  # True, რადგან 10-ი უდრის 10-ს
result6 = a >= d  # True, რადგან 10-ი 5-ზე მეტია

# 4
result7 = a <= b  # True, რადგან 10-ი 20-ზე ნაკლებია
result8 = b <= a  # False, რადგან 20-ი 10-ზე მეტია

# 5
result9 = a != b  # True, რადგან 10-ი არ უდრის 20-ს
result10 = c != a  # False, რადგან 10-ი უდრის 10-ს

# 6
result11 = a == c  # True, რადგან 10-ი უდრის 10-ს
result12 = b == d  # False, რადგან 20-ი არ უდრის 5-ს

print(result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11, result12)