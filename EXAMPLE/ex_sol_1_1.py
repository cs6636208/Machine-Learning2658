import numpy as np

scores = [80, 75, 90, 60, 85]
print("คะแนนนักเรียนคนที่ 2 ถึง 4:", scores[1:4])
print("คะแนนเฉลี่ย:", sum(scores) / len(scores))
scores.append(95)
print("หลังเพิ่มคะแนนคนที่ 6:", scores)
scores.remove(min(scores))
print("หลังลบคะแนนต่ำสุด:", scores)

