class CarFleet:
    def __init__(self,pos,spd,target):
        self.pos = pos
        self.spd = spd
        self.target = target

    def car_fleet_stack(self):
        pair = [(p, s) for p, s in zip(self.pos, self.spd)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((self.target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)