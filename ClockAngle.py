def ClockAngle(h,m):
  hAngle = 0.5 * ( 60 * h + m )
  mAngle = 6 * m
  print ('angle between Hour and Minute clock for ' , h , ' hour ', m ,' minute = ' , hAngle - mAngle)

ClockAngle(5,24)
amund@blr-mpsrr:[~/Downloads/FromEarlierMac/amund/Downloads/Scripts/Python]$ python ClockAngle.py 
('angle between Hour and Minute clock for ', 5, ' hour ', 24, ' minute = ', 18.0)
