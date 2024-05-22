class DailyTemperatures:
    def __init__(self, temperatures):
        self.temperatures = temperatures

    def daily_temperatures_stack(self):
        stack = []
        res = [0] * len(self.temperatures)

        for i in range(len(self.temperatures)):
            if stack:
                while stack and (stack[-1][0] < self.temperatures[i]):
                    x = stack.pop()
                    days = i - x[1]
                    res[x[1]] = days
            stack.append((self.temperatures[i], i))

        return res