class RAPLFile:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.baseline = []
        self.process = []
        self.recent = 0
        self.num_process_checks =0
        self.process_average = 0
        self.baseline_average = 0
    def set_recent(val):
        self.recent = val

    def average(baseline_checks):
        self.process_average = self.process/self.num_process_checks
        self.baseline_average = self.baseline/baseline_checks

    def __repr__():
        print(name,path,recent)
