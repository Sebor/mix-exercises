def getAngle(hours, minutes):
	WholeCircle = 360
	AngleMinutes = minutes * WholeCircle / 60
	AngleHours = hours * (WholeCircle / 12) + (WholeCircle / 12) / (WholeCircle / AngleMinutes)
	return abs(AngleHours - AngleMinutes)


if __name__ == '__main__':
	hours, minutes = map(int, input().split())
	print(getAngle(hours, minutes))
