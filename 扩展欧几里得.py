#-*-coding:utf-8-*- 
# 扩展欧几里得算法
# 输入m n 
# 输出 m n的最大公约数 还有s,t
# 
# 默认 m > n
 
import sys
 
def exgcd(m,n,x,y):
	if n == 0:
		x = 1
		y = 0
		return (m,x,y)
	a1 = b = 1
	a = b1 = 0
	c = m
	d = n
	q = int(c/d)
	r = c%d
	while r:
		c = d
		d = r
		t = a1
		a1 = a
		a = t-q*a
		t = b1
		b1 = b
		b = t-q*b
		q = int(c/d)
		r = c%d
	x = a
	y = b
	return (d,x,y)
 
m = 5
n = 19
ans = exgcd(m,n,0,0)
 
print("gcd(%d,%d) = %d"%(m,n,ans[0]))
print("s = %d, t = %d"%(ans[1],ans[2]))