class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True

    def install(self, app, memory):
        if self.memory >= memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= memory
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"