class DetectionCounter:
    def __init__(self):
        self.count = 0
        self.current_class = None

    def compare_and_update(self, cls):
        if cls is not None and cls == self.current_class:
            self.count += 1
            return

        self.current_class = cls
        self.count = 0

    def get_count(self):
        return self.count