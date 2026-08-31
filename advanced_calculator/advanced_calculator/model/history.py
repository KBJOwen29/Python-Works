class History:
    def __init__(self, records=None):
        self.records = records or []

    def add(self, calculation):
        self.records.append(calculation)

    def clear(self):
        self.records.clear()

    def count(self):
        return len(self.records)
