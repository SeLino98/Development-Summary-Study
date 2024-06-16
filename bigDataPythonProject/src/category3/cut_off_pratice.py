# cut_off 연습
import numpy as np
predict_proba = np.array([0.5, 0.49, 0.51, 0.3, 0.48, 0.67, 0.55])
cut_off_limits_value = 0.5
predict = (predict_proba >= cut_off_limits_value).astype('int')

print(predict)


print(round(2.5))



# [[참조 - 영상 강의 내용에는 없습니다.]]
# python에서의 round 함수 (numpy, pandas 동일)
import numpy as np
data = np.array([-2.5, -1.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
data_proba = np.array([0.49, 0.5, 0.500001, 0.51, 0.9])
print(data.round())
print((data+0.5).astype('int'))
print((data_proba>=0.5).astype('int')) # 0 ~ 1의 확률인 경우에 사용


# 반올림, 내림처리
import numpy as np
data = np.array([-2.3, -1.5, -1.0, 0.5, 1.1, 2.5, 3.2, 4.0001])
print((data+0.5).astype('int')) # 반올림 처리
print(data.astype('int'))       # 내림 처리


