
class PartEvent:
    def __init__(self, part):
        self.part = part

    def Touched(part, user):
        return f"Part has been touched by {user}"

    def Destroy(part):
        return part